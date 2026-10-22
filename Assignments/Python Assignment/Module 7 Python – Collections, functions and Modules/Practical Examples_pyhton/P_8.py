# Python program to create a tuple with multiple data types

my_tuple = (100, "Python", 75.5, True, 'B')


print("Tuple Elements:")
print(my_tuple)

print("\nElements with Data Types:")

for item in my_tuple:
    print(item, "->", type(item))