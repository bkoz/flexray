#
# Chapter 5 - Sillouette of a sphere
#
from Point import Point
from Vector import *
from Canvas import *
from Matrix import *
from Color import *
from Sphere import *
import os

print(f'{os.cpu_count()} logical threads available')

# Canvas
canvas_pixels = 100
canvas = Canvas(canvas_pixels, canvas_pixels)
color = Color(1, 0, 0)
ray_origin = Point([0, 0, -5])
wall_z = 10
wall_size = 7
pixel_size = wall_size / canvas_pixels
half = wall_size / 2
shape = Sphere()

for y in range(canvas_pixels - 1):
    world_y = half - pixel_size * y
    for x in range(canvas_pixels - 1):
        world_x = -half + pixel_size * x
        position = Point([world_x, world_y, wall_z])
        r = Ray(ray_origin, normalize(position - ray_origin))
        xs = shape.intersect(r)
        if (xs):
            canvas.write_pixel(x, y, color)
    
canvas.canvas_to_ppm()