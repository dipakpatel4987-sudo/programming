# Write a Python program to create a tuple with multiple data types.

my_tuple=(10,"apple",56.33,True,"A")

print("Original Tuple")
print(my_tuple)

print("\nElements with Data Types:")

for item in my_tuple:
    print(item,"->",type(item))