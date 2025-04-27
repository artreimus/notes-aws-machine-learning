# Linear and Logistic Regression

Linear regression is a supervised learning algorithm that models the relationship between a continuous dependent variable and one or more independent variables by fitting an affine function to minimize the mean squared error  ([Linear regression](https://en.wikipedia.org/wiki/Linear_regression?utm_source=chatgpt.com)). In contrast, logistic regression is a supervised classification algorithm that predicts the probability of a binary (or categorical) outcome by applying the logistic (sigmoid) function to a linear combination of input features  ([Logistic regression - Wikipedia](https://en.wikipedia.org/wiki/Logistic_regression?utm_source=chatgpt.com)). Linear regression coefficients are typically estimated via ordinary least squares (OLS) by minimizing the residual sum of squares  ([Linear vs. Logistic Regression](https://www.spiceworks.com/tech/artificial-intelligence/articles/linear-regression-vs-logistic-regression/)). Logistic regression parameters are learned via maximum likelihood estimation (MLE) by maximizing the likelihood of observed class labels under a Bernoulli model  ([Linear vs. Logistic Regression](https://www.spiceworks.com/tech/artificial-intelligence/articles/linear-regression-vs-logistic-regression/), [Logistic Regression — Machine-Learning-Course 1.0 documentation](https://machine-learning-tutorial-abi.readthedocs.io/en/latest/content/supervised/logistic_regression.html?utm_source=chatgpt.com)). The outputs also differ: linear regression produces continuous real-valued predictions, whereas logistic regression outputs probabilities between 0 and 1 that can be thresholded to yield class labels  ([Linear vs. Logistic Regression](https://www.spiceworks.com/tech/artificial-intelligence/articles/linear-regression-vs-logistic-regression/)).

## Overview of Linear Regression

Linear regression estimates a linear predictor function of the form  
\[
y = \beta_0 + \beta_1 x_1 + \dots + \beta_p x_p
\]  
where \(y\) is continuous and \(x_i\) are input features  ([Linear regression](https://en.wikipedia.org/wiki/Linear_regression?utm_source=chatgpt.com), [Linear vs. Logistic Regression](https://www.spiceworks.com/tech/artificial-intelligence/articles/linear-regression-vs-logistic-regression/)). Coefficients \(\beta\) are found by minimizing the mean squared error between predictions and true values using ordinary least squares (OLS)  ([Linear vs. Logistic Regression](https://www.spiceworks.com/tech/artificial-intelligence/articles/linear-regression-vs-logistic-regression/)). The resulting model produces continuous, unbounded outputs that can take any real value  ([Linear vs. Logistic Regression](https://www.spiceworks.com/tech/artificial-intelligence/articles/linear-regression-vs-logistic-regression/)). Common use cases include forecasting and trend analysis in finance, marketing, and the physical sciences, as well as explanatory modeling to quantify relationships between variables  ([Linear regression](https://en.wikipedia.org/wiki/Linear_regression?utm_source=chatgpt.com)).

## Overview of Logistic Regression

Logistic regression models the log-odds of the probability of a binary outcome as a linear function of input features and applies the logistic function  
\[
\sigma(z) = \frac{1}{1 + e^{-z}}
\]  
to map the result to \([0,1]\)  ([Logistic regression - Wikipedia](https://en.wikipedia.org/wiki/Logistic_regression?utm_source=chatgpt.com)). The model’s form can be written as  
\[
P(y=1 \mid \mathbf{x}) = \sigma\bigl(\beta_0 + \beta_1 x_1 + \dots + \beta_p x_p\bigr).
\]  
Parameters are estimated via maximum likelihood estimation, iteratively optimizing the log-likelihood of observing the given class labels  ([Linear vs. Logistic Regression](https://www.spiceworks.com/tech/artificial-intelligence/articles/linear-regression-vs-logistic-regression/)). The output is a probability score, which can be thresholded (commonly at 0.5) to assign class labels  ([Logistic regression - Simple English Wikipedia, the free encyclopedia](https://simple.wikipedia.org/wiki/Logistic_regression?utm_source=chatgpt.com)). Logistic regression is widely applied in spam detection, credit scoring, and medical diagnosis for its probabilistic interpretation and ease of implementation  ([Logistic regression - Wikipedia](https://en.wikipedia.org/wiki/Logistic_regression?utm_source=chatgpt.com), [What is Logistic Regression Used for? - H2O.ai](https://h2o.ai/wiki/logistic-regression/?utm_source=chatgpt.com)).

## Comparison Table

| Aspect                | Linear Regression                                  | Logistic Regression                                                                 |
|-----------------------|----------------------------------------------------|-------------------------------------------------------------------------------------|
| **Purpose**           | Predict continuous outcomes                        | Predict probabilities of categorical (binary) outcomes                              |
| **Dependent Variable**| Continuous real-valued                             | Binary (0/1) or categorical                                                         |
| **Model Equation**    | \(y = \beta_0 + \sum_i \beta_i x_i\)               | \(P(y=1) = \sigma(\beta_0 + \sum_i \beta_i x_i)\)                                   |
| **Estimation Method** | Ordinary Least Squares (minimize MSE)              | Maximum Likelihood Estimation (maximize log-likelihood)                             |
| **Output**            | Unbounded real values                              | Probabilities in \([0,1]\) that can be thresholded                                  |
| **Underlying Loss**   | Mean Squared Error                                 | Cross-entropy (log loss)                                                            |
| **Assumed Distribution** | Gaussian noise on residuals                   | Bernoulli distribution of outcomes                                                  |
| **Common Use Cases**  | Forecasting, trend analysis, explanatory modeling  | Classification tasks (spam detection, credit scoring, medical diagnosis)            |

*Sources: Wikipedia (Linear Regression)  ([Linear regression](https://en.wikipedia.org/wiki/Linear_regression?utm_source=chatgpt.com)); Wikipedia (Logistic Regression)  ([Logistic regression - Wikipedia](https://en.wikipedia.org/wiki/Logistic_regression?utm_source=chatgpt.com)); Spiceworks  ([Linear vs. Logistic Regression](https://www.spiceworks.com/tech/artificial-intelligence/articles/linear-regression-vs-logistic-regression/)); Machine-Learning Tutorial  ([Logistic Regression — Machine-Learning-Course 1.0 documentation](https://machine-learning-tutorial-abi.readthedocs.io/en/latest/content/supervised/logistic_regression.html?utm_source=chatgpt.com)); Simple Wikipedia  ([Logistic regression - Simple English Wikipedia, the free encyclopedia](https://simple.wikipedia.org/wiki/Logistic_regression?utm_source=chatgpt.com)).*