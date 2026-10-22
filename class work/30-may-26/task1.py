import random
class Parent:
    def prime(self):
        n=int(input("Enter your number:"))
        prime=0
        for i in range(1,n+1):
            if n%i==0:
                prime+=1
        if prime==2:
            print("number is prime!!")
        else:
            print("Number is not prime!!!")
class Child(Parent):
    def reverse(self):
        n=input("Enter reverse number!!!")
        # rev=0
        # for i in range(n):
        #     digit=n%10
        #     rev=rev*10+digit
        #     n=n//10
        # print(rev)
        rev=""
        for i in n:
            rev=i+rev
        print("Reverse number:",rev)
class child2(Child):
    def otp1(self):
        otp=random.randint(111,999)
        print("Your number:",otp)
        user_otp=int(input("Enter your otp:"))
        if user_otp==otp:
            print("Number Add seccessfully!!!")
        else:
            print("worng nummber!!!")

obj=child2()
print("prime number!!")
print("Reverse number!!")
print("OTP number!!")
choice=int(input("Enter your choice:"))
if choice==1:
    obj.prime()
elif choice==2:
    obj.reverse()
elif choice==3:
    obj.otp1()
else:
    print("Wrong choice!!")