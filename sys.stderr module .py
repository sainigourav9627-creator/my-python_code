sys.stderr

sys.stderr का मतलब है Standard Error.

Python में errors या warning messages को standard error stream पर भेजा जा सकता है।


import sys

age = int(input("Enter your age: "))

if age < 18:
    sys.stderr.write("Error: You are not eligible\n")
else:
    print("You are eligible")
