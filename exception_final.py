try:
    marks = int(input("Enter the marks: "))

    if marks < 0 or marks > 100:
        raise ValueError("Invalid marks")

except ValueError as e:
    print("Error:", e)

else:
    print("Marks valid")

finally:
    print("Program finished")
