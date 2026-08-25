from datetime import datetime

date = datetime.strptime("25-08-2026", "%d-%m-%Y")

new_date = date.strftime("%A, %d %B %Y")

print(new_date)
