
class User():
    def __init__(self,name):
        self.name = name
        self.account_balance = 0

    def make_deposit(self,amount):
        self.account_balance += amount
    
    def make_withdrawal(self,amount):
        self.account_balance -=amount
    
    def display_user_balance(self):
        return self.account_balance

    @classmethod
    def transfer_money(cls,transer_from, transfer_to, cash_amount):
        transer_from.make_withdrawal(cash_amount)
        transfer_to.make_deposit(cash_amount)


# 1st user   
runner = User("asbel")
runner.make_deposit(50)
runner.make_deposit(70)
runner.make_deposit(100)
runner.make_withdrawal(40)
print(runner.name, runner.display_user_balance())

# # 2nd user
# jogger = User("kim")
# jogger.make_deposit(100)
# jogger.make_deposit(240)
# jogger.make_withdrawal(80)
# jogger.make_withdrawal(60)
# print(jogger.name, jogger.display_user_balance())

# 3rd user
racer = User("Alex")
racer.make_deposit(1000)
racer.make_withdrawal(240)
racer.make_withdrawal(100)
racer.make_withdrawal(200)
print(racer.name, racer.display_user_balance())

# Tranfer monery from one user to another
User.transfer_money(runner,racer,100)

print(runner.name, runner.display_user_balance())
print(racer.name, racer.display_user_balance())
