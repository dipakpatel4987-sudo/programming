class A:
    def fun1(self):
        n=int(input("Enter your number:"))
        prime=0
        for i in range(n):
            if n %i==0:
                prime+=1
        if prime==2:
            print("number is prime!!!")
        else:
            print("number is not prime!!")
class B:
    def fun1(self):
        super.fun1()
        n=int(input("Enter your number:"))
        n1=int(input("Enter your number:"))
        print("Your number:",n+n1)
        print("Your number:",n-n1)
        print("Your number:",n*n1)
        print("Your number:",n/n1)
class C(A,B):
    
    def fun1(self):
        super.fun1()
        n=int(input("Enter your numbre:"))
        reverse=""
        for i in n:
            reverse=i + reverse
        print("reverse number=",reverse)

obj= C
obj.fun1()


