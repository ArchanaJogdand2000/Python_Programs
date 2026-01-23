# Write a program which accept N numbers from user and store it into lits. 
# retuen mimimum number from that list

def Minimum(Arr):
    iMin = Arr[0]

    for i in range(len(Arr)):

        if(Arr[i] < iMin ):
           iMin = Arr[i] 
    return iMin
       
def main():
    print("enter the number of elements")
    Size = int(input())

    Data = list()

    print("enter the elements")
    
    for no in range(Size):
        Value = int(input())
        Data.append(Value)

    iRet = Minimum(Data)
    print("smallest number is :",iRet)

if __name__ == "__main__":
    main()

   