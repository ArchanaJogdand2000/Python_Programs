class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter first number : "))
        self.Value2 = int(input("Enter second number : "))
    
    def Addition(self):
        Add = 0
        Add = self.Value1 + self.Value2
        print("Additon is :",Add)
    
    def Subtraction(self):
        Sub = 0
        Sub = self.Value1 - self.Value2
        print("Subtraction is :",Sub)

    def Multiplication(self):
        Mult = 0
        Mult = self.Value1 * self.Value2
        print("Multiplication is :",Mult)

    def Division(self):
        div = 0
        try:
            div = self.Value1 / self.Value2
            print("Division is :",div)

        except ZeroDivisionError as zobj:
            print("Division by zero is not allowed!")
        

obj = Arithmetic()
obj.Accept()
obj.Addition()
obj.Subtraction()
obj.Multiplication()
obj.Division()