# SageMaker Spot Training

## Overview

Amazon SageMaker Spot Training allows you to use Amazon EC2 Spot Instances to run your training jobs at a significantly reduced cost compared to on-demand instances. Spot Instances are spare EC2 compute capacity offered at steep discounts, but they can be interrupted by AWS with a two-minute warning if the capacity is needed elsewhere.

## How It Works

- **Managed Spot Training**:  
  SageMaker can automatically allocate Spot Instances for your training jobs. You can specify which jobs use Spot Instances and set a stopping condition (e.g., maximum wait time).
- **Checkpointing**:  
  Since Spot Instances can be interrupted, SageMaker supports checkpointing—periodically saving the model state to Amazon S3. If an interruption occurs, SageMaker can resume training from the last checkpoint instead of starting over.
- **Automatic Retry**:  
  SageMaker will automatically retry interrupted jobs by obtaining new Spot capacity and resuming from the latest checkpoint.

## Key Features

- **Cost Savings**:  
  Spot Training can reduce training costs by up to 90% compared to on-demand pricing.
- **Seamless Recovery**:  
  With checkpointing, training jobs can resume from the last saved state, minimizing wasted compute time.
- **Flexible Scheduling**:  
  Spot Training is ideal for jobs that are flexible in terms of start time and duration.

## Best Practices

- **Implement Checkpointing**:  
  Always configure checkpointing to avoid losing progress if a Spot Instance is interrupted. Use the `CheckpointConfig` parameter to specify the S3 location for checkpoints.
- **Use Built-in Algorithms with Checkpointing Support**:  
  Some built-in algorithms (e.g., Object Detection, Semantic Segmentation, Image Classification) support checkpointing out of the box.
- **Set MaxWaitTimeInSeconds**:  
  Use this parameter to control the total duration (including wait time for Spot capacity) for your training job.

## Example Use Cases

- Large-scale training jobs where cost savings are important.
- Experimentation and hyperparameter tuning jobs that can tolerate interruptions.

## References

- [AWS Blog: Managed Spot Training](https://aws.amazon.com/blogs/aws/managed-spot-training-save-up-to-90-on-your-amazon-sagemaker-training-jobs/)
- [SageMaker Documentation: Managed Spot Training](https://docs.aws.amazon.com/sagemaker/latest/dg/model-managed-spot-training.html)
