chdir() = Change Directory

Iska use current working directory ko change karne ke liye hota hai.

Syntax:
os.chdir("folder_path")

import os

os.chdir("C:\\Users\\Gourav\\Documents")

print(os.getcwd())



Practice

Aap apne laptop par ek folder ka path dekar ye program likho:

import os

os.chdir("________")
print(os.getcwd())



तरीका 1 — Raw string ⭐
import os

os.chdir(r"C:\Users\YourName\OneDrive\Desktop")

print(os.getcwd())


तरीका 2 — Double \\
import os

os.chdir("C:\\Users\\YourName\\OneDrive\\Desktop")

print(os.getcwd())
