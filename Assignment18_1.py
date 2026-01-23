# Write a program which accept N numbers from user and store it into lits. 
# retuen addition of all elements from that list

def Summation(Arr):
    Sum = 0

    for i in range(len(Arr)):
        Sum = Sum + Arr[i]

    return Sum   
   
def main():
    print("enter the number of elements")
    Size = int(input())

    Data = list()

    print("enter the elements")
    
    for no in range(Size):
        Value = int(input())
        Data.append(Value)

    iRet = Summation(Data)
    print("addition of given numbers is :",iRet)

if __name__ == "__main__":
    main()

   