from datetime import datetime, timedelta

date = datetime(2026, 8, 25, 10, 30, 0)

new_date = date + timedelta(hours=5)

print(new_date)
