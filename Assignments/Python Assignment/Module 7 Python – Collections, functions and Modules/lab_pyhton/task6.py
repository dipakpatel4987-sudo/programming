    # Write a Python program to sort a list using both sort() and sorted().

list=[50,40,30,20,10]

print("Original List")
print(list)

list.sort()
print("After using sort()")
print(list)

new_list=sorted(list,reverse=True)

print("\nList after sorted() ")
print(new_list)