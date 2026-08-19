# Week 5 — Perceptron Notes

## Weights

Weights determine how strongly each input contributes to the neuron.

## Bias

Bias shifts the decision boundary.

The basic equation is:

z = wᵀx + b

---

## Perceptron

A perceptron is a simple binary classifier based on an artificial neuron.

It calculates a weighted sum and applies a step function.

---

## Step Function

y = 1 if z >= 0

y = 0 if z < 0

---

## Binary Classification

The perceptron assigns an input to one of two classes:

0 or 1

---

## Decision Boundary

The decision boundary separates the two predicted classes.

For:

z = wᵀx + b

the boundary occurs when:

wᵀx + b = 0

For two features:

w₁x₁ + w₂x₂ + b = 0

---

## Linear Separability

A dataset is linearly separable when a straight line can separate the classes.

A perceptron can learn linearly separable patterns.

---

## XOR

XOR produces:

| x₁ | x₂ | Output |
|----|----|--------|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

XOR is not linearly separable.

Therefore, a single-layer perceptron cannot solve XOR.

This limitation motivates the use of multiple layers.

---

## Key Takeaways

- Weights control input influence.
- Bias shifts the decision boundary.
- A perceptron is a binary classifier.
- The step function produces 0 or 1.
- A perceptron works for linearly separable data.
- XOR cannot be solved by a single-layer perceptron.
