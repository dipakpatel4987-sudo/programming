n=int(input("Enter number:"))
a=0
b=1

print("this fibonacci series")

for i in range(n):
    print(a,end=" ")

    c=a+b
    a=b
    b=c
    c=a
    print("\n")
   

    

