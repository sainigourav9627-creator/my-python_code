Date/Time Module — Syntax Sheet

Topic	Main Syntax

datetime	                             datetime.now()
date.today()	                         date.today()
weekday()	                             date.weekday()
strftime()	                           datetime.strftime("format")
strptime()	                           datetime.strptime("string", "format")
timedelta()	                           timedelta(days=5)



datetime
from datetime import datetime

now = datetime.now()


🔹 date.today()
from datetime import date

today = date.today()


🔹 weekday()
date.weekday()


🔹 strftime()
now.strftime("format")


Examples:

now.strftime("%d-%m-%Y")
now.strftime("%A")
now.strftime("%H:%M:%S")


🔹 strptime()
datetime.strptime("25-08-2026", "%d-%m-%Y")


🔹 timedelta()
date + timedelta(days=5)
date - timedelta(days=5)


और units:

timedelta(days=5)
timedelta(weeks=2)
timedelta(hours=5)
timedelta(minutes=30)
timedelta(seconds=30)



🧠 सबसे जरूरी 6 Syntax
datetime.now()
date.today()
date.weekday()
datetime.strftime("format")
datetime.strptime("string", "format")
timedelta(days=5)

🎯 यही आपकी Date/Time Module की main syntax cheat sheet है।
