import math
import numpy as np

class Matrix(np.ndarray):
    def __new__(cls, *args, **kwargs):
        r = 0
        for i in args:
            for j in i:
                r += 1
                c = 0
                for k in j:
                    c += 1
        a = np.array(args)
        return np.ndarray.__new__(cls, shape = (r, c), dtype = np.float, buffer = a.astype(np.float))

    def __array_finalize__(self, obj):
        pass
            
    #
    # Equality test
    #
    def __eq__(self, other):
        l = []
        s = np.array(self)
        o = np.array(other)
        for i,j in zip(s.flatten(), o.flatten()):
            l.append(math.isclose(i, j, rel_tol=1e-4))
        ret = (True in l) and (False not in l)
        return ret

    def __ne__(self, other):
        l = []
        s = np.array(self)
        o = np.array(other)
        for i,j in zip(s.flatten(), o.flatten()):
            l.append(math.isclose(i, j, rel_tol=1e-4))
        ret = (True not in l) and (False in l)
        return ret

    def __mul__(self, other):
        return np.dot(self, other)
    
    @staticmethod
    def identity():
        return Matrix(np.identity(4))
    
    def transpose(self):
        return Matrix(np.transpose(self))
    
    def determinant(self):
        return np.linalg.det(self)

    def submatrix(self, row, col):
        tmp = np.delete(self, row, axis=0)
        return Matrix(np.delete(tmp, col, axis=1))
    
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
        return Matrix(np.linalg.inv(self))

