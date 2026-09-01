re.match() string की शुरुआत से pattern check करता है।

import re

text = "Python is easy"

result = re.match("Python", text)

print(result.group()) 


Output:

Python


  
  or


import re

text = "I love Python"

result = re.match("Python", text)

print(result)


Output:

None
