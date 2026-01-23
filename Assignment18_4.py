# Write a program which accept N numbers from user and store it into lits. 
# Accept another number from user and return frequency of that number from list


def Frequency(Arr,No):
    freq = 0
   
    for i in range(len(Arr)):
        if(No == Arr[i]):
            freq = freq + 1
    return freq

def main():
    print("enter the number of elements")
    Size = int(input())

    Data = list()

    print("enter the elements")
    
    for no in range(Size):
        Value = int(input())
        Data.append(Value)

    print("Enter the number that you want to search in the list :")
    Number = int(input())

    iRet = Frequency(Data,Number)
    print("Frequency is :",iRet)

if __name__ == "__main__":
    main()

   