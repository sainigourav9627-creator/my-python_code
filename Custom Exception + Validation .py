class InvalidAgeError(Exception):
    pass


try:
    age = int(input("Enter age: "))

    if age < 18:
        raise InvalidAgeError("Age 18 ya usse zyada honi chahiye.")

    print("Eligible.")

except ValueError:
    print("Please enter a valid number.")

except InvalidAgeError as e:
    print("Error:", e)
