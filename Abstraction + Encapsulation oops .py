from abc import ABC, abstractmethod


class Bank(ABC):

    def __init__(self, balance):
        self.__balance = balance

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self.__balance


class SBI(Bank):

    def withdraw(self, amount):
        if amount <= self.__balance:
            print("Withdraw successful")
        else:
            print("Insufficient balance")
