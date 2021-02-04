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

    # def __str__(self):
    #     return "print"
                
    #
    # Equality test for Matrix, Matrix or Tuple, Tuple floats.
    # The numpy.array.ndim handles the special case when Tuples or Points are passed in.
    #
    def __eq__(self, other):
        l = []
        # if (self._.ndim == 2):
        #     for i,j in zip(self._, other._):
        #         for a,b in zip(i,j):
        #             l.append(math.isclose(a, b, rel_tol=1e-04))
        #     ret = True in l and False not in l
        # else:
        #     for i,j in zip(self._, other._):
        #         l.append(math.isclose(i, j,rel_tol=1e-04))
        #     ret = True in l and False not in l   
        # return ret
        for r in range(self.shape[0]):
            for c in range(self.shape[1]):
                l.append(self[r][c] == other[r][c])
        ret = True in l and False not in l
        return ret

    def __ne__(self, other):
        l = []
        for r in range(self.shape[0]):
            for c in range(self.shape[1]):
                l.append(self[r][c] == other[r][c])
        ret = True not in l and False in l
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

