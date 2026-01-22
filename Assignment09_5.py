# Write a program which accept one number and checks whether it is divisible by 3 and 5

def ChkDivisible(No):

   if(((No%3)==0) and ((No%5)==0)):
      return True
   else:
      return False

   
def main():
   iRet = 0

   print("Enter  number :")
   Value = int(input())

   iRet = ChkDivisible(Value)

   if(iRet == True):
      print("Divisible by 3 and 5")
   else:
      print("Not divisible by 3 and 5")   

   
if __name__ == "__main__":
    main()
   
