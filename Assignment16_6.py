#Write a program which accept number from user and check whether that 
# number number is positive or negative or zero

def ChkNum(No):
    
    if(No== 0):
       return 1
    elif(No < 0):
        return 2
    else:
        return 3
    
def main():
    print("Enter number : ")
    Value = int(input())

    iRet = ChkNum(Value)

    if(iRet == 1):
        print("number is zero")
    elif(iRet == 2):
        print("number is negative")
    else:
        print("number is positive")
   
   
if __name__ == "__main__":
    main()