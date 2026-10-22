from tkinter import *

root=Tk()
root.geometry("500x500")
root.title("REGISTRATION FORM")

name=Label(root,text="name",font=("arial",12,"blod"))
name.place(x=50,y=50)

email=Label(root,text="email",font=("arial",12,"blod"))
email.place(x=50,y=50)

password=Label(root,text="password",font=("arial",12,"blod"))
password.place(x=50,y=50)

mobile=Label(root,text="mobile",font=("arial",12,"blod"))
mobile.place(x=50,y=50)

ename=Entry(root,bg="yellow")
ename.place(x=250,y=100)

email=Entry(root,bg="yellow")
email.place(x=250,y=100)

epassword=Entry(root,bg="yellow")
password.place(x=250,y=100)

emobile=Entry(root,bg="yellow")
mobile.place(x=250,y=100)
INSERT=Button(root,font=("arial",16,"italic"),fg="red",text="insert")
INSERT.place(x=50,y=280)

root.mainloop()

