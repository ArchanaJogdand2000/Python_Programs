# Write a program which contains one lambda function which accept one parameter and return power of two

PowerOfTwo = lambda No : No * No

def main():
    print("Enter number :")
    Value = int(input())

    iRet = PowerOfTwo(Value)
    print(iRet)


if __name__ == "__main__":
    main()

