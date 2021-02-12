from Point import Point
from Vector import *
from Canvas import *

class Projectile:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

class Environment:
    def __init__(self, gravity, wind):
        self.gravity = gravity
        self.wind = wind

def tick(env, proj):
    position = proj.position + proj.velocity
    velocity = proj.velocity + env.gravity + env.wind
    return Projectile(position, velocity)

# Canvas
width = 900
height = 550
canvas = Canvas(width, height)

# Set initial projectile position and direction.
start = Point(0, 1, 0)
initial_velocity = normalize(Vector(1, 1.8, 0)) * 11.25

p = Projectile(start, initial_velocity)
# Set environment gravity and wind vectors.
gravity = Vector(0, -0.1, 0)
wind = Vector(-0.01, 0, 0)
e = Environment(gravity, wind)

pen = Color(1,0.5,0)
while (p.position[1] > 0):
    if (p.position[0] > 0 and p.position[0] < width) and (p.position[1] > 0 and p.position[1] < height):
        x = round(p.position[0])
        y = height - round(p.position[1])
        canvas.write_pixel(x, y, pen)
    p = tick(e, p)

canvas.canvas_to_ppm()