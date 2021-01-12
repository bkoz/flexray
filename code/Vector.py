from Tuple import Tuple
import math

class Vector(Tuple):
    def __init__(self, x, y, z):
        Tuple.__init__(self, x, y, z, 0)
        
    def __str__(self):
        return "({0}, {1}, {2})".format(self.x, self.y, self.z)

def magnitude(v):
    return math.sqrt(v.x * v.x + v.y * v.y + v.z * v.z)

def normalize(v):
    m = magnitude(v)
    return Vector(v.x/m, v.y/m, v.z/m)