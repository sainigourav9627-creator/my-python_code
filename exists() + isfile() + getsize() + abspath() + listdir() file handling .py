import os

file_name = "student.txt"

# 1. File मौजूद है?
print("Exists:", os.path.exists(file_name))

# 2. File है?
print("Is File:", os.path.isfile(file_name))

# 3. File का size
print("Size:", os.path.getsize(file_name), "bytes")

# 4. File का पूरा path
print("Path:", os.path.abspath(file_name))

# 5. Current folder की files/folders
print("Folder Contents:")
print(os.listdir("."))
