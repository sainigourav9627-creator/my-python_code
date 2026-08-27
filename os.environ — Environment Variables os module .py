os.environ — Environment Variables

os.environ का use Python में Operating System के Environment Variables को access करने के लिए होता है।

पहले समझो: Environment Variable क्या है?

Windows कुछ important information को variables में store करता है, जैसे:

USERNAME
USERPROFILE
OneDrive
PATH

Syntax

import os

print(os.environ["VARIABLE_NAME"])


आपके PC पर Practical

आपका USERPROFILE:

import os
print(os.environ["USERPROFILE"])



OneDrive भी देख सकते हैं

import osprint(os.environ["OneDrive"])


os.environ को ऐसे समझो
os.environ
    ↓
Environment Variables की जानकारी
    ↓
USERPROFILE
OneDrive
PATH
USERNAME
etc.


os.environ.get() भी important है
import os

print(os.environ.get("USERNAME"))
