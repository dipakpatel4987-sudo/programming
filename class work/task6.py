print("star Date")
d1=int(input("Enter day:"))
m1=int(input("Enter month:"))
y1=int(input("Enter year:"))

print("End star")

d2=int(input("Enter  day:"))
m2=int(input("enter month:"))
y2=int(input("enter year:"))

total1= y1*365 + m1*31 + d1
total2= y2*365 + m2*31 + d2

total_difference = total2 - total1
month= total_difference/31
year =total_difference/365

print("result:",total_difference)

print("year:",year ,"month :",month ,"day:",total_difference)




