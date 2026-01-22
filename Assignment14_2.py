# Write a lambda function which accept one number and returns cube of that number

cube = lambda No : No**3

def main():
    print("Enter number :")
    Value = int(input())

    iRet = cube(Value)
    print("cube",iRet)

if __name__ == "__main__":
    main()








