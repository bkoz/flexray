from Tuple import Tuple
import math
import numpy

class Vector(Tuple):
    def __init__(self, tuple):
        self._ = numpy.array([0.0, 0.0, 0.0, 0.0])
        self._[0] = tuple[0]
        self._[1] = tuple[1]
        self._[2] = tuple[2]

    def __str__(self):
        return "{0}".format(self._)

def magnitude(v):
    assert v.isaVector(), "Input is not a Vector!"
    return math.sqrt(v._[0] * v._[0] + v._[1] * v._[1] + v._[2] * v._[2])

def normalize(v):
    assert v.isaVector(), "Input is not a Vector!"
    m = magnitude(v)
    return Vector([v._[0]/m, v._[1]/m, v._[2]/m])

def dot(a, b):
    assert a.isaVector(), "Input is not a Vector!"
    assert b.isaVector(), "Input is not a Vector!"
    return a._[0] * b._[0] + a._[1] * b._[1] + a._[2] * b._[2] + a._[3] * b._[3]

def cross(a, b):
    assert a.isaVector(), "Input is not a Vector!"
    assert b.isaVector(), "Input is not a Vector!"
    return Vector([a._[1] * b._[2] - a._[2] * b._[1], a._[2] * b._[0] - a._[0] * b._[2], a._[0] * b._[1] - a._[1] * b._[0]])