from behave import *
from Color import Color

@given(u'c ← color(-0.5, 0.4, 1.7)')
def step_impl(context):
    context.c = Color(-0.5, 0.4, 1.7)
@then(u'c.red = -0.5')
def step_impl(context):
    assert(context.c.red == -0.5)
@then(u'c.green = 0.4')
def step_impl(context):
    assert(context.c.green == 0.4)
@then(u'c.blue = 1.7')
def step_impl(context):
    assert(context.c.blue == 1.7)

@given(u'c1 ← color(0.9, 0.6, 0.75)')
def step_impl(context):
    context.c1 = Color(0.9, 0.6, 0.75)
@given(u'c2 ← color(0.7, 0.1, 0.25)')
def step_impl(context):
    context.c2 = Color(0.7, 0.1, 0.25)
@then(u'c1 + c2 = color(1.6, 0.7, 1.0)')
def step_impl(context):
    assert(context.c1 + context.c2 == Color(1.6, 0.7, 1.0))

@then(u'c1 - c2 = color(0.2, 0.5, 0.5)')
def step_impl(context):
    assert(context.c1 - context.c2 == Color(0.2, 0.5, 0.5))

@given(u'c ← color(0.2, 0.3, 0.4)')
def step_impl(context):
    context.c = Color(0.2, 0.3, 0.4)
@then(u'c * 2 = color(0.4, 0.6, 0.8)')
def step_impl(context):
    context.c.scale(2) == Color(0.4, 0.6, 0.8)

@given(u'c1 ← color(1, 0.2, 0.4)')
def step_impl(context):
    context.c1 = Color(1, 0.2, 0.4)
@given(u'c2 ← color(0.9, 1, 0.1)')
def step_impl(context):
    context.c2 = Color(0.9, 1, 0.1)
@then(u'c1 * c2 = color(0.9, 0.2, 0.04)')
def step_impl(context):
    assert(context.c1 * context.c2 == Color(0.9, 0.2, 0.04))