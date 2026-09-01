import time

result = time.localtime()

print(result)



Output कुछ ऐसा दिख सकता है:

time.struct_time(
    tm_year=2026,
    tm_mon=9,
    tm_mday=1,
    tm_hour=10,
    tm_min=45,
    tm_sec=20,
    ...
)



इसमें अलग-अलग जानकारी मिलती है:

tm_year → Year
tm_mon  → Month
tm_mday → Day
tm_hour → Hour
tm_min  → Minute
tm_sec  → Second


import time

now = time.localtime()

print(now.tm_year)
print(now.tm_mon)
print(now.tm_mday)
