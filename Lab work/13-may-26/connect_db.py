
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student_db"
)

print("Database Connected Successfully")

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for table in mycursor:
    print(table)