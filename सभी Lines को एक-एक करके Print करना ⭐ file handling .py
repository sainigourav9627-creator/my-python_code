with open("student.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print(line, end="")



इस बार readlines() से मिली list पर for loop लगाएंगे:
