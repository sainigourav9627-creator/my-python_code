with open("student.txt", "r") as file:
    data = file.read()

count = data.count("a")

print("Character 'a' count:", count)
