file.write("Hello\n")
file.write("Python\n")

लेकिन writelines() में हम कई lines एक साथ दे सकते हैं।



file = open("student.txt", "w")

lines = [
    "My name is Gourav.\n",
    "I am learning Python.\n",
    "I am learning File Handling.\n"
]

file.writelines(lines)

file.close()
