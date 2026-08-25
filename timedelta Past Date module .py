from datetime import datetime, timedelta

date_string = input("Enter date: ")

date = datetime.strptime(date_string, "%d-%m-%Y")

new_date = date - timedelta(days=30)

print(new_date)
