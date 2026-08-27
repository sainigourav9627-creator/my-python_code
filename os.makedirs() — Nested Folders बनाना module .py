import os

os.makedirs("Python/Modules/OS")


Important Interview Point

अगर folders पहले से मौजूद हो सकते हैं और error नहीं चाहिए, तो:

import os

os.makedirs("Python/Modules/OS", exist_ok=True)

exist_ok=True का मतलब:

Folder पहले से मौजूद है तो error मत दो।
