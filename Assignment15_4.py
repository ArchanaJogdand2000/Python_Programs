# Write a lambda function using reduce() which accepts a list of number and returns the addition of all elements

from functools import reduce

Add = lambda A, B :  A + B

def main():
    print("Enter number of elements :")
    Size = int(input())

    Data = list()

    print("enter elements that we want to addition of them :")
    
    for no in range(Size):
        Value = int(input())
        Data.append(Value)
    
    RData = reduce(Add,Data)
    print("Addition of given data is : ",RData)

if __name__ == "__main__":
    main()








