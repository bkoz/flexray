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
        assert self.m.__len__() == other.m.__len__() == 4, 'Matrix dimensions !='
        r = []
        for x in range(self.m.__len__()):
            for y in range(self.m.__len__()):
                r.append(math.isclose(self.m[x][y], other.m[x][y]))
        return True in r and False not in r

    #
    # Matrix rows and columns must be equal length.
    #
    def __mul__(self, other):
        assert self.m.__len__() == other.m.__len__() == 4, 'Matrix dimensions are not compatible'
        r = Matrix()
        r.m=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        for row in range(self.m.__len__()):
            for col in range(self.m.__len__()):
                r.m[row][col] += self.m[row][0] * other.m[0][col] + self.m[row][1] * other.m[1][col] \
                     + self.m[row][2] * other.m[2][col] + self.m[row][3] * other.m[3][col]
        return r
    
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
