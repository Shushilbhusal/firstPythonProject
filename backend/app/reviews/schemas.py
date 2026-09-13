from pydantic import BaseModel, Field


class ReviewCreate(BaseModel):
    review_text: str = Field(
        ...,
        min_length=3,
        max_length=5000,
        description="Customer review text",
    )


class ReviewResponse(BaseModel):
    id: int | None = None
    review_text: str
    sentiment: str | None = None
    rating: int | None = None
    summary: str | None = None
    topics: list[str] = Field(default_factory=list)
    pros: list[str] = Field(default_factory=list)
    cons: list[str] = Field(default_factory=list)
    created_at: str | None = None
    saved: bool = True