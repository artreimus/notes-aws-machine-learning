Amazon SageMaker offers a broad portfolio of built-in algorithms for both supervised and unsupervised learning, enabling use cases from classification and regression to clustering, anomaly detection, and topic modeling ([Built-in algorithms and pretrained models in Amazon SageMaker - Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html), [Unsupervised Built-in SageMaker AI Algorithms - Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/algorithms-unsupervised.html)). Below are concise notes on the key AWS models in each paradigm, followed by separate tables summarizing their core characteristics.

## Supervised Learning Models in AWS

Amazon SageMaker’s supervised algorithms train on labeled datasets to predict categorical or continuous outputs. They span general-purpose tabular methods, advanced feature engineering techniques, and specialized forecasting tools:

- **AutoGluon-Tabular**: An open-source AutoML framework that ensembles and stacks multiple models automatically for classification and regression tasks on tabular data ([Built-in Algorithms - Amazon SageMaker Python SDK - Read the Docs](https://sagemaker.readthedocs.io/en/stable/algorithms/index.html?utm_source=chatgpt.com)).
- **CatBoost**: Gradient-boosted decision trees that introduce ordered boosting and efficient categorical feature handling for high accuracy with minimal preprocessing ([Built-in algorithms and pretrained models in Amazon SageMaker - Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html)).
- **Factorization Machines**: Extends linear models to capture pairwise feature interactions in high-dimensional sparse datasets, commonly used in recommendation systems ([Built-in algorithms and pretrained models in Amazon SageMaker - Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html)).
- **K-Nearest Neighbors (k-NN)**: A non-parametric method that assigns labels or predicts values based on the k closest labeled examples, suitable for both classification and regression ([Amazon SageMaker Built-in Algorithms | AWS Machine Learning](https://k21academy.com/amazon-web-services/aws-ml/amazon-sagemaker-algorithms/)).
- **LightGBM**: Implements gradient-boosted trees with innovations like Gradient-based One-Side Sampling (GOSS) and Exclusive Feature Bundling (EFB) for faster training on large datasets ([Built-in algorithms and pretrained models in Amazon SageMaker - Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html)).
- **Linear Learner**: Learns a linear function for continuous regression or a linear threshold for binary/multiclass classification, optimized for large-scale tabular data ([Amazon SageMaker Built-in Algorithms | AWS Machine Learning](https://k21academy.com/amazon-web-services/aws-ml/amazon-sagemaker-algorithms/)).
- **TabTransformer**: Applies self-attention–based transformer blocks to tabular inputs, capturing complex feature interactions via deep learning ([Built-in algorithms and pretrained models in Amazon SageMaker - Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html)).
- **XGBoost**: A high-performance implementation of gradient-boosted trees that ensembles many weak learners for robust classification and regression ([Amazon SageMaker Built-in Algorithms | AWS Machine Learning](https://k21academy.com/amazon-web-services/aws-ml/amazon-sagemaker-algorithms/)).
- **Object2Vec**: Learns dense embeddings of high-dimensional objects to produce features that accelerate and improve downstream supervised models ([Built-in algorithms and pretrained models in Amazon SageMaker - Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html)).
- **DeepAR**: Uses recurrent neural networks to generate probabilistic forecasts for scalar (one-dimensional) time-series data, valuable for demand planning and financial projections ([Amazon SageMaker Built-in Algorithms | AWS Machine Learning](https://k21academy.com/amazon-web-services/aws-ml/amazon-sagemaker-algorithms/)).

### Table of Supervised Learning Models

| Algorithm              | Description                                                          | Common Use Cases                     | Input Domain |
| ---------------------- | -------------------------------------------------------------------- | ------------------------------------ | ------------ |
| AutoGluon-Tabular      | Automated ensembling and stacking of models for tabular data         | Classification, Regression           | Tabular      |
| CatBoost               | Gradient-boosted trees with ordered boosting and categorical support | Classification, Regression           | Tabular      |
| Factorization Machines | Captures feature interactions economically in sparse datasets        | Recommendation, Click prediction     | Tabular      |
| K-Nearest Neighbors    | Distance-based classification/regression using nearest points        | Classification, Regression           | Tabular      |
| LightGBM               | Efficient gradient-boosted trees with GOSS and EFB                   | High-volume tabular tasks            | Tabular      |
| Linear Learner         | Linear models for regression or threshold classification             | Binary/multiclass classification     | Tabular      |
| TabTransformer         | Transformer architecture for capturing tabular feature interactions  | Complex tabular modeling             | Tabular      |
| XGBoost                | Ensemble of weak learners via gradient boosting                      | Classification, Regression           | Tabular      |
| Object2Vec             | Embedding learning for high-dimensional objects                      | Feature engineering                  | Tabular      |
| DeepAR                 | RNN-based probabilistic forecasting for scalar time series           | Demand forecasting, Financial trends | Time Series  |

## Unsupervised Learning Models in AWS

Unsupervised algorithms discover hidden patterns in unlabeled data, supporting clustering, dimensionality reduction, anomaly detection, and topic modeling:

- **Principal Component Analysis (PCA)**: Projects data onto its top principal components to reduce dimensionality while retaining maximal variance ([Unsupervised Built-in SageMaker AI Algorithms - Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/algorithms-unsupervised.html)).
- **K-Means**: Partitions data into k clusters by minimizing intra-cluster variance, widely used for customer segmentation and anomaly grouping ([Amazon SageMaker Built-in Algorithms | AWS Machine Learning](https://k21academy.com/amazon-web-services/aws-ml/amazon-sagemaker-algorithms/)).
- **IP Insights**: Learns usage patterns of IPv4 addresses to reveal associations and detect suspicious or malicious behavior ([Unsupervised Built-in SageMaker AI Algorithms - Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/algorithms-unsupervised.html)).
- **Random Cut Forest (RCF)**: Assigns anomaly scores based on deviations from normal data structures, suitable for streaming anomaly detection ([AWS Certified Machine Learning Cheat Sheet — Built In Algorithms 3/5 | by tanta base | Medium](https://medium.com/%40tantabase/aws-certified-machine-learning-cheat-sheet-built-in-algorithms-3-8-50332ef8de1c)).
- **Latent Dirichlet Allocation (LDA)**: A probabilistic model that discovers latent topics in document collections without labeled data ([AWS SageMaker Built-in Algorithms Summary](https://jayendrapatil.com/aws-sagemaker-built-in-algorithms-summary/)).
- **Neural Topic Model (NTM)**: Uses neural networks to perform scalable, flexible topic modeling on text corpora ([AWS SageMaker Built-in Algorithms Summary](https://jayendrapatil.com/aws-sagemaker-built-in-algorithms-summary/)).

### Table of Unsupervised Learning Models

| Algorithm                          | Description                                                  | Common Use Cases                       | Input Domain  |
| ---------------------------------- | ------------------------------------------------------------ | -------------------------------------- | ------------- |
| Principal Component Analysis (PCA) | Dimensionality reduction via principal component projection  | Feature reduction, Preprocessing       | Tabular       |
| K-Means                            | Cluster analysis by partitioning into k groups               | Customer segmentation, Clustering      | Tabular       |
| IP Insights                        | Unsupervised discovery of IPv4 address usage patterns        | IP anomaly detection                   | CSV, RecordIO |
| Random Cut Forest (RCF)            | Anomaly detection through forest-based scoring of deviations | Time-series anomaly detection          | CSV, RecordIO |
| Latent Dirichlet Allocation (LDA)  | Probabilistic topic modeling for document corpora            | Topic discovery, Document organization | Text          |
| Neural Topic Model (NTM)           | Neural network–based unsupervised topic extraction           | Topic modeling, Recommendation         | Text          |
