import threading

def EvenSum(Arr):
    Sum = 0
    i = 0
    for i in range(len(Arr)):
      if(Arr[i] % 2==0):
         Sum = Sum + Arr[i]
    print("Sum of even numbers is : ",Sum)
    

def OddSum(Arr):
    Sum = 0
    i = 0
    for i in range(len(Arr)):
      if(Arr[i] % 2 !=0):
         Sum = Sum + Arr[i]
    print("Sum of odd numbers is : ",Sum)
    

def main():
    print("Enter number :")
    Size = int(input())

    Data = list()

    print("Enter elements :")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    t1 = threading.Thread(target=EvenSum,args=(Data,))
    t2 = threading.Thread(target=OddSum,args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("Exit from main...")
   

if __name__ == "__main__":
    main()  

     