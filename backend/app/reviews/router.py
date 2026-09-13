from fastapi import APIRouter

from app.reviews.schemas import ReviewCreate
from app.ai.gemini import analyze_review


router = APIRouter(
    prefix="/api/reviews",
    tags=["Reviews"]
)


@router.post("/analyze")
def analyze_customer_review(review: ReviewCreate):
    result = analyze_review(review.review_text)

    return {
        "review": review.review_text,
        "analysis": result
    }