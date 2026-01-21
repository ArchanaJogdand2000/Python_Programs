# Write a program which accept radius of circle and prints area of circle

def AreaOfRect(radius,pi=3.14):

    Area = pi*radius*radius
    return Area


def main():
    print("Enter radius of circle : ")
    Value = int(input())

    iRet = AreaOfRect(Value)

    print("Area of cirscle is : ",iRet)


if __name__ == "__main__":
    main()