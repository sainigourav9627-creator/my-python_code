from datetime import datetime

date1_string = input("Enter first date and time: ")
date2_string = input("Enter second date and time: ")

date1 = datetime.strptime(date1_string, "%d-%m-%Y %H:%M:%S")
date2 = datetime.strptime(date2_string, "%d-%m-%Y %H:%M:%S")

difference = date2 - date1

print(difference)
