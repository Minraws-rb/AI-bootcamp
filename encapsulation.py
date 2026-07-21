class Students:
    def __init__(self):
        self.name = "RAM"

s = Students()
print(s.name) # this output will be RAM because the name attribute is public and can be accessed directly.

class Teachers:
    def __init__(self):
        self._name = "HNT"

s = Teachers()
print(s._name) # this output will be HNT because the _name attribute is protected and should only be accessed within the class or its subclasses.

class Principals:
    def __init__(self):
        self.__name = "GG"

s = Principals()
print(s.__name) # this will raise an AttributeError because the __name attribute is