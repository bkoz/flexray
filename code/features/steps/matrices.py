from behave import *
from Matrix import *

@given(u'the following 4x4 matrix M')
def step_impl(context):
    context.M = Matrix()
    context.M.m = [ [1, 2, 3, 4], [5.5, 6.5, 7.5, 8.5], [9, 10, 11, 12], [13.5, 14.5, 15.5, 16.5] ]
@then(u'M[0,0] = 1')
def step_impl(context):
    assert(context.M[0][0] == 1)
@then(u'M[0,3] = 4')
def step_impl(context):
    assert(context.M[0][3] == 4)
@then(u'M[1,0] = 5.5')
def step_impl(context):
    assert(context.M[1][0] == 5.5)
@then(u'M[1,2] = 7.5')
def step_impl(context):
    assert(context.M[1][2] == 7.5)
@then(u'M[2,2] = 11')
def step_impl(context):
    assert(context.M[2][2] == 11)
@then(u'M[3,0] = 13.5')
def step_impl(context):
    assert(context.M[3][0] == 13.5)
@then(u'M[3,2] = 15.5')
def step_impl(context):
    assert(context.M[3][2] == 15.5)
