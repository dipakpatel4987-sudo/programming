import pymysql

mydb=pymysql.connect(host="localhost",user="root",password="",port=3307)
mycursor=mydb.cursor()

mycursor.execute("create database if not exists user_db")
mydb.commit()

mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    port=3307,
    database="user_db"
)
mycursor=mydb.cursor()

mycursor.execute("""
CREATE TABLE IF NOT EXISTS ACCOUNT(
                ID INT PRIMARY KEY AUTO_INCREMENT,
                NAME varchar(50),
                PASSWORD varchar(50))""")
mydb.commit()

