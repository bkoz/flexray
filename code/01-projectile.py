from Point import Point
from Vector import *

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

# Set initial projectile position and direction.
p = Projectile(Point(0, 1, 0), normalize(Vector(1, 1, 0)))
# Set environment gravity and wind vectors.
e = Environment(Vector(0, -0.1, 0), Vector(-0.01, 0, 0))

step = 0
while (p.position.y > 0):
    print("Step: {0}, Position: ({1}, {2})".format(step, p.position.x, p.position.y))
    p = tick(e, p)
    step += 1
