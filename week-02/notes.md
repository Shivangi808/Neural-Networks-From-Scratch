# Week 2 - Linear Algebra Notes

## Why Linear Algebra?

Linear Algebra is the language of Deep Learning.

Every neural network operation, from a single neuron to a transformer, is built on vectors and matrices.

---

## Scalar

A scalar is a single numerical value.

Examples:
- 5
- -2
- 3.14

In Machine Learning:
- Learning rate
- Bias
- Loss value

---

## Vector

A vector is an ordered collection of numbers.

Example:

[2, 5, 7]

Represents:
- Features of one sample
- Word embeddings
- Image pixels

---

## Row Vector

Shape:

(1, n)

Example:

[1 2 3]

Usually represents one training example.

---

## Column Vector

Shape:

(n, 1)

Example:

[1
 2
 3]

Used in many mathematical derivations.

---

## Matrix

A matrix is a collection of vectors arranged in rows and columns.

Example:

[[1,2],
 [3,4]]

Represents:
- Dataset
- Weight matrix
- Images

---

## Matrix Shape

Shape = (rows, columns)

Examples:

(3,4)

means

3 rows
4 columns

---

## Dot Product

Formula:

a · b = Σ(ai × bi)

Example:

[1,2,3]

·

[4,5,6]

=

1×4 + 2×5 + 3×6

=

32

Uses:
- Similarity
- Neuron computation
- Forward propagation

---

## Matrix Multiplication

Condition:

Columns of Matrix A = Rows of Matrix B

If

A = (2,3)

then

B must be

(3,n)

Result:

(2,n)

---

## Identity Matrix

Diagonal elements = 1

Everything else = 0

Example

[[1,0],
 [0,1]]

Acts like multiplying by 1.

---

## Transpose

Rows become columns.

Example

(2,3)

↓

(3,2)

Notation:

Aᵀ

---

## Applications in Deep Learning

Input Matrix

↓

Weight Matrix

↓

Matrix Multiplication

↓

Bias Addition

↓

Activation Function

↓

Prediction

Almost every neural network starts with

Z = XW + b

---

## Important NumPy Functions

np.array()

np.shape

np.matmul()

@

np.eye()

np.zeros()

np.ones()

.T

np.random.randint()

---

## Things I Learned This Week

- Why vectors represent data.
- Why matrices store datasets.
- How matrix multiplication powers neural networks.
- Shape compatibility in multiplication.
- Difference between row and column vectors.

---

## Revision Checklist

- [x] Scalar
- [x] Vector
- [x] Row Vector
- [x] Column Vector
- [x] Matrix
- [x] Shape
- [x] Dot Product
- [x] Matrix Multiplication
- [x] Identity Matrix
- [x] Transpose
- [x] NumPy implementation
