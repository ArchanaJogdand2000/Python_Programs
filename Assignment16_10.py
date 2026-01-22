# Write a program which accept name from user and display length of its name

def DisplayLen(str):

    print(len(str))
    
def main():
    print("Enter name : ")
    Value = input()

    DisplayLen(Value)
    
if __name__ == "__main__":
    main()