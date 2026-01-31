import sqlite3

def init_db():
    conn = sqlite3.connect('digest.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            link TEXT,
            content TEXT,
            source TEXT,
            timestamp DATETIME
        )
    ''')
    conn.commit()
    conn.close()

def save_items(items):
    conn = sqlite3.connect('digest.db')
    c = conn.cursor()
    for item in items:
        c.execute('INSERT INTO items (title, content, source, timestamp) VALUES (?, ?, ?, ?)',
                  (item['title'], item['content'], item['source'], item['timestamp']))
    conn.commit()
    conn.close()

# def get_items():
#     conn = sqlite3.connect('digest.db')
#     c = conn.cursor()
#     c.execute('SELECT title, content FROM items')
#     items = c.fetchall()
#     conn.close()
#     return items

def get_items():
    conn = sqlite3.connect('digest.db')
    c = conn.cursor()
    c.execute('SELECT title, link, content, source, timestamp FROM items')
    rows = c.fetchall()
    conn.close()
    items = []
    for row in rows:
        items.append({
            'title': row[0],
            'link': row[1],
            'content': row[2],
            'source': row[3],
            'timestamp': row[4]
        })
    return items

def clear_items():
    conn = sqlite3.connect('digest.db')
    c = conn.cursor()
    c.execute('DELETE FROM items')
    conn.commit()
    conn.close()