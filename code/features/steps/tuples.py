from behave import *
from Tuple import Tuple
from Point import Point
from Vector import Vector

@given('a ← tuple(4.3, -4.2, 3.1, 1.0)')
def step_impl(context):
    context.a = Tuple(4.3, -4.2, 3.1, 1.0)
@then('a.x = 4.3')
def step_impl(context):
    assert(context.a.x == 4.3)
@then('a.y = -4.2')
def step_impl(context):
    assert(context.a.y == -4.2)
@then('a.z = 3.1')
def step_impl(context):
    assert(context.a.z == 3.1)
@then('a.w = 1.0')
def step_impl(context):
    assert(context.a.w == 1.0)
@then('a is a point')
def step_impl(context):
    assert(context.a.isaPoint() is True)
@then('a is not a vector')
def step_impl(context):
    assert(context.a.isaVector() is False)

@given('a ← tuple(4.3, -4.2, 3.1, 0.0)')
def step_impl(context):
    context.a = Tuple(4.3, -4.2, 3.1, 0.0)
@then('a.w = 0.0')
def step_impl(context):
    assert(context.a.w == 0.0)
@then('a is not a point')
def step_impl(context):
    assert(context.a.isaPoint() is False)
@then('a is a vector')
def step_impl(context):
    assert(context.a.isaVector() is True)

@given(u'p ← point(4, -4, 3)')
def step_impl(context):
    context.p = Point(4, -4, 3)
@then(u'p = tuple(4, -4, 3, 1)')
def step_impl(context):
    assert(context.p == Tuple(4, -4, 3, 1))

@given(u'v ← vector(4, -4, 3)')
def step_impl(context):
    context.v = Vector(4, -4, 3)
@then(u'v = tuple(4, -4, 3, 0)')
def step_impl(context):
    assert(context.v == Tuple(4, -4, 3, 0))

@given(u'a1 ← tuple(3, -2, 5, 1)')
def step_impl(context):
    context.a1 = Tuple(3, -2, 5, 1)
@given(u'a2 ← tuple(-2, 3, 1, 0)')
def step_impl(context):
    context.a2 = Tuple(-2, 3, 1, 0)
@then(u'a1 + a2 = tuple(1, 1, 6, 1)')
def step_impl(context):
    assert(context.a1 + context.a2 == Tuple(1, 1, 6, 1))

@given(u'p1 ← point(3, 2, 1)')
def step_impl(context):
    context.p1 = Point(3, 2, 1)
@given(u'p2 ← point(5, 6, 7)')
def step_impl(context):
    context.p2 = Point(5, 6, 7)
@then(u'p1 - p2 = vector(-2, -4, -6)')
def step_impl(context):
    assert(context.p1 - context.p2 == Vector(-2, -4, -6))

@given(u'p ← point(3, 2, 1)')
def step_impl(context):
    context.p = Point(3, 2, 1)
@given(u'v ← vector(5, 6, 7)')
def step_impl(context):
    context.v = Vector(5, 6, 7)
@then(u'p - v = point(-2, -4, -6)')
def step_impl(context):
    assert(context.p - context.v == Point(-2, -4, -6))

@given(u'v1 ← vector(3, 2, 1)')
def step_impl(context):
    context.v1 = Vector(3, 2, 1)
@given(u'v2 ← vector(5, 6, 7)')
def step_impl(context):
    context.v2 = Vector(5, 6, 7)
@then(u'v1 - v2 = vector(-2, -4, -6)')
def step_impl(context):
    assert(context.v1 - context.v2 == Vector(-2, -4, -6))

@given(u'zero ← vector(0, 0, 0)')
def step_impl(context):
    context.zero = Vector(0, 0, 0)
@given(u'v ← vector(1, -2, 3)')
def step_impl(context):
    context.v = Vector(1, -2, 3)
@then(u'zero - v = vector(-1, 2, -3)')
def step_impl(context):
    assert(context.zero - context.v == Vector(-1, 2, -3))