# Write a lambda function which accept one number and returns True if divisible by 5


ChkDivisible = lambda No : (No % 5 == 0)

       
def main():
    Value = 0
    iRet = False
    
    print("Enter number : ")
    Value = int(input())

    iRet = ChkDivisible(Value)
   
    if(iRet == True):
        print("True")
    else:
        print("False")    


if __name__ == "__main__":
    main()   







