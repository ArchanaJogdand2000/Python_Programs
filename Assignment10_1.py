# Write a program which accept one number and prints multiplication table of that number


def Table(No):
    mult = 1
   
    if(No < 0):
        No = -No
    
    print("multiplication table of ",No)
    for i in range(1,11):
        mult = i * No
        
        print(mult)

def main():

   iRet = 0
  
   print("Enter a number :")
   Value = int(input())

   iRet = Table(Value)
   
   
if __name__ == "__main__":
    main()
