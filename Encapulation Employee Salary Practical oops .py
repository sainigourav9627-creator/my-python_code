class Employee:
    def __init__(self, salary):
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value >= 0:
            self.__salary = value
        else:
            print("Invalid salary")


emp = Employee(20000)

print("Salary:", emp.salary)

emp.salary = 25000
print("Salary:", emp.salary)

emp.salary = -5000
print("Salary:", emp.salary)
