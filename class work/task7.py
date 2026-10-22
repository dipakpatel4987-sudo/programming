#nested if-else
n1=int(input("Enter number 1: "))
n2=int(input("Enter number 2: "))
n3=int(input("Enter number 3: "))
n4=int(input("Enter number 4: "))

if(n1>n2):
    if(n1>n3):
        print("number 1 is greatest!!")
    
    elif(n1>n4):
        print("number 1 is greatest")

    else:
        print("number 3 is greatest!!")

else:
    if(n2>n3):
        print("number 2 is greatest!!!")

    elif(n2>n4):

        print("number 2 is greatest")

    else:
        print("number 4 is greatest!!")