Program 6 — सबसे छोटी Line ढूँढना ⭐

अभी हमने max() से सबसे लंबी line निकाली थी।
अब min() से सबसे छोटी line निकालेंगे।


with open("student.txt", "r") as file:
    lines = file.readlines()

shortest_line = min(lines, key=len)

print("Shortest line:", shortest_line)
