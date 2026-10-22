import pymysql
import random

bank={}
class BankingSystem:
    # Create Database
    mydb = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        port=3307
    )

    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS banking_system")
    mydb.commit()




    def open_account(self):

        username = input("Enter Your Name: ")
        password = input("Enter Password: ")
        cfpassword = input("Confirm Password: ")
        balance = 50000

        if password == cfpassword:

            a_no = random.randint(1000000000, 9999999999)

            print("\nACCOUNT OPENED SUCCESSFULLY!")
            print("Username :", username)
            print("Account Number :", a_no)
            print("Balance :", balance)

            mydb = pymysql.connect(
                host="localhost",
                user="root",
                password="",
                port=3307,
                database="banking_system"
            )

            mycursor = mydb.cursor()

            mycursor.execute("""
                CREATE TABLE IF NOT EXISTS new_acc(
                    a_no BIGINT PRIMARY KEY,
                    username VARCHAR(50),
                    acc_password VARCHAR(50),
                    COMFORM_PASSWORD varchar(50),
                    balance INT
                )
            """)

            query = """
                INSERT INTO new_acc
                (a_no, username, acc_password,comform_password,balance)
                VALUES (%s, %s, %s, %s,%s)
            """

            value= (a_no, username, password,cfpassword,balance)

            mycursor.execute(query,value)
            mydb.commit()

            

        else:
            print("Passwords do not match!")
        self.a_no=a_no
        self.username = username
        self.password = password
        self.cfpassword = cfpassword
        self.balance = balance

        bank[username]={
            "Account_Number":a_no,
            "User Name":username,
            "Password":password,
            "Comform Password":cfpassword,
            "Balance":balance
        }
        print("Data Inserted Successfully!")
        
    def deposit(self):
        


        self.username=input("Enter your name:")
        self.password=input("Enter your password:")
        self.a_no=int(input("Enter your Account Number:"))

        if self.username in bank:
            if self.password==bank["username"]["password"] and self.a_no==bank["username"]["Account Number"] :
                otp=random.randint(1000,9999)
                print("YOUR OTP!!",otp)
                user_otp=int(input("Entre your otp:"))
                if otp==user_otp:
                    dep=int(input("Enter your DIPOSITE AMOUNT"))
                    self.balance+=dep
                    mydb=pymysql.connect(
                        host="localhost",
                        user="root",
                        password="",
                        port=3307,
                        database="banking_system"
                    )
                    mycursor=mydb.cursor()


                    mycursor.execute("""
                            CREATE TABLE if not exists DEPOSIT
                            (ACCOUNT_NUMBER BIGINT PRAMRY KEY ,
                            USERNAME VARCHAR(50),
                            acc_PASSWORD VARCHAR(50),
                            DEPOSIT_AMOUNT INT 
                            )"""
                    )
                    query="""
                    INSERT INTO DEPOSIT(ACCOUNT_NUMBER,USERNAME,acc_PASSWORD,DEPOSIT_AMOUNT)VALUES(%s,%s,%s,%s)
                    """
                    value=(self.a_no,self.username,self.password,dep)
                    mycursor.execute(query,value)
                    mydb.commit()

                    
                    query="""UPDATE new_acc SET BALANCE='%s' WHERE a_no='%s' """
                    value=(self.balance,self.a_no)
                    mycursor.execute(query,value)

                    mydb.commit()

                


                


obj = BankingSystem()
while True:
    mainu="""
    press 1 for OPEN AACOUNT 
    PRESS 2 FOR DEPOSIT
    """
    print(mainu)
    choice=int(input("Enter your number:"))
    if choice==1:
        obj.open_account()
    elif choice==2:
        obj.deposit()