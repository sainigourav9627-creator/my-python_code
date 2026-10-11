marks = [65, 80, 72, 90, 55]

print("Marks =", marks)
print("Total =", sum(marks))
print("Average =", sum(marks) / len(marks))
print("Highest =", max(marks))
print("Lowest =", min(marks))

marks.append(88)
marks.sort()

print("Updated Marks =", marks)
