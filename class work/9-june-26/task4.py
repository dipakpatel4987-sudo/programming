from tkinter import *
from tkinter import messagebox
import sqlite3

# Database Connection
conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts(
    acc_no INTEGER PRIMARY KEY,
    name TEXT,
    password TEXT,
    balance REAL
)
""")
conn.commit()


class BankingSystem:

    def create_account(self):
        acc_no = int(acc_entry.get())
        name = name_entry.get()
        password = pass_entry.get()
        balance = float(balance_entry.get())

        cursor.execute("SELECT * FROM accounts WHERE acc_no=?", (acc_no,))
        account = cursor.fetchone()

        if account:
            messagebox.showerror("Error", "Account Already Exists!")
            return

        cursor.execute(
            "INSERT INTO accounts VALUES(?,?,?,?)",
            (acc_no, name, password, balance)
        )
        conn.commit()

        messagebox.showinfo("Success", "Account Created Successfully!")

    def login(self):
        acc_no = int(login_acc.get())
        password = login_pass.get()

        cursor.execute(
            "SELECT * FROM accounts WHERE acc_no=? AND password=?",
            (acc_no, password)
        )

        account = cursor.fetchone()

        if account:
            messagebox.showinfo("Success", "Login Successful")
        else:
            messagebox.showerror("Error", "Invalid Account or Password")

    def deposit(self):
        acc_no = int(login_acc.get())
        amount = float(amount_entry.get())

        cursor.execute(
            "UPDATE accounts SET balance = balance + ? WHERE acc_no=?",
            (amount, acc_no)
        )
        conn.commit()

        messagebox.showinfo("Success", "Amount Deposited")

    def withdraw(self):
        acc_no = int(login_acc.get())
        amount = float(amount_entry.get())

        cursor.execute(
            "SELECT balance FROM accounts WHERE acc_no=?",
            (acc_no,)
        )

        result = cursor.fetchone()

        if result:
            balance = result[0]

            if amount > balance:
                messagebox.showerror(
                    "Error",
                    "Insufficient Balance"
                )
            else:
                cursor.execute(
                    "UPDATE accounts SET balance = balance - ? WHERE acc_no=?",
                    (amount, acc_no)
                )
                conn.commit()

                messagebox.showinfo(
                    "Success",
                    "Withdrawal Successful"
                )

    def check_balance(self):
        acc_no = int(login_acc.get())

        cursor.execute(
            "SELECT balance FROM accounts WHERE acc_no=?",
            (acc_no,)
        )

        result = cursor.fetchone()

        if result:
            messagebox.showinfo(
                "Balance",
                f"Current Balance: ₹{result[0]}"
            )


bank = BankingSystem()

# Main Window
root = Tk()
root.title("Banking System")
root.geometry("500x600")

Label(root,
      text="BANKING SYSTEM",
      font=("Arial", 18, "bold")
      ).pack(pady=10)

# Registration Section
Label(root, text="Create Account",
      font=("Arial", 14, "bold")
      ).pack()

Label(root, text="Account Number").pack()
acc_entry = Entry(root)
acc_entry.pack()

Label(root, text="Name").pack()
name_entry = Entry(root)
name_entry.pack()

Label(root, text="Password").pack()
pass_entry = Entry(root, show="*")
pass_entry.pack()

Label(root, text="Opening Balance").pack()
balance_entry = Entry(root)
balance_entry.pack()

Button(root,
       text="Create Account",
       command=bank.create_account,
       bg="green",
       fg="white").pack(pady=10)

# Login Section
Label(root,
      text="Login",
      font=("Arial", 14, "bold")
      ).pack()

Label(root, text="Account Number").pack()
login_acc = Entry(root)
login_acc.pack()

Label(root, text="Password").pack()
login_pass = Entry(root, show="*")
login_pass.pack()

Button(root,
       text="Login",
       command=bank.login,
       bg="blue",
       fg="white").pack(pady=10)

# Transaction Section
Label(root, text="Amount").pack()
amount_entry = Entry(root)
amount_entry.pack()

Button(root,
       text="Deposit",
       command=bank.deposit).pack(pady=5)

Button(root,
       text="Withdraw",
       command=bank.withdraw).pack(pady=5)

Button(root,
       text="Check Balance",
       command=bank.check_balance).pack(pady=5)

root.mainloop()

conn.close()