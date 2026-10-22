# Write a Python program to create a list with elements of multiple data types (integers,
# strings, floats, etc.).
my_list=["deepak",23,"A",67.44,True]

print("List elements:")

print(my_list)

print("\nElements with Data Types:")

for item in my_list:
    print(item,"->",type(item))