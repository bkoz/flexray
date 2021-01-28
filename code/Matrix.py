import math
import numpy

class Matrix(list):
    def __init__(self, l):
        self._ = numpy.array(l)
        
    def __str__(self):
        return "{0}".format(self._)
        
    #
    # Equality test for Matrix, Matrix or Tuple, Tuple floats.
    # The numpy.array.ndim handles the special case when Tuples or Points are passed in.
    #
    def __eq__(self, other):
        l=[]
        if (self._.ndim == 2):
            for i,j in zip(self._, other._):
                for a,b in zip(i,j):
                    l.append(math.isclose(a, b, rel_tol=1e-04))
            ret = True in l and False not in l
        else:
            for i,j in zip(self._, other._):
                l.append(math.isclose(i, j,rel_tol=1e-04))
            ret = True in l and False not in l   
        return ret
    
    def __ne__(self, other):
        eq = self._ == other._
        return True not in eq and False in eq

    def __mul__(self, other):
        return Matrix(numpy.dot(self._, other._))
    
    @staticmethod
    def identity():
        return Matrix(numpy.identity(4))
    
    def transpose(self):
        return Matrix(numpy.transpose(self._))
    
    def determinant(self):
        return numpy.linalg.det(self._)

    def submatrix(self, row, col):
        tmp = numpy.delete(self._, row, axis=0)
        return Matrix(numpy.delete(tmp, col, axis=1))
    
    def minor(self, row, col):
        return self.submatrix(row, col).determinant()
    
    def cofactor(self, row, col):
        minor = self.minor(row, col)
        if ((row + col) % 2):
            minor = -minor
        return minor
    
    def isInvertable(self):
        if (math.isclose(self.determinant(), 0)):
            invertable = False
        else:
            invertable = True
        return invertable

    def inverse(self):
        return Matrix(numpy.linalg.inv(self._))

