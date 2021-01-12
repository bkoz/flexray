from behave import *
from Tuple import Tuple

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