अब पता करेंगे कि student.txt में कुल कितनी lines हैं


with open("student.txt", "r") as file:
    lines = file.readlines()

print("Total lines:", len(lines))
