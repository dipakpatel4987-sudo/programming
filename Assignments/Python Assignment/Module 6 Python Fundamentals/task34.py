'''Write a Python program that filters out even numbers using the filter() function.'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

def is_odd(x):
    return x % 2 !=0 

result=filter(is_odd,numbers)

print("original number:",numbers)
print("filter number:",list(result))