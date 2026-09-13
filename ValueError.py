Example:
age = int("hello")



Output:
ValueError



try:
    age = int(input("Enter age: "))

except ValueError:
    print("Numbers only.")
