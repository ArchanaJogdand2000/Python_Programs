# Write a lambda function which accept two numbers and returns minimum number

Mini = lambda No1,No2 : No1 < No2

def main():
    print("Enter number :")
    Value1 = int(input())

    print("Enter number :")
    Value2 = int(input())

    iRet = Mini(Value1,Value2)
    if(iRet == True):
        print(Value1,"is minimum")
    else:
        print(Value2,"is minimum")

if __name__ == "__main__":
    main()








