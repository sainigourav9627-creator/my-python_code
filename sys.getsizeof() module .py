sys.getsizeof()

sys.getsizeof() का उपयोग किसी Python object का memory size bytes में जानने के लिए किया जाता है।

import sys

x = 10
name = "Gourav"
numbers = [1, 2, 3, 4, 5]

print(sys.getsizeof(x))
print(sys.getsizeof(name))
print(sys.getsizeof(numbers))
