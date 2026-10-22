import tkinter as tk
from tkinter import messagebox
import sqlite3

# Create Database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    password TEXT
)
""")
conn.commit()


# Register Function
def register():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if name == "" or email == "" or password == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    cursor.execute(
        "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
        (name, email, password)
    )
    conn.commit()

    messagebox.showinfo("Success", "Registration Successful!")

    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)


# Main Window
root = tk.Tk()
root.title("Registration Form")
root.geometry("400x300")

# Heading
title = tk.Label(root, text="User Registration Form",
                 font=("Arial", 16, "bold"))
title.pack(pady=10)

# Name
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

# Email
tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root, width=30)
email_entry.pack(pady=5)

# Password
tk.Label(root, text="Password").pack()
password_entry = tk.Entry(root, width=30, show="*")
password_entry.pack(pady=5)

# Register Button
register_btn = tk.Button(root,
                         text="Register",
                         command=register,
                         bg="green",
                         fg="white",
                         width=15)
register_btn.pack(pady=20)

root.mainloop()

# Close Database Connection
conn.close()    