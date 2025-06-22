# Interpretability Techniques in Machine Learning

Interpretability techniques help us understand how machine learning models make decisions. These techniques can be grouped into:

- **Global Interpretability:** Explains the overall behavior of the model across the entire dataset.
- **Local Interpretability:** Explains why the model made a specific prediction for an individual instance.

---

## Global Interpretability Methods

### 1. **Partial Dependence Plots (PDP)**

- **Purpose:** Show the average effect of one or two features on the predicted outcome.
- **How it works:** For a feature set \(S\), the partial dependence function is  
  \[
  \hat f*S(x_S) = \frac{1}{n}\sum*{i=1}^n f\bigl(x*S, x*{C}^{(i)}\bigr)
  \]
  where \(C\) are the other features and \(x\_{C}^{(i)}\) are observed values.
- **Strengths:** Reveals linear, monotonic, or complex relationships.
- **Limitations:** Assumes features are independent; can be misleading if features are correlated.

### 2. **Accumulated Local Effects (ALE)**

- **Purpose:** Address PDP’s limitations with correlated features by focusing on local changes.
- **How it works:** Divides a feature’s range into intervals and computes the average change in prediction within each interval, then accumulates these effects:
  \[
  \Delta*{j,k} = \frac{1}{|N_k|}\sum*{i\in N*k} \Bigl[f(x*{i,j}=z*k) - f(x*{i,j}=z\_{k-1})\Bigr]
  \]
- **Strengths:** Unbiased under feature correlation; computationally efficient.
- **Limitations:** Needs enough data in each interval; sensitive to interval width.

### 3. **Permutation Feature Importance (PFI)**

- **Purpose:** Quantifies the importance of each feature for the model’s predictions.
- **How it works:** Randomly shuffles a feature’s values and measures the increase in model error:
  \[
  I*j = L\bigl(\hat f,\,X*{\mathrm{perm}(j)},\,y\bigr) - L\bigl(\hat f,\,X,\,y\bigr)
  \]
- **Strengths:** Model-agnostic; easy to implement.
- **Limitations:** Can be biased by correlated features; results may vary due to randomness.

---

## Local Interpretability Methods

### 1. **LIME (Local Interpretable Model-agnostic Explanations)**

- **Purpose:** Explains individual predictions by approximating the model locally with a simple surrogate (e.g., linear) model.
- **How it works:**
  - Generates perturbed samples around the instance of interest.
  - Gets predictions from the black-box model.
  - Fits a simple model weighted by proximity to the original instance:
    \[
    \underset{g}{\mathrm{argmin}}\;\sum\_{z\in Z}\pi_x(z)\bigl[f(z)-g(z)\bigr]^2 + \Omega(g)
    \]
- **Strengths:** Intuitive, model-agnostic, highlights which features influenced a specific prediction.
- **Limitations:** Explanations can be unstable; depends on sampling and kernel choice.

### 2. **SHAP (SHapley Additive exPlanations)**

- **Purpose:** Fairly attributes a model’s prediction for an instance to each feature.
- **How it works:**
  - Based on Shapley values from cooperative game theory.
  - Considers all possible combinations of features to compute each feature’s contribution.
  - Satisfies desirable properties (efficiency, symmetry, dummy, additivity).
- **Computation:** Exact calculation is exponential in the number of features; approximations like Kernel SHAP and Tree SHAP make it practical.
- **Strengths:** Theoretically sound, consistent, and provides both local and global insights.
- **Limitations:** Can be computationally expensive for large models.

---

## Summary Table

| Technique | Type         | Model-agnostic | Main Use                 | Handles Correlation? | Notes                                 |
| --------- | ------------ | -------------- | ------------------------ | -------------------- | ------------------------------------- |
| PDP       | Global       | Yes            | Feature effect (average) | No                   | Misleading with correlated features   |
| ALE       | Global       | Yes            | Feature effect (local)   | Yes                  | Needs enough data per interval        |
| PFI       | Global       | Yes            | Feature importance       | No                   | Repeat permutations for stability     |
| LIME      | Local        | Yes            | Explaining predictions   | N/A                  | Surrogate model, can be unstable      |
| SHAP      | Local/Global | Yes/Some       | Feature attribution      | Yes (Tree SHAP)      | Theoretically grounded, computational |

---

## References

- [Interpretable Machine Learning (Molnar)](https://christophm.github.io/interpretable-ml-book/)
- [SHAP Documentation](https://shap.readthedocs.io/)
- [LIME Documentation](https://github.com/marcotcr/lime)
