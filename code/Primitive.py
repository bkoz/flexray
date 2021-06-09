from Point import *
from Matrix import *

class Primitive:
    def __init__(self):
        self.origin = Point([0, 0, 0])
        self.transform = Matrix.identity()

    def __str__(self):
        return "{0}".format(self.origin)
    
    def getOrigin(self):
        print("Primitive getOrigin()")
        return self.origin
    
    def setOrigin(self, o):
        print("Primitive setOrigin()")
        self.origin = o
    
    def setTransform(self, matrix):
        self.transform = matrix
    
    def getTransform(self):
        return self.transform