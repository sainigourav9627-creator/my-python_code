import time

result = time.time()

print(result)


or


import time

start = time.time()

for i in range(1000000):
    pass

end = time.time()

print("Time taken:", end - start)
