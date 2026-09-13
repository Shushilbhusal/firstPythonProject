from app.database.database import get_connection


def save_review(
    review_text: str,
    sentiment: str,
    rating: int,
    summary: str,
    topics: str,
    pros: str,
    cons: str,
):
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO reviews (
            review_text,
            sentiment,
            rating,
            summary,
            topics,
            pros,
            cons
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            review_text,
            sentiment,
            rating,
            summary,
            topics,
            pros,
            cons,
        ),
    )

    connection.commit()

    review_id = cursor.lastrowid

    connection.close()

    return review_id