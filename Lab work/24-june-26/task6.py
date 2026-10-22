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

while True:
    mainu="""
1.create a data
2.update
3.datele
4.fetch
5.exist
"""
    print(mainu)
    choice = int(input("Enter you number:"))

    if choice==1:
        def account():
            name=input("Enter your name:")
            password=input("Enter your password:")

            query=("insert into account(name,password)values(%s,%s)")
            args=(name,password)

            mycursor.execute(query,args)
            mydb.commit()
            print("data add success full")
        print(account())
    elif choice==2:
        def update():
            id=int(input("Enter your id :"))
            name=input("Enter your name:")
            password=input("Enter your password:")

            query=("update account set name=%s ,password=%s where id =%s")
            args=(name,password,id)

            mycursor.execute(query,args)
            mydb.commit()
        print(update())
    elif choice==3:
        def delete():
            id=int(input("Enter your id :"))

            query=("delete from account where id=%s")
            args=(id)

            mycursor.execute(query,args)
            mydb.commit()
        print(delete())
    elif choice==4:
        def fetch():
            query="select*from account"
            mycursor.execute(query)

            data=mycursor.fetchall()
            print(data)
        print(fetch())
    elif choice==5:
        print("THANK YOU")
        break
            

            


    