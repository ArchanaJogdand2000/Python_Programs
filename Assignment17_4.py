# Write a program which accept number from user and 
# return addition of its factor
     
def AddFactors(No):
    Sum = 0

    if(No < 0):
        No = -No
     
    for i in range(1,( (No//2) + 1) ):
        if(No % i == 0):
           Sum = Sum + i
        
    return Sum
   
def main():
    print("Enter number :")
    Value = int(input())

    iRet = AddFactors(Value)
    print("Additon of factors is :",iRet)


if __name__ == "__main__":
    main()

   