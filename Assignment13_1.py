# Write a program which accept length and wirth of rectangle and prints area

def AreaOfRect(lengh, width):

    Area = lengh * width
    return Area


def main():
    print("Enter lenth of rectangle : ")
    len = int(input())

    print("Enter width of rectangle : ")
    Wid = int(input())
    
    iRet = AreaOfRect(len,Wid)
    print("Area of reactangle is : ",iRet)


if __name__ == "__main__":
    main()
