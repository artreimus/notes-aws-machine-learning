In supervised learning, model error can be decomposed into three parts:

- squared bias
- variance
- irreducible noise

Together, these determine how accurately the model will perform on unseen data ([Bias–variance tradeoff - Wikipedia](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff)).

Bias measures the systematic error introduced by approximating a complex problem with a simpler model ([Bias of an estimator - Wikipedia](https://en.wikipedia.org/wiki/Bias_of_an_estimator)).

Variance measures the sensitivity of model predictions to fluctuations in the training data ([What are bias and variance in machine learning?](https://datascience.stackexchange.com/questions/80157/what-are-bias-and-variance-in-machine-learning)).

Irreducible error (noise) captures randomness inherent in the data generation process that no model can eliminate ([Bias–variance tradeoff - Wikipedia](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff)).

The bias–variance tradeoff refers to the inverse relationship between bias and variance as model complexity changes ([Understanding the Bias-Variance Tradeoff | by Seema Singh - Medium](https://medium.com/towards-data-science/understanding-the-bias-variance-tradeoff-165e6942b229)). Striking the right balance is critical for good generalization: too much bias leads to underfitting, while too much variance leads to overfitting ([Bias Variance Tradeoff - MLU-Explain](https://mlu-explain.github.io/bias-variance/)).

## What Is Bias?

Bias is the error due to overly simplistic assumptions in the learning algorithm, causing it to miss relevant patterns in the data ([Bias–Variance Tradeoff in Machine Learning: Concepts & Tutorials](https://www.bmc.com/blogs/bias-variance-machine-learning/)). Formally, it’s the difference between the expected model prediction and the true underlying function ([Bias of an estimator - Wikipedia](https://en.wikipedia.org/wiki/Bias_of_an_estimator)). Models with high bias are too rigid and underfit both training and test data, leading to high error across the board ([Bias-Variance Trade Off – Machine Learning | GeeksforGeeks](https://www.geeksforgeeks.org/ml-bias-variance-trade-off/)).

## What Is Variance?

Variance is the error due to the model’s sensitivity to small fluctuations in the training set ([Bias–Variance Tradeoff in Machine Learning: Concepts & Tutorials](https://www.bmc.com/blogs/bias-variance-machine-learning)). It quantifies how much the model’s predictions would change if we trained on different data samples ([Bias Variance Tradeoff - MLU-Explain](https://mlu-explain.github.io/bias-variance)). High-variance models are overly complex, fit noise in the training data, and perform poorly on new data despite low training error ([Overfitting - Wikipedia](https://en.wikipedia.org/wiki/Overfitting)).

## The Bias–Variance Tradeoff

As model complexity increases, bias decreases and variance increases, and vice versa ([Bias-Variance Trade Off – Machine Learning | GeeksforGeeks](https://www.geeksforgeeks.org/ml-bias-variance-trade-off/)). An underfitted model (high bias, low variance) fails to capture true relationships, while an overfitted model (low bias, high variance) captures noise as if it were signal ([Bias–Variance Tradeoff in Machine Learning: Concepts & Tutorials](https://www.bmc.com/blogs/bias-variance-machine-learning/)). Effective learning algorithms allow tuning or automatically finding the sweet spot between bias and variance to minimize total error ([Supervised learning](https://en.wikipedia.org/wiki/Supervised_learning)).

### Error Decomposition

The expected prediction error at a point x can be written as:  
\[
\mathbb{E}[(y - \hat f(x))^2] = \bigl(\text{Bias}[\hat f(x)]\bigr)^2 + \text{Var}[\hat f(x)] + \sigma\_{\epsilon}^2,
\]  
where σ²ₑ is the irreducible noise variance ([Bias–variance tradeoff - Wikipedia](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff)).

### Practical Implications

- **Model selection:** Simpler models (e.g., linear regression) have higher bias but lower variance; complex models (e.g., deep trees, high-degree polynomials) have lower bias but higher variance ([What are bias and variance in machine learning?](https://datascience.stackexchange.com/questions/80157/what-are-bias-and-variance-in-machine-learning)).
- **Regularization & data augmentation:** Techniques like L1/L2 penalties, dropout, or adding more training data help reduce variance without overly increasing bias ([Bias Variance Tradeoff - MLU-Explain](https://mlu-explain.github.io/bias-variance/)).

The table below summarizes key differences between bias and variance ([Bias–variance tradeoff - Wikipedia](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff), [Bias–Variance Tradeoff in Machine Learning: Concepts & Tutorials](https://www.bmc.com/blogs/bias-variance-machine-learning/)):

| Aspect                       | Bias                                                   | Variance                                                       |
| ---------------------------- | ------------------------------------------------------ | -------------------------------------------------------------- |
| **Definition**               | Systematic error from oversimplified model assumptions | Sensitivity of model predictions to training data fluctuations |
| **Source of Error**          | Incorrect model form; underfitting                     | Overly complex model; overfitting                              |
| **Effect on Training Error** | High                                                   | Low                                                            |
| **Effect on Test Error**     | High                                                   | High                                                           |
| **Typical Remedies**         | Increase model complexity, add features                | Regularization, reduce complexity, gather more data            |
| **Example**                  | Linear regression on nonlinear data                    | Decision tree without pruning; k-NN with very small k          |
