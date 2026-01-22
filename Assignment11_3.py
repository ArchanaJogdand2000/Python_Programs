# Write a program which accept one number and print sum of digits 

def SumDigit(No):
    Sum = 0
    Digit = 0
    
    if(No < 0):
        No = -No

    while(No > 0):
        Digit = No % 10
        No = int(No / 10)

        Sum = Sum + Digit
        
    return Sum    
       

def main():

   iRet = 0
  
   print("Enter a number :")
   Value = int(input())

   iRet = SumDigit(Value)
   print("Addition of degits of a given number is:",iRet)


if __name__ == "__main__":
    main()
