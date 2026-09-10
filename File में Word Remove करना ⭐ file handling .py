replace() की मदद से किसी word को empty string "" से replace करके remove कर सकते हैं।

अभी हमारी file में Java मौजूद है। उसे remove करते हैं:

with open("student.txt", "r") as file:
    data = file.read()

data = data.replace("Java", "")

with open("student.txt", "w") as file:
    file.write(data)
🧠 Logic
