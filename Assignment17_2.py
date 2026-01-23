# pattern printing 
#       *   *   *   *   *
#       *   *   *   *   *
#       *   *   *   *   *
#       *   *   *   *   *
#       *   *   *   *   *


def pattern(No):
    
    for raw in range(No):
    
        for col in range(No):
            print("*",end=" ")
        print("\n")    
 
def main():
    print("Enter number :")
    Value = int(input())

    pattern(Value)


if __name__ == "__main__":
    main()
