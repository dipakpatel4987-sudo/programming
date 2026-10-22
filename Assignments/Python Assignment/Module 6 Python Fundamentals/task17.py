"""Write a generator function that generates the first 10 even numbers."""
def sum():
    for i in range(1,11):
        yield i*2

for num in sum():
    print(num)