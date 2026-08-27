os.path.getsize() का use किसी file का size bytes में पता करने के लिए होता है।


Syntax

import os

os.path.getsize("file_path")


import os

path = r"C:\Users\ajski\OneDrive\Desktop\Python_Practice\test.txt"

size = os.path.getsize(path)

print(size)
