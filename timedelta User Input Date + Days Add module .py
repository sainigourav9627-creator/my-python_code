from datetime import datetime, timedelta

date_string = input("Enter date: ")

date = datetime.strptime(date_string, "%d-%m-%Y")

d = date + timedelta(days=5)

print(d)
