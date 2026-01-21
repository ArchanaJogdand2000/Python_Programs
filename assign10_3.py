# Write a program which accept one number and prints factorial of that number

def Table(No):
    Fact = 1
   
    if(No < 0):
        No = -No

    for i in range(1,No+1):
        Fact = Fact * i
        
    return Fact     

def main():

   iRet = 0
  
   print("Enter a number :")
   Value = int(input())

   iRet = Table(Value)
   print("Factorial of given number is :",iRet)
   
   
if __name__ == "__main__":
    main()