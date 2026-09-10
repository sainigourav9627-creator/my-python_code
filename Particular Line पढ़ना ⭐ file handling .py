अब हम file की एक specific line निकालेंगे।

with open("student.txt", "r") as file:
    lines = file.readlines()

print("Second line:", lines[1])
