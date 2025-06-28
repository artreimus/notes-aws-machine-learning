**Random Cut Forest (RCF) in Amazon SageMaker**

**Purpose:**

Random Cut Forest (RCF) is an unsupervised machine learning algorithm developed by Amazon Web Services (AWS) for anomaly detection. It identifies data points that deviate significantly from the majority, such as unexpected spikes in time-series data, disruptions in periodic patterns, or unclassifiable observations. Each data point is assigned an anomaly score, with higher scores indicating greater likelihood of being anomalous.

**Training Input Requirements:**

- **Data Formats:** RCF accepts data in `RecordIO-protobuf` or CSV formats.
- **Modes:** Both File and Pipe modes are supported for training.
- **Optional Test Channel:** A test channel can be provided with labeled data (anomalous or not) to compute metrics such as accuracy, precision, recall, and F1-score.

**How It Works:**

RCF constructs a forest of random cut trees, each built from a random sample of the data. The algorithm partitions data recursively using random cuts, creating a tree structure that captures the data's distribution. The anomaly score for a data point is based on the change in the tree's complexity when the point is added; points that cause significant changes are considered more anomalous.

**Important Hyperparameters:**

- **`num_trees`:** Specifies the number of trees in the forest. Increasing this value can reduce noise in anomaly detection.
- **`num_samples_per_tree`:** Determines the number of samples used to build each tree. It should be set such that the inverse approximates the ratio of anomalous to normal data points.

**Instance Recommendations:**

- **Training:** RCF does not utilize GPUs; therefore, CPU instances like `ml.m5`, `ml.c5`, or `ml.c4` are recommended.
- **Inference:** For deployment, instances such as `ml.c5.xlarge` are suitable.
