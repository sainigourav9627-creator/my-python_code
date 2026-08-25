from datetime import datetime

date1_string = input("Enter first date: ")
date2_string = input("Enter second date: ")

date1 = datetime.strptime(date1_string, "%d-%m-%Y")
date2 = datetime.strptime(date2_string, "%d-%m-%Y")

difference = date2 - date1

print(difference.days)
