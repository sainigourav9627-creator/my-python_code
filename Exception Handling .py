a = 10
b = 0

print(a / b)

Output:

ZeroDivisionError: division by zero



try:
    a = 10
    b = 0
    print(a / b)

except ZeroDivisionError:
    print("0 se divide nahi kar sakte")



Output:

0 se divide nahi kar sakte
