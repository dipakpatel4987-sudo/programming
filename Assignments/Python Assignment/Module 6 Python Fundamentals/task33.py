'''Write a Python program that uses reduce() to find the product of a list of numbers'''
from functools import reduce

number=[10,20,30,40,50]
def add(x,y):
    return x+y

result=reduce(add,number)

print("original list:",number)
print("reduce list:",result)