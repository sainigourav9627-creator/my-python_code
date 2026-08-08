def number(*args):
    sum=0
    for value in args:
        sum=sum+value
    return sum
result=number(10,20,30)
print(result)

