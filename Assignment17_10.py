# Write a program which accept number from user and 
# return addition of digits in that number 
     
def AddDigit(No):
    Sum = 0

    if(No < 0):
       No = -No
    
    while(No > 0):
       Digit = No % 10
       Sum = Sum + Digit
       No = No // 10      # in python if we use / oprator then give answer in flaat division 
                          # thats why loop is continuously rotate 
    return Sum

def main():
    print("Enter number :")
    Value = int(input())

    iRet = AddDigit(Value)
    print("addition of digits is :",iRet)


if __name__ == "__main__":
    main()

   