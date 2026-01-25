import threading


def EvenFactorsSum(No):
    Sum = 0
    for i in range(2,int(No/2)+1,2):
       if(No % i == 0):
           Sum = Sum + i
    print("Sum of even factors is : ",Sum)
    

def OddFactorsSum(No):
    Sum = 0
    for i in range(1,int(No/2)+1,2):
       if(No % i == 0):
           Sum = Sum + i
    print("Sum of odd factors is : ",Sum)
 

def main():
    print("Enter number :")
    Value = int(input())

    t1 = threading.Thread(target=EvenFactorsSum,args=(Value,))
    t2 = threading.Thread(target=OddFactorsSum,args=(Value,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("Exit from main...")
   

if __name__ == "__main__":
    main()  

     