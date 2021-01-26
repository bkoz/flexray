import math
import numpy

class Matrix(list):
    def __init__(self, l):
        self._ = numpy.array(l)
        
    def __str__(self):
        return "{0}".format(self._)
        
    def __eq__(self, other):
        eq = self._ == other._
        return True in eq and False not in eq
    
    def __ne__(self, other):
        eq = self._ == other._
        return True not in eq and False in eq

    def __mul__(self, other):
        return Matrix(numpy.dot(self._, other._))
    
"""     def __add__(self, other):
        r = self.x + other.x
        g = self.y + other.y
        b = self.z + other.z
        return Color(r, g, b)
    
    def __sub__(self, other):
        r = self.x - other.x
        g = self.y - other.y
        b = self.z - other.z
        return Color(r, g, b)

    def __truediv__(self, scalar):
        r = self.x / scalar
        g = self.y / scalar
        b = self.z / scalar
        return Color(r, g, b)
    
    def __neg__(self):
        return Color(-self.x, -self.y, -self.z)

    def scale(self, scalar):
        r = self.x * scalar
        g = self.y * scalar
        b = self.z * scalar
        return Color(r, g, b) """
