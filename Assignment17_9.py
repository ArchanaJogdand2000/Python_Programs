# Write a program which accept number from user and 
# return number of digits in that number 
     
def NumDigit(No):
    iCnt = 0

    if(No < 0):
    
       No = -No
    
    while(No > 0):
       
       No = No // 10      # in python if we use / oprator then give answer in flaat division 
       iCnt = iCnt + 1        # thats why loop is continuously rotate 

    return iCnt

def main():
    print("Enter number :")
    Value = int(input())

    iRet = NumDigit(Value)
    print("number of digits are :",iRet)


if __name__ == "__main__":
    main()

   