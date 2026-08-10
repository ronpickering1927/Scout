import sqlite3
from pathlib import Path

from backend.app.models import Opportunity


DATABASE_PATH = Path(__file__).parent.parent / "data" / "scout.db"


def get_connection():
    return sqlite3.connect(DATABASE_PATH)


def create_tables():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS opportunities (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            company TEXT NOT NULL,
            location TEXT NOT NULL,
            salary TEXT NOT NULL,
            url TEXT NOT NULL
        )
        """
    )

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


def get_all_opportunities() -> list[Opportunity]:
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, title, company, location, salary, url
        FROM opportunities
        ORDER BY id
        """
    )

    rows = cursor.fetchall()
    connection.close()

    return [
        Opportunity(
            id=row[0],
            title=row[1],
            company=row[2],
            location=row[3],
            salary=row[4],
            url=row[5],
        )
        for row in rows
    ]
def get_opportunity_by_id(opportunity_id: int):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, title, company, location, salary, url
        FROM opportunities
        WHERE id = ?
        """,
        (opportunity_id,),
    )

    row = cursor.fetchone()
    connection.close()

    if row is None:
        return None

    return Opportunity(
        id=row[0],
        title=row[1],
        company=row[2],
        location=row[3],
        salary=row[4],
        url=row[5],
    )

def update_opportunity(opportunity):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE opportunities
        SET title = ?,
            company = ?,
            location = ?,
            salary = ?,
            url = ?
        WHERE id = ?
        """,
        (
            opportunity.title,
            opportunity.company,
            opportunity.location,
            opportunity.salary,
            opportunity.url,
            opportunity.id,
        ),
    )

    connection.commit()
    connection.close()


def delete_opportunity(opportunity_id: int):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM opportunities
        WHERE id = ?
        """,
        (opportunity_id,),
    )

    connection.commit()
    connection.close()