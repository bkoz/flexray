#
# Build a Matrix string from a 'behave' feature Matrix.
#
# Example:
#
# echo "|  8 | -5 |  9 |  2 |
#       |  7 |  5 |  6 |  1 |
#       | -6 |  0 |  9 |  6 |
#       | -3 |  0 | -9 | -4 |" | python build-matrix.py

import sys

#f=open('input.txt')

matrix=[]
vector=[]

#lines = f.readlines()
lines = sys.stdin.readlines()
for line in lines:
  vector=[]
  for c in line:
    if(c.isnumeric()):
      vector.append(int(c))
  matrix.append(vector)

print('Matrix({0})'.format(matrix))



