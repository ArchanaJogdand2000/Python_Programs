# pattern printing 

#       1   
#       1   2     
#       1   2   3   4    
#       1   2   3   4   5
      

def pattern(No):
    
    for raw in range(1,No+1):
    
        for col in range(1,No+1):
            
            if(raw >= col):  
               print(col,end=" ")
        print("\n")    
 
def main():
    print("Enter number :")
    Value = int(input())

    pattern(Value)


if __name__ == "__main__":
    main()

   