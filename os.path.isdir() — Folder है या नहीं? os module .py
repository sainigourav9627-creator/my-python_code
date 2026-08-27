os.path.isdir() का use check करने के लिए होता है कि दिया गया path directory/folder है या नहीं।


Syntax

import os
os.path.isdir("path")



यह भी:

True  → Folder है
False → Folder नहीं है





📁 os.path.isdir() Practical

आपका Python_Practice एक folder है।



import os
path = r"C:\Users\ajski\OneDrive\Desktop\Python_Practice"
print(os.path.isdir(path))



Output:

True

क्योंकि Python_Practice एक directory/folder है। ✅



File पर check

अगर Python_Practice में test.txt file है:



import os

path = r"C:\Users\ajski\OneDrive\Desktop\Python_Practice\test.txt"

print(os.path.isdir(path))





Output:

False

क्योंकि test.txt file है, folder नहीं।


