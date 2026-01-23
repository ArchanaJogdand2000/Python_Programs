# Write a program which accept N numbers from user and store it into lits. 
#Return addition of all prime numbers from that List. Main python file accepts N numbers from user and pass each 
# number to ChkPrime() function which is part of out user define module named as MarvellousNum. 
# Name of the function from main python file should be ListPrime().

import MarvellousNum18_5

   
def ListPrime(Arr):
    Sum = 0
    i = 0
    for i in range(len(Arr)):
        if MarvellousNum18_5.ChkPrime(Arr[i]):
            Sum = Sum + Arr[i]
    return Sum

def main():


    print("enter the number of elements")
    Size = int(input())

    Data = list()

    print("enter the elements")

    for no in range(Size):
        Value = int(input())
        Data.append(Value)


    iRet = ListPrime(Data)
    print("Addition of all prime numbers is:", iRet)

if __name__ == "__main__":
     main()




   