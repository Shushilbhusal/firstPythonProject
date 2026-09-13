from fastapi import FastAPI

from app.database.models import create_reviews_table
from app.reviews.router import router as reviews_router


app = FastAPI(
    title="Customer Review Analyzer API",
    description="Analyze customer reviews using Gemini AI.",
    version="1.0.0",
)



## runs code when the server starts.  runs code when the server starts.
@app.on_event("startup")
def startup():
    create_reviews_table()


app.include_router(reviews_router)


@app.get("/")
def root():
    return {
        "message": "Customer Review Analyzer API is running"
    }