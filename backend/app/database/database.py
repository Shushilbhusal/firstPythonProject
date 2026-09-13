import sqlite3

from app.config.settings import settings


def get_connection():
    connection = sqlite3.connect(
        settings.DATABASE_URL.replace("sqlite:///", "")    ## it wiill create a database file in the backend directory if it does not exist
    )

    connection.row_factory = sqlite3.Row

    return connection