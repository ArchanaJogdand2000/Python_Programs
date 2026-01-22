# Write a lambda function using reduce() which accepts a list of number and returns the maximum element

from functools import reduce

Maximum = lambda A, B : A if (A > B)else B

def main():
    print("Enter number of elements :")
    Size = int(input())

    Data = list()

    print("enter elements :")
    
    for no in range(Size):
        Value = int(input())
        Data.append(Value)
    
    RData = reduce(Maximum,Data)
    print("largest number is : ",RData)

if __name__ == "__main__":
    main()








