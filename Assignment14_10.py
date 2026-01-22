# Write a lambda function which accept three numbers abd returns largest number

Max = lambda No1,No2,No3 : No1 if( No1 > No2 and No1 > No3) else (No2 if  No2 > No3 else No3) 

def main():
    print("Enter number :")
    Value1 = int(input())

    print("Enter number :")
    Value2 = int(input())

    print("Enter number :")                  
    Value3 = int(input())

    iRet = Max(Value1,Value2,Value3)
    
    print(iRet,"is largest")
    
if __name__ == "__main__":
    main()








