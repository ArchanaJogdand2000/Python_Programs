#Write a program which accepts one number and checks whethers it is prime or not

def CheckPrime(No):
   for i in range(2, int(No/2)+1):
     if((No%i)== 0):
       
       return False
      

def main():
   number = 0
  
   print("Enter a number :")
   number = int(input())

   iRet = CheckPrime(number) 

   if(iRet == False):
       print("Given number is not prime")
   else:
       print("Given number is prime")
      
 

if __name__ == "__main__":
    main()
