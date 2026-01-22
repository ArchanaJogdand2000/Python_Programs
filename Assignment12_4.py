#write a program which accept one number and prints that many numbers starting from 1

def Serial(No):
    for i in range(1,No+1):
        print(i,end=" ") #print output in same line like \t in c


def main():
   
    print("Enter number : ")
    Value1 = int(input())

    Serial(Value1)

     
if __name__ == "__main__":
    main()    
    
