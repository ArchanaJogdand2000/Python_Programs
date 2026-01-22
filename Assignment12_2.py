#write a program which accept one number and prints its factors

def Factors(No):
    A = []
    for i in range(1,No+1):
        if((No%i)==0):
          A = print(i)
     
def main():
   
    print("Enter number : ")
    Value = int(input())

    Factors(Value)
    
     
if __name__ == "__main__":
    main()    
    
