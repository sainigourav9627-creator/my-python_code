import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Gourav", 30, 85])
    writer.writerow(["Rahul", 25, 90])

print("Data saved")
