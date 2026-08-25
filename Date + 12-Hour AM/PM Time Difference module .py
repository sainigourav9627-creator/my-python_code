from datetime import datetime

date1 = datetime.strptime(
    "25-08-2026 10:30:00 AM",
    "%d-%m-%Y %I:%M:%S %p"
)

date2 = datetime.strptime(
    "25-08-2026 02:30:00 PM",
    "%d-%m-%Y %I:%M:%S %p"
)

difference = date2 - date1

print(difference)
