Ensemble learning methods combine multiple “base” models to produce a stronger overall model. Three of the most popular techniques are **bagging**, **boosting**, and **stacking**:

---

## 1. Bagging (Bootstrap Aggregating)

- **Core idea**  
  Train multiple instances of the _same_ base learner in **parallel**, each on a different random subset of the training data (drawn _with_ replacement, i.e. bootstrap samples). Then aggregate their predictions—commonly by majority vote (classification) or averaging (regression).

- **Why it helps**  
  Reduces **variance**: since each model sees a slightly different dataset, their errors tend to “cancel out” when averaged, making the ensemble more stable than any single model.

- **Typical example**  
  **Random Forest**: an ensemble of decision trees trained on bootstrap samples and each split considers only a random subset of features.

- **Pros & cons**
  - ✅ Great at preventing overfitting
  - ✅ Easy to parallelize
  - ❌ Doesn’t necessarily reduce bias (if base learner is too simple)

---

## 2. Boosting

- **Core idea**  
  Train base learners **sequentially**, where each new model focuses more on the examples the previous models got wrong. Final prediction is a weighted combination of all models.

- **Why it helps**  
  Reduces **bias** by turning many “weak” learners (slightly better than random) into a strong composite learner.

- **Popular algorithms**

  - **AdaBoost** (Adaptive Boosting): weights misclassified examples more heavily in subsequent rounds.
  - **Gradient Boosting** (e.g., XGBoost, LightGBM, CatBoost): fits each new model to the _residual errors_ of the combined ensemble so far, using gradient descent in function space.

- **Pros & cons**
  - ✅ Often achieves very high accuracy
  - ✅ Naturally focuses on “hard” cases
  - ❌ More prone to overfitting if not regularized
  - ❌ Generally **sequential**, so slower to train than bagging

---

## 3. Stacking (Stacked Generalization)

- **Core idea**  
  Train **diverse** base learners (they can be different algorithms) in parallel on the full training set, then train a **meta-learner** (second-level model) to combine their predictions.

- **Why it helps**  
  Exploits **complementarity**: different algorithms capture different patterns; the meta-learner learns how to weight and blend them optimally.

- **Workflow**

  1. **Split** training data into _k_ folds.
  2. For each base learner:
     - Train on _k–1_ folds, predict on the held-out fold → collect out-of-fold predictions.
     - Repeat to get a full set of predictions on all training examples.
  3. **Train meta-learner** on these out-of-fold predictions (features) vs. true targets.
  4. **At test time**: each base learner predicts on new data; their predictions form input features for the meta-learner, which produces the final output.

- **Pros & cons**
  - ✅ Can leverage strengths of very different models
  - ✅ Often yields state-of-the-art performance
  - ❌ More complex to implement and tune
  - ❌ Risk of overfitting if meta-learner is too powerful or if stacking “leaks” training information

---

### Choosing Between Them

| Method       | Main Benefit               | When to Use                                                                     |
| ------------ | -------------------------- | ------------------------------------------------------------------------------- |
| **Bagging**  | Variance reduction         | If your base model overfits (high variance)                                     |
| **Boosting** | Bias reduction             | If your base model underfits (high bias) or you need maximal accuracy           |
| **Stacking** | Model diversity & blending | When you want to combine very different models to squeeze out extra performance |

All three are powerful ensemble strategies—your choice depends on the problem at hand, the computational budget, and whether you care more about bias vs. variance vs. leveraging heterogeneous models.

Image Illustration: [Bagging, Boosting, and Stacking](https://i0.wp.com/spotintelligence.com/wp-content/uploads/2024/03/bagging-boosting-stacking-1024x576.webp?resize=1024%2C576&ssl=1)
