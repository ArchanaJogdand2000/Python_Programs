# write a program which accept one number and print count of digits in that number

def CountDigit(No):
    Count = 0
    Digits = 0

    if(No < 0):
        No = -No

    while(No > 0):
        Digits = int(No % 10)
        print(Digits)
        
        No = int(No / 10)
        Count = Count + 1
    return Count    
       

def main():

   iRet = 0
  
   print("Enter a number :")
   Value = int(input())

   iRet = CountDigit(Value)
   print("digits in given number are:",iRet)


if __name__ == "__main__":
    main()
