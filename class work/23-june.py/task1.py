class User:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self, obj1):
        x=self.a+obj1.a
        y=self.b+obj1.b
        return x,y

obj=User(10,20)
print(obj)

obj1=User(30,40)
print(obj)
print("cunstructuter",obj+ obj1)