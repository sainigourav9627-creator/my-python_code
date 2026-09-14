class InvalidMarksError(Exception):
    pass


try:
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks 0 se 100 ke beech hone chahiye.")

    print("Valid marks:", marks)

except ValueError:
    print("Please enter numbers only.")

except InvalidMarksError as e:
    print("Error:", e)
