# Write a program which accept one number and print sum of first N natural numbers 


def Table(No):
    Sum = 0
   
    if(No < 0):
        No = -No

    for i in range(1,No+1):
        Sum = i + Sum
        
    return Sum     

def main():

   iRet = 0
  
   print("Enter a number :")
   Value = int(input())

   iRet = Table(Value)
   print("Addition of given N numbers :",iRet)
   
   
if __name__ == "__main__":
    main()
