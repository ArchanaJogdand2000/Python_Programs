# Write a program which contains one lambda function
#  which accept two parameter and return its multiplication

PowerOfTwo = lambda No1, No2 : No1 * No2

def main():
    print("Enter first number :")
    Value1 = int(input())

    print("Enter second number :")
    Value2 = int(input())

    iRet = PowerOfTwo(Value1,Value2)
    print("multiplication is",iRet)


if __name__ == "__main__":
    main()

