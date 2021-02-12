import numpy as np
import math

class Tuple(np.ndarray):
    def __new__(cls, *args, **kwargs):
        a = np.array(args)
        return np.ndarray.__new__(cls, shape = (4), dtype = np.float, buffer = a.astype(np.float))

    def __array_finalize__(self, obj):
        pass

    def __eq__(self, other):
        l = []
        for i in range(self.shape[0]):
            l.append(self[i] == other[i])
        return True in l and False not in l

    def isaPoint(self):
        return self[3] == 1.0

    def isaVector(self):
        return self[3] == 0.0

