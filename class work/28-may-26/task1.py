class MyClass:
    def prime(self):
        n=int(input("Enter your number:"))
        prime=0

        for i in range(1,n+1):
            if n%i==0:
                prime+=1
        if prime==2:
            print("number is prime!!!")
        else:
            print("Number is not prime")

class Myclass1:
    def rev(self):
        # n=int(input("Enter your number:"))
       

        # for i in range(n+1):
        #     digit=n%10
        #     reverse=reverse*10 + digit
        #     n=n // 10
        # print("Reverse number:",reverse)
        num = int(input("Enter Number: "))
        reverse = 0

        while num > 0:
            digit = num % 10
            reverse = reverse * 10 + digit
            num = num // 10

        print("Reverse Number =", reverse)
class MyClass2:
     
        def fun1(self):
            for i in range(1, 6):
                print("*" * i)


obj=MyClass()
obj1=Myclass1()

while True:
    
    print("<-----mainu--------->")

    print("prime")
    print("reverse number")
    print("pattent")
    choice=int(input("Enter number:"))
    if choice==1:
        obj.prime()
    elif choice==2:
        obj1.rev()
    
    
    else:
        print("invaild choice")

    