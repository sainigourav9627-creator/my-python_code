try:
    age = int(input("Enter age: "))

    if age < 18:
        raise ValueError("Age 18 se kam hai.")

    print("You can vote.")

except ValueError as e:
    print("Error:", e)
