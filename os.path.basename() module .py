os.path.basename()

os.path.basename() का use किसी पूरے path में से आखिरी नाम निकालने के लिए होता है।

यह आखिरी नाम file भी हो सकता है या folder भी।




import os

path = r"C:\Users\ajski\OneDrive\Desktop\Python_Practice"

print(os.path.basename(path))



Output:

Python_Practice
