from Point import *

class Primitive:
    def __init__(self):
        self.origin = Point([0, 0, 0])
        print("Primitive constructor")

    def __str__(self):
        return "{0}".format(self.origin)
    
    def getOrigin(self):
        print("Primitive getOrigin()")
        return self.origin
    
    def setOrigin(self, o):
        print("Primitive setOrigin()")
        self.origin = o