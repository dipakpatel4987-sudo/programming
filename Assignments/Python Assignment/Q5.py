''': Write a Python program to print each fruit in a list using a simple for
loop. List1 = ['apple', 'banana', 'mango']'''

# List1 = ['apple', 'banana', 'mango']

# for fruit in List1:
#     print(fruit)


'''Write a Python program to find the length of each string in List1.'''

# List1 = ['apple', 'banana', 'mango']

# for fruit in List1:
#      print(fruit,"=",len(fruit))




''' Write a Python program to find a specific string in the list using a simple
for loop and if condition.'''

# List1 = ['apple', 'banana', 'mango']

# search=input("enter fruit name:")

# found= False

# for furit in List1:
#     found=True
#     furit == search

# if found:
#     print("Fruit found in the list.")
# else:
#     print("Fruit not found in the list.")

'''Print this pattern using nested for loop:
markdown
Copy code
*
**
***
****
***** '''

row=5

for i in range(1,row +1):
    for j in range(i):
        print("*", end=" ")
    print()