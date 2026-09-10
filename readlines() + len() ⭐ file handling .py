file = open("student.txt", "r")

data = file.readlines()

print(len(data))

file.close()
