try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print(a / b)

except ValueError as e:
    print("Value Error:", e)

except ZeroDivisionError as e:
    print("Zero Error:", e)
