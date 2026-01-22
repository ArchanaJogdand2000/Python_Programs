# Write a lambda function using filter() which accepts a list of numbers 
# and return a list of numbers divisible by 3 and 5

Divisible = lambda No : No if(No % 3 == 0) and (No % 5 == 0) else False

def main():
    print("Enter number of elements :")
    Size = int(input())

    Data = list()

    print("enter elemets :")
    
    for no in range(Size):
        Value = int(input())
        Data.append(Value)

    FData = list(filter(Divisible,Data))
    print("Data after filter",FData)
    
if __name__ == "__main__":
    main()








