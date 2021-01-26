from behave import *
from Matrix import *
from Tuple import *

@given(u'the following 4x4 matrix M')
def step_impl(context):
    context.M4 = Matrix([[1, 2, 3, 4], [5.5, 6.5, 7.5, 8.5], [9, 10, 11, 12], [13.5, 14.5, 15.5, 16.5]])
@then(u'M[0,0] = 1')
def step_impl(context):
    assert(context.M4._[0][0] == 1)
@then(u'M[0,3] = 4')
def step_impl(context):
    assert(context.M4._[0][3] == 4)
@then(u'M[1,0] = 5.5')
def step_impl(context):
    assert(context.M4._[1][0] == 5.5)
@then(u'M[1,2] = 7.5')
def step_impl(context):
    assert(context.M4._[1][2] == 7.5)
@then(u'M[2,2] = 11')
def step_impl(context):
    assert(context.M4._[2][2] == 11)
@then(u'M[3,0] = 13.5')
def step_impl(context):
    assert(context.M4._[3][0] == 13.5)
@then(u'M[3,2] = 15.5')
def step_impl(context):
    assert(context.M4._[3][2] == 15.5)

@given(u'the following 2x2 matrix M')
def step_impl(context):
    context.M2 = Matrix([[-3, 5], [1, -2]])
@then(u'M[0,0] = -3')
def step_impl(context):
    assert(context.M2._[0][0] == -3)
@then(u'M[0,1] = 5')
def step_impl(context):
    assert(context.M2._[0][1] == 5)
@then(u'M[1,0] = 1')
def step_impl(context):
    assert(context.M2._[1][0] == 1)
@then(u'M[1,1] = -2')
def step_impl(context):
    assert(context.M2._[1][1] == -2)

@given(u'the following 3x3 matrix M3')
def step_impl(context):
    context.M3 = Matrix([[-3, 5, 0], [1, -2, -7], [0, 1, 1]])
@then(u'M3[0,0] = -3')
def step_impl(context):
    assert(context.M3._[0][0] == -3)
@then(u'M3[2,2] = 1')
def step_impl(context):
    assert(context.M3._[1,1] == -2)
@then(u'M3[1,1] = -2')
def step_impl(context):
    assert(context.M3._[2][2] == 1)


@given(u'the following matrix A')
def step_impl(context):
    context.A = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])
@given(u'the following matrix B')
def step_impl(context):
    context.B = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])
@then(u'A = B')
def step_impl(context):
    assert(context.A == context.B)

@given(u'the following matrix C')
def step_impl(context):
    context.C = Matrix([[2, 3, 4, 5], [6, 7, 8, 9], [8, 7, 6, 5], [4, 3, 2, 1]])
@then(u'A != C')
def step_impl(context):
    assert(context.A != context.C)

@given(u'the following matrix D')
def step_impl(context):
    context.D = Matrix([[-2, 1, 2, 3], [3 ,2 , 1, -1], [4, 3, 6,  5], [1 ,2, 7, 8]])
@given(u'the following matrix E')
def step_impl(context):
    context.E = Matrix([[20, 22, 50, 48], [44, 54, 114, 108], [40, 58, 110, 102], [16, 26, 46, 42]])
@then(u'A * D = E')
def step_impl(context):
    assert((context.A * context.D) == context.E)

@given(u'the following matrix A1')
def step_impl(context):
    context.A1 = Matrix([[1 ,2 , 3 , 4 ],[ 2 , 4 , 4 , 2 ], [8 , 6 , 4 , 1 ],[ 0 , 0 , 0 , 1 ]])
@given(u'b1 ← tuple(1, 2, 3, 1)')
def step_impl(context):
    context.b1 = Tuple([1, 2, 3, 1])
@then(u'A1 * b1 = tuple(18, 24, 33, 1)')
def step_impl(context):
    assert((context.A1 * context.b1) == Tuple([18, 24, 33, 1]))