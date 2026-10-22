# i=1
# ev=0
# od=0
# evsum=0
# oddsum=0
# evtotal=0
# odtotal=0
# sum=0
# while(i<=5):

#     n=int(input("Enter the number: "))
#     if(n%2==0):
#         print("evenn!!")
#         ev=ev+1
#         evsum=evsum+1
#         evtotal=evtotal+n
#     else:
#         print("odd!!")
#         od=od+1
#         oddsum=oddsum+n
    
#     sum=sum+n
#     i=i+1

# print("ev",ev)
# print("od",od)
# print("evsum",evsum)
# print("odsum",oddsum)
# print("evtotal",evtotal)
# print("odtotal",odtotal)
# print("total",sum)

# i=int(input("enter number"))
# sum=0
# while(i>=1):
#     print(i)
#     sum=sum+i
#     i=i-1
# print("sum",sum)

i=int(input("enter number"))
sum=1
while(i>=1):
    print(i)
    sum=sum*i
    i=i-1
print("sum",sum)