# Write a lambda function using filter() which accepts a list of number and returns a list of even  numbers*

ChkEven = lambda No : (No % 2 == 0)

def main():
    print("Enter number of elements :")
    Size = int(input())

    Data = list()

    print("Enter Actual elements that you want check even or not ")
    for no in range(Size):
        Value = int(input())
        Data.append(Value)

    FData = list(filter(ChkEven,Data))
    print("Data after fiter is : ",FData)    
   
if __name__ == "__main__":
    main()








