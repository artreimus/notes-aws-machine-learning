# SageMaker Linear Learner Tracking

## Overview

Amazon SageMaker Linear Learner is a built-in algorithm for supervised learning tasks such as binary classification, multiclass classification, and regression. It is optimized for large datasets and provides efficient, scalable training.

## Tracking Metrics During Training

SageMaker Linear Learner automatically tracks and reports key metrics during the training process, which are visible in the SageMaker console and available via CloudWatch. These metrics help you monitor model performance and diagnose issues.

### Common Tracked Metrics

- **Loss:**  
  The primary objective function value being minimized (e.g., log loss for classification, mean squared error for regression).
- **Accuracy:**  
  For classification tasks, measures the proportion of correct predictions.
- **Precision, Recall, F1 Score:**  
  For binary and multiclass classification, these metrics provide deeper insight into model performance.
- **AUC (Area Under Curve):**  
  For binary classification, measures the ability of the model to distinguish between classes.
- **RMSE (Root Mean Squared Error):**  
  For regression tasks, indicates the average prediction error.

### How Tracking Works

- **Automatic Logging:**  
  During training, SageMaker logs metrics at each epoch or iteration. These are accessible in the SageMaker console under the training job details.
- **CloudWatch Integration:**  
  Metrics are also sent to Amazon CloudWatch, enabling custom dashboards and alerts.
- **Model Artifacts:**  
  After training, SageMaker stores the trained model and a metrics JSON file in the specified S3 output location.

### Best Practices

- **Monitor Training Jobs:**  
  Regularly review training metrics to detect overfitting, underfitting, or data issues.
- **Use Early Stopping:**  
  Enable early stopping to halt training when performance stops improving, saving time and resources.
- **Compare Experiments:**  
  Use tracked metrics to compare different training runs and select the best model.

### References

- [SageMaker Linear Learner Documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/linear-learner.html)
- [Monitoring Training with CloudWatch](https://docs.aws.amazon.com/sagemaker/latest/dg/training-job-monitor.html)
