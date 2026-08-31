sys.modules

sys.modules Python में already loaded/imported modules की dictionary होती है।


import os
import sys

print("os" in sys.modules)
print("sys" in sys.modules)
