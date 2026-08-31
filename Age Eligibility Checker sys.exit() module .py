import sys

age = int(input("Enter your age: "))

if age < 18:
    print("Not eligible")
    sys.exit()

print("Eligible")
