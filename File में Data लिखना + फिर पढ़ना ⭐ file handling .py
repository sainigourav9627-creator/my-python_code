अभी student.txt खाली है। अब उसी file में data लिखकर तुरंत पढ़ेंगे।

with open("student.txt", "w") as file:
    file.write("My name is Gourav.\n")
    file.write("I am learning Python.\n")
    file.write("File Handling is easy.")

with open("student.txt", "r") as file:
    data = file.read()

print(data)
