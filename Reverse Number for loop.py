Aaj tumne ek bahut important pattern seekh liya
Program	Sirf Logic


Sum of Digits	total = total + digit
Armstrong	total = total + digit ** 3
Palindrome	reverse = reverse * 10 + digit + Compare
Reverse	reverse = reverse * 10 + digit + print(reverse)

num=int(input("enter the armstrong numbe:"))
original=num
reverse=0
while num > 0:
   digit=num%10
   reverse=reverse*10+digit
   num=num//10
print(reverse)
