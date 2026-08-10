import sqlite3
from pathlib import Path

DATABASE_PATH = Path(__file__).parent.parent / "data" / "scout.db"


def get_connection():
    return sqlite3.connect(DATABASE_PATH)
def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS opportunities (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            company TEXT NOT NULL,
            location TEXT NOT NULL,
            salary TEXT NOT NULL,
            url TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()

def add_opportunity(opportunity):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO opportunities
        (id, title, company, location, salary, url)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            opportunity.id,
            opportunity.title,
            opportunity.company,
            opportunity.location,
            opportunity.salary,
            opportunity.url,
        ),
    )

    connection.commit()
    connection.close()    