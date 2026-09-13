import json
import logging

from google import genai
from google.genai import errors

from app.ai.prompts import create_review_prompt
from app.config.settings import settings

logger = logging.getLogger(__name__)

client = genai.Client(api_key=settings.GEMINI_API_KEY)

ANALYSIS_SCHEMA = {
    "type": "OBJECT",
    "properties": {
        "sentiment": {
            "type": "STRING",
            "enum": ["positive", "negative", "neutral"],
        },
        "rating": {"type": "INTEGER"},
        "summary": {"type": "STRING"},
        "topics": {"type": "ARRAY", "items": {"type": "STRING"}},
        "pros": {"type": "ARRAY", "items": {"type": "STRING"}},
        "cons": {"type": "ARRAY", "items": {"type": "STRING"}},
    },
    "required": ["sentiment", "rating", "summary", "topics", "pros", "cons"],
}

OUTPUT_CONFIG = {
    "response_mime_type": "application/json",
    "response_schema": ANALYSIS_SCHEMA,
}

SENTIMENTS = {"positive", "negative", "neutral"}
REQUIRED_FIELDS = {"sentiment", "rating", "summary", "topics", "pros", "cons"}


def _model_pool() -> list[str]:
    models = [settings.GEMINI_MODEL, *settings.GEMINI_FALLBACK_MODELS]
    return list(dict.fromkeys(models))


def _as_str_list(value) -> list[str]:
    if isinstance(value, list):
        return [str(item) for item in value if item is not None]
    return []


def _validate_analysis(text: str | None) -> dict:
    if not text:
        raise ValueError("Gemini returned an empty response.")

    data = json.loads(text)

    if not isinstance(data, dict):
        raise ValueError("Gemini response is not a JSON object.")

    missing = REQUIRED_FIELDS - data.keys()
    if missing:
        raise ValueError(
            f"Gemini response is missing fields: {sorted(missing)}"
        )

    sentiment = str(data["sentiment"]).strip().lower()
    if sentiment not in SENTIMENTS:
        raise ValueError(f"Unexpected sentiment: {data['sentiment']}")

    try:
        rating = int(data["rating"])
    except (TypeError, ValueError):
        raise ValueError(f"Invalid rating: {data['rating']}")

    rating = max(1, min(5, rating))

    summary = str(data.get("summary")).strip() or "No summary provided."

    return {
        "sentiment": sentiment,
        "rating": rating,
        "summary": summary,
        "topics": _as_str_list(data.get("topics")),
        "pros": _as_str_list(data.get("pros")),
        "cons": _as_str_list(data.get("cons")),
    }


def analyze_review(review_text: str) -> dict:
    last_error: Exception | None = None

    for model in _model_pool():
        try:
            chat = client.chats.create(model=model, config=OUTPUT_CONFIG)
            response = chat.send_message(create_review_prompt(review_text))
            return _validate_analysis(response.text)
        except (errors.APIError, json.JSONDecodeError, ValueError) as exc:
            logger.warning("Model %s failed: %s", model, exc)
            last_error = exc

    raise RuntimeError(f"All Gemini models unavailable: {last_error}")