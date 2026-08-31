import sys

age = int(input("Enter your age: "))

if age < 18:
    sys.stderr.write("Error: You are not eligible\n")
else:
    print("You are eligible")
