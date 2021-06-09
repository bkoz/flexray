from Matrix import Matrix
from Sphere import *
from Vector import *
import math
import logging
from behave import *

# logging.basicConfig(level=logging.INFO)

@given(u's ← sphere()')
def step_impl(context):
    context.s = Sphere()
@when(u'n ← normal_at(s, point(1, 0, 0))')
def step_impl(context):
    context.n = context.s.normal_at(Point(1, 0, 0))
@then(u'n = vector(1, 0, 0)')
def step_impl(context):
    assert context.n == Vector(1, 0, 0)

@when(u'n ← normal_at(s, point(0, 1, 0))')
def step_impl(context):
    context.n = context.s.normal_at(Point(0, 1, 0))
@then(u'n = vector(0, 1, 0)')
def step_impl(context):
    assert context.n == Vector(0, 1, 0)

@when(u'n ← normal_at(s, point(0, 0, 1))')
def step_impl(context):
    context.n = context.s.normal_at(Point(0, 0, 1))
@then(u'n = vector(0, 0, 1)')
def step_impl(context):
    assert context.n == Vector(0, 0, 1)

@when(u'n ← normal_at(s, point(√3/3, √3/3, √3/3))')
def step_impl(context):
    context.n = context.s.normal_at(Point(math.sqrt(3)/3, math.sqrt(3)/3, math.sqrt(3)/3))
@then(u'n = vector(√3/3, √3/3, √3/3)')
def step_impl(context):
    assert context.n == Vector(math.sqrt(3)/3, math.sqrt(3)/3, math.sqrt(3)/3)

@then(u'n = normalize(n)')
def step_impl(context):
    assert context.n == normalize(context.n)

@given(u'set_transform(s, translation(0, 1, 0))')
def step_impl(context):
    context.s.setTransform(Matrix.translation(0, 1, 0))
@when(u'n ← normal_at(s, point(0, 1.70711, -0.70711))')
def step_impl(context):
    context.n = context.s.normal_at(Point(0, 1.70711, -0.70711))
@then(u'n = vector(0, 0.70711, -0.70711)')
def step_impl(context):
    assert context.n == Vector(0.0, 0.70711, -0.70711)    

@given(u'm ← scaling(1, 0.5, 1) * rotation_z(π/5)')
def step_impl(context):
    context.m = Matrix.scaling(1, 0.5, 1) * Matrix.rotation_z(math.pi/5)
@given(u'set_transform(s, m)')
def step_impl(context):
    context.s.setTransform(context.m)
@when(u'n ← normal_at(s, point(0, √2/2, -√2/2))')
def step_impl(context):
    context.n = context.s.normal_at(Point(0, math.sqrt(2)/2, -math.sqrt(2)/2))
@then(u'n = vector(0, 0.97014, -0.24254)')
def step_impl(context):
    assert context.n == Vector(0, 0.97014, -0.24254)