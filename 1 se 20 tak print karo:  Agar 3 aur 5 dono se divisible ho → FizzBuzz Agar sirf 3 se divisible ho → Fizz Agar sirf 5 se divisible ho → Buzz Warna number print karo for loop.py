#1 se 20 tak print karo:

#Agar 3 aur 5 dono se divisible ho → FizzBuzz
#Agar sirf 3 se divisible ho → Fizz
#Agar sirf 5 se divisible ho → Buzz
#Warna number print karo.

for i in range(1,21):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0  :
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
