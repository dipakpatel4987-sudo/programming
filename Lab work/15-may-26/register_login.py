import random

user={}#empty dictionary
while True:


    print("====WELLCOME====")
    print("1.Register!!!")
    print("2.Login")

    try:
        choice=int(input("Enter choice:"))


        if choice==1:
            
                    username=input("Enter Username:")
                    Password=input("Enter Password:")
                    cfpassword=input("Enter conform password:")

                    user_id=random.randint(1,10000)

                    if Password==cfpassword:

                        otp=random.randint(1001,9999)

                        print("\nyour otp",otp)

                        user_otp=int(input("Enter OTP for verification:"))
                
                        if user_otp==otp:

                            user[username]={
                                "password":Password,
                                "id":user_id
                            }
                            print("\nRegistration Successful!")
                            print("Your User ID is:", user_id)

                        else:
                            print("Wrong OTP! Registration Failed.")

                    else:
                        print("Password don't match ")
                        break

                

        elif choice==2:

                username=input("Enter your name:")
                Password=input("Enter your password:")

                if username in user:
                    if user[username]["password"]==Password:

                        otp=random.randint(1001,9999)
                        print("\nyour otp",otp)

                        user_otp=int(input("Enter Login OTP:"))

                        if user_otp==otp:

                            print("\n login seccessfolly!!!")
                            print("WELLCOME",username)
                            print("Your ID:",user[username]["id"])

                        else:
                            print("Wrong otp!!")

                    else:
                        print("Wrong passwrod or name")

                else:
                        print("User not found!")
                        break

        else:
            print("Invaild choice")
            break
    
    except Exception as e:
            print(e)
            print("invalid input!!!")


        
        
            



