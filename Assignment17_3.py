# Write a program which accept number from user and 
# return its factorial
     
def Factorial(No):
    fact = 1
    
    for i in range(1,No+1):
        fact = fact * i

    return fact
   
def main():
    print("Enter number :")
    Value = int(input())

    iRet = Factorial(Value)
    print("Factorial is :",iRet)


if __name__ == "__main__":
    main()

   