#1) Single Inheritance
class Parent:
    def show(self):
        print("This is parent class")

class Child(Parent):
    def display(self):
        print("This is child class")

obj = Child()
obj.show()
obj.display()
#2) Multilevel Inheritance

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

#3) Multiple Inheritance


class Father:
    def father(self):
        print("Father class")

class Mother:
    def mother(self):
        print("Mother class")

class Child(Father, Mother):
    def child(self):
        print("Child class")

obj = Child()
obj.father()
obj.mother()
obj.child()

#4) Hierarchical Inheritance

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

#5) Hybrid Inheritance



class A:
    def showA(self):
        print("Class A")

class B(A):
    def showB(self):
        print("Class B")

class C(A):
    def showC(self):
        print("Class C")

class D(B, C):
    def showD(self):
        print("Class D")

obj = D()

obj.showA()
obj.showB()
obj.showC()
obj.showD()