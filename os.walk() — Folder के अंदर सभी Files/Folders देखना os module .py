os.walk() का use किसी folder के अंदर सभी subfolders और files को recursively देखने के लिए होता है।

यानी अगर structure ऐसा है:

Python_Practice
├── test.txt
├── Python
│   ├── program.py
│   └── Notes
│       └── notes.txt
└── Data
    └── marks.csv

तो os.walk() पूरी structure को एक-एक करके देख सकता है।


Syntax

import os

for root, dirs, files in os.walk("folder_path"):
    print(root)
    print(dirs)
    print(files)


तीन चीजें मिलती हैं

root  → Current folder का path
dirs  → उस folder के अंदर मौजूद folders


import os

path = r"C:\Users\ajski\OneDrive\Desktop\Python_Practice"

for root, dirs, files in os.walk(path):
    print("Root:", root)
    print("Folders:", dirs)
    print("Files:", files)
files → उस folder के अंदर मौजूद files


R-D-F

R → Root  → कहाँ हूँ?
D → Dirs  → कौन-कौन से folders हैं?
F → Files → कौन-कौन सी files हैं?
