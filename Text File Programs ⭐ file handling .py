File में Word Search करना


with open("student.txt", "r") as file:
    data = file.read()

if "Python" in data:
    print("Python word found")
else:
    print("Python word not found")
