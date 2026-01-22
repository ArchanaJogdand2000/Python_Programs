#Write a program which accept number from user and print that number of "*" on sceen.

def Display(No):
    
    for i in range(No):
        print("*",end="  ")

        
def main():
    print("Enter number : ")
    Value = int(input())

    Display(Value)
    
    
if __name__ == "__main__":
    main()