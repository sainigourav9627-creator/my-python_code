sys.setrecursionlimit()

sys.setrecursionlimit() का उपयोग Python की recursion limit को बदलने के लिए किया जाता है।


import sys

print("Old limit:", sys.getrecursionlimit())

sys.setrecursionlimit(1500)

print("New limit:", sys.getrecursionlimit())
