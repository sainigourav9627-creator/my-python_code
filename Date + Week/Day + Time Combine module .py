Program 60: Date + Week/Day + Time Combine

Is program mein hum 3 cheezein ek saath print karenge:

Date → %d-%m-%Y
Week/Day → %A
Time → %H:%M:%S


import datetime

d = datetime.datetime.now()

print(d.strftime("%d-%m-%Y"))
print(d.strftime("%A"))
print(d.strftime("%H:%M:%S"))


or


from datetime import datetime

now = datetime.now()

print(now.strftime("%d-%m-%Y"))
print(now.strftime("%A"))
print(now.strftime("%H:%M:%S"))
