import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("student.db")

# Create cursor object
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

# Insert data into table
cursor.execute("INSERT INTO student (name, age) VALUES (?, ?)",
               ("Dipak", 22))

cursor.execute("INSERT INTO student (name, age) VALUES (?, ?)",
               ("Rahul", 21))

# Commit changes
conn.commit()

# Fetch data from table
cursor.execute("SELECT * FROM student")

rows = cursor.fetchall()

# Display data
print("Student Records:")

for row in rows:
    print(row)

# Close database connection
conn.close()