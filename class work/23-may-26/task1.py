# # file=open("text.txt","w")

# # file.write("hello world")
# # file.close()

# file=open("text.txt","r")
# print(file.read())
# file.close()

# products = {
#     101: {"name": "Laptop", "price": 55000},
#     102: {"name": "Mouse", "price": 500},
#     103: {"name": "Keyboard", "price": 1200},
#     104: {"name": "Headphone", "price": 1500},
#     105: {"name": "USB Cable", "price": 250}
# }
#data=str(products)

fill=open("task1.txt","w")
fill.write(data)
fill.close()

file=open("task2.txt","w+")
file.write("w+ method !!")
print(file.tell())
file.seek(0)
print(file.read())
file.close()