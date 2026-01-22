# Write a lambda function using reduce() which accepts a list of number
#  and returns the product of all elements 


from functools import reduce

Product = lambda A, B : A * B

def main():
    print("Enter number of elements :")
    Size = int(input())

    Data = list()

    print("enter elements :")
    
    for no in range(Size):
        Value = int(input())
        Data.append(Value)
    
    RData = reduce(Product,Data)
    print("product of given numbers is : ",RData)

if __name__ == "__main__":
    main()








