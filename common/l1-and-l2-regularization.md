## Summary

L1 and L2 regularization are techniques that add penalty terms to the loss function to discourage overly complex models and reduce overfitting by constraining model coefficients ([Regularization (mathematics) - Wikipedia](https://en.wikipedia.org/wiki/Regularization_%28mathematics%29?utm_source=chatgpt.com)). L1 regularization penalizes the absolute values of coefficients (∑|wᵢ|), leading to sparse solutions and intrinsic feature selection ([Difference Between L1 and L2 Regularization - Tutorialspoint](https://www.tutorialspoint.com/difference-between-l1-and-l2-regularization?utm_source=chatgpt.com)). In contrast, L2 regularization penalizes the squares of coefficients (∑wᵢ²), shrinking weights smoothly and distributing them evenly across features ([Regularization (mathematics) - Wikipedia](https://en.wikipedia.org/wiki/Regularization_%28mathematics%29?utm_source=chatgpt.com), [Fighting Overfitting With L1 or L2 Regularization: Which One Is Better?](https://neptune.ai/blog/fighting-overfitting-with-l1-or-l2-regularization?utm_source=chatgpt.com)).

## L1 Regularization

L1 regularization, also known as LASSO (Least Absolute Shrinkage and Selection Operator), adds a penalty term proportional to the absolute value of model coefficients to the objective function ([Regularization in Machine Learning | GeeksforGeeks](https://www.geeksforgeeks.org/regularization-in-machine-learning/?utm_source=chatgpt.com), [Regularization (mathematics) - Wikipedia](https://en.wikipedia.org/wiki/Regularization_%28mathematics%29?utm_source=chatgpt.com)). The mathematical formulation modifies the cost function to minimize:  
\[
\text{Loss}(\theta) + \lambda \sum*{i} |\theta_i|,
\]  
where λ ≥ 0 controls the strength of regularization ([Regularization — Understanding L1 and L2 regularization for Deep ...](https://medium.com/analytics-vidhya/regularization-understanding-l1-and-l2-regularization-for-deep-learning-a7b9e4a409bf?utm_source=chatgpt.com)). This absolute-value penalty exerts a constant marginal cost on coefficients, which can drive less-informative weights exactly to zero, effectively performing feature selection ([difference in l1 and l2 regularization - Data Science Stack Exchange](https://datascience.stackexchange.com/questions/74341/difference-in-l1-and-l2-regularization?utm_source=chatgpt.com)). As a result, models using L1 regularization tend to be more interpretable due to their sparse weight vectors and can handle high-dimensional, sparse datasets efficiently ([Regularization (mathematics) - Wikipedia](https://en.wikipedia.org/wiki/Regularization*%28mathematics%29?utm_source=chatgpt.com)).

## L2 Regularization

L2 regularization, commonly known as Ridge regression, adds a penalty term proportional to the square of the model coefficients, i.e., λ∑θᵢ² ([Difference Between L1 and L2 Regularization - Tutorialspoint](https://www.tutorialspoint.com/difference-between-l1-and-l2-regularization?utm_source=chatgpt.com)). The modified objective becomes:  
\[
\text{Loss}(\theta) + \lambda \sum*{i} \theta_i^2,
\]  
where λ ≥ 0 determines the influence of the penalty on model complexity ([L1 and L2 Regularization (Part 1): A Complete Guide - Medium](https://medium.com/%40alejandro.itoaramendia/l1-and-l2-regularization-part-1-a-complete-guide-51cf45bb4ade?utm_source=chatgpt.com)). This quadratic penalty yields a smooth marginal cost that shrinks all coefficients towards zero but never exactly to zero, preventing overfitting without eliminating features entirely ([Regularization (mathematics) - Wikipedia](https://en.wikipedia.org/wiki/Regularization*%28mathematics%29?utm_source=chatgpt.com)). L2 regularization distributes weight more evenly across correlated features, enhancing numerical stability and reducing model variance ([Fighting Overfitting With L1 or L2 Regularization: Which One Is Better?](https://neptune.ai/blog/fighting-overfitting-with-l1-or-l2-regularization?utm_source=chatgpt.com)). It is widely used when multicollinearity is present or when one desires small but nonzero coefficients for all features ([L1 and L2 Regularization Methods, Explained - Built In](https://builtin.com/data-science/l2-regularization?utm_source=chatgpt.com)).

## Comparison Table

| Feature                 | L1 Regularization (LASSO)                               | L2 Regularization (Ridge)                      |
| ----------------------- | ------------------------------------------------------- | ---------------------------------------------- | --- | ----- |
| **Penalty Term**        | λ∑                                                      | wᵢ                                             |     | λ∑wᵢ² |
| **Effect on Weights**   | Drives many weights exactly to zero                     | Shrinks weights smoothly, none exactly zero    |
| **Feature Selection**   | Yes (sparse solutions)                                  | No                                             |
| **Solution Uniqueness** | May have multiple solutions (non-strict convexity)      | Unique solution (strict convexity)             |
| **Use Cases**           | High-dimensional data, when feature selection is needed | Multicollinearity, when retaining all features |
| **Computational Cost**  | Slightly higher due to non-differentiable penalty       | Lower due to differentiable quadratic penalty  |
| **Geometric View**      | Diamond-shaped constraint causes corners at axes        | Circular constraint leads to smooth shrinkage  |

This comparison highlights how L1 emphasizes sparsity and interpretability, while L2 emphasizes stability and uniform shrinkage across features.
