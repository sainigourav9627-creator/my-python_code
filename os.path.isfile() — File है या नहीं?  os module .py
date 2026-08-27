os.path.isfile() — File है या नहीं?

os.path.isfile() का use यह check करने के लिए होता है कि दिया गया path एक file है या नहीं।

Syntax

import os
os.path.isfile("path")


import os

path = r"C:\Users\ajski\OneDrive\Desktop\Python_Practice\test.txt"

print(os.path.isfile(path))

true


Folder पर check करें


import os
path = r"C:\Users\ajski\OneDrive\Desktop\Python_Practice"

print(os.path.isfile(path))




Output:

False

क्योंकि Python_Practice एक folder है, file नहीं।
