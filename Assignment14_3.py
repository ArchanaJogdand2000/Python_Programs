# Write a lambda function which accept two numbers and returns maximum number

Max = lambda No1,No2 : No1 > No2

def main():
    print("Enter number :")
    Value1 = int(input())

    print("Enter number :")
    Value2 = int(input())

    iRet = Max(Value1,Value2)
    if(iRet == True):
        print(Value1,"is greater")
    else:
        print(Value2,"is greater")

if __name__ == "__main__":
    main()








