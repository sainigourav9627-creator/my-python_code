✅ Armstrong Number Complete
Tumhe yaad hona chahiye:
Line	Purpose

original = num	                  Compare ke liye
total = 0	                           Sum store karne ke liye
digit = num % 10	             Last digit nikalne ke liye
num = num // 10	                      Last digit hatane ke liye
digit ** 3	                         Digit ka cube
if total == original	           Armstrong check

num=int(input("enter the armstrong numbe:"))
original=num
total=0
while num > 0:
   digit=num%10
   total=total+digit**3
   num=num//10
if total==original:
     print("amrstrong number")
else:
       print("Not armstrong number")
