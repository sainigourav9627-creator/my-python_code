age = int(input("Enter age: "))
print(age)

abc डालने पर program crash ❌

Handling के साथ:

try:
    age = int(input("Enter age: "))
    print(age)

except ValueError:
    print("Please enter a number.")
