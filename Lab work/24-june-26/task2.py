import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")
records = cursor.fetchall()

for row in records:
    print(row)

conn.close()
