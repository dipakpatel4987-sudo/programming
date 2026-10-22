import sqlite3


conn = sqlite3.connect("college.db")


cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")


conn.commit()


conn.close()

print("Database and table created successfully.")