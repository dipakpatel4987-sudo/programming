
'''Write a Python program to find greater and less than a number using
if_else.'''
# n1=int(input("Enter n1 Number:"))
# n2=int(input("Enter n2 Number:"))

# if(n1>n2):
#     print("n1 is greatest!!")
# else:
#     print("n2 is greatest!!")


# num=int(input("Enter number:"))


'''Write a Python program to check if a number is prime using if_else. '''

# if num <= 1:
#     print("not number is prime!!")

# elif num == 2 or num== 3 or num== 5 or num==7:
#     print("number is prime!!")

# elif num%2==0 or num%3==0 or num%5==0 or num%7==0:
#     print("not number is  prime!!")

# else:
#     print("prime number!!")

''' Write a Python program to calculate grades based on percentage using
if-else ladder.'''

# per=int(input("Enter percentage:"))

#  if(per>=80 and per<=100):
#      print("your gread is: A")
#  elif(per>=60 and per<=79):
#      print("your gread is: B")
#  elif(per>=35 and per<=59):
#      print("your gread is: C")
#  else:
#      print("you are fail 'batter luck next time!!'")


''' Write a Python program to check if a person is eligible to donate blood
using a nested if.
'''
age=int(input("enter your age: "))
weight=float(input("Enter your weight:"))

if(age>=18):
    if(weight>=50.0):
        print("You are eligible to donate blood.")
    else:
        print("You are not eligible (Weight must be at least 50 kg).")
else:
    print("You are not eligible (Age must be at least 18).")

