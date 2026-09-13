from app.database.database import get_connection


def create_reviews_table():
    connection = get_connection()

    cursor = connection.cursor()  ## this cursor object is used to execute SQL queries and fetch results from the database.

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            review_text TEXT NOT NULL,
            sentiment TEXT,
            rating INTEGER,
            summary TEXT,
            topics TEXT,
            pros TEXT,
            cons TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    connection.commit()
    connection.close()