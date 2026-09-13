from fastapi import APIRouter, HTTPException

from app.ai.gemini import analyze_review
from app.reviews.schemas import ReviewCreate, ReviewResponse
from app.reviews.service import save_review


router = APIRouter(
    prefix="/api/reviews",
    tags=["Reviews"],
)


@router.post("/analyze", response_model=ReviewResponse)
def analyze_customer_review(review: ReviewCreate):
    try:
        analysis = analyze_review(review.review_text)
    except (RuntimeError, ValueError) as exc:
        raise HTTPException(
            status_code=503,
            detail="Review analysis is temporarily unavailable, please try again later.",
        ) from exc

    return save_review(
        review_text=review.review_text,
        sentiment=analysis["sentiment"],
        rating=analysis["rating"],
        summary=analysis["summary"],
        topics=analysis["topics"],
        pros=analysis["pros"],
        cons=analysis["cons"],
    )