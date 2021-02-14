# flexray.py
#
# Transform testing.
#
from Matrix import *
from Point import *
from Vector import *
from Ray import *
from Sphere import *

p = Point([1, 0, 1])
A = Matrix.rotation_x(math.pi / 2)
B = Matrix.scaling(5, 5, 5)
C = Matrix.translation(10, 5, 7)

p2 = A * p
assert(p2 == Point([1, -1, 0]))
p3 = B * p2
assert(p3 == Point([5, -5, 0]))
p4 = C * p3
assert(p4 == Point([15, 0, 7]))

print(p4)

T = C * B * A
assert(T * p == Point([15, 0, 7]))
print(T * p)

Tf = Matrix.translation(10, 5, 7) * Matrix.scaling(5, 5, 5) * Matrix.rotation_x(math.pi/2)
assert(Tf * p == Point([15, 0, 7]))

print(Tf * p)

s = Sphere()
r1 = Ray(Point([0, 0, 5]), Vector([0, 0, 1]))
i = s.intersect(r1)
if (i != None):
    print(f'Ray {r1} Intersected a {i.object}, count = {i.count}, t1 = {i.t[0]}, t2 = {i.t[1]}')

r2 = Ray(Point([0, 1, 5]), Vector([0, 0, 1]))
i = s.intersect(r2)
if (i != None):
    print(f'Ray {r2} Intersected a {i.object}, count = {i.count}, t1 = {i.t[0]}, t2 = {i.t[1]}')

r3 = Ray(Point([0, 2, 5]), Vector([0, 0, 1]))
i = s.intersect(r3)
if (i != None):
    print(f'Ray {r3} Intersected a {i.object}, count = {i.count}, t1 = {i.t[0]}, t2 = {i.t[1]}')
