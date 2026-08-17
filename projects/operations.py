import numpy as np


def add_vectors(a, b):
    return a + b


def subtract_vectors(a, b):
    return a - b

def scalar_multiply(scalar, vector):
    return scalar * vector


def dot_product_numpy(a, b):
    return np.dot(a, b)


def dot_product_manual(a, b):
    result = 0

    for i in range(len(a)):
        result += a[i] * b[i]

    return result
