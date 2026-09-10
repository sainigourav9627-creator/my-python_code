अगला Program 4 — File में characters की संख्या ⭐

अब पूरे file में कुल कितने characters हैं, यह निकालेंगे:


with open("student.txt", "r") as file:
    data = file.read()

print("Total characters:", len(data))
