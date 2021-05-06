class User():
    def __init__(self,name):
        self.name = name
        self.account_balance = 0

    def __str__(self):
        return "Name: " + str(self.name) + "  Account balance: " + str(self.account_balance)
        

    def make_deposit(self,amount):
        self.account_balance += amount
        return self
    
    def make_withdrawal(self,amount):
        self.account_balance -=amount
        return self
    
    def display_user_balance(self):
        return self.account_balance
