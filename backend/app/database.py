import sqlite3
from pathlib import Path

DATABASE_PATH = Path(__file__).parent.parent / "data" / "scout.db"


def get_connection():
    return sqlite3.connect(DATABASE_PATH)