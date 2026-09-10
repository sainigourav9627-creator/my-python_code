with open("student.txt", "r") as file1:
    data1 = file1.read()

with open("student_copy.txt", "r") as file2:
    data2 = file2.read()

if data1 == data2:
    print("Both files are same")
else:
    print("Files are different")
