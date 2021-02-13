#
# Chapter 4 - Clock
#
from Point import Point
from Vector import *
from Canvas import *
from Matrix import *
from Color import *

# Canvas
width = 500
height = 500
radius = 1
canvas = Canvas(2*width, 2*height)
pen = Color(1, 1 ,1)

# (1/12 of a circle)
deltaR = 2 * math.pi / 12
r = 0
origin = Point([0, 0, 0])
for i in range(12):
    T = Matrix.translation(0, 0, radius)
    R = Matrix.rotation_y(r)
    position = R * T * origin
    #
    # World to device coordinates not right
    # Need a transform for this.
    # Should not have to clamp row and col values.
    #
    row = round(width * position[0]) + width - 1
    if row < 0:
        row = 0
    col = round(height * position[2]) + height - 1
    if col < 0:
        col = 0
    canvas.write_pixel(row, col, pen)

    print(f'Angle = {r}, x = {position[0]}, z = {position[2]}')
    #print(f'row = {row}, col = {col}')
    r += deltaR



canvas.canvas_to_ppm()