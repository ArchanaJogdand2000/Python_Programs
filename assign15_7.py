# Write a lambda function using filter() which accepts a list of string 
# and return a list of strings having length greater than 5

String = lambda str :str if (len(str)>5) else None

def main():
    print("Enter number of string :")
    Size = int(input())

    Data = list()

    print("enter strings :")
    
    for no in range(Size):
        Value = input()
        Data.append(Value)

    FData = list(filter(String,Data))
    print("Data after filter",FData)
    
if __name__ == "__main__":
    main()








