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

@given(u'the following 2x2 matrix M')
def step_impl(context):
    context.M = Matrix()
    context.M.m = [ [-3, 5], [1, -2] ]
@then(u'M[0,0] = -3')
def step_impl(context):
    assert(context.M[0][0] == -3)
@then(u'M[0,1] = 5')
def step_impl(context):
    assert(context.M[0][1] == 5)
@then(u'M[1,0] = 1')
def step_impl(context):
    assert(context.M[1][0] == 1)
@then(u'M[1,1] = -2')
def step_impl(context):
    assert(context.M[1][1] == -2)

@given(u'the following 3x3 matrix M')
def step_impl(context):
    context.M = Matrix()
    context.M.m = [ [-3, 5, 0], [1, -2, -7], [0, 1, 1] ]
@then(u'N[0,0] = -3')
def step_impl(context):
    assert(context.N[0][0] == -3)
@then(u'M[2,2] = 1')
def step_impl(context):
    assert(context.M[2][2] == 1)

@given(u'the following matrix A')
def step_impl(context):
    context.A = Matrix()
    context.A.m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]]
@given(u'the following matrix B')
def step_impl(context):
    context.B = Matrix()
    context.B.m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]]
@then(u'A = B')
def step_impl(context):
    assert(context.A.m == context.B.m)

@given(u'the following matrix C')
def step_impl(context):
    context.C = Matrix()
    context.C.m = [[2, 3, 4, 5], [6, 7, 8, 9], [8, 7, 6, 5], [4, 3, 2, 1]]
@then(u'A != C')
def step_impl(context):
    assert(context.A.m != context.C.m)

@given(u'the following matrix D')
def step_impl(context):
    context.D = Matrix()
    context.D.m = [[-2, 1, 2, 3], [3 ,2 , 1, -1], [4, 3, 6,  5], [1 ,2, 7, 8]]
@given(u'the following matrix E')
def step_impl(context):
    context.E = Matrix()
    context.E.m = [[20, 22, 50, 48], [44, 54, 114, 108], [40, 58, 110, 102], [16, 26, 46, 42]]
@then(u'A * D = E')
def step_impl(context):
    assert(context.A * context.D == context.E)
