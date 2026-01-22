# Write a lambda function using reduce() which accepts a list of number
#  and returns the count of even numbers

from functools import reduce
                              
                             
CountEven = lambda  iCnt , No : iCnt + (1 if No % 2 == 0 else 0 )

def main():
    print("Enter number of elements :")
    Size = int(input())

    Data = list()

    print("enter elements :")
    
    for no in range(Size):
        Value = int(input())
        Data.append(Value)
    
    RData = reduce(CountEven,Data,0)
    print("Count of even numbers are : ",RData)

if __name__ == "__main__":
    main()








