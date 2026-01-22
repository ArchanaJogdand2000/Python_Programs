# write a program which contains one function named as ChkNum() which accept one parameter as number.
# if number is even then it should display "Even number" otherwise display "Odd number" on console

def ChkEven(No):
    if(No % 2 == 0):
      return True
    else:
        return False
    
def main():
    print("Enter number : ")
    Value = int(input())

    iRet = ChkEven(Value)
    if(iRet == True):
        print("Even number")
    else:
        print("Odd number")

if __name__ == "__main__":
    main()