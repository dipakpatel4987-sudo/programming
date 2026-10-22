class Father:
    def show_father(self):
        print("Father class")

class Mother:
    def show_mother(self):
        print("Mother class")

class Child(Father, Mother):
    def show_child(self):
        print("Child class")

obj = Child()

obj.show_father()
obj.show_mother()
obj.show_child()