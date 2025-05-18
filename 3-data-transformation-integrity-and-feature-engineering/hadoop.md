# What is Apache Hadoop?

**Apache Hadoop** is an open-source framework for distributed storage and processing of large datasets across clusters of computers. It is designed to scale from a single server to thousands of machines, each offering local computation and storage.

## Core Components

- **Hadoop Distributed File System (HDFS):**  
  A distributed file system that stores data across multiple nodes, providing high throughput and fault tolerance.
- **MapReduce:**  
  A programming model for processing large datasets in parallel by dividing the work into independent tasks.
- **YARN (Yet Another Resource Negotiator):**  
  Manages and schedules resources across the cluster for various applications.

## Key Features

- **Scalability:**  
  Easily scales to handle petabytes of data by adding more nodes.
- **Fault Tolerance:**  
  Automatically replicates data and recovers from hardware failures.
- **Cost-Effective:**  
  Runs on commodity hardware, reducing infrastructure costs.

## Relevance to Machine Learning

- **Batch Data Processing:**  
  Hadoop is commonly used for ETL (Extract, Transform, Load) operations and preprocessing large datasets before ML model training.
- **Integration with ML Libraries:**  
  Can be integrated with tools like Apache Mahout or Spark MLlib for distributed machine learning.
- **AWS Integration:**  
  Available as a managed service on Amazon EMR, making it easy to process big data in the cloud and feed results into ML workflows.

## Typical Use Cases

- Large-scale data transformation and aggregation.
- Log processing and analytics.
- Preprocessing data for downstream ML tasks.

**References:**  
- [Apache Hadoop Documentation](https://hadoop.apache.org/)
