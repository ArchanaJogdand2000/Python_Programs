#Write a program which contains one function that accept one number 
# from user and returns true if number is divisible by 5 otherwise return false

def Divisible(No):
    
    if((No % 5 )== 0):
       return True
    else:
        return False
        
    
def main():
    print("Enter number : ")
    Value = int(input())

    iRet = Divisible(Value)
    print(iRet)
    

if __name__ == "__main__":
    main()