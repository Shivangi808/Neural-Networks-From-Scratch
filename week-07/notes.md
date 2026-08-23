# Week 7 — Loss Functions & Forward Propagation

## Prediction

A neural network produces a predicted value:

ŷ = predicted value

The actual value is:

y = actual value

A loss function measures how different the prediction is from the actual value.

---

## Loss Function

Loss tells us how wrong the model's prediction is.

Lower loss generally means a better prediction.

General idea:

Loss = f(y, ŷ)

---

## Mean Squared Error (MSE)

Used mainly for regression.

MSE = mean((y - ŷ)²)

The errors are squared, so larger errors are penalized more heavily.

---

## Mean Absolute Error (MAE)

MAE = mean(|y - ŷ|)

It measures the average absolute difference between actual and predicted values.

Unlike MSE, it does not square the errors.

---

## Binary Cross Entropy (BCE)

Used for binary classification.

It compares the actual binary label with the predicted probability.

BCE strongly penalizes confident incorrect predictions.

---

## Categorical Cross Entropy

Used for multi-class classification.

The model produces probabilities for multiple classes.

Example:

Class A → 0.70
Class B → 0.20
Class C → 0.10

The loss depends on how much probability the model assigned to the correct class.

---

## Forward Propagation

Forward propagation is the process of passing input through a neural network to produce a prediction.

For a single neuron:

z = wᵀx + b

Then the activation function is applied:

ŷ = activation(z)

The complete flow is:

Input
→ Weighted Sum
→ Activation
→ Prediction

---

## Connecting Prediction and Loss

After forward propagation, the prediction is compared with the actual value.

Input
→ Weighted Sum
→ Activation
→ Prediction
→ Loss

---

## Important Notation

x = input

w = weights

b = bias

z = weighted sum

y = actual value

ŷ = predicted value

Loss = prediction error

---

## Key Takeaways

- A prediction is the model's output.
- Loss measures prediction error.
- MSE is commonly used for regression.
- MAE measures average absolute error.
- BCE is used for binary classification.
- Categorical cross entropy is used for multi-class classification.
- Forward propagation produces the model's prediction.
- The basic neuron calculation is z = wᵀx + b.
- Training aims to reduce the loss.
