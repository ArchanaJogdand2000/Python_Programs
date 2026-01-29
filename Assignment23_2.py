class BankAccount:
    ROI = 10.5 # rate of interest

    def __init__(self,Name,Amt):
        self.Name = Name
        self.Amount = Amt

    def Display(self):
        print("Account holder name is : ",self.Name,"Current ballance is : ",self.Amount) 

    def Deposit(self):
        deposit = int(input("Enter Amount that you want to add in your account : "))

        self.Amount = self.Amount + deposit
        print("After deposit money in your account now Available balance is : ",self.Amount)

    def Withdraw(self):
        withdraw_Amount = int(input("Enter Amount that you want to withdraw from your account : "))

        if(withdraw_Amount <= self.Amount):
           self.Amount = self.Amount - withdraw_Amount
           print("After withdraw money from your account now Available balance is : ",self.Amount)

        else:
            print("Sorry your bank account does not have enough balance plz check balance:")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100


obj1 = BankAccount("Archana Jogdand",20000)
obj1.Display()
obj1.Deposit()
obj1.Withdraw()
obj1.CalculateInterest()

obj1 = BankAccount("Surbhi Jadhav",50000)
obj1.Display()
obj1.Deposit()
obj1.Withdraw()
obj1.CalculateInterest()

