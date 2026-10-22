from task4 import *
import pymysql

mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    port=3307,
    database="user_db"
)
mycursor=mydb.cursor()

def account():
    name=input("Enter your name:")
    password=input("Enter your password:")

    query=("insert into account(name,password)values(%s,%s)")
    args=(name,password)
    mycursor.execute(query, args)
print(account())
    
    