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
        
