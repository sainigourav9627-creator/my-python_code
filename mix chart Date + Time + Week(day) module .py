सबसे जरूरी Cheat Sheet
Code	Meaning	Example

%d	Day	24
%m	Month number	08
%B	Full month	August
%b	Short month	Aug
%Y	4-digit year	2026
%y	2-digit year	26
%A	Full weekday	Monday
%a	Short weekday	Mon
%H	24-hour	15
%I	12-hour	03
%M	Minutes	30
%S	Seconds	45
%p	AM/PM	PM


 Date + Time + Week/Day — Complete strftime() Chart

1️⃣ Date
Code	Meaning	Example

%d	Day of month	24
%m	Month number	08
%Y	4-digit Year	2026
%y	2-digit Year	26

  
2️⃣ Week / Day

Code	Meaning	Example
%A	Full weekday	Monday
%a	Short weekday	Mon

  
3️⃣ Month Name
Code	Meaning	Example

%B	Full month name	August
%b	Short month name	Aug

  
4️⃣ Time
Code	Meaning	Example

  
%H	24-hour	15
%I	12-hour	03
%M	Minutes	30
%S	Seconds	45
%p	AM/PM	PM



सबसे Important Differences

  
%m  → Month       → 08
%M  → Minutes     → 30

%H  → 24-hour     → 15
%I  → 12-hour     → 03

%B  → Full month  → August
%b  → Short month → Aug

%A  → Full day    → Monday
%a  → Short day   → Mon

%Y  → 4-digit year → 2026
%y  → 2-digit year → 26

  

  🔥 Common Syntax

from datetime import datetime
now = datetime.now()

print(now.strftime("%d-%m-%Y"))
print(now.strftime("%A"))
print(now.strftime("%H:%M:%S"))



🔥 Date + Day + Time एक साथ
print(now.strftime("%d-%m-%Y %A %H:%M:%S"))



Output:

24-08-2026 Monday 15:30:45




🔥 12-hour Time
print(now.strftime("%I:%M:%S %p"))




Output:

03:30:45 PM
