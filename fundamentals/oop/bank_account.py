
class BankAccount():
    bank_accounts=[]

    def __init__(self,int_rate = 0.07,balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.bank_accounts.append(self)
    def display_account_info(self):
        return "Interest rate:"+ str(self.int_rate) + " balance: " + str(self.balance) + " Interest: " + str(self.yieldinterest())
   
    def deposit(self,amount):
        self.balance += amount
        return self

    def withdraw(self,amount): 
        if(self.is_insufficient(amount,self.balance)): 
            print("You have insufficient funds. You've been fined $5.")
            self.balance -= 5
        else: 
            self.balance -= amount
        return self

    def yieldinterest(self):
        interest = self.int_rate * self.balance
        return interest

    @staticmethod
    def is_insufficient(amount,balance):
        if(balance-amount < 0):
            return True
        else:
            return False

    @classmethod
    def all_accounts(cls):
        for account in cls.bank_accounts:
             print(f"{str(account)} Interest rate: {account.int_rate} balance: {account.balance}")
            
        return cls

    def __str__(cls):
        return "Interest rate: " + str(cls.int_rate) + "  Account balance: " + str(cls.balance)
    

hobby_account = BankAccount(.08, 70)
hobby_account.deposit(100).deposit(200).deposit(50).withdraw(20)
print(hobby_account.display_account_info())

savings_account = BankAccount(.05,300)
savings_account.deposit(500).deposit(400).withdraw(80).withdraw(60).withdraw(100).withdraw(40)
print(savings_account.display_account_info())


BankAccount.all_accounts()


