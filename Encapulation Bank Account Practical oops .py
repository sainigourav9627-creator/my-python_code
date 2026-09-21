class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value
        else:
            print("Invalid balance")


account = BankAccount(5000)

print("Balance:", account.balance)

account.balance = 7000
print("Balance:", account.balance)

account.balance = -2000
print("Balance:", account.balance)
