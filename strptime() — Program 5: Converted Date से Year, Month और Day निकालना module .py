from datetime import datetime

date = datetime.strptime("25-08-2026", "%d-%m-%Y")

print(date.year)
print(date.month)
print(date.day)
