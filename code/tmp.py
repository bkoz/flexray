from Color import Color
class Canvas:
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.pixels = []
        self.clear(Color(0, 0, 0))     

    def __str__(self):
        return "({0}, {1})".format(self.width, self.height)

    def clear(self, c):
        self.pixels.clear()
        for _ in range(self.width * self.height):
            self.pixels.append(c)

c = Canvas(512,512)
