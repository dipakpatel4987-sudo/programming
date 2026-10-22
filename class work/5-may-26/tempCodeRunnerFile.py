import pymysql
import random

mydb = pymysql.connect(host="localhost",user="root",password="", port=3307)
mycursor = mydb.cursor()
mycursor.execute("create  database if not exists banking_system")
mydb.commit()

class Banking_system:
    def open(self):
        username=input("Enter YOur name:")
        password=input("Enter your Password:")
        cfpassword=input("Enter Conform Password:")
        balance=50000
        
        if password==cfpassword:
            a_no=random.randint(1000000000,9999999999)
            print("YOUR ACCOUNT OPEN SUCCESSFULLY!!!")
            print("Username :",username)
            print("Account Number:",a_no)
            print("Balance:",balance)
             
            mydb=pymysql.connect(host="localhost",user="root",password="",port=3307,database="banking_system")
            mycursor=mydb.cursor()
            mycursor.execute("create table if not exists new_account(a_no int primary key ,password varchar(50),cfpassword varchar(50),balance int,username varchar(50))")
            mydb.commit()

            query =  "insert into new_account(a_no,username, password,cfpassword,balnce) values (%s, %s,%s,%s,%s)"
            args = (a_no,username,password,cfpassword,balance)
            mycursor.execute(query % args)
            mydb.commit()
            print("data insterted")
           
        else:
            print("password don't match!!!")


obj=Banking_system()
obj.open()
