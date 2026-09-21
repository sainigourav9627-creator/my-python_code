class Bank:

    def __init__(self):
        self.balance = 5000

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def show_balance(self):
        print(self.balance)


account = Bank()

account.deposit(1000)
account.withdraw(500)

account.show_balance()

