from Tuple import Tuple

class Point(Tuple):
    def __init__(self, x, y, z):
        Tuple.__init__(self, x, y, z, 1.0)
        
    def __str__(self):
        return "({0}, {1}, {2})".format(self.x, self.y, self.z)
