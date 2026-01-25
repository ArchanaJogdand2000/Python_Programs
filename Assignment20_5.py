import threading 


 # critical section la lock lavtat

def Display():
    for no in range(1,10+1):
        print(no)

    lobj = threading.Lock()    # thread synchronization

def DisplayReverse():
     
     for no in range(10,0,-1):
        print(no)
     lobj = threading.Lock()
     
def main():
    global iCnt
    
    t1 = threading.Thread(target=Display)
    t2 = threading.Thread(target=DisplayReverse)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()