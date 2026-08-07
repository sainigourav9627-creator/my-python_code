def armstrong(num):
    original=num
    total=0
    while num>0:
        digit=num%10
        total=total+digit**3
        num=num//10
    if total == original:
        return "armstrong"
    else:
        return "not armstrong"

result = armstrong(153)
print(result)
