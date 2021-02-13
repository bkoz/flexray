from behave import *
from Point import Point
from Matrix import *
from Vector import Vector
import math

@given(u'transform ← translation(5, -3, 2)')
def step_impl(context):
    context.t = Matrix.translation(5, -3, 2)
@given(u'p ← point(-3, 4, 5)')
def step_impl(context):
    context.p = Point([-3, 4, 5])
@then(u'transform * p = point(2, 1, 7)')
def step_impl(context):
    assert(context.t * context.p == Point(2, 1, 7))

@given(u'inv ← inverse(transform)')
def step_impl(context):
    context.inv = Matrix.inverse(context.t)
@then(u'inv * p = point(-8, 7, 3)')
def step_impl(context):
    assert(context.inv * context.p == Point([-8, 7, 3]))

@given(u'v ← vector(-3, 4, 5)')
def step_impl(context):
    context.v = Vector([-3, 4, 5])
@then(u'transform * v = v')
def step_impl(context):
    assert(context.t * context.v == context.v)

@given(u'transform ← scaling(2, 3, 4)')
def step_impl(context):
    context.t = Matrix.scaling(2, 3, 4)
@given(u'p ← point(-4, 6, 8)')
def step_impl(context):
    context.p = Point([-4, 6, 8])
@then(u'transform * p = point(-8, 18, 32)')
def step_impl(context):
    assert(context.t * context.p == Point([-8, 18, 32]))

@given(u'v ← vector(-4, 6, 8)')
def step_impl(context):
    context.v = Vector([-4, 6, 8])
@then(u'transform * v = vector(-8, 18, 32)')
def step_impl(context):
    assert(context.t * context.v == Vector([-8, 18, 32]))

@then(u'inv * v = vector(-2, 2, 2)')
def step_impl(context):
    assert(context.inv * context.v == Vector([-2, 2, 2]))

@given(u'transform ← scaling(-1, 1, 1)')
def step_impl(context):
    context.t = Matrix.scaling(-1, 1, 1)
@given(u'p ← point(2, 3, 4)')
def step_impl(context):
    context.p = Point([2, 3, 4])
@then(u'transform * p = point(-2, 3, 4)')
def step_impl(context):
    assert(context.t * context.p == Point([-2, 3, 4]))

@given(u'p ← point(0, 1, 0)')
def step_impl(context):
    context.p = Point([0, 1, 0])
@given(u'half_quarter ← rotation_x(π / 4)')
def step_impl(context):
    context.half_quarter = Matrix.rotation_x(math.pi / 4)
@given(u'full_quarter ← rotation_x(π / 2)')
def step_impl(context):
    context.full_quarter = Matrix.rotation_x(math.pi / 2)
@then(u'half_quarter * p = point(0, √2/2, √2/2)')
def step_impl(context):
    assert(context.half_quarter * context.p == Point([0, math.sqrt(2)/2, math.sqrt(2)/2]))
@then(u'full_quarter * p = point(0, 0, 1)')
def step_impl(context):
    print(context.full_quarter * context.p)
    assert(context.full_quarter * context.p == Point([0, 0, 1]))

@given(u'inv ← inverse(half_quarter)')
def step_impl(context):
    context.inv = Matrix.inverse(context.half_quarter)
@then(u'inv * p = point(0, √2/2, -√2/2)')
def step_impl(context):
    assert(context.inv * context.p == Point([0, math.sqrt(2)/2, -math.sqrt(2)/2]))

@given(u'p ← point(0, 0, 1)')
def step_impl(context):
    context.p = Point([0, 0, 1])
@given(u'half_quarter ← rotation_y(π / 4)')
def step_impl(context):
    context.half_quarter = Matrix.rotation_y(math.pi / 4)
@given(u'full_quarter ← rotation_y(π / 2)')
def step_impl(context):
    context.full_quarter = Matrix.rotation_y(math.pi / 2)
@then(u'half_quarter * p = point(√2/2, 0, √2/2)')
def step_impl(context):
    assert(context.half_quarter * context.p == Point([math.sqrt(2)/2, 0, math.sqrt(2)/2]))
@then(u'full_quarter * p = point(1, 0, 0)')
def step_impl(context):
    assert(context.full_quarter * context.p == Point([1, 0, 0]))

# Defined above
# @given(u'p ← point(0, 1, 0)')
# def step_impl(context):
#     context.p = Point([0, 1, 0])
@given(u'half_quarter ← rotation_z(π / 4)')
def step_impl(context):
    context.half_quarter = Matrix.rotation_z(math.pi / 4)
@given(u'full_quarter ← rotation_z(π / 2)')
def step_impl(context):
    context.full_quarter = Matrix.rotation_z(math.pi / 2)
@then(u'half_quarter * p = point(-√2/2, √2/2, 0)')
def step_impl(context):
    assert(context.half_quarter * context.p == Point([-math.sqrt(2)/2, math.sqrt(2)/2, 0]))
@then(u'full_quarter * p = point(-1, 0, 0)')
def step_impl(context):
    assert(context.full_quarter * context.p == Point([-1, 0, 0]))

@given(u'transform ← shearing(1, 0, 0, 0, 0, 0)')
def step_impl(context):
    context.t = Matrix.shearing(1, 0, 0, 0, 0, 0)
@then(u'transform * p = point(5, 3, 4)')
def step_impl(context):
    assert(context.t * context.p == Point([5, 3, 4]))

@given(u'transform ← shearing(0, 1, 0, 0, 0, 0)')
def step_impl(context):
    context.t = Matrix.shearing(0, 1, 0, 0, 0, 0)
@then(u'transform * p = point(6, 3, 4)')
def step_impl(context):
    assert(context.t * context.p == Point([6, 3, 4]))

@given(u'transform ← shearing(0, 0, 1, 0, 0, 0)')
def step_impl(context):
    context.t = Matrix.shearing(0, 0, 1, 0, 0, 0)
@then(u'transform * p = point(2, 5, 4)')
def step_impl(context):
        assert(context.t * context.p == Point([2, 5, 4]))

@given(u'transform ← shearing(0, 0, 0, 1, 0, 0)')
def step_impl(context):
    context.t = Matrix.shearing(0, 0, 0, 1, 0, 0)
@then(u'transform * p = point(2, 7, 4)')
def step_impl(context):
    assert(context.t * context.p == Point([2, 7, 4]))

@given(u'transform ← shearing(0, 0, 0, 0, 1, 0)')
def step_impl(context):
    context.t = Matrix.shearing(0, 0, 0, 0, 1, 0)
@then(u'transform * p = point(2, 3, 6)')
def step_impl(context):
    assert(context.t * context.p == Point([2, 3, 6]))

@given(u'transform ← shearing(0, 0, 0, 0, 0, 1)')
def step_impl(context):
    context.t = Matrix.shearing(0, 0, 0, 0, 0, 1)
@then(u'transform * p = point(2, 3, 7)')
def step_impl(context):
    assert(context.t * context.p == Point([2, 3, 7]))

@given(u'p ← point(1, 0, 1)')
def step_impl(context):
    context.p = Point([1, 0, 1])
@given(u'A ← rotation_x(π / 2)')
def step_impl(context):
    context.A = Matrix.rotation_x(math.pi / 2)
@given(u'B ← scaling(5, 5, 5)')
def step_impl(context):
    context.B = Matrix.scaling(5, 5, 5)
@given(u'C ← translation(10, 5, 7)')
def step_impl(context):
    context.C = Matrix.translation(10, 5, 7)
@when(u'p2 ← A * p')
def step_impl(context):
    context.p2 = context.A * context.p
@then(u'p2 = point(1, -1, 0)')
def step_impl(context):
    assert(context.p2 == Point([1, -1, 0]))
@when(u'p3 ← B * p2')
def step_impl(context):
    context.p3 = context.B * context.p2
@then(u'p3 = point(5, -5, 0)')
def step_impl(context):
    assert(context.p3 == Point([5, -5, 0]))
@when(u'p4 ← C * p3')
def step_impl(context):
    context.p4 = context.C * context.p3
@then(u'p4 = point(15, 0, 7)')
def step_impl(context):
    assert(context.p4 == Point([15, 0, 7]))


