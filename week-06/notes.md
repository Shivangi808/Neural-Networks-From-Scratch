# Week 6 — Activation Functions Notes

## Activation Function

An activation function transforms the weighted sum of a neuron.

The neuron first calculates:

z = wᵀx + b

Then:

output = activation(z)

Activation functions introduce non-linearity into neural networks.

---

## Step Function

f(z) = 1 if z >= 0
f(z) = 0 if z < 0

Used by the basic perceptron.

Output range: 0 to 1.

---

## Sigmoid

σ(z) = 1 / (1 + e^(-z))

Output range:

0 < σ(z) < 1

Useful for binary classification output probabilities.

---

## Tanh

tanh(z)

Output range:

-1 to 1

Tanh is zero-centered.

---

## ReLU

ReLU(z) = max(0, z)

For positive values, the output is z.

For negative values, the output is 0.

ReLU is widely used in neural networks.

---

## Leaky ReLU

Leaky ReLU allows a small negative output instead of completely becoming zero for negative inputs.

This helps reduce the dying ReLU problem.

---

## Softmax

Softmax converts multiple scores into probabilities.

The probabilities sum to 1.

It is commonly used for multi-class classification.

---

## Non-linearity

Without non-linear activation functions, stacking multiple linear layers would still produce a linear transformation.

Non-linear activation functions allow neural networks to learn complex patterns.

---

## Key Takeaways

- Activation functions transform neuron outputs.
- They introduce non-linearity.
- Step function is used by the basic perceptron.
- Sigmoid outputs values between 0 and 1.
- Tanh outputs values between -1 and 1.
- ReLU outputs 0 for negative values and z for positive values.
- Leaky ReLU keeps a small negative slope.
- Softmax converts multiple scores into probabilities.
