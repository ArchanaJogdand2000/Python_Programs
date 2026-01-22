# Write a program which accept one number and prints reverse of that number 

def ReverseNumber(No):
    iRev = 0
    Digit = 0
    
    if(No < 0):
        No = -No

    while(No > 0):
        Digit = No % 10
        iRev = (iRev * 10) + Digit
        No = int(No / 10)

    return iRev   
       

def main():

   iRet = 0
  
   print("Enter a number :")
   Value = int(input())

   iRet = ReverseNumber(Value)
   print("Reverse number is : ",iRet)
   


if __name__ == "__main__":
    main()
