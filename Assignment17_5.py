# Write a program which accept one number from user and check whether number is prime or not

def ChkPrime(No):
   bFlage = True
   
   if (No <0):
      No = -No
   
   for i in range(2,(No//2) + 1):
       if(No % i == 0):
           bFlage = False
           break
   return bFlage
       
def main():
    print("Enter number :")
    Value = int(input())

    iRet = ChkPrime(Value)
    if(iRet == True):
       print("it is prime number")
    else:
       print("it is not prime")
    
if __name__ == "__main__":
    main()