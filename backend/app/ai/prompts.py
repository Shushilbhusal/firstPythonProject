def create_review_prompt(review_text: str) -> str:
    return f"""
Analyze the following customer review and return ONLY valid JSON.

Review:
{review_text}

Return the JSON in exactly this shape:
{{
  "sentiment": "one of: positive, negative, neutral",
  "rating": 1-5,
  "summary": "short summary",
  "topics": ["..."],
  "pros": ["..."],
  "cons": ["..."]
}}

Do not include anything outside the JSON object.
"""