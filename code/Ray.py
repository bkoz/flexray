class Ray:
    def __init__(self, origin, dir):
        self.origin = origin
        self.direction = dir

    def __str__(self):
        return "({0}, {1})".format(self.origin, self.direction)
    
    def position(self, t):
        return self.origin + self.direction * t