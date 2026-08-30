os.path.dirname()

os.path.dirname() का use किसी पूरے path में से आखिरी नाम हटाकर उसका directory/folder वाला path निकालने के लिए होता है।

Syntax
os.path.dirname(path)



import os

path = r"C:\Users\ajski\OneDrive\Desktop\Python_Practice\test.txt"

print(os.path.dirname(path))


Output:

C:\Users\ajski\OneDrive\Desktop\Python_Practice
