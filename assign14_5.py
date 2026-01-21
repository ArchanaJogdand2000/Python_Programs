# Write a lambda function which accept one number and returns True if number is even otherwise False

#def CheckEven(No):
 #  return (No % 2 == 0)
CheckEven = lambda No : (No % 2 == 0)

       
def main():
    Value = 0
    iRet = False
    
    print("Enter number : ")
    Value = int(input())

    iRet = CheckEven(Value)
   
    if(iRet == True):
        print("it is even ")
    else:
        print("it is odd ")    


if __name__ == "__main__":
    main()   







