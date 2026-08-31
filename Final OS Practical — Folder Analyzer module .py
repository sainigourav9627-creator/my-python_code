import os

path = r"C:\Users\ajski\OneDrive\Desktop\Python_Practice"

print("Current Location:")
print(os.getcwd())

print("\nItems:")
print(os.listdir(path))

print("\nFolder Exists:")
print(os.path.exists(path))

print("\nIs File:")
print(os.path.isfile(path))

print("\nIs Folder:")
print(os.path.isdir(path))

print("\nFolder Analysis:")

for root, dirs, files in os.walk(path):
    print("\nRoot:", root)
    print("Folders:", dirs)
    print("Files:", files)

    for file in files:
        file_path = os.path.join(root, file)
        print(file, "->", os.path.getsize(file_path), "bytes")



इसमें क्या-क्या revise होगा?

getcwd()       → Current location
listdir()      → Files + folders
exists()       → Path exists?
isfile()       → File?
isdir()        → Folder?
walk()         → पूरी directory tree
join()         → Complete file path
getsize()      → File size

इसे run करो और पूरा output भेजो। फिर मैं तुम्हें बताऊँगा कि हर line में कौन-सा OS concept काम कर रहा है। 🎯
