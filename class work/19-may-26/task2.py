

# try :
#     n= int(input("Enter your number:"))

#     if n%2==0:
#         print("even!!")
#     else:
#         print("odd!!")

# except ZeroDivisionError as e:
#     print(e)
# else:
#     print("else is running:")

# finally:
#     print("finally open!!")

try:
    n=int(input("Enter your number:"))
    n1=int(input("Enter number "))

    print("division number",n/n1)
    
except ZeroDivisionError as e:
    print(e)
