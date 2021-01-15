from sys import float_info

def float_eq(a, b):
    return abs(a - b) < float_info.epsilon