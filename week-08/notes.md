# Week 8 — Gradient Descent & Learning Rate

## Optimization

Optimization is the process of finding parameter values that minimize a loss function.

In machine learning, we generally try to minimize the model's loss.

---

## Gradient Descent

Gradient descent is an optimization algorithm used to minimize a function.

It repeatedly updates parameters in the direction opposite to the gradient.

---

## Gradient

The gradient tells us the direction in which the function increases most rapidly.

To minimize the function, we move in the opposite direction.

---

## Learning Rate

The learning rate controls the size of each update.

A small learning rate takes smaller steps.

A large learning rate takes larger steps.

If the learning rate is too large, the algorithm may overshoot the minimum or fail to converge.

---

## Gradient Descent Update Rule

For a parameter w:

w_new = w_old - learning_rate × gradient

The gradient determines the direction of the update.

The learning rate determines the size of the update.

---

## Iterations

Gradient descent performs the update repeatedly.

Each update is called an iteration or step.

The goal is to gradually approach a minimum of the loss function.

---

## Convergence

Gradient descent is said to converge when the parameter values and loss stop changing significantly.

---

## Example

Suppose:

w = 5

gradient = 10

learning rate = 0.1

Then:

w_new = 5 - (0.1 × 10)

w_new = 4

The parameter moves in the direction that reduces the function.

---

## Batch Gradient Descent

Batch gradient descent calculates the gradient using the entire training dataset before updating the parameters.

---

## Gradient Descent Flow

Initialize Parameters
→ Calculate Predictions
→ Calculate Loss
→ Calculate Gradient
→ Update Parameters
→ Repeat

---

## Key Takeaways

- Gradient descent minimizes a function.
- The gradient determines the direction of change.
- Gradient descent moves opposite to the gradient.
- Learning rate controls the size of each update.
- A learning rate that is too large can cause overshooting.
- A learning rate that is too small can make learning very slow.
- Gradient descent repeatedly updates parameters until convergence.
