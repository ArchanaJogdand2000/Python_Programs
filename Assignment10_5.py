# Write a program which accept one number and prints all odd numbers till that number

def Table(No):
    Fact = 1
   
    if(No < 0):
        No = -No

    for i in range(1,No+1):
       if((i%2)!=0):
           print(i)
        

def main():

   iRet = 0
  
   print("Enter a number :")
   Value = int(input())

   iRet = Table(Value)
   
   
   
if __name__ == "__main__":
    main()
