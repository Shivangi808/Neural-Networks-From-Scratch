# Week 9 — Backpropagation

## Objective

Understand how neural networks calculate gradients and learn by propagating the error backward through the network.

## Topics Covered

- Why Backpropagation
- Chain Rule
- Computational Graph
- Forward Propagation
- Loss
- Backward Propagation
- Gradients
- Weight Gradients
- Bias Gradients
- Gradient Descent Connection
- Neural Network Training Loop

## Core Concept

Backpropagation calculates how much each parameter contributed to the final loss.

The gradients are then used by gradient descent to update the parameters.

## Core Flow

Input
→ Forward Propagation
→ Prediction
→ Loss
→ Backpropagation
→ Gradients
→ Gradient Descent
→ Updated Parameters

## Chain Rule

For a sequence of functions:

dy/dx = (dy/da) × (da/dx)

The chain rule allows gradients to be propagated backward through multiple operations.

## Neural Network

For a simple neuron:

z = wᵀx + b

ŷ = activation(z)

The gradient of the loss with respect to the parameters is calculated using the chain rule.

## Weight Update

w_new = w_old - learning_rate × gradient

## Libraries

- NumPy

## Notebooks

- `chain_rule.ipynb`
- `backpropagation.ipynb`

## Project

Neural Network from Scratch

## Progress

- [ ] Why Backpropagation
- [ ] Chain Rule
- [ ] Computational Graph
- [ ] Forward Propagation
- [ ] Loss
- [ ] Backward Propagation
- [ ] Gradients
- [ ] Weight Gradients
- [ ] Bias Gradients
- [ ] Gradient Descent Connection
- [ ] Complete Training Loop
- [ ] NumPy Implementation
- [ ] Project
- [ ] GitHub Upload
