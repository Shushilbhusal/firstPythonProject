from google import genai

from app.config.settings import settings
from app.ai.prompts import create_review_prompt


def analyze_review(review_text: str):
    # Create Gemini client
    client = genai.Client(
        api_key=settings.GEMINI_API_KEY
    )

    # Create our prompt
    prompt = create_review_prompt(review_text)

    # Send prompt to Gemini
    response = client.interactions.create(
        model="gemini-3.6-flash",
        input=prompt,
    )

    # Return Gemini's text response
    return response.output_text