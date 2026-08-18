# Week 3 — Calculus Foundations

## Why Calculus?

Calculus helps us understand how a change in one quantity affects another.

In Machine Learning and Deep Learning, derivatives and gradients help us understand how changing model parameters affects the loss.

---

## 1. Function

A function maps an input to an output.

Example:

f(x) = x²

If:

x = 3

then:

f(3) = 9

---

## 2. Derivative

A derivative measures the rate at which a function changes with respect to its input.

For:

f(x) = x²

the derivative is:

f'(x) = 2x

### Intuition

- Positive derivative → function is increasing
- Negative derivative → function is decreasing
- Zero derivative → slope is zero

---

## 3. Geometric Meaning

The derivative represents the slope of a function at a particular point.

A large absolute derivative means the function is changing rapidly.

A derivative close to zero means the function is changing slowly.

---

## 4. Partial Derivative

A partial derivative is used when a function has multiple variables.

Example:

f(x,y) = x² + y²

Partial derivative with respect to x:

∂f/∂x = 2x

Partial derivative with respect to y:

∂f/∂y = 2y

When calculating one partial derivative, the other variables are treated as constants.

---

## 5. Chain Rule

The chain rule is used to differentiate a composite function.

If:

y = f(g(x))

then:

dy/dx = f'(g(x)) × g'(x)

### Example

Let:

u = x² + 1

y = u³

Then:

dy/du = 3u²

du/dx = 2x

Therefore:

dy/dx = 3u² × 2x

---

## 6. Gradient

A gradient is a vector containing the partial derivatives of a function with respect to its variables.

For:

f(x,y) = x² + y²

the gradient is:

∇f = [2x, 2y]

The gradient points in the direction of the greatest increase of the function.

---

## 7. Gradient Descent Connection

Gradient descent moves in the opposite direction of the gradient.

Why?

Because the gradient points toward the direction of greatest increase.

To minimize a loss function, we move in the opposite direction.

Basic update:

new_parameter = old_parameter - learning_rate × gradient

---

## 8. Connection to Deep Learning

Calculus is used in:

- Gradient Descent
- Backpropagation
- Weight Updates
- Optimization

A neural network uses gradients to determine how its parameters should change to reduce the loss.

---

## NumPy Functions Used

- `np.linspace()`
- `np.gradient()`
- `np.array()`
- `np.exp()`
- `np.sin()`
- `np.cos()`

---

## Matplotlib Functions Used

- `plt.plot()`
- `plt.scatter()`
- `plt.xlabel()`
- `plt.ylabel()`
- `plt.title()`
- `plt.legend()`
- `plt.grid()`
- `plt.show()`

---

## Key Takeaways

- A derivative measures rate of change.
- A derivative can be interpreted as the slope of a function.
- Partial derivatives are used for functions with multiple variables.
- The chain rule is important for differentiating composite functions.
- A gradient contains partial derivatives.
- Gradient descent moves opposite to the gradient.
- Calculus forms the mathematical foundation of backpropagation.
