#Week/Day Codes:
   
#%j — Day of Year
#%U — Week Number (Sunday-based)
#%W — Week Number (Monday-based)
#%w — Weekday Number



Practical combinations भी complete
Day + Weekday Number ✅
Full Weekday + Number ✅
Short Weekday + Number ✅
Day of Year + Weekday Number ✅
Week Number + Weekday Number ✅
Week Number + Full Weekday ✅
Week Number + Short Weekday ✅
Monday Week Number + Full Weekday ✅
Monday Week Number + Short Weekday ✅
Year + Day of Year ✅
Year + Week Number ✅
Year + Monday Week Number ✅
Month + Weekday Number ✅
Month + Day of Year ✅
Day + Week Number ✅
Day + Monday Week Number ✅
Full Date + Day of Year ✅


import datetime
d = datetime.date(2026, 12, 25)


#%j → Year का Day number
print(d.strftime("%j"))  

#%U → Week Sunday से शुरू
print(d.strftime("\n%U"))


#%W → Week Monday से शुरू
print(d.strftime("%W"))


#Weekday Number
print(d.strftime("\n%w"))


#Day + Weekday Number
print(d.strftime("%d %w"))

#Weekday Name + Weekday Number
print(d.strftime("\n%A %w"))


#Short Weekday + Weekday 
print(d.strftime("%a %w"))


#Day of Year + Weekday Number
print(d.strftime("\n%j %w"))

#Week Number + Weekday Number
print(d.strftime("%U %w"))

#Week Number + Full 
print(d.strftime("\n%U %A"))

#Week Number + Short Weekday
print(d.strftime("%U %a"))



# %U K REPLACE KRKE %W USE




#Monday-Based Week Number + Full Weekday
print(d.strftime("\n%W %A"))


#Monday-Based Week Number + Short Weekday 
print(d.strftime("%W %a"))


#Year + Day of Year
print(d.strftime("\n%Y %j"))


#Year + Week Number
print(d.strftime("\n%Y %U"))

#Year + Monday-Based Week Number
print(d.strftime("%Y %W"))

#Month + Weekday Number
print(d.strftime("\n%m %w"))

#Month + Day of Year
print(d.strftime("%m %j"))

#Day + Week Number
print(d.strftime("\n%d %U"))

#Day + Monday-Based Week Number
print(d.strftime("%d %W"))

#Full Date + Day of Year
print(d.strftime("\n%d %B %Y-Day %j"))




