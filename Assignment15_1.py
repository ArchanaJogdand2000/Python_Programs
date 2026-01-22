# Write a lambda function using map() which accepts a list of number and returns a list of squares os each number

square = lambda No : No * No

def main():
   
   print("Enter the number of elements")
   Size = int(input())

   Data = list()

   print("Enter Actual elements that you want square of these elements ")
   for i in range(Size):
       Value = int(input())
       Data.append(Value)  

   iRet = list(map(square,Data))
   print(iRet)

       
if __name__ == "__main__":
    main()








