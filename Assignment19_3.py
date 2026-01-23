from functools import  reduce

ChkRange = lambda No1: No1 if (No1 >= 70 and No1 <= 90) else 0

Update = lambda No1 : No1 + 10

Product = lambda No1, No2 : No1 * No2

def main():
    print("Enter number of elements :")
    Size = int(input())

    Data = list()

    print("Enter elements :")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    FData = list(filter(ChkRange,Data))
    print("Data after filter",FData)

    MData =  list(map(Update,FData))
    print("Data after mapping",MData)

    RData = reduce(Product,MData)
    print("Data after recuce :",RData)

if __name__ == "__main__":
    main()

