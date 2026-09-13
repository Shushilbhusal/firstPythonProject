from fastapi import APIRouter, HTTPException, Query

from app.ai.gemini import analyze_review
from app.reviews.schemas import ReviewCreate, ReviewResponse
from app.reviews.service import list_reviews, save_review


router = APIRouter(
    prefix="/api/reviews",
    tags=["Reviews"],
)


@router.post("/analyze", response_model=ReviewResponse)
def analyze_customer_review(review: ReviewCreate):
    try:
        # print("Analyzing review:", review.review_text)
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


@router.get("", response_model=list[ReviewResponse])
def get_recent_reviews(
    limit: int = Query(default=20, ge=1, le=100),
):
    try:
        return list_reviews(limit)
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="Could not load recent reviews.",
        ) from exc