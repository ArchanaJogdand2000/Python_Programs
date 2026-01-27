# Display a python application where multiple threads update a shared variable.
# Use a Lock to avoid race condition.
# Each thread should increment the shared counter multiple times.
# Display the final value of the counter after all threads complete execution.


import threading
import time

iCnt=0

lobj=threading.Lock()

def Increment(No):
    global iCnt
    for i in range(No):
        with lobj:
            iCnt=iCnt+1
def main():

    num_threads = int(input("Enter number of threads: "))
    increments_per_thread = int(input("Enter increments per thread: "))

    threads = [] 

    # Create threads
    for i in range(num_threads):
        t = threading.Thread(target=Increment, args=(increments_per_thread,))
        threads.append(t) # thraeds che objects list madhe store kele 

    # Start threads
        t.start()

    # Wait for all threads to finish
        t.join()

    print("Final value of counter:", iCnt)

if __name__ == "__main__":
    main()
