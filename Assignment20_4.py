import threading

def Small(str):
    print("Inside Small function : ",threading.get_ident())
    print(threading.current_thread().name)

    Count = 0
    for i in range(len(str)):
        if(str[i] >= 'a' and str[i] <= 'z'):
            Count = Count + 1
    print("lowercase characters are : ",Count)

def Capital(str):  
    print("Inside Capital function : ",threading.get_ident())
    print(threading.current_thread().name)

    Count = 0
    for i in range(len(str)):
        if(str[i] >= 'A' and str[i] <= 'Z'):
            Count = Count + 1
    print("lowercase characters are : ",Count)

def Digits(str):
    print("Inside Digits function : ",threading.get_ident())
    print(threading.current_thread().name)

    Count = 0
    for i in range(len(str)):
        if(str[i] >= '0' and str[i] <= '9'):
            Count = Count + 1
    print("number of numeric digits are : ",Count)


def main():
    print("Inside Small function : ",threading.get_ident())
    print(threading.current_thread().name)
    
    print("Enter string :")
    Value = input()

    t1 = threading.Thread(target=Small,args=(Value,))
    t2 = threading.Thread(target=Capital,args=(Value,))
    t3 = threading.Thread(target=Digits,args=(Value,))


    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    

if __name__ == "__main__":
    main()  

     