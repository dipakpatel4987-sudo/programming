class Parent:
    def show(self):
        print("Parent class")

class Child1(Parent):
    def display1(self):
        print("Child 1 class")

class Child2(Parent):
    def display2(self):
        print("Child 2 class")

obj1 = Child1()
obj2 = Child2()

obj1.show()
obj1.display1()

obj2.show()
obj2.display2()