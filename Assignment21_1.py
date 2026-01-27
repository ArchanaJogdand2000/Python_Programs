# Design a python application that creates two threads named prime and nonprime.
# Both threads should accept a list of integers.
# The prime thread should display all prime numbers from list.
# The NonPrime thread should display all non-prime numbers from the list.

import threading
import time

def ChkPrime(No):
    if No<=1:
        return False
    for i in range(2,int(No/2)+1):
        if No%i==0:
            return False
    return True

def Prime(Arr):
    DataPrime=list()
    size=len(Arr)
    for i in range(size):
        if(ChkPrime(Arr[i])):
            DataPrime.append(Arr[i])
    print("The Prime numbers are:")
    print(DataPrime)

def NonPrime(Arr):
    DataNonPrime=list()
    size=len(Arr)
    for i in range(size):
        if(not ChkPrime(Arr[i])):
            DataNonPrime.append(Arr[i])
    print("The non-prime numbers are:")
    print(DataNonPrime)
        
def main():
    
    print("Enter the number of elements")
    Size = int(input())

    Data = list()

    print("Enter elements :")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    t1 = threading.Thread(target=Prime,args=(Data,))
    t2 = threading.Thread(target=NonPrime,args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()        