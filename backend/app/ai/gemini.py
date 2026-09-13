import json

from google import genai
from google.genai import errors

from app.ai.prompts import create_review_prompt
from app.config.settings import settings

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


def _model_pool() -> list[str]:
    models = [settings.GEMINI_MODEL, *settings.GEMINI_FALLBACK_MODELS]
    return list(dict.fromkeys(models))


def analyze_review(review_text: str) -> dict:
    last_error: Exception | None = None

    for model in _model_pool():
        try:
            chat = client.chats.create(model=model, config=OUTPUT_CONFIG)
            response = chat.send_message(create_review_prompt(review_text))
            return json.loads(response.text)
        except (errors.ServerError, json.JSONDecodeError) as exc:
            last_error = exc

    raise RuntimeError(f"All Gemini models unavailable: {last_error}")