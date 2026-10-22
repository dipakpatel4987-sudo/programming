class Grandparent:
    def show1(self):
        print("Grandparent class")

class Parent(Grandparent):
    def show2(self):
        print("Parent class")

class Child(Parent):
    def show3(self):
        print("Child class")

obj = Child()

obj.show1()
obj.show2()
obj.show3()