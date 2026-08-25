from datetime import datetime

date1 = datetime.strptime("25-08-2026", "%d-%m-%Y")
date2 = datetime.strptime("30-08-2026", "%d-%m-%Y")

if date1 > date2:
    print("Date 1 is greater")
elif date1 < date2:
    print("Date 2 is greatrer")
else:
    print("both date are equal")
