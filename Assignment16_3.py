#Addition of two numbers


def Add(No1,No2):
    Sum = No1 + No2
    return Sum

def main():
    print("Enter number : ")
    Value1 = int(input())

    print("Enter number : ")
    Value2 = int(input())

    iRet = Add(Value1,Value2)
    print("Addition is : ",iRet)
   
if __name__ == "__main__":
    main()