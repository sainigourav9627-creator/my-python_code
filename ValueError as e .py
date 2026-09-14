try:
    age = int(input("Enter age: "))
    print("Age:", age)

except ValueError as e:
    print("Error:", e)
