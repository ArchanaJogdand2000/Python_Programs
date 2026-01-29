import gc # garbage collector

class Demo:
    Value = 10

    def __init__(self,A,B):
        self.no1 = A
        self.no2 = B

    def fun(self):
        print("Inside instantace method fun",self.no1,self.no2)

    def gun(self):
        print("Inside instantace method gun",self.no1,self.no2)

obj1 = Demo(11 ,21)
obj2 = Demo(51 , 101)

obj1.fun()
obj2.fun()

obj1.gun()
obj2.gun()


