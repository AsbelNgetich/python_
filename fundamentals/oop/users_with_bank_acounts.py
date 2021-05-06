class User():
    def __init__(self, name):
        self.name = name
        self.account = BankAccount(int_rate = 0.02, balance = 0)

    def make_deposit(self,amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        return self.account.display_account_info()

class BankAccount():

    bank_accounts=[]

    def __init__(self, int_rate = 0.07,  balance = 0):
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

big_bell = User("asbel")
result = big_bell.account.deposit(1000).withdraw(200).display_account_info()

print(result)
