import random
# otp=random.randint(100,999)
# print(otp)

lucky=random.randint(1,50)
print("****************number between 1 to 50!!******************" )

while True:
    

    for i in range(1,5):
        choice=int(input("Enter your number:"))

        if choice > 50:
            print("invaild number!!")
            break
        elif choice == lucky:
            print("You are win!!!")
        elif choice > lucky:
            print("number is geater then original number!!!")
        else:
            print("number is lower than original number!!!")


