num=int(input("enter the number:"))
original=num
total=0
while num>0:
       digit=num%10
      
       factorial = 1

       for i in range(1, digit + 1):
          factorial = factorial * i

       total = total + factorial
       num=num//10
if total== original:
    print("Strong Number")
else:
    print("Not Strong Number")



Interview Important Strong Numbers

Ye numbers yaad rakhna:

1
2
145
40585



