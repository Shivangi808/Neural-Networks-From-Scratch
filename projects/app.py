import numpy as np

from operations import (
    add_vectors,
    subtract_vectors,
    scalar_multiply,
    dot_product_numpy,
    dot_product_manual
)


# Scalars
scalar = np.array(5)

print("Scalar:", scalar)


# Vectors
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("\nVector A:", a)
print("Vector B:", b)


# Vector addition
print("\nA + B =", add_vectors(a, b))


# Vector subtraction
print("A - B =", subtract_vectors(a, b))


# Scalar multiplication
print("3A =", scalar_multiply(3, a))


# Dot product
numpy_result = dot_product_numpy(a, b)
manual_result = dot_product_manual(a, b)

print("\nNumPy dot product:", numpy_result)
print("Manual dot product:", manual_result)


# Verification
print("\nResults match:", numpy_result == manual_result)