os.path.join()

os.path.join() का use दो या दो से ज्यादा path parts को सही तरीके से जोड़कर एक complete path बनाने के लिए होता है।

Syntax
os.path.join(path1, path2)

import os

path = os.path.join("Python_Practice", "test.txt")

print(path)



os.path.join(
    "C:\\Users\\ajski\\OneDrive\\Desktop",
    "Python_Practice",
    "test.txt"
)



import os

base = r"C:\Users\ajski\OneDrive\Desktop"

path = os.path.join(base, "Python_Practice")

print(path)
