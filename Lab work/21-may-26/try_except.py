import random
user={}
while True:
    try:
        print("\n<----CHOICE---->\n")
        print("Regiter From\n")
        print("Login From\n")

        choice=int(input("Enter your choice!!!"))

        if choice==1:
            try:
                username=input("Enter your name:")
              
                password=input("Enter your password:")
                cfpassword=input("Enter your conform password:")
                user_id=random.randint(1,999)

                if password==cfpassword:
                    otp=random.randint(1001,9999)
                    print("Your OTP:",otp)

                    user_otp=int(input("Enter The OTP:"))
                    if user_otp==otp:
                        user[username]={
                            "password":password,
                            "ID":user_id
                        }
                        print("Your regisration successfully!!!\n")
                        print("Your user.ID:",user_id)
                        print(user)
                    else:
                        print("Wrong OTP!!\n")
                else:
                    print("Password Dos't match!!!\n")
            except Exception as p:
                print(p)
                print("Somthing Wrong!!!\n")

        elif choice==2:
            try:
                username=input("Enter your username:")
                password=input("Enter the password:")

                
                if user[username]["password"]==password:
                    otp=random.randint(1001,9999)
                    print("Your OTP :",otp)
                    user_otp=int(input("Enter your OTP:"))
                    if user_otp==otp:
                        print("\nLOGIN successfully!!!\n")
                        print("Wellcome,",username)
                        print("\nUSER ID:",user_id)
                    else:
                        print("WRONG OTP")
                else:
                    print("WRONG PASSWORD!!!")

            except Exception as a:
                print(a)
        
        else:
            print("Invaild choice!!!")
            break

    except Exception as e:
        print(e)
        print("invaild input!!!")
