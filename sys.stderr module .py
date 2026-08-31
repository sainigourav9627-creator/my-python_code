sys.stderr

sys.stderr का मतलब है Standard Error.

Python में errors या warning messages को standard error stream पर भेजा जा सकता है।


import sys

sys.stdout.write("This is normal output\n")
sys.stderr.write("This is error output\n")
