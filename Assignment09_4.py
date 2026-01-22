# Write a program which accept one number and prints cube of that number

def Cube(No):
   sqr = 0
   sqr = (No**3)

   return sqr

def main():
   iRet = 0
   print("Enter  number :")
   Value = int(input())

   iRet = Cube(Value)
   print(iRet)

   
if __name__ == "__main__":
    main()
   
