from rayUtils import *

class Color:
    def __init__(self, r, g, b):
        self.red = r
        self.green = g
        self.blue = b

    def __str__(self):
        return "({0}, {1}, {2})".format(self.red, self.green, self.blue)

    def __add__(self, other):
        r = self.red + other.red
        g = self.green + other.green
        b = self.blue + other.blue
        return Color(r, g, b)
    
    def __sub__(self, other):
        r = self.red - other.red
        g = self.green - other.green
        b = self.blue - other.blue
        return Color(r, g, b)

    def __mul__(self, c):
        r = self.red * c.red
        g = self.green * c.green
        b = self.blue * c.blue
        return Color(r, g, b)

    def __truediv__(self, scalar):
        r = self.red / scalar
        g = self.green / scalar
        b = self.blue / scalar
        return Color(r, g, b)
    
    def __neg__(self):
        return Color(-self.red, -self.green, -self.blue)

    def __eq__(self, other):
        return float_eq(self.red, other.red) \
            and float_eq(self.green, other.green) \
                and float_eq(self.blue, other.blue)

    def scale(self, scalar):
        r = self.red * scalar
        g = self.green * scalar
        b = self.blue * scalar
        return Color(r, g, b)
