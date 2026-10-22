from tkinter import*

def login():
    root = Tk()
    root.geometry("500x500")
    root.title("REGISTRATION FORM")

    name = Label(root, text="Name", font=("Arial", 12, "bold"))
    name.place(x=50, y=50)
    password = Label(root, text="Password", font=("Arial", 12, "bold"))
    password.place(x=50, y=150)

    ename = Entry(root, bg="yellow")
    ename.place(x=250, y=50)

    epassword = Entry(root, bg="yellow", show="*")
    epassword.place(x=250, y=150)

