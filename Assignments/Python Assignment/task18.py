"""Write a Python program that uses a custom iterator to iterate over a list of integers.""" 
def kay(data):
    for item in data:
        yield item

number=[10,20,30,40,50]

for num in kay(number):
    print(num)