def ChkPrime(Num):
  
    if Num <= 1:
        return False 
                      #int(Num**0.5) + 1)
    for i in range(2, int(Num/2) + 1):
        if Num % i == 0:
            return False
    return True

    
   