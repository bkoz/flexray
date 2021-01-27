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

@then(u'A * identity_matrix = A')
def step_impl(context):
    assert(context.A * Matrix.identity() == context.A)

@given(u'a ← tuple(1, 2, 3, 4)')
def step_impl(context):
    context.a = Tuple((1, 2, 3, 4))
@then(u'identity_matrix * a = a')
def step_impl(context):
    assert(Matrix.identity() * context.a == context.a)

@then(u'transpose(A) is the following matrix')
def step_impl(context):
    assert(Matrix.transpose(Matrix([[0,9,3,0],[9,8,0,8],[1,8,5,3],[0,0,5,8]])) == Matrix([[0,9,1,0],[9,8,8,0],[3,0,5,5],[0,8,3,8]]))

@given(u'A ← transpose(identity_matrix)')
def step_impl(context):
    context.A = Matrix.transpose(Matrix.identity())
@then(u'A = identity_matrix')
def step_impl(context):
    assert(context.A == Matrix.identity())

@given(u'the following 2x2 matrix A')
def step_impl(context):
    context.A = Matrix([[1,5],[-3,2]])
@then(u'determinant(A) = 17')
def step_impl(context):
    assert(context.A.determinant() == 17)

@given(u'the following 3x3 matrix A')
def step_impl(context):
    context.A = Matrix([[1, 5, 0], [-3, 2, 7], [0, 6, -3]])
@then(u'submatrix(A, 0, 2) is the following 2x2 matrix')
def step_impl(context):
    assert(context.A.submatrix(0, 2) == Matrix([[-3, 2], [0, 6]]))

@given(u'the following 4x4 matrix A')
def step_impl(context):
    context.A = Matrix([[-6, 1, 1, 6], [-8, 5, 8, 6], [-1, 0, 8, 2], [-7, 1, -1, 1]])
@then(u'submatrix(A, 2, 1) is the following 3x3 matrix')
def step_impl(context):
    assert(context.A.submatrix(2, 1) == Matrix([[-6, 1, 6], [-8, 8, 6],[-7, -1, 1]]))

@given(u'B ← submatrix(A, 1, 0)')
def step_impl(context):
    context.A = Matrix([[3, 5, 0], [2, -1, -7], [6, -1, 5]])
    context.B = context.A.submatrix(1, 0)
@then(u'determinant(B) = 25')
def step_impl(context):
    assert(math.isclose(context.B.determinant(), 25))
@then(u'minor(A, 1, 0) = 25')
def step_impl(context):
    assert(math.isclose(context.A.minor(1, 0), 25))

@given(u'the following 3x3 matrix A3')
def step_impl(context):
    context.A3 = Matrix([[3, 5, 0], [2, -1, -7], [6, -1, 5]])
@then(u'minor(A3, 0, 0) = -12')
def step_impl(context):
    assert(math.isclose(context.A3.minor(0, 0), -12))
@then(u'cofactor(A3, 0, 0) = -12')
def step_impl(context):
    assert(math.isclose(context.A3.cofactor(0, 0), -12))
@then(u'minor(A3, 1, 0) = 25')
def step_impl(context):
    assert(math.isclose(context.A3.minor(1, 0), 25))
@then(u'cofactor(A3, 1, 0) = -25')
def step_impl(context):
    assert(math.isclose(context.A3.cofactor(1, 0), -25))

@given(u'the following 3x3 matrix A4')
def step_impl(context):
    context.A = Matrix([[1, 2, 6], [-5, 8, -4], [2, 6, 4]])
@then(u'cofactor(A4, 0, 0) = 56')
def step_impl(context):
    assert(math.isclose(context.A.cofactor(0, 0), 56))
@then(u'cofactor(A4, 0, 1) = 12')
def step_impl(context):
    assert(math.isclose(context.A.cofactor(0, 1), 12))
@then(u'cofactor(A4, 0, 2) = -46')
def step_impl(context):
    assert(math.isclose(context.A.cofactor(0, 2), -46))
@then(u'determinant(A4) = -196')
def step_impl(context):
    assert(math.isclose(context.A.determinant(), -196))

@given(u'the following 4x4 matrix AD')
def step_impl(context):
    context.A = Matrix([[-2,-8,3,5],[-3,1,7,3],[1,2,-9,6],[-6,7,7,-9]])
@then(u'cofactor(AD, 0, 0) = 690')
def step_impl(context):
    assert(math.isclose(context.A.cofactor(0, 0), 690))
@then(u'cofactor(AD, 0, 1) = 447')
def step_impl(context):
    assert(math.isclose(context.A.cofactor(0, 1), 447))
@then(u'cofactor(AD, 0, 2) = 210')
def step_impl(context):
    assert(math.isclose(context.A.cofactor(0, 2), 210))
@then(u'cofactor(AD, 0, 3) = 51')
def step_impl(context):
    assert(math.isclose(context.A.cofactor(0, 3), 51))
@then(u'determinant(AD) = -4071')
def step_impl(context):
    assert(math.isclose(context.A.determinant(), -4071))


