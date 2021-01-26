import numpy

class Tuple:
    def __init__(self, t):
        self._ = numpy.array(t)

    def __str__(self):
        return "{0}".format(self._)

    def __add__(self, other):
        return Tuple(self._ + other._)
    
    def __sub__(self, other):
        return Tuple(self._ - other._)

    def __mul__(self, scalar):
        return Tuple(self._ * scalar)

    def __truediv__(self, scalar):
        return Tuple(self._ / scalar)
    
    def __neg__(self):
        return Tuple([self._[0] * -1, self._[1] * -1, self._[2] * -1, self._[3] * -1]) 
        
    def __eq__(self, other):
        eq = self._ == other._
        return True in eq and False not in eq
    
    def isaPoint(self):
        return self._[3] == 1.0

    def isaVector(self):
        return self._[3] == 0.0

