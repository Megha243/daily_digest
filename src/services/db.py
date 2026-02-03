import sqlite3
from datetime import datetime


DB_NAME = "digest.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            link TEXT,
            content TEXT,
            source TEXT,
            timestamp DATETIME
        )
    """)
    conn.commit()
    conn.close()


def save_items(items):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    for item in items:
        c.execute(
            """
            INSERT INTO items (title, link, content, source, timestamp)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                item.get("title"),
                item.get("link"),              # ✅ FIX: save link
                item.get("content"),
                item.get("source"),
                item.get("timestamp", datetime.utcnow())  # safe default
            )
        )

    conn.commit()
    conn.close()


def get_items():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
        SELECT title, link, content, source, timestamp
        FROM items
    """)

    rows = c.fetchall()
    conn.close()

    items = []
    for row in rows:
        items.append({
            "title": row[0],
            "link": row[1],        # ✅ now guaranteed
            "content": row[2],
            "source": row[3],
            "timestamp": row[4],
        })

    return items


def clear_items():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM items")
    conn.commit()
    conn.close()
