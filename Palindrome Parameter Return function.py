def Palindrome(num):
    original=num
    reverse=0
    while num>0:
        digit=num%10
        reverse=reverse*10+digit
        num=num//10
    if reverse == original:
        return "Palindrome"
    else:
        return "not Palindrome"

result = Palindrome(441)
print(result)
