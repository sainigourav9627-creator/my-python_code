re Module

re का मतलब है Regular Expression।

इसका इस्तेमाल text के अंदर pattern खोजने, match करने और replace करने के लिए होता है।

पहले:

import re

सबसे basic function: re.search() ⭐

re.search() पूरे string में दिए गए pattern को खोजता है।

import re

text = "I am learning Python"

result = re.search("Python", text)

print(result)
