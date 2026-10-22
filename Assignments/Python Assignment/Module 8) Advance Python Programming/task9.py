class Animal:
    def sound(self):
        print("Animals make sounds")

class Dog(Animal):
    # Overriding parent method
    def sound(self):
        print("Dog barks")

# Creating object
obj = Dog()

# Calling overridden method
obj.sound()