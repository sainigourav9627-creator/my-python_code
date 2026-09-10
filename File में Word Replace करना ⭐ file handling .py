अब हम file के अंदर किसी पुराने word को नए word से replace करेंगे।

उदाहरण:
Python → Java

with open("student.txt", "r") as file:
    data = file.read()

data = data.replace("Python", "Java")

with open("student.txt", "w") as file:
    file.write(data)
