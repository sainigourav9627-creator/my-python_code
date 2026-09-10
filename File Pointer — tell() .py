File Pointer — tell()

जब Python file को पढ़ता या लिखता है, तो उसके अंदर एक current position/pointer होती है।

tell() बताता है कि pointer अभी कहाँ है



file = open("student.txt", "r")

print(file.tell())

data = file.read(5)

print(data)

print(file.tell())

file.close()
