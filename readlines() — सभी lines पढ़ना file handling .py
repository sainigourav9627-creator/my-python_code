file.readlines()

से file की सारी lines एक साथ मिलती हैं।


file = open("student.txt", "r")

lines = file.readlines()

print(lines)
print(lines[0])

file.close()
