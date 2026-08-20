def fibo())
    n = int(input("Enter the number :  "))
    # n = 8
    first = 0
    second = 1
    for i in range(n):
       print(first)
       third = first + second
       first = second
       second = third
fibo()
