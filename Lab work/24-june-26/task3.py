from tkinter import *

root = Tk()
root.title("Registration Form")
root.geometry("500x500")
root.configure(bg="lightblue")

# Heading
title = Label(
    root,
    text="User Registration Form",
    font=("Arial", 20, "bold"),
    bg="lightblue",
    fg="darkblue"
)
title.pack(pady=20)

# Name
Label(root, text="Full Name", font=("Arial", 12), bg="lightblue").pack()
name_entry = Entry(root, width=30, font=("Arial", 12))
name_entry.pack(pady=5)

# Email
Label(root, text="Email", font=("Arial", 12), bg="lightblue").pack()
email_entry = Entry(root, width=30, font=("Arial", 12))
email_entry.pack(pady=5)

# Mobile Number
Label(root, text="Mobile Number", font=("Arial", 12), bg="lightblue").pack()
mobile_entry = Entry(root, width=30, font=("Arial", 12))
mobile_entry.pack(pady=5)

# Password
Label(root, text="Password", font=("Arial", 12), bg="lightblue").pack()
password_entry = Entry(root, width=30, show="*", font=("Arial", 12))
password_entry.pack(pady=5)

# Confirm Password
Label(root, text="Confirm Password", font=("Arial", 12), bg="lightblue").pack()
confirm_password_entry = Entry(root, width=30, show="*", font=("Arial", 12))
confirm_password_entry.pack(pady=5)

# Gender
Label(root, text="Gender", font=("Arial", 12), bg="lightblue").pack()

gender = StringVar()
Radiobutton(root, text="Male", variable=gender, value="Male",
            bg="lightblue").pack()
Radiobutton(root, text="Female", variable=gender, value="Female",
            bg="lightblue").pack()

# Register Button
Button(
    root,
    text="Register",
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    width=15
).pack(pady=20)

# Reset Button
Button(
    root,
    text="Reset",
    font=("Arial", 12, "bold"),
    bg="red",
    fg="white",
    width=15
).pack()

root.mainloop()