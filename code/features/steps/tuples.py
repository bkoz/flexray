from behave import *
from Tuple import Tuple
from Point import Point
from Vector import *
import math

@given('a ← tuple(4.3, -4.2, 3.1, 1.0)')
def step_impl(context):
    context.a = Tuple([4.3, -4.2, 3.1, 1.0])
@then('a.x = 4.3')
def step_impl(context):
    assert(context.a[0] == 4.3)
@then('a.y = -4.2')
def step_impl(context):
    assert(context.a[1] == -4.2)
@then('a.z = 3.1')
def step_impl(context):
    assert(context.a[2] == 3.1)
@then('a.w = 1.0')
def step_impl(context):
    assert(context.a[3] == 1.0)
@then('a is a point')
def step_impl(context):
    assert(context.a.isaPoint() == True)
@then('a is not a vector')
def step_impl(context):
    assert(context.a.isaVector() == False)

@given('a ← tuple(4.3, -4.2, 3.1, 0.0)')
def step_impl(context):
    context.a = Tuple([4.3, -4.2, 3.1, 0.0])
@then('a.w = 0.0')
def step_impl(context):
    assert(context.a[3] == 0.0)
@then('a is not a point')
def step_impl(context):
    assert(context.a.isaPoint() == False)
@then('a is a vector')
def step_impl(context):
    assert(context.a.isaVector() == True)

@given(u'p ← point(4, -4, 3)')
def step_impl(context):
    context.p = Point([4, -4, 3])
@then(u'p = tuple(4, -4, 3, 1)')
def step_impl(context):
    assert(context.p == Tuple([4, -4, 3, 1]))

@given(u'v ← vector(4, -4, 3)')
def step_impl(context):
    context.v = Vector([4, -4, 3])
@then(u'v = tuple(4, -4, 3, 0)')
def step_impl(context):
    assert(context.v == Tuple([4, -4, 3, 0]))

@given(u'a1 ← tuple(3, -2, 5, 1)')
def step_impl(context):
    context.a1 = Tuple([3, -2, 5, 1])
@given(u'a2 ← tuple(-2, 3, 1, 0)')
def step_impl(context):
    context.a2 = Tuple([-2, 3, 1, 0])
@then(u'a1 + a2 = tuple(1, 1, 6, 1)')
def step_impl(context):
    assert((context.a1 + context.a2) == Tuple([1, 1, 6, 1]))

@given(u'p1 ← point(3, 2, 1)')
def step_impl(context):
    context.p1 = Point([3, 2, 1])
@given(u'p2 ← point(5, 6, 7)')
def step_impl(context):
    context.p2 = Point([5, 6, 7])
@then(u'p1 - p2 = vector(-2, -4, -6)')
def step_impl(context):
    assert(context.p1 - context.p2 == Vector([-2, -4, -6]))

@given(u'p ← point(3, 2, 1)')
def step_impl(context):
    context.p = Point([3, 2, 1])
@given(u'v ← vector(5, 6, 7)')
def step_impl(context):
    context.v = Vector([5, 6, 7])
@then(u'p - v = point(-2, -4, -6)')
def step_impl(context):
    assert(context.p - context.v == Point([-2, -4, -6]))

@given(u'v1 ← vector(3, 2, 1)')
def step_impl(context):
    context.v1 = Vector([3, 2, 1])
@given(u'v2 ← vector(5, 6, 7)')
def step_impl(context):
    context.v2 = Vector([5, 6, 7])
@then(u'v1 - v2 = vector(-2, -4, -6)')
def step_impl(context):
    assert(context.v1 - context.v2 == Vector([-2, -4, -6]))

@given(u'zero ← vector(0, 0, 0)')
def step_impl(context):
    context.zero = Vector([0, 0, 0])
@given(u'v ← vector(1, -2, 3)')
def step_impl(context):
    context.v = Vector([1, -2, 3])
@then(u'zero - v = vector(-1, 2, -3)')
def step_impl(context):
    assert(context.zero - context.v == Vector([-1, 2, -3]))

@given(u'a ← tuple(1, -2, 3, -4)')
def step_impl(context):
    context.a = Tuple([1, -2, 3, -4])
@then(u'-a = tuple(-1, 2, -3, 4)')
def step_impl(context):
    assert(-context.a == Tuple([-1, 2, -3, 4]))

@then(u'a * 3.5 = tuple(3.5, -7, 10.5, -14)')
def step_impl(context):
    assert(context.a * 3.5 == Tuple([3.5, -7, 10.5, -14]))

@then(u'a * 0.5 = tuple(0.5, -1, 1.5, -2)')
def step_impl(context):
    assert(context.a * 0.5 == Tuple([0.5, -1, 1.5, -2]))

@then(u'a / 2 = tuple(0.5, -1, 1.5, -2)')
def step_impl(context):
    assert(context.a / 2 == Tuple([0.5, -1, 1.5, -2]))

@given(u'v ← vector(1, 0, 0)')
def step_impl(context):
    context.v = Vector([1, 0, 0])
@then(u'magnitude(v) = 1')
def step_impl(context):
    assert(magnitude(context.v) == 1)

@given(u'v ← vector(0, 1, 0)')
def step_impl(context):
    context.v = Vector([0, 1, 0])

@given(u'v ← vector(0, 0, 1)')
def step_impl(context):
    context.v = Vector([0, 0, 1])

@given(u'v ← vector(1, 2, 3)')
def step_impl(context):
    context.v = Vector([1, 2, 3])
@then(u'magnitude(v) = √14')
def step_impl(context):
    assert(magnitude(context.v) == math.sqrt(14))
@then(u'normalize(v) = approximately vector(0.26726, 0.53452, 0.80178)')
def step_impl(context):
    assert(normalize(context.v) == Vector([0.2672612419124244, 0.5345224838248488, 0.8017837257372732]))

@given(u'v ← vector(-1, -2, -3)')
def step_impl(context):
    context.v = Vector([-1, -2, -3])

@given(u'v ← vector(4, 0, 0)')
def step_impl(context):
    context.v = Vector([4, 0, 0])
@then(u'normalize(v) = vector(1, 0, 0)')
def step_impl(context):
    assert(normalize(context.v) == Vector([1, 0, 0]))

@when(u'norm ← normalize(v)')
def step_impl(context):
    context.norm = normalize(context.v)
@then(u'magnitude(norm) = 1')
def step_impl(context):
    assert(magnitude(context.norm) == 1)

@given(u'a ← vector(1, 2, 3)')
def step_impl(context):
    context.a = Vector([1, 2, 3])
@given(u'b ← vector(2, 3, 4)')
def step_impl(context):
    context.b = Vector([2, 3, 4])
@then(u'dot(a, b) = 20')
def step_impl(context):
    assert(dot(context.a, context.b) == 20)

@then(u'cross(a, b) = vector(-1, 2, -1)')
def step_impl(context):
    assert(cross(context.a, context.b) == Vector([-1, 2, -1]))
@then(u'cross(b, a) = vector(1, -2, 1)')
def step_impl(context):
    assert(cross(context.b, context.a) == Vector([1, -2, 1]))

@given(u'v ← vector(1, -1, 0)')
def step_impl(context):
    context.v = Vector(1, -1, 0)
@given(u'n ← vector(0, 1, 0)')
def step_impl(context):
    context.n = Vector(0, 1, 0)
@when(u'r ← reflect(v, n)')
def step_impl(context):
    context.r = Tuple.reflect(context.v, context.n)
@then(u'r = vector(1, 1, 0)')
def step_impl(context):
    assert context.r == Vector(1, 1, 0)

@given(u'v ← vector(0, -1, 0)')
def step_impl(context):
    context.v = Vector(0, -1, 0)
@given(u'n ← vector(√2/2, √2/2, 0)')
def step_impl(context):
    context.n = Vector(math.sqrt(2)/2, math.sqrt(2)/2, 0)
@then(u'r = vector(1, 0, 0)')
def step_impl(context):
    assert context.r == Vector(1, 0, 0)