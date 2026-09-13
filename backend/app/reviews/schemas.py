from pydantic import BaseModel, Field


class ReviewCreate(BaseModel):
    review_text: str = Field(
        ...,
        min_length=3,
        description="Customer review text"
    )


class ReviewResponse(BaseModel):
    id: int
    review_text: str
    sentiment: str | None
    rating: int | None
    summary: str | None
    topics: list[str]
    pros: list[str]
    cons: list[str]
    created_at: str