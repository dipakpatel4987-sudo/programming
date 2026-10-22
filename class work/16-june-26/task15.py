import pymysql

mydb = pymysql.connect(host="localhost",user="root",password="", port=3307)
mycursor = mydb.cursor()

mycursor.execute("create  database if not exists python33")
mydb.commit()
mydb=pymysql.connect(host="localhost",user="root",password="",port=3307,database="python33")
mycursor=mydb.cursor()
mycursor.execute("create table if not exists python45(id int ,roll int,name varchar(50))")
mydb.commit()

