try:
    a = int(input("Enter first number: "))

    try:
        b = int(input("Enter second number: "))
        print("Result:", a / b)

    except ZeroDivisionError:
        print("0 se divide nahi kar sakte.")

except ValueError:
    print("Numbers only.")
