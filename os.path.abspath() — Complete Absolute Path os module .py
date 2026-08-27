os.path.abspath() का use किसी relative path को complete absolute path में बदलने के लिए होता है।

Syntax
import os

os.path.abspath("path")

import os

print(os.path.abspath("Python_Practice"))


Example with file


import os

print(os.path.abspath("test.txt"))
