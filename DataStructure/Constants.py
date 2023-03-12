import math

minFloat = 0.00000000000000000000000001
leptonId = [11, 13]
neutrinoId = [12, 14]


def dot3d(a, b) -> float:
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def cross3d(a, b):
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]


def normalize3d(a):
    length: float = dot3d(a, a)
    if length < minFloat:
        return [0.0, 0.0, 0.0]
    length = math.sqrt(length)
    return [a[0] / length, a[1] / length, a[2] / length]
