# Write a program which accept one number and prints square of that number

def Square(No):
   sqr = 0
   sqr = No * No

   return sqr

def main():
   iRet = 0
   print("Enter  number :")
   Value = int(input())

   iRet = Square(Value)
   print(iRet)

   
if __name__ == "__main__":
    main()
   
