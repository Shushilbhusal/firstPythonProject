import json

from app.database.database import supabase
from app.reviews.schemas import ReviewResponse


def _as_list(value) -> list[str]:
    if isinstance(value, list):
        return value
    if isinstance(value, str):
        parsed = json.loads(value) if value else []
        return parsed if isinstance(parsed, list) else []
    return []


def save_review(
    review_text: str,
    sentiment: str,
    rating: int,
    summary: str,
    topics: list[str],
    pros: list[str],
    cons: list[str],
) -> dict:
    response = (
        supabase.table("reviews")
        .insert(
            {
                "review_text": review_text,
                "sentiment": sentiment,
                "rating": rating,
                "summary": summary,
                "topics": topics,
                "pros": pros,
                "cons": cons,
            }
        )
        .execute()
    )

    saved = response.data[0]
    saved["topics"] = _as_list(saved.get("topics"))
    saved["pros"] = _as_list(saved.get("pros"))
    saved["cons"] = _as_list(saved.get("cons"))

    return {field: saved.get(field) for field in ReviewResponse.model_fields}