class Bank:

    def __init__(self):
        self.balance = 5000


account = Bank()

account.balance = -10000

print(account.balance)


Without control:
Outside → Data change ❌

With Encapsulation:
Outside → Controlled Method/Property → Data ✅
