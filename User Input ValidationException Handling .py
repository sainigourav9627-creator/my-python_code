try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age negative nahi ho sakti.")

    print("Valid age:", age)

except ValueError as e:
    print("Error:", e)
