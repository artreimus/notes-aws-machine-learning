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
