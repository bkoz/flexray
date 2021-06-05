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
            l.append(math.isclose(i, j, rel_tol=1e-4, abs_tol=0.000001))
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
    
    def translation(x, y, z):
        t = Matrix.identity()
        t[0][3] = x
        t[1][3] = y
        t[2][3] = z
        return t
    
    def scaling(x, y, z):
        t = Matrix.identity()
        t[0][0] = x
        t[1][1] = y
        t[2][2] = z
        return t
    
    def rotation_x(r):
        t = Matrix.identity()
        t[1][1] = math.cos(r)
        t[1][2] = -math.sin(r)
        t[2][1] = math.sin(r)
        t[2][2] = math.cos(r)
        return t
    
    def rotation_y(r):
        t = Matrix.identity()
        t[0][0] = math.cos(r)
        t[0][2] = math.sin(r)
        t[2][0] = -math.sin(r)
        t[2][2] = math.cos(r)
        return t

    def rotation_z(r):
        t = Matrix.identity()
        t[0][0] = math.cos(r)
        t[0][1] = -math.sin(r)
        t[1][0] = math.sin(r)
        t[1][1] = math.cos(r)
        return t
    
    def shearing(xy, xz, yx, yz, zx, zy):
        t = Matrix.identity()
        t[0][1] = xy
        t[0][2] = xz
        t[1][0] = yx
        t[1][2] = yz
        t[2][0] = zx
        t[2][1] = zy
        return t
    
    # TODO
    def view_transform(fromP, to, up):
        t = Matrix.identity()
        t[0][0] = 33.3
        

        return t