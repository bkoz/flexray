import numpy as np

class Point(np.ndarray):
    def __new__(cls, *args, **kwargs):
        a = np.array(args)
        a.resize(4)
        a[3] = 1.0
        return np.ndarray.__new__(cls, shape = (4), dtype = np.float, buffer = a.astype(np.float))

    def __array_finalize__(self, obj):
        pass

    def __eq__(self, other):
        l = []
        for i in range(self.shape[0]):
            l.append(self[i] == other[i])
        return True in l and False not in l

    