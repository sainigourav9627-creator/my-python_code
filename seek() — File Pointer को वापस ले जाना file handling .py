अब seek() pointer को किसी position पर ले जाता है।


file = open("student.txt", "r")

print(file.tell())

data = file.read(5)
print(data)

print(file.tell())

file.seek(0)

print(file.tell())

data = file.read(5)
print(data)

file.close()
