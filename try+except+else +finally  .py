try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("0 se divide nahi kar sakte.")

else:
    print("Result:", result)

finally:
    print("Program finished.")
