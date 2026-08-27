os.path.basename() का use किसी complete path में से आखिरी part का नाम निकालने के लिए होता है।

os.path.basename(path)


आपके Python_Practice के साथ Example
import os

path = r"C:\Users\ajski\OneDrive\Desktop\Python_Practice\test.txt"

print(os.path.basename(path))



Folder के साथ


import os

path = r"C:\Users\ajski\OneDrive\Desktop\Python_Practice"

print(os.path.basename(path))
