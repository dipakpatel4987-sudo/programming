mainu="""
choice 1: fact number!!!
choice 2: prime number!!!
choice 3: rev number!!!
"""
print(mainu)

while True:

    choice =int(input("enter choice:"))
    fact=1

    if choice==1:
        n=int(input("enter fact number:"))
        for i in range(1,n+1):
            fact=fact*i

        print(fact)
    elif choice==2:
        prime=0
        
        n=int(input("enter prime number:"))
        for i in range(1,n+1):
                 if(n%i==0):
                    prime+= 1
        
        if prime==2:
             print("number is prime:")
        else:
            print("number not prime:")
        

    elif choice==3:
            rev=0
            rem=0
            n=int(input("enter rev number:"))
            
            while(n>0):
                rem=n%10
                rev=rev*10+rem
                n//=10
                

            print(rev)
    elif choice==4:

        print("thank you!!")
        break


         



