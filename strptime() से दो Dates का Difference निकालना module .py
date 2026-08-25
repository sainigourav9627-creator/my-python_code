from datetime import datetime

date1 = datetime.strptime("25-08-2026", "%d-%m-%Y")
date2 = datetime.strptime("30-08-2026", "%d-%m-%Y")

difference = date2 - date1
print(difference.days)
