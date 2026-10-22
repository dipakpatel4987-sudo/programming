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


cursor.execute(
    "INSERT INTO student (name, age, course) VALUES (?, ?, ?)",
    ("Dipak", 22, "Python")
)

cursor.execute(
    "INSERT INTO student (name, age, course) VALUES (?, ?, ?)",
    ("Rahul", 21, "Java")
)


conn.commit()

cursor.execute("SELECT * FROM student")

records = cursor.fetchall()


print("Student Records:")

for row in records:
    print(row)


conn.close()