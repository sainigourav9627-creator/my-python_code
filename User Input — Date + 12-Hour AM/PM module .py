from datetime import datetime

date_string = input("Enter date and time: ")

date = datetime.strptime(
    date_string,
    "%d-%m-%Y %I:%M:%S %p"
)

print(date)
