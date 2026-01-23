# List contains numbers which are accepted from user
# filter ------> filter out all prime numbers 
# Map ---------> map function will Multiple all numbers by 2
# reduce-------> reduce function will return maximum number from that number

from functools import  reduce

def ChkPrime(No):
    bflage = True

    for i in range(2,int(No/2)):
        if(No % i == 0):
           bflage = False
           break
    if(bflage == True):
        return No
    

def Maximum(No1,No2):
    if(No1>No2):
        return No1
    else:
        return No2
    

def main():
    print("Enter number of elements :")
    Size = int(input())

    Data = list()

    print("Enter elements :")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    FData = list(filter(ChkPrime,Data))
    print("Data after filter",FData)

    MData =  list(map(( lambda No : No * 2 ),FData))
    print("Data after mapping",MData)

    RData = reduce(Maximum,MData)
    print("Data after recuce :",RData)

if __name__ == "__main__":
    main()

