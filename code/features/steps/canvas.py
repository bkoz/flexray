from behave import *
from Canvas import Canvas
from Color import Color

@given(u'c ← canvas(10, 20)')
def step_impl(context):
    context.c = Canvas(10, 20)
@then(u'c.width = 10')
def step_impl(context):
    assert(context.c.width == 10)
@then(u'c.height = 20')
def step_impl(context):
    assert(context.c.height == 20)
@then(u'every pixel of c is color(0, 0, 0)')
def step_impl(context):
    context.black = Color(0, 0, 0) 
    for i in range(context.c.width * context.c.height):
        assert(context.c.pixels[i] == context.black)

@given(u'red ← color(1, 0, 0)')
def step_impl(context):
    context.red = Color(1, 0, 0)
@when(u'write_pixel(c, 2, 3, red)')
def step_impl(context):
    context.c.write_pixel(2, 3, context.red)
@then(u'pixel_at(c, 2, 3) = red')
def step_impl(context):
    assert(context.c.pixel_at(2, 3) == context.red)