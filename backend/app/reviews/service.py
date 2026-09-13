import json
import logging

from postgrest.exceptions import APIError

from app.database.database import supabase

logger = logging.getLogger(__name__)


def _as_list(value) -> list[str]:
    if isinstance(value, list):
        return value
    if isinstance(value, str):
        parsed = json.loads(value) if value else []
        return parsed if isinstance(parsed, list) else []
    return []


def _normalize(row: dict, saved: bool = True) -> dict:
    return {
        "id": row.get("id"),
        "review_text": row.get("review_text"),
        "sentiment": row.get("sentiment"),
        "rating": row.get("rating"),
        "summary": row.get("summary"),
        "topics": _as_list(row.get("topics")),
        "pros": _as_list(row.get("pros")),
        "cons": _as_list(row.get("cons")),
        "created_at": row.get("created_at"),
        "saved": saved,
    }


def save_review(
    review_text: str,
    sentiment: str,
    rating: int,
    summary: str,
    topics: list[str],
    pros: list[str],
    cons: list[str],
) -> dict:
    analysis = {
        "review_text": review_text,
        "sentiment": sentiment,
        "rating": rating,
        "summary": summary,
        "topics": topics,
        "pros": pros,
        "cons": cons,
    }

    try:
        response = supabase.table("reviews").insert(analysis).execute()
        return _normalize(response.data[0])
    except APIError as exc:
        logger.warning(
            "Could not save review to database (returning analysis only): %s",
            exc,
        )
        return _normalize(analysis, saved=False)


def list_reviews(limit: int = 20) -> list[dict]:
    response = (
        supabase.table("reviews")
        .select("*")
        .order("created_at", desc=True)
        .limit(limit)
        .execute()
    )
    return [_normalize(row) for row in response.data]