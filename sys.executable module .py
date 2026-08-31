sys.executable

sys.executable हमें बताता है कि कौन-सा Python executable/interpreter हमारे program को चला रहा है।

तुम्हारे case में यह खास useful है क्योंकि तुम uv वाला Python 3.14.6 चला रहे हो।


import sys

print(sys.executable)


