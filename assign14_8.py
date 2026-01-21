# Write a lambda function which accept two numbers and returns addition

Add = lambda No1,No2 : No1 + No2

def main():
  
    iRet = False
    
    print("Enter number :")
    Value1 = int(input())

    print("Enter number :")
    Value2 = int(input())

    iRet = Add(Value1,Value2)
    
    print("Addition is",iRet)
       
if __name__ == "__main__":
    main()   







