# Write a lambda function which accept one number and returns True if number is odd otherwise False

#def CheckEven(No):
 #  return (No % 2 != 0)
CheckOdd = lambda No : (No % 2 != 0)

       
def main():
    Value = 0
    iRet = False
    
    print("Enter number : ")
    Value = int(input())

    iRet = CheckOdd(Value)
   
    if(iRet == True):
        print("it is odd ")
    else:
        print("it is even ")    


if __name__ == "__main__":
    main()   







