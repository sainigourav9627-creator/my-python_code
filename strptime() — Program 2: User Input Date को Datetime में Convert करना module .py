from datetime import datetime

date_string = input("Enter date: ")

date = datetime.strptime(date_string, "%d-%m-%Y")

print(date)
