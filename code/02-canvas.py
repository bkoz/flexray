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

# def pos_to_pixel(width, height, x, y):

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
while (p.position.y > 0):
    if (p.position.x > 0 and p.position.x < width) and (p.position.y > 0 and p.position.y < height):
        x = round(p.position.x) - 1
        y = height - round(p.position.y) - 1
        canvas.write_pixel(x, y, pen)
    p = tick(e, p)

canvas.canvas_to_ppm()