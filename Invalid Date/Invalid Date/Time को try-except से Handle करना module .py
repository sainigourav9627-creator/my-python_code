from datetime import datetime

date_string = input("Enter date and time: ")

try:
    date = datetime.strptime(
        date_string,
        "%d-%m-%Y %I:%M:%S %p"
    )
    print(date)

except ValueError:
    print("Invalid date or time")
