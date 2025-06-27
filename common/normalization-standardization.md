# Normalization and Standardization

Normalization and standardization are **data preprocessing techniques** used to rescale features before feeding them into machine learning models. Here's a detailed comparison:

---

## **Normalization (Min-Max Scaling)**

### **Definition:**

Rescales the data to a **fixed range**, typically $[0, 1]$ or $[-1, 1]$.

### **Formula:**

$$
x_{\text{normalized}} = \frac{x - x_{\min}}{x_{\max} - x_{\min}}
$$

### **Characteristics:**

- Preserves the shape of the original distribution.
- Sensitive to **outliers**, since max/min values are affected.
- Good for **bounded data** or when the algorithm expects data in a specific range (e.g., neural networks with sigmoid activation).

### **Use Cases:**

- **K-Nearest Neighbors (KNN)**
- **Neural Networks**
- Algorithms sensitive to the **magnitude** of data

## **Standardization (Z-score Scaling)**

### **Definition:**

Rescales the data to have **zero mean** and **unit variance**.

### **Formula:**

$$
x_{\text{standardized}} = \frac{x - \mu}{\sigma}
$$

Where:

- $\mu$ = mean of the feature
- $\sigma$ = standard deviation of the feature

### **Characteristics:**

- Centers the data around zero.
- Less sensitive to outliers compared to normalization.
- Assumes data is (approximately) normally distributed.

### **Use Cases:**

- **Linear Regression**
- **Logistic Regression**
- **Support Vector Machines (SVM)**
- **Principal Component Analysis (PCA)**

## **Impact on Underfitting and Overfitting**

### **How Poor Scaling Leads to Underfitting:**

1. **Feature Dominance**: Without proper scaling, features with larger magnitudes (e.g., income in dollars vs. age in years) can dominate the learning process, causing the model to ignore smaller-scale but potentially important features.

2. **Gradient Descent Issues**: In algorithms using gradient descent, unscaled features can cause:

   - **Slow convergence** or failure to converge
   - **Oscillating gradients** that prevent the model from finding optimal parameters
   - **Premature stopping** before the model learns meaningful patterns

3. **Distance-Based Algorithm Problems**: KNN, K-means, and SVM are particularly affected by unscaled features, leading to poor decision boundaries and underfitting.

### **How Improper Scaling Can Cause Overfitting:**

1. **Data Leakage Through Scaling**:

   - **Wrong**: Scaling the entire dataset before train/test split
   - **Result**: Test set statistics leak into training, causing artificially high performance and overfitting

2. **Outlier Amplification**:

   - Normalization can amplify the effect of outliers, especially in small datasets
   - This can cause the model to overfit to these extreme values

3. **Over-Regularization**:
   - Incorrect scaling can make regularization parameters (like in Ridge/Lasso) behave unexpectedly
   - May lead to over-penalization of certain features

### **Best Practices to Prevent Under/Overfitting:**

#### **Proper Scaling Workflow:**

```
1. Split data into train/validation/test sets
2. Fit scaler ONLY on training data
3. Transform train, validation, and test sets using the fitted scaler
4. Never fit scaler on validation or test data
```

#### **Choosing the Right Scaling Method:**

- **Use Standardization when**:

  - Features have different units/scales
  - Data is approximately normally distributed
  - Using algorithms sensitive to feature scale (SVM, neural networks, PCA)
  - Want to reduce impact of outliers

- **Use Normalization when**:
  - Need bounded output range
  - Data is uniformly distributed
  - Using distance-based algorithms (KNN)
  - Working with image data or neural networks with specific activation functions

#### **Handling Outliers:**

- **Robust Scaling**: Use median and interquartile range instead of mean/std
- **Quantile Transformation**: Maps features to uniform or normal distribution
- **Outlier Detection**: Remove or cap extreme values before scaling

### **AWS SageMaker Considerations:**

- **Built-in Algorithms**: Many SageMaker algorithms (Linear Learner, XGBoost) handle scaling internally
- **Feature Processing**: Use SageMaker Data Wrangler for visual scaling and transformation
- **Pipeline Integration**: Include scaling steps in SageMaker Pipelines for consistent preprocessing
- **Model Monitor**: Track feature distributions over time to detect scaling drift

## Summary Table

| Aspect                 | Normalization          | Standardization         |
| ---------------------- | ---------------------- | ----------------------- |
| Range                  | Typically $[0, 1]$     | Mean = 0, Std = 1       |
| Sensitive to outliers  | Yes                    | Less so                 |
| Preserves distribution | Yes                    | No (centers and scales) |
| Best for               | Neural nets, KNN       | SVM, regression, PCA    |
| Overfitting Risk       | Higher with outliers   | Lower, more robust      |
| Underfitting Risk      | Lower if done properly | Lower if done properly  |

## **Key Takeaways:**

- **Always scale after splitting** your data to prevent data leakage
- **Choose scaling method** based on your data distribution and algorithm requirements
- **Monitor for outliers** that might skew your scaling parameters
- **Validate scaling effectiveness** by checking model performance on validation set
- **Consider robust scaling methods** for datasets with significant outliers

If you're unsure which to use:

- Use **normalization** when using distance-based models or if the data has known bounds.
- Use **standardization** for models that assume Gaussian-like data or use regularization.
- **Always validate** your scaling choice through cross-validation and monitoring for over/underfitting patterns.
