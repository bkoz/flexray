#
# Build a Matrix string from a 'behave' feature Matrix.
#
# Example:
#
# echo "  8  -5   9   2 
#         7   5   6   1 
#        -6   0   9   6 
#        -3   0  -9  -4 "  python build-matrix.py

import numpy

f=open('input.txt')

matrix=[]

lines = f.readlines()
for line in lines:
    matrix.append(line.split())

print(repr(numpy.array(matrix, dtype=float)))



