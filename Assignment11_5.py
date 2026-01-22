# Write a program which accept one number and check whether it is palindrom or not
# 
# --------a number (such as 16361) that remains the same when its digits are reversed.---------------------


def Palindrom(No):
    iRev = 0
    Digit = 0
    temp = No
    
    if(No < 0):
        No = -No

    while(No > 0):
        Digit = No % 10
        iRev = (iRev * 10) + Digit
        No = int(No / 10)

        if(iRev == temp):

            return True  
       

def main():

   iRet = 0
  
   print("Enter a number :")
   Value = int(input())

   iRet = Palindrom(Value)
   if(iRet == True):
      print("given number is palindrom : ")
   else:
      print("given number is not palindrom : ")
       
       
   


if __name__ == "__main__":
    main()
