time.ctime()

अब time.time() के timestamp को readable date & time में देखना हो तो ctime() उपयोगी है।


import time

print(time.ctime())


Output कुछ ऐसा:

Tue Sep  1 10:40:25 2026

यह current day + date + time + year को readable form में दिखाता है।





Difference
time.time()
→ Timestamp (float)

time.ctime()
→ Readable date & time (string)
