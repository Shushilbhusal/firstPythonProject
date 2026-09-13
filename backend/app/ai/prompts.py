def create_review_prompt(review_text: str) -> str:
    return f"""
Analyze the following customer review.

Review:
{review_text}

Return the following information:

1. Sentiment
2. Rating from 1 to 5
3. Short summary
4. Main topics
5. Pros
6. Cons

Keep the response structured and easy to parse.
"""