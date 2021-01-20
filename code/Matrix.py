import math

class Matrix(list):
    def __init__(self):
        self.m = [[1, 0], [0, 1]]
        
    def __str__(self):
        return "Matrix ({0}x{0}) {1}".format(self.m.__len__(), self.m)
    
    def get(self, r, c):
        return self.m[r][c]
    
    def __getitem__(self, r):
        return self.m[r]
    
    def __eq__(self, other):
        r = []
        for x in range(self.m.__len__()):
            for y in range(self.m.__len__()):
                r.append(math.isclose(self.m[x][y], other.m[x][y]))
        return True in r and False not in r

"""     def __add__(self, other):
        r = self.x + other.x
        g = self.y + other.y
        b = self.z + other.z
        return Color(r, g, b)
    
    def __sub__(self, other):
        r = self.x - other.x
        g = self.y - other.y
        b = self.z - other.z
        return Color(r, g, b)

    def __mul__(self, c):
        r = self.x * c.x
        g = self.y * c.y
        b = self.z * c.z
        return Color(r, g, b)

    def __truediv__(self, scalar):
        r = self.x / scalar
        g = self.y / scalar
        b = self.z / scalar
        return Color(r, g, b)
    
    def __neg__(self):
        return Color(-self.x, -self.y, -self.z)

    def scale(self, scalar):
        r = self.x * scalar
        g = self.y * scalar
        b = self.z * scalar
        return Color(r, g, b) """
