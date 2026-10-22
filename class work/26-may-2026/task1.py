class MyClass:
    def prime(self):
        prime=0
        n=int(input("Enter number:"))
        for i in range(1,n+1):
            if n%i==0:
                prime+=1
        
        if prime==2:
            print("numbe is prime")
        else:
            print("number not prime")
    
    def fun1(self):
       for i in range(1, 6):
        print("*" * i)

    def fun2(self):
        num = int(input("Enter Number: "))
        reverse = 0

        while num > 0:
            digit = num % 10
            reverse = reverse * 10 + digit
            num = num // 10

        print("Reverse Number =", reverse)



obj=MyClass()
while True:
    print("<-----mainu--------->")
    print("prime")
    print("reverse number")
    print("pattent")
    choice=int(input("Enter number:"))
    if choice==1:
        obj.prime()
    elif choice==2:
        obj.fun1()
    elif choice==3:
        obj.fun2()
    else:
        print("invaild choice")

    