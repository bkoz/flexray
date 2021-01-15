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
    
    def write_pixel(self, x, y, color):
        index = self.width * y + x
        self.pixels[index] = color

    def pixel_at(self, x, y):
        index = self.width * y + x
        return self.pixels[index]
    
    def pix_to_char(self, p):
        c = round(p * 255)
        if (c < 0):
            c = 0
        if (c > 255):
            c = 255
        return c

    def canvas_to_ppm(self):
        f = open('image{0}x{1}.ppm'.format(self.width, self.height), 'w')
        f.write('P3\n')
        f.write('{0} {1}\n'.format(self.width, self.height))
        f.write('255\n')

        count = 0
        for y in range(self.height):
            for x in range(self.width):
                if (count > 5):
                    f.write('\n')
                    count = 0
                index = self.width * y + x
                f.write('{0} {1} {2} '.format(self.pix_to_char(self.pixels[index].red), \
                    self.pix_to_char(self.pixels[index].green), \
                        self.pix_to_char(self.pixels[index].blue)))
                count += 1
        f.close()
