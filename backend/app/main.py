from fastapi import FastAPI
from app.reviews.router import router as reviews_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Customer Review Analyzer API",
    description="Analyze customer reviews using Gemini AI.",
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*",
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(reviews_router)


@app.get("/")
def root():
    return {
        "message": "Customer Review Analyzer API is running"
    }