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
radius = 0.5
canvas = Canvas(width, height)
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
    # Screen to canvas(raster) coordinates a hack.
    #
    # Translate, scale and clip to Canvas coords.
    #
    x = position[0] + 0.5
    z = position[2] + 0.5
    row = round(x * (width - 1))
    if row < 0:
        row = 0
    col = round(z * (height - 1))
    if col < 0:
        col = 0
    canvas.write_pixel(row, col, pen)

    #print(f'Angle = {r}, x = {x}, z = {z}')
    print(f'row = {row}, col = {col}')
    r += deltaR

canvas.canvas_to_ppm()