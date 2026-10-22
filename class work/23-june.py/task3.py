from tkinter import *
from task44 import*
from task4 import*
from task5 import*
import pymysql



root = Tk()
root.geometry("500x500")
root.title("REGISTRATION FORM")

mydb=pymysql.connect(host="localhost",
                     user="root",
                     password="",
                     port=3307)
mycursor=mydb.cursor()

mycursor.execute("create database if not exists registration_from")
mydb.commit()
mydb=pymysql.connect(host="localhost",
                     user="root",
                     password="",
                     database="registration_from",
                     port=3307)
mycursor=mydb.cursor()

mycursor.execute("""create table if not exists registration(
                 name varchar(50),
                 email varchar(50),
                 password varchar()
)""")
mydb.commit()
def insert_data():
    name=ename.get()
    email=eemail.get()
    password=epassword.get()

    query=("insert into registration_from(name,email,password) values (%s,%s,%s)")
    args=(name,email,password)
    mycursor.execute(query,args)




name = Label(root, text="Name", font=("Arial", 12, "bold"))
name.place(x=50, y=50)

email_lbl = Label(root, text="Email", font=("Arial", 12, "bold"))
email_lbl.place(x=50, y=100)

password = Label(root, text="Password", font=("Arial", 12, "bold"))
password.place(x=50, y=150)

mobile = Label(root, text="Mobile", font=("Arial", 12, "bold"))
mobile.place(x=50, y=200)


ename = Entry(root, bg="yellow")
ename.place(x=250, y=50)

eemail = Entry(root, bg="yellow")
eemail.place(x=250, y=100)

epassword = Entry(root, bg="yellow", show="*")
epassword.place(x=250, y=150)

emobile = Entry(root, bg="yellow")
emobile.place(x=250, y=200)


insert_btn = Button(root, text="INSERT",
                    font=("Arial", 16, "italic"),
                    fg="red",
                    command=login)
insert_btn.place(x=100, y=250)

update = Button(root, text="Update",
                    font=("Arial", 16, "italic"),
                    fg="red",
                    command=update
                   )
update.place(x=200, y=250)

delete = Button(root, text="Delete",
                    font=("Arial", 16, "italic"),
                    fg="red",
                    command=delete
                   )
delete.place(x=300, y=250)

root.mainloop()