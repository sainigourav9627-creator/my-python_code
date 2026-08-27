os.mkdir("Python") ne Python bana diya, 
phir os.makedirs("Python/Modules/OS") 
uske andar Modules/OS bana dega — ye bilkul valid hai.

import os

# mkdir() → ek folder
os.mkdir("Python")


# makedirs() → nested folders
os.makedirs("Python/Modules/OS")



import os

os.mkdir("SingleFolder")

os.makedirs("Parent/Child/GrandChild")
