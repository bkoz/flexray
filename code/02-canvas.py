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
width = 512
height = 512
canvas = Canvas(width, height)

# Set initial projectile position and direction.
start = Point(0, 1, 0)
initial_velocity = normalize(Vector(1, 1.8, 0)) * 7.5

p = Projectile(start, initial_velocity)
# Set environment gravity and wind vectors.
gravity = Vector(0, -0.1, 0)
wind = Vector(-0.01, 0, 0)
e = Environment(gravity, wind)

step = 0
pen = Color(1,1,1)
while (p.position.y > 0):
    print("Step: {0}, Position: ({1}, {2})".format(step, p.position.x, p.position.y))
    if (p.position.x > 0 and p.position.x < width) and (p.position.y > 0 and p.position.y < height):
        canvas.write_pixel(round(p.position.x), height - round(p.position.y), pen)
    p = tick(e, p)
    step += 1

canvas.canvas_to_ppm()