'''Write a Python program to apply the map() function to square a list of numbers'''

number=[1,2,3,4,5]

def squared_numbers(x):
    return x*x
result=map(squared_numbers,number)

print("original list:",number)
print("squared list",list(result))