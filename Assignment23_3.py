class Numbers:

    def __init__(self,No):
        self.Value = No
        
    def ChkPrime(self):
        bFlage = True

        for i in range(2, int(self.Value / 2 )+ 1):
            if (self.Value % i == 0):
                bFlage = False
                break
        
        if(bFlage == True):
            print("number is prime ")
        else:
            print("number is not prime")

    def Factor(self):
        print("Factors of given number are : ")
        for i in range(1,self.Value):
            if(self.Value % i == 0):
                print(i, end=" ")

    def SumFactors(self):
        Sum = 0
        for i in range(1,self.Value):
            if(self.Value % i== 0):
               Sum = Sum + i
        return Sum
        
    def ChkPerfect(self):
        iRet = self.SumFactors()
        print("\nAddition of factors is : ",iRet)

        if(self.Value == iRet):
            print("it is a perfect number")
        else:
             print("it is not perfect number")

def main():
    num = int(input("Enter number : "))

    obj = Numbers(num)
    obj.ChkPrime()
    obj.Factor()
    obj.ChkPerfect()
    
    obj.SumFactors()
    
if __name__ == "__main__":
    main()   
    