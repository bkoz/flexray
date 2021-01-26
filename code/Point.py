from Tuple import Tuple
import numpy

class Point(Tuple):
    def __init__(self, tuple):
        self._ = numpy.array([0.0, 0.0, 0.0, 1.0])
        self._[0] = tuple[0]
        self._[1] = tuple[1]
        self._[2] = tuple[2]

    def __str__(self):
        return "{0}".format(self._)
