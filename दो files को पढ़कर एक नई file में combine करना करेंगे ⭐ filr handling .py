with open("student.txt", "r") as file1:
    data1 = file1.read()

with open("clean_student.txt", "r") as file2:
    data2 = file2.read()

with open("combined.txt", "w") as file3:
    file3.write(data1)
    file3.write("\n")
    file3.write(data2)

print("Files combined successfully")
