import pymysql

mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    port=3307
)
mycursor=mydb.cursor()
mycursor.execute("create database if not exists student1_db")
mydb.commit()
