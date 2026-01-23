from functools import  reduce

def main():
    print("Enter number of elements :")
    Size = int(input())

    Data = list()

    print("Enter elements :")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    FData = list(filter(lambda No:( No % 2 == 0),Data))
    print("Data after filter",FData)

    MData =  list(map(( lambda No : No * No ),FData))
    print("Data after mapping",MData)

    RData = reduce(lambda No1, No2 : No1 + No2,MData)
    print("Data after recuce :",RData)

if __name__ == "__main__":
    main()

