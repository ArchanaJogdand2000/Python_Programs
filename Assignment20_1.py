import threading
import time

def Even(No):
   
    for i in range(2,No+1,2):
        print(i)

def Odd(No):
  
    for i in range(1,No+1,2):
        print(i)

def main():
    start_time = time.time()
    t1 = threading.Thread(target=Even,args=(20,))
    t2 = threading.Thread(target=Odd,args=(20,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
   
    end_time = time.time()

    print("Time required :",end_time-start_time)

        
if __name__ == "__main__":
    main()  

     