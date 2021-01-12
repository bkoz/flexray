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