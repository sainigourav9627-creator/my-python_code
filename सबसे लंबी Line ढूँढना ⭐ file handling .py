Program 5 — सबसे लंबी Line ढूँढना ⭐

अब student.txt की सभी lines पढ़कर सबसे लंबी line निकालेंगे।


with open("student.txt", "r") as file:
    lines = file.readlines()

longest_line = max(lines, key=len)

print("Longest line:", longest_line)
