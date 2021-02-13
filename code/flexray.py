# flexray.py
#
# Fluent API-style transform chaining.
#
from Matrix import *
from Point import *

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

print(Tf * p)