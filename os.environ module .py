os.environ

os.environ का use Operating System के Environment Variables को access करने के लिए होता है।

Environment variables ऐसी settings/information होती हैं जिन्हें Windows और दूसरे programs use करते हैं।


Syntax
import os

print(os.environ)


आपके system पर Practical

हमने अभी OneDrive का environment variable इस्तेमाल किया था:

import os
print(os.environ.get("OneDrive"))

आपके system पर output:
C:\Users\ajski\OneDrive



os.environ
     ↓
Environment variables
     ↓
.get("OneDrive")
     ↓
OneDrive का path


import os

print(os.environ.get("USERPROFILE"))



os.environ["NAME"]
