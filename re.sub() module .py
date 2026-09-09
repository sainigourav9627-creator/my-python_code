re.sub() क्या करता है?

re.sub() का काम है text के किसी pattern को दूसरे text से replace करना।


import re

text = "I like Java"

result = re.sub("Java", "Python", text)

print(result)
