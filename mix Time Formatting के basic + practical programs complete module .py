#याद रखो
#%H → 24-hour
#%I → 12-hour
#%p → AM/PM


Code	Meaning	Program

%H	24-hour	53
%I	12-hour	54
%p	AM/PM	55
%M	Minutes	56
%S	Seconds	57
%H:%M:%S	Complete 24-hour time	58
%I:%M:%S %p	Complete 12-hour time + AM/PM	59

import datetime

d = datetime.datetime.now()


# %H → 24-Hour
print(d.strftime("%H"))



# %I → 12-Hour
print(d.strftime("%I"))



# %p → AM / PM
print(d.strftime("%p"))



# %M → Minutes
print(d.strftime("%M"))



# %S → Seconds
print(d.strftime("%S"))



# 24-Hour + Minutes + Seconds
print(d.strftime("%H:%M:%S"))

# 12-Hour + Minutes + Seconds + AM/PM
print(d.strftime("%I:%M:%S %p"))
