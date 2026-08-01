num = int(input("Enter the number:"))

found = False

while num > 0:
    digit = num % 10

    if digit == 0:
        found = True

    num = num // 10

if found:
    print("Duck Number")
else:
    print("Not Duck Number")

100 102 121 100
