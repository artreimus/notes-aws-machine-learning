# AWS SageMaker Built‑in Algorithms Cheat Sheet

| Algorithm                   | What it is                                                                   | Capabilities                           | Training Data                   | Training Instances     | Inference Instances    |
| --------------------------- | ---------------------------------------------------------------------------- | -------------------------------------- | ------------------------------- | ---------------------- | ---------------------- |
| Linear Learner              | Generalised linear models for binary/multiclass classification or regression | Classification, Regression, Multiclass | CSV or RecordIO                 | **CPU / GPU**          | **CPU / GPU**          |
| XGBoost                     | Gradient‑boosted decision trees                                              | Classification, Regression             | CSV, LibSVM (Parquet supported) | **CPU / GPU**          | **CPU / GPU**          |
| Factorization Machines      | Sparse feature‑interaction model                                             | Binary classification, Regression      | **RecordIO (training)**         | **CPU / GPU**          | **CPU / GPU**          |
| K‑Means                     | Unsupervised clustering                                                      | Clustering                             | CSV or RecordIO                 | **CPU (optional GPU)** | **CPU (optional GPU)** |
| PCA                         | Dimensionality reduction                                                     | Feature extraction                     | CSV or RecordIO                 | **CPU / GPU**          | **CPU / GPU**          |
| Random Cut Forest           | Anomaly detection in streaming/tabular data                                  | Unsupervised anomaly detection         | CSV or RecordIO                 | **CPU**                | **CPU**                |
| Object Detection            | Detects and classifies multiple objects in images                            | Object localisation & labels           | RecordIO or images + JSON       | **GPU**                | **CPU / GPU**          |
| Image Classification        | Convolutional image labeler                                                  | Image classification                   | RecordIO or images (+ manifest) | **GPU**                | **CPU / GPU**          |
| Semantic Segmentation       | Pixel‑level image classification                                             | Image segmentation                     | Images + pixel masks            | **GPU**                | **CPU / GPU**          |
| Seq2Seq                     | Encoder‑decoder neural networks                                              | Translation, Summarisation             | RecordIO (tokenised sequences)  | **GPU**                | **GPU**                |
| BlazingText                 | High‑performance FastText/Word2Vec                                           | Text classification, Embeddings        | Plain text                      | **CPU / GPU**          | **CPU / GPU**          |
| DeepAR                      | Probabilistic autoregressive RNN forecaster                                  | Time‑series forecasting                | JSON Lines or CSV               | **CPU / GPU**          | **CPU / GPU**          |
| IP Insights                 | Entity–IP anomaly scorer                                                     | Unsupervised anomaly detection         | CSV (entity, IP)                | **CPU / GPU**          | **CPU / GPU**          |
| Latent Dirichlet Allocation | Topic modelling for text                                                     | Unsupervised NLP (topics)              | Bag‑of‑words CSV/RecordIO       | **CPU**                | **CPU**                |

**Bold** entries highlight where CPU/GPU support or data‑format details differ from the original version.

## Hyperparameters for AWS SageMaker Built-in Algorithms

### Overview

**Hyperparameters** are external configurations set before training that control how a machine learning model learns from data. They significantly influence model performance, training efficiency, and generalization ability. Understanding which hyperparameters are required versus optional is crucial for effective model training and [hyperparameter tuning](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning.html).

### Supervised Learning Algorithms

#### Linear Learner

**Required Hyperparameters:**

- `predictor_type`: Specifies the type of target variable (`binary_classifier`, `multiclass_classifier`, or `regressor`)
- `num_classes`: Number of classes (required when `predictor_type` is `multiclass_classifier`)

**Key Optional Hyperparameters:**

- `learning_rate`: Controls the step size during optimization (default: auto)
- `mini_batch_size`: Number of samples per batch (default: 1000)
- `l1`: L1 regularization parameter (default: auto)
- `wd`: Weight decay/L2 regularization parameter (default: auto)
- `epochs`: Maximum number of passes over training data (default: 15)
- `balance_multiclass_weights`: Use class weights for multiclass problems (default: false)
- `optimizer`: Optimization algorithm (`auto`, `sgd`, `adam`, `rmsprop`) (default: auto)
- `loss`: Loss function specification (default: auto)

#### XGBoost

**Required Hyperparameters:**

- None (all hyperparameters have defaults)

**Key Optional Hyperparameters:**

- `max_depth`: Maximum depth of trees (default: 6)
- `eta`: Learning rate/step size shrinkage (default: 0.3)
- `gamma`: Minimum loss reduction for further partitioning (default: 0)
- `subsample`: Fraction of training samples used (default: 1)
- `alpha`: L1 regularization term (default: 0)
- `lambda`: L2 regularization term (default: 1)
- `eval_metric`: Evaluation metric (`auc`, `error`, `rmse`, etc.)
- `scale_pos_weight`: Balance positive/negative weights (default: 1)
- `tree_method`: Tree construction algorithm (`auto`, `exact`, `approx`, `hist`, `gpu_hist`)

#### Factorization Machines

**Required Hyperparameters:**

- None (all hyperparameters have defaults)

**Key Optional Hyperparameters:**

- `num_factors`: Number of latent factors (default: 64)
- `bias_init`: Initialization method for bias terms (`uniform`, `normal`, `constant`)
- `factors_init`: Initialization method for factor matrices (`uniform`, `normal`, `constant`)
- `linear_init`: Initialization method for linear terms (`uniform`, `normal`, `constant`)
- `l1_regularization`: L1 regularization strength (default: 0)
- `l2_regularization`: L2 regularization strength (default: 0.01)
- `mini_batch_size`: Number of samples per batch (default: 1000)
- `learning_rate`: Step size during optimization (default: 0.1)

#### K-Nearest Neighbors (k-NN)

**Required Hyperparameters:**

- None (all hyperparameters have defaults)

**Key Optional Hyperparameters:**

- `k`: Number of nearest neighbors to consider (default: 3)
- `sample_size`: Size of training data sample (default: depends on data size)
- `predictor_type`: Type of prediction (`classifier` or `regressor`) (default: classifier)
- `dimension_reduction_target`: Target dimension for dimensionality reduction
- `dimension_reduction_type`: Method for dimensionality reduction (`sign`, `fjlt`)
- `index_metric`: Distance metric for indexing (`COSINE`, `INNER_PRODUCT`, `L2`)

#### DeepAR

**Required Hyperparameters:**

- `prediction_length`: Number of time points to predict
- `context_length`: Number of time points the model observes before prediction
- `freq`: Frequency of time series (e.g., 'D' for daily, 'H' for hourly)

**Key Optional Hyperparameters:**

- `epochs`: Number of training epochs (default: 100)
- `mini_batch_size`: Number of samples per batch (default: 32)
- `learning_rate`: Step size during optimization (default: 0.001)
- `num_cells`: Number of RNN cells per layer (default: 40)
- `num_layers`: Number of RNN layers (default: 2)
- `dropout_rate`: Dropout probability (default: 0.1)
- `embedding_dimension`: Dimension of embedding for categorical features

#### Object2Vec

**Required Hyperparameters:**

- None (all hyperparameters have defaults)

**Key Optional Hyperparameters:**

- `enc0_network`: Encoder type for first input channel (`hcnn`, `bilstm`, `pooled_embedding`)
- `enc1_network`: Encoder type for second input channel (`hcnn`, `bilstm`, `pooled_embedding`)
- `enc_dim`: Dimensionality of embedding vectors (default: 4096)
- `comparator_list`: Methods to compare embeddings (`hadamard`, `concat`, `abs_diff`)
- `dropout`: Dropout probability (default: 0)
- `learning_rate`: Step size during optimization (default: 0.001)
- `mini_batch_size`: Number of samples per batch (default: 32)
- `epochs`: Number of training epochs (default: 30)

### Computer Vision Algorithms

#### Image Classification

**Required Hyperparameters:**

- `num_classes`: Number of object categories to predict
- `num_training_samples`: Total number of training examples

**Key Optional Hyperparameters:**

- `mini_batch_size`: Number of samples per batch (default: 32)
- `learning_rate`: Step size during optimization (default: 0.1)
- `optimizer`: Optimization algorithm (`sgd`, `adam`, `rmsprop`, `nag`) (default: sgd)
- `momentum`: Momentum for SGD optimizer (default: 0.9)
- `weight_decay`: L2 regularization parameter (default: 0.0001)
- `epochs`: Number of training epochs (default: 30)
- `use_pretrained_model`: Whether to use pre-trained weights (default: 1)

#### Object Detection

**Required Hyperparameters:**

- `num_classes`: Number of object categories to predict
- `num_training_samples`: Total number of training examples

**Key Optional Hyperparameters:**

- `base_network`: Architecture for base network (`vgg-16`, `resnet-50`)
- `mini_batch_size`: Number of samples per batch (default: 32)
- `learning_rate`: Step size during optimization (default: 0.001)
- `optimizer`: Optimization algorithm (`sgd`, `adam`, `rmsprop`, `adadelta`)
- `momentum`: Momentum for SGD (default: 0.9)
- `weight_decay`: L2 regularization (default: 0.0005)
- `epochs`: Number of training epochs (default: 30)
- `early_stopping`: Enable early stopping (default: false)

#### Semantic Segmentation

**Required Hyperparameters:**

- `num_classes`: Number of classes for segmentation

**Key Optional Hyperparameters:**

- `algorithm`: Segmentation algorithm (`fcn`, `psp`, `deeplab`) (default: fcn)
- `backbone`: Backbone network (`resnet50`, `resnet101`) (default: resnet50)
- `epochs`: Number of training epochs (default: 10)
- `learning_rate`: Step size during optimization (default: 0.001)
- `mini_batch_size`: Number of samples per batch (default: 16)
- `optimizer`: Optimization algorithm (default: sgd)
- `momentum`: Momentum for SGD (default: 0.9)
- `weight_decay`: L2 regularization (default: 0.0001)

### Natural Language Processing Algorithms

#### BlazingText

**Text Classification Mode:**
**Required Hyperparameters:**

- `mode`: Training mode (`supervised` for text classification)

**Key Optional Hyperparameters:**

- `epochs`: Number of training epochs (default: 5)
- `learning_rate`: Step size during optimization (default: 0.05)
- `word_ngrams`: Maximum length of word n-grams (default: 1)
- `vector_dim`: Size of word vectors (default: 100)
- `min_count`: Minimum number of word occurrences (default: 5)

**Word2Vec Mode:**
**Required Hyperparameters:**

- `mode`: Training architecture (`batch_skipgram`, `skipgram`, `cbow`)

**Key Optional Hyperparameters:**

- `learning_rate`: Step size during training (default: 0.025)
- `window_size`: Number of context words (default: 5)
- `vector_dim`: Dimensionality of word vectors (default: 100)
- `negative_samples`: Number of negative samples (default: 5)
- `epochs`: Number of training epochs (default: 5)

#### Sequence-to-Sequence (Seq2Seq)

**Required Hyperparameters:**

- None (all hyperparameters have defaults)

**Key Optional Hyperparameters:**

- `batch_size`: Mini-batch size for gradient descent (default: 64)
- `optimizer_type`: Optimization algorithm (`adam`, `sgd`, `rmsprop`) (default: adam)
- `learning_rate`: Step size during optimization (default: 0.0003)
- `num_layers_encoder`: Number of encoder layers (default: 1)
- `num_layers_decoder`: Number of decoder layers (default: 1)
- `hidden_size_encoder`: Hidden size for encoder (default: 512)
- `hidden_size_decoder`: Hidden size for decoder (default: 512)
- `max_seq_len_source`: Maximum source sequence length (default: 100)
- `max_seq_len_target`: Maximum target sequence length (default: 100)

### Unsupervised Learning Algorithms

#### K-Means

**Required Hyperparameters:**

- `k`: Number of clusters

**Key Optional Hyperparameters:**

- `feature_dim`: Number of features in input data (default: auto)
- `mini_batch_size`: Number of samples per batch (default: 5000)
- `max_iterations`: Maximum number of iterations (default: 100)
- `tol`: Tolerance for convergence (default: 1e-4)
- `init_method`: Initialization method (`random`, `kmeans++`) (default: random)
- `local_init_method`: Local initialization method (`kmeans++`, `random`) (default: kmeans++)
- `half_life_time_size`: Half-life time for learning rate decay

#### Principal Component Analysis (PCA)

**Required Hyperparameters:**

- None (all hyperparameters have defaults)

**Key Optional Hyperparameters:**

- `algorithm_mode`: Algorithm variant (`regular`, `randomized`) (default: regular)
- `subtract_mean`: Whether to center data by subtracting mean (default: true)
- `num_components`: Number of principal components to compute (default: min(features, samples))
- `feature_dim`: Number of features in input data (default: auto)
- `mini_batch_size`: Number of samples per batch (default: 500)
- `extra_components`: Extra components for randomized algorithm (default: 10)

#### Random Cut Forest (RCF)

**Required Hyperparameters:**

- None (all hyperparameters have defaults)

**Key Optional Hyperparameters:**

- `num_trees`: Number of trees in the forest (default: 100)
- `num_samples_per_tree`: Number of samples per tree (default: 256)
- `feature_dim`: Number of features in input data (default: auto)
- `eval_metrics`: Evaluation metrics to compute (default: auto)

#### IP Insights

**Required Hyperparameters:**

- None (all hyperparameters have defaults)

**Key Optional Hyperparameters:**

- `num_entity_vectors`: Number of unique entity vectors (default: 10000)
- `vector_dim`: Size of embedding vectors (default: 128)
- `hash_size`: Hash size for entity representation (default: 2 \* num_entity_vectors)
- `epochs`: Number of training epochs (default: 5)
- `learning_rate`: Step size during optimization (default: 0.01)
- `batch_size`: Number of samples per batch (default: 32)
- `num_ip_encoder_layers`: Number of IP encoder layers (default: 1)

#### Latent Dirichlet Allocation (LDA)

**Required Hyperparameters:**

- `num_topics`: Number of topics to discover

**Key Optional Hyperparameters:**

- `alpha0`: Initial guess for concentration parameter (default: 1.0)
- `feature_dim`: Number of features/vocabulary size (default: auto)
- `mini_batch_size`: Number of documents per batch (default: 100)
- `max_restarts`: Maximum number of restarts (default: 10)
- `max_iterations`: Maximum iterations per restart (default: 1000)
- `tol`: Tolerance for convergence (default: 1e-3)

#### Neural Topic Model (NTM)

**Required Hyperparameters:**

- `num_topics`: Number of topics to learn

**Key Optional Hyperparameters:**

- `feature_dim`: Number of features/vocabulary size (default: auto)
- `mini_batch_size`: Number of documents per batch (default: 100)
- `learning_rate`: Step size during optimization (default: 0.001)
- `epochs`: Number of training epochs (default: 50)
- `optimizer`: Optimization algorithm (`adadelta`, `adam`, `sgd`) (default: adadelta)
- `clip_gradient`: Gradient clipping threshold (default: 10.0)
- `weight_decay`: L2 regularization parameter (default: 0.0)

### Best Practices for Hyperparameter Tuning

#### Critical Hyperparameters Based on Web Research

Based on recent research on diffusion models and machine learning hyperparameter optimization, several key principles apply to SageMaker algorithms:

1. **Learning Rate and Batch Size**: These are among the most critical hyperparameters across all algorithms. As noted in [current diffusion model research](https://milvus.io/ai-quick-reference/what-hyperparameters-are-critical-when-training-a-diffusion-model), proper learning rate configuration significantly affects training stability and convergence.

2. **Regularization Parameters**: L1 and L2 regularization (where applicable) help prevent overfitting and improve generalization.

3. **Architecture-Specific Parameters**: For neural network-based algorithms (DeepAR, Object2Vec, NTM), parameters like layer depth, hidden dimensions, and dropout rates are crucial.

#### Hyperparameter Tuning Strategies

- **Start Simple**: Begin with default values and adjust incrementally
- **Use SageMaker Automatic Model Tuning**: Leverage Bayesian optimization for efficient hyperparameter search
- **Cross-Validation**: Always validate hyperparameter choices on unseen data
- **Monitor Training Metrics**: Watch for signs of overfitting or underfitting
- **Resource Considerations**: Balance hyperparameter complexity with computational costs

#### Algorithm-Specific Recommendations

- **Tree-based algorithms (XGBoost)**: Focus on `max_depth`, `eta`, and regularization parameters
- **Neural networks (DeepAR, Object2Vec)**: Prioritize `learning_rate`, `batch_size`, and architecture parameters
- **Clustering (K-Means)**: The choice of `k` is critical; use elbow method or silhouette analysis
- **Dimensionality reduction (PCA)**: `num_components` should balance information retention with computational efficiency

### Additional Resources

- [AWS SageMaker Hyperparameter Tuning Documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning.html)
- [SageMaker Built-in Algorithms Documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html)
- [Hyperparameter Optimization Best Practices](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-considerations.html)
