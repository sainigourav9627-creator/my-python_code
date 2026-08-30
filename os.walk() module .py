os.walk()

os.walk() का use किसी folder के अंदर मौजूद सभी folders और files को recursively देखने के लिए होता है।


Syntax
import os

for root, dirs, files in os.walk("path"):
    print(root)
    print(dirs)
    print(files)


आपके Python_Practice में Practical


import os
path = r"C:\Users\ajski\OneDrive\Desktop\Python_Practice"

for root, dirs, files in os.walk(path):
    print("Root:", root)
    print("Folders:", dirs)
    print("Files:", files)
