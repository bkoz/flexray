import math
import numpy as np

class Vector(np.ndarray):
    def __new__(cls, *args, **kwargs):
        a = np.array(args)
        a.resize(4)
        a[3] = 0.0
        return np.ndarray.__new__(cls, shape = (4), dtype = np.float, buffer = a.astype(np.float))

    def __array_finalize__(self, obj):
        pass

    def __eq__(self, other):
        l = []
        for i in range(self.shape[0]):
            l.append(math.isclose(self[i], other[i], rel_tol=1e-4, abs_tol=0.000001))
        return True in l and False not in l

def magnitude(v):
    return math.sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2])

def normalize(v):
    m = magnitude(v)
    return Vector([v[0]/m, v[1]/m, v[2]/m])

def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2] + a[3] * b[3]

def cross(a, b):
    return Vector([a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]])