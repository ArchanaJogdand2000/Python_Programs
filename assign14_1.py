# Write a lambda function which accept one number and returns square of that number

sqr = lambda No : No * No

def main():
    print("Enter number :")
    Value = int(input())

    iRet = sqr(Value)
    print("Square is",iRet)

if __name__ == "__main__":
    main()








