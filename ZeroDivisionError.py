a = 10
b = 0

print(a / b)

Output:
ZeroDivisionError

try:
    print(10 / 0)

except ZeroDivisionError:
    print("0 se divide nahi kar sakte.")
