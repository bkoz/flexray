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

#
# Build the clock face.
#

# (1/12 of a circle)
deltaR = 2 * math.pi / 12
r = 0
origin = Point([0, 0, 0])
for i in range(12):
    T = Matrix.translation(0, 0, radius)
    R = Matrix.rotation_y(r)
    position = R * T * origin
    
    #
    # Translate and scale to Canvas coords.
    # These transform matrices should be calculated outside
    # of this loop.
    #
    Translate = Matrix.translation(0.5, 1.0, 0.5)
    Scale = Matrix.scaling(width - 1, 1, height - 1)
    position = Scale * Translate * position
    
    #
    # Round and clip to Canvas coordinates.
    #
    row = round(position[0])
    if row < 0:
        row = 0
    if row > width - 1:
        row = width - 1

    col = round(position[2])
    if col < 0:
        col = 0
    if col > height - 1:
        col = height -1
    
    canvas.write_pixel(row, col, pen)
    r += deltaR

canvas.canvas_to_ppm()