original = num → Compare ke liye ✔️

✅ reverse = 0 → Reverse store karne ke liye ✔️

✅ digit = num % 10 → Last digit nikalne ke liye ✔️

✅ reverse = reverse * 10 + digit → Reverse banane ke liye ✔️

✅ num = num // 10 → Last digit hatane ke liye ✔️

✅ if reverse == original → Compare karne ke liye ✔️

⭐ Compare
num=int(input("enter the armstrong number:"))
original=num
reverse=0
while num > 0:
   digit=num%10
   reverse=reverse*10+digit
   num=num//10
if reverse==original:
     print("Palindrome Number")
else:
       print("NotPalindrome Number")
  
121 141 151 1331 1441
