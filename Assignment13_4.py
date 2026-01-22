# Write a program which accept one number and prints binary equivalent


def Binary(iNo):
    if(iNo == 0):
        print("The binary equivalent of 0 is 0")

    binary_digits = []
    
    while(iNo > 0):
        remainder = iNo % 2
        iNo = iNo // 2
        binary_digits.append(str(remainder)) # interger list string madhe convert keli
   
    binary_digits.reverse() 
    return "".join(binary_digits)# digits join kele 

    
def main():
    print("Enter number : ")
    Value = int(input())

    iRet = Binary(Value)
    print(iRet)

    
if __name__ == "__main__":
    main()
