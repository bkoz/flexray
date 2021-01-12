class Tuple:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __str__(self):
        return "({0}, {1}, {2}, {3})".format(self.x, self.y, self.z, self.w)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        w = self.w + other.w
        return Tuple(x, y, z, w)
    
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        w = self.w - other.w
        return Tuple(x, y, z, w)

    def __mul__(self, scalar):
        x = self.x * scalar
        y = self.y * scalar
        z = self.z * scalar
        w = self.w * scalar
        return Tuple(x, y, z, w)

    def __truediv__(self, scalar):
        x = self.x / scalar
        y = self.y / scalar
        z = self.z / scalar
        w = self.w / scalar
        return Tuple(x, y, z, w)
    
    def __neg__(self):
        return Tuple(-self.x, -self.y, -self.z, -self.w)

    def __eq__(self, other):
        return((self.x == other.x) and (self.y == other.y) and (self.z == other.z) and (self.w == other.w))
    
    def isaPoint(self):
        return self.w == 1.0

    def isaVector(self):
        return self.w == 0.0

