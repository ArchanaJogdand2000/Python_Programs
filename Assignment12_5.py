#write a program which accept one number and prints that many numbers in reverce order

def Serial(No):
    for i in range(No,0,-1):
        print(i,end=" ") #print output in same line like \t in c


def main():
   
    print("Enter only positive number : ")
    Value1 = int(input())

    Serial(Value1)

     
if __name__ == "__main__":
    main()    
    
