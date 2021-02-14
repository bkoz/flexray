from behave import *
from Point import *
from Vector import *
from Ray import *

@given(u'origin ← point(1, 2, 3)')
def step_impl(context):
    context.origin = Point([1, 2, 3])
@given(u'direction ← vector(4, 5, 6)')
def step_impl(context):
    context.direction = Vector([4, 5, 6])
@when(u'r ← ray(origin, direction)')
def step_impl(context):
    context.r = Ray(context.origin, context.direction)
@then(u'r.origin = origin')
def step_impl(context):
    assert(context.r.origin == context.origin)
@then(u'r.direction = direction')
def step_impl(context):
    assert(context.r.direction == context.direction)

@given(u'r ← ray(point(2, 3, 4), vector(1, 0, 0))')
def step_impl(context):
    context.r = Ray(Point([2, 3, 4]), Vector([1, 0, 0]))
@then(u'position(r, 0) = point(2, 3, 4)')
def step_impl(context):
    assert(context.r.position(0) == Point([2, 3, 4]))
@then(u'position(r, 1) = point(3, 3, 4)')
def step_impl(context):
    assert(context.r.position(1) == Point([3, 3, 4]))
@then(u'position(r, -1) = point(1, 3, 4)')
def step_impl(context):
    assert(context.r.position(-1) == Point([1, 3, 4]))
@then(u'position(r, 2.5) = point(4.5, 3, 4)')
def step_impl(context):
    assert(context.r.position(2.5) == Point([4.5, 3, 4]))