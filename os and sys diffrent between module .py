os = Computer की Files & Folders 🗂️


बस एक लाइन याद करो:

🗂️ os = Computer की Files/Folders से काम
🐍 sys = Python के अंदर/runtime से काम


import os

os.getcwd()       # मैं किस folder में हूँ?
os.listdir()      # इस folder में क्या है?
os.mkdir()        # नया folder बनाओ
os.makedirs()     # nested folders बनाओ
os.chdir()        # folder बदलो
os.remove()       # file delete करो
os.rmdir()        # folder delete करो
os.path.exists()  # path मौजूद है?
os.path.isfile()  # file है?
os.path.isdir()   # folder है?

os → Files, Folders, Paths


sys = Python की Runtime/Interpreter Information 🐍



| काम                       | Module |
| ------------------------- | ------ |
| Current folder देखना      | `os`   |
| Files की list देखना       | `os`   |
| Folder बनाना              | `os`   |
| File delete करना          | `os`   |
| Path check करना           | `os`   |
| Python version देखना      | `sys`  |
| Command-line arguments    | `sys`  |
| Program बंद करना          | `sys`  |
| Input/output streams      | `sys`  |
| Python executable का path | `sys`  |
| Module search path        | `sys`  |
