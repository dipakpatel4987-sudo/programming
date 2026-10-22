def fac_odd_even():
    n=int(input("Enter number:"))
    if(n%2==0):
        print("NUmber is even!!")
    else:
        print("NUmber is odd!!")

def date_convert():
    date=int(input("Enter the date:"))
    
    month=date*30
    print("month is ",month)

    year=date*365
    print("year is ",year)

    week=date*7
    print("week is",week)

def table():
    n1=int(input("enter number:"))

    for i in range(1,n1+1):
        i=n1*i
        print(i)

mainu="""
choice 1: fact number!!!
choice 2: prime number!!!
choice 3: rev number!!!
"""
while True:

    print(mainu)
    choice=int(input("enter your choice:"))
    if choice==1:
        fac_odd_even()
    elif choice==2:
        date_convert()
    elif choice==3:
        table()
    else:
        print("thank you!!")
        break