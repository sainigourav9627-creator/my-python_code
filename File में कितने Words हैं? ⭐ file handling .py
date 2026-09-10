इसमें हम split() का use करेंगे:

with open("student.txt", "r") as file:
    data = file.read()

words = data.split()

print("Total words:", len(words))
