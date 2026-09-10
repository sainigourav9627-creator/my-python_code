अब हम पता करेंगे कि Python word कितनी बार आया है।

with open("student.txt", "r") as file:
    data = file.read()

words = data.split()

count = words.count("Python")

print("Python count:", count)
🧠 Logic
