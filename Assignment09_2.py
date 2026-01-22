# Write a program which contains one function ChkGreater() that accepts two numbers and prints the grater number

def ChkGreater(No1,No2):
    if(No1 > No2):
      return True

    
def main():
   iRet = 0
   print("Enter first number :")
   Value1 = int(input())

   print("Enter second number :")
   Value2 = int(input())

   iRet = ChkGreater(Value1,Value2)

   if(iRet == True):
      print(Value1,"is greater")
   else:
      print(Value2,"is greater")
       
       


if __name__ == "__main__":
    main()
   
