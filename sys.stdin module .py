sys.stdin

sys.stdin का उपयोग user से input लेने के लिए होता है।


import sys

print("Enter your name:")
name = sys.stdin.readline().strip()

print("Welcome", name)
