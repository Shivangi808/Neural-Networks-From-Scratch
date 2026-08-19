# Week 4 — Artificial Neuron Notes

## AI

Artificial Intelligence is the broader field concerned with creating systems capable of performing tasks associated with human intelligence.

## Machine Learning

Machine Learning is a subset of AI where systems learn patterns from data.

## Deep Learning

Deep Learning is a subset of Machine Learning that uses neural networks with multiple layers.

---

## Biological Neuron

A biological neuron receives signals through its dendrites, processes information in the cell body, and sends signals through the axon.

Neurons communicate with other neurons through synapses.

---

## Artificial Neuron

An artificial neuron is a mathematical model inspired by the biological neuron.

It receives inputs, applies weights, adds a bias, and produces an output.

---

## Inputs

Inputs represent the features provided to a neuron.

Example:

x = [x₁, x₂, x₃]

---

## Weights

Each input has an associated weight.

Weights determine how strongly each input contributes to the neuron.

---

## Bias

Bias is an additional parameter added to the weighted sum.

It allows the neuron to shift its output.

---

## Weighted Sum

The neuron calculates:

z = w₁x₁ + w₂x₂ + ... + wₙxₙ + b

This can also be written as:

z = wᵀx + b

---

## Output

The weighted sum represents the neuron's raw output before applying an activation function.

Activation functions will be studied later.

---

## Connection to Neural Networks

A neural network consists of many interconnected artificial neurons.

Each neuron performs a weighted combination of its inputs.

Learning involves finding suitable weights and biases.

---

## Key Takeaways

- AI is broader than ML.
- ML is a subset of AI.
- DL is a subset of ML.
- Artificial neurons are inspired by biological neurons.
- Inputs represent features.
- Weights control the contribution of inputs.
- Bias shifts the weighted sum.
- The basic neuron equation is z = wᵀx + b.
