# Write a program which accept one number and checks whether it is perfect or not 

def PerfectNumber(iNo):
    Sum = 0

    
    if(iNo < 0):  #updater
   
       iNo = -iNo
   
    for i in range(1,iNo):

        if((iNo % i)== 0):
            Sum = Sum + i

    if(Sum == iNo):
        return True
    else:
        return False

def main():
    print("Enter number : ")
    Value = int(input())

    iRet = PerfectNumber(Value)

    if(iRet == True):
        print("perfect number")
    else:
        print("Not perfect number")

   

if __name__ == "__main__":
    main()
