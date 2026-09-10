अब एक ही program में Append + Read करेंगे।

with open("student.txt", "a") as file:
    file.write("\nFile Handling is interesting.")

with open("student.txt", "r") as file:
    data = file.read()

print(data)
