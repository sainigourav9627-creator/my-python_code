Type	Syntax	Meaning

Public	name	Normally kahin se bhi access
Protected	_name	Internal/subclass use ke liye convention
Private	__name	Class ke andar direct use ke liye intended

class Student:
    def __init__(self):
        self.name = "Gourav"       # Public
        self._age = 25             # Protected
        self.__marks = 80          # Private
