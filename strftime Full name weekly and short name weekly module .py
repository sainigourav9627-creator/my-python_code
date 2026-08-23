import datetime

d = datetime.date(2026,12,25)


print(d.strftime("\n%a/%d/%Y"))     
print(d.strftime("%d/%a/%Y"))
print(d.strftime("%d/%Y/%a"))

print(d.strftime("\n%d/%A/%Y"))     
print(d.strftime("%A/%d/%Y"))
print(d.strftime("%A/%Y/%d"))
