import random

class Banck_Open:
    def open(self):
        username=input("Enter YOur name:")
        password=input("Enter your Password:")
        cfpassword=input("Enter Conform Password:")
        balance=50000
        self.balance=balance
        self.username=username
        self.password=password
        self.username=username

        if password==cfpassword:
            ac_number=random.randint(1000000000,9999999999)

            print("Username :",username)
            print("Account Number:",ac_number)
            print("Balance:",balance)
        else:
            print("Password is Wrong!!!")
    def diposit(self):
        username=input("Enter YOur name:")
        password=input("Enter your Password:")
        if username==self.username and password==self.password:
            damount=int(input("Enter your number:"))
            self.balance+=damount

            print("Balance:",self.balance)
        else:
            print("Password dosn't match!!!")
    def withdraw(self):
        username=input("Enter YOur name:")
        password=input("Enter your Password:")
        if username==self.username and password==self.password:
            withdraw=int(input("Enter your number:"))
            self.balance-=withdraw

            print("Balance:",self.balance)
        else:
            print("Password dosn't match!!!")
    def check_balance(self):
        username=input("Enter YOur name:")
        password=input("Enter your Password:")
        if username==self.username and password==self.password:
            
            print("Balance:",self.balance)
        else:
            print("Password dosn't match!!!")
obj=Banck_Open()
    
mainu="""
1.OPEN ACCOUNT!!!
2.EXIT
"""
print(mainu)
choice=int(input("Enter your choice:"))
while True:
    if choice==1:
        mainu1="""
1.Open Account
2.Diposit Amount
3.Withdraw Amount
4.Exit
"""
        print(mainu1)
        choice1=int(input("Enter your choice:"))
        if choice1==1:
            obj.open()
        elif choice1==2:
            obj.diposit()
        elif choice1==3:
            obj.withdraw()
        elif choice1==4:
            print("thank you!!!")
            break
    elif choice==2:
        print("thank you!!!")
        break
    


    
                
            
                

