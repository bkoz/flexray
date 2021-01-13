from Tuple import Tuple
import math

class Vector(Tuple):
    def __init__(self, x, y, z):
        Tuple.__init__(self, x, y, z, 0)
        
    def __str__(self):
        return "({0}, {1}, {2})".format(self.x, self.y, self.z)

def magnitude(v):
    assert v.isaVector(), "Input is not a Vector!"
    return math.sqrt(v.x * v.x + v.y * v.y + v.z * v.z)

def normalize(v):
    assert v.isaVector(), "Input is not a Vector!"
    m = magnitude(v)
    return Vector(v.x/m, v.y/m, v.z/m)

def dot(a, b):
    assert a.isaVector(), "Input is not a Vector!"
    assert b.isaVector(), "Input is not a Vector!"
    return a.x * b.x + a.y * b.y + a.z * b.z + a.w * b.w

def cross(a, b):
    assert a.isaVector(), "Input is not a Vector!"
    assert b.isaVector(), "Input is not a Vector!"
    return Vector(a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z, a.x * b.y - a.y * b.x)