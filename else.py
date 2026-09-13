try:
    age = int(input("Enter age: "))

except ValueError:
    print("Invalid age.")

else:
    print("Age successfully entered:", age)
