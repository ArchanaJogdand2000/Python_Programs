# Write a program which accept N numbers from user and store it into lits. 
# retuen maximum number from that list

def Maximum(Arr):
    iMax = Arr[0]

    for i in range(len(Arr)):

        if(Arr[i] > iMax ):
           iMax = Arr[i] 
    return iMax
       
def main():
    print("enter the number of elements")
    Size = int(input())

    Data = list()

    print("enter the elements")
    
    for no in range(Size):
        Value = int(input())
        Data.append(Value)

    iRet = Maximum(Data)
    print("largest number is :",iRet)

if __name__ == "__main__":
    main()

   