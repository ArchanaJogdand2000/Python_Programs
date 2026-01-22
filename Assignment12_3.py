#write a program which accept two numbers and print addition, subtraction, multi.,and division.

def Add(No1,No2):
    Ans = 0
    Ans = No1 + No2

    return Ans

def Sub(No1,No2):
    Ans = 0
    Ans = No1 - No2

    return Ans

def Multiplication(No1,No2):
    Ans = 0
    Ans = No1 * No2

    return Ans

def Division(No1,No2):
    Ans = 0
    Ans = No1 / No2

    return Ans



def main():
   
    print("Enter first number : ")
    Value1 = int(input())

    print("Enter second number : ")
    Value2 = int(input())
    

    iRet = Add(Value1, Value2)
    print("Addition is :",iRet)

    iRet = Sub(Value1, Value2)
    print("Substraction is :",iRet)

    iRet = Multiplication(Value1, Value2)
    print("Multiplication is :",iRet)

    iRet = Division(Value1, Value2)
    print("Division is :",iRet)

     
if __name__ == "__main__":
    main()    
    
