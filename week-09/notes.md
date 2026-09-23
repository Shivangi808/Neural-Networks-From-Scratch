# Week 9 — Backpropagation Notes

## Backpropagation

Backpropagation is the process used by a neural network to calculate how much each parameter contributed to the final loss.

It works by propagating the error backward through the network and calculating gradients.

Backpropagation itself calculates the gradients.

Gradient descent then uses those gradients to update the parameters.

---

## Why Backpropagation?

A neural network contains many weights and biases.

After making a prediction, the network calculates a loss.

The network needs to determine:

- Which parameters contributed to the error?
- How much did each parameter contribute?
- In which direction should the parameters change?

Backpropagation answers these questions by calculating gradients.

---

## Forward Propagation

Forward propagation passes the input through the network to produce a prediction.

For a simple neuron:

z = wᵀx + b

Then an activation function may be applied:

ŷ = activation(z)

The general flow is:

Input
→ Weighted Sum
→ Activation
→ Prediction

---

## Loss

The prediction is compared with the actual value.

The difference is measured using a loss function.

For example:

L = Loss(y, ŷ)

where:

y = actual value

ŷ = predicted value

The goal of training is to minimize the loss.

---

## Computational Graph

A computational graph represents the sequence of operations used to calculate the output.

Example:

x → multiply by w → z → loss → L

For:

z = wx

L = z²

the computational graph is:

x
↓
× w
↓
z
↓
square
↓
L

The forward pass moves from input toward the loss.

The backward pass moves from the loss toward the parameters.

---

## Chain Rule

The chain rule allows us to calculate derivatives through a sequence of functions.

If:

a = f(x)

y = g(a)

then:

dy/dx = (dy/da) × (da/dx)

The chain rule is the mathematical foundation of backpropagation.

---

## Simple Chain Rule Example

Suppose:

z = wx

and:

L = z²

We want to calculate:

dL/dw

Using the chain rule:

dL/dw = (dL/dz) × (dz/dw)

Since:

L = z²

dL/dz = 2z

And:

z = wx

dz/dw = x

Therefore:

dL/dw = 2z × x

---

## Gradients

A gradient tells us how the loss changes with respect to a parameter.

For a weight:

dL/dw

For a bias:

dL/db

The gradient contains information about:

- Direction of change
- Rate of change

Gradient descent uses this information to update the parameters.

---

## Backward Propagation

During backpropagation, gradients are calculated starting from the loss and moving backward through the computational graph.

General flow:

Loss
↓
Prediction
↓
Activation
↓
Weighted Sum
↓
Weights and Biases

The chain rule is applied at each step.

---

## Backpropagation Through a Neuron

For a neuron:

z = wx + b

ŷ = activation(z)

L = Loss(y, ŷ)

We want to calculate:

dL/dw

and:

dL/db

Using the chain rule:

dL/dw =
(dL/dŷ) × (dŷ/dz) × (dz/dw)

Similarly:

dL/db =
(dL/dŷ) × (dŷ/dz) × (dz/db)

The exact derivatives depend on the loss function and activation function being used.

---

## Gradient Descent

After backpropagation calculates the gradients, gradient descent updates the parameters.

For a weight:

w_new = w_old - learning_rate × dL/dw

For a bias:

b_new = b_old - learning_rate × dL/db

The negative sign is used because gradient descent moves in the direction that reduces the loss.

---

## Complete Training Process

A neural network learns through repeated cycles:

Initialize Parameters
→ Forward Propagation
→ Prediction
→ Calculate Loss
→ Backpropagation
→ Calculate Gradients
→ Update Parameters
→ Repeat

As training progresses, the goal is for the loss to decrease.

---

## Example

Suppose:

x = 2

w = 3

Then:

z = wx

z = 3 × 2

z = 6

If:

L = z²

then:

L = 36

Now calculate the gradient.

dL/dz = 2z

dL/dz = 12

dz/dw = x

dz/dw = 2

Therefore:

dL/dw = 12 × 2

dL/dw = 24

The gradient tells us how the loss changes with respect to the weight.

---

## Backpropagation vs Gradient Descent

These two concepts are related but different.

### Backpropagation

Calculates the gradients.

### Gradient Descent

Uses the gradients to update the parameters.

Therefore:

Backpropagation
→ Calculate Gradients

Gradient Descent
→ Update Parameters

---

## Important Notation

x = input

w = weight

b = bias

z = weighted sum

ŷ = predicted value

y = actual value

L = loss

dL/dw = gradient of loss with respect to weight

dL/db = gradient of loss with respect to bias

η = learning rate

---

## Neural Network Learning Flow

Input
↓
Weighted Sum
↓
Activation
↓
Prediction
↓
Loss
↓
Backpropagation
↓
Gradients
↓
Gradient Descent
↓
Updated Weights and Bias
↓
Repeat

---

## Key Takeaways

- Backpropagation calculates gradients.
- It propagates error information backward through the network.
- The chain rule is the mathematical foundation of backpropagation.
- Forward propagation produces the prediction.
- Loss measures prediction error.
- Backpropagation calculates how parameters affect the loss.
- Gradients tell us how the loss changes with respect to parameters.
- Gradient descent uses gradients to update weights and biases.
- Backpropagation and gradient descent are different processes.
- Neural networks learn by repeating forward propagation, loss calculation, backpropagation, and parameter updates.
