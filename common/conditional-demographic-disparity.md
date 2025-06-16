# Conditional Demographic Disparity (CDD)

**Conditional Demographic Disparity (CDD)** is a fairness metric used to measure the difference in positive prediction rates between demographic groups, while conditioning on relevant features (such as income, education, or other contextually important variables).

## Why Use CDD?

- **Detects Subtle Biases:**  
  By conditioning on relevant features, CDD can reveal biases that may be hidden when only considering overall prediction rates.
- **Ensures Contextual Fairness:**  
  It helps ensure that a model's decisions are fair across different groups, given their specific circumstances.

## How CDD Works

- **Step 1:** Identify the demographic groups of interest (e.g., gender, race).
- **Step 2:** Select relevant conditioning features (e.g., income).
- **Step 3:** Compare the rates of positive predictions (e.g., loan approval) between groups, holding the conditioning feature(s) constant.
- **Step 4:** Calculate the disparity in these rates to assess fairness.

## Example

Suppose a loan approval model predicts higher approval rates for one demographic group over another. By conditioning on income, CDD checks if this disparity persists among applicants with similar incomes, helping to identify if the model is unfairly biased beyond what can be explained by income differences.

## Importance in ML Fairness

- CDD is especially useful in regulated industries (finance, healthcare) where fairness across groups must be demonstrated not just overall, but within relevant subgroups.
- It provides a more nuanced view of model fairness than unconditioned demographic disparity.

**References:**

- [Fairness in Machine Learning (AWS)](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-fairness.html)
