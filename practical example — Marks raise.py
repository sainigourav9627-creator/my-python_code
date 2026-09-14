try:
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks 0 se 100 ke beech hone chahiye.")

    print("Valid marks:", marks)

except ValueError as e:
    print("Error:", e)
