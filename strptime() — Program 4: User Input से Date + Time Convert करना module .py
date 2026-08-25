from datetime import datetime

date_string = input("\nEnter date and time: ")

date = datetime.strptime(date_string, "%d-%m-%Y %H:%M:%S")

print(date)
