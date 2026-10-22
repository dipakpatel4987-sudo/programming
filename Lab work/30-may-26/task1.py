import random
user={}
try:
    class Login_From:
        def regiter(self):
            username=input("Enter your name:")
            password=input("Enter your password:")
            cfpassword=input("Enter conform password:")
            if password==cfpassword:
                otp=random.randint(1001,9999)
                user_id=random.randint(1,999)
                print("your OTP:",otp)
                user_otp=int(input("Enter OTP"))
                if user_otp==otp:
                    user[username]={
                        "password":password,
                        "ID":user_id
                    }
                    print("Your regisration successfully!!!\n")
                    print("Your user.ID:",user_id)
                    print(user)
                else:
                    print("Wrong Otp!!!")
            else:
                print("Wrong Password!!!")
        def login(self):
            username=input("Enter Your name:")
            password=input("Enter Your Password:")

            if user[username]["password"]==password:
                otp=random.randint(1001,9999)
                print("Your OTP:",otp)
                user_otp=int(input("Enter OTP:"))
                if user_otp==otp:
                    print("\nLOGIN successfully!!!\n")
                    print("Wellcome,",username)
                    print("\nUSER ID:",user["ID"])
                else:
                        print("WRONG OTP")
            else:
                print("WRONG PASSWORD!!!")


    obj=Login_From()

    while True:
        print("-"*20,"mainu","-"*20)
        print("Regiter From\n")
        print("Login From\n")
        print("EXIT\n")


        choice=int(input("Enter Your Choice:"))
        if choice==1:
            obj.regiter()
        elif choice==2:
            obj.login()
        else:
            print("EXITING!!!!")
            break

except Exception as p:
    print("invaild choice!!")
    print(p)
