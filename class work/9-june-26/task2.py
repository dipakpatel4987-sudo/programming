class A:
    def fun1(self):
        a=10
        self.a=a 
    
    def fun2(self):

        print(self.a)

obj=A()
obj.fun2()