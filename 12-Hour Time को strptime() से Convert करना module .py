Important Format Codes

%I → 12-hour format
%M → Minute
%S → Second
%p → AM / PM



  from datetime import datetime

date = datetime.strptime("10:30:25 PM", "%I:%M:%S %p")

print(date)




  


  
