from datetime import datetime

date = datetime.strptime(
    "25-08-2026 10:30:25 PM",
    "%d-%m-%Y %I:%M:%S %p"
)

print(date)
