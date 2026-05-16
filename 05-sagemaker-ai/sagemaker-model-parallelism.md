---
title: "Distributed Training in SageMaker"
exam: "MLA-C01"
status: "draft"
domain:
  - "2.2"
  - "3.1"
  - "4.1"
service:
  - "none"
tags:
  - "aws"
  - "mla-c01"
  - "domain-2"
  - "domain-3"
  - "domain-4"
  - "05_sagemaker_ai"
aliases:
  - "Distributed Training in SageMaker"
last_verified: "2026-05-16"
source_type: "aws-official"
---

# Distributed Training in SageMaker

### 1. Topic

**Distributed Training**: Scaling individual model training across multiple GPUs and instances.

---

### 2. Why It Matters

- **Single‑instance limits**: Even the largest ML instances (e.g., `ml.p4d.24xlarge` with 8 GPUs) may not hold or train extremely large models (billions + parameters).
- **Faster convergence**: Parallelism can reduce wall‑clock training time.
- **Cost vs. efficiency trade‑off**: Larger single instances often outperform multiple smaller ones due to lower communication overhead.

---

### 3. Types of Parallelism

| Parallelism Type      | What Is Parallelized         | When to Use                                                |
| --------------------- | ---------------------------- | ---------------------------------------------------------- |
| **Job Parallelism**   | Multiple independent jobs    | Training different models or hyperparameter trials in bulk |
| **Data Parallelism**  | Training data across GPUs    | Same model & dataset split across devices/nodes            |
| **Model Parallelism** | Model parameters across GPUs | Model too large for one GPU’s memory                       |

---

### 4. Distributed Data Parallelism (DDP)

#### 🔹 Concept

- **AllReduce** collective: each worker computes gradients on its data shard, then gradients are averaged (reduced) across all workers.
- **AllGather** collective: when needed, workers share intermediate data or metadata.

#### 🔹 SageMaker SMDDP

- Built on AWS Custom Collectives (optimized for EC2 network)
- **Enable in Estimator**:

  ```python
  from sagemaker.pytorch import PyTorch

  estimator = PyTorch(
      …,
      distribution={
        'smdistributed_dataparallel': {'enabled': True}
      }
  )
  ```

- **Benefits**: Lower all‑reduce overhead than native PyTorch DDP; works seamlessly with mixed‑precision and large batch sizes.

#### 🔹 Alternative Frameworks

- **PyTorch native DDP**: `distribution={'pytorchx': {'enabled': True}}`
- **TorchRun** (`torch.distributed`): MPI‑style, requires `ml.p3`/`ml.p4`/`ml.trn1` instances
- **Horovod**: MPI-based framework; enable via `sagemaker.horovod.Horovod` estimator
- **DeepSpeed**: Microsoft’s library for ultra‑scale (ZeRO optimizations), often used via Hugging Face on SageMaker

---

### 5. Distributed Model Parallelism (MPP)

#### 🔹 Concept

Split a single model’s parameters and states across GPUs/nodes when it cannot fit into one device.

#### 🔹 SageMaker SM Model Parallelism

- **Enable in Estimator**:
  ```python
  estimator = PyTorch(
      …,
      distribution={
        'smdistributed_modelparallel': {
          'enabled': True,
          'parameters': {
            'microbatches': 4,
            'placement_strategy': 'spread',
            // additional MPP configs
          }
        }
      }
  )
  ```
- **Key Techniques**:
  1. **Optimization State Sharding**
     - Shard optimizer states (weights, momentum) across GPUs
     - Requires stateful optimizers (e.g., Adam, AdamW)
  2. **Activation Checkpointing**
     - Discard intermediate activations during forward pass
     - Recompute them during backward pass to save memory
  3. **Activation Offloading**
     - Swap checkpointed activations to CPU memory, freeing GPU RAM
     - Trades off data‑transfer time for reduced GPU memory footprint
  4. **Sharded Data Parallelism**
     - Combines optimizer sharding with parameter & gradient sharding
     - Further reduces per‑GPU memory usage and scales to larger clusters

---

### 6. Choosing Parallelism Strategy

1. **Max out single instance** first (e.g., `ml.p4d.24xlarge` with 8 GPUs).
2. If model fits but training is slow → **Data Parallelism** (SMDDP or native DDP).
3. If model doesn’t fit GPU memory → **Model Parallelism** (SMMP) ± sharded data parallelism.
4. For extreme scale or custom needs → consider **Horovod** or **DeepSpeed**.

---

### 7. Best Practices & Tips

- **Minimize cross‑node communication**: Increase batch sizes and microbatch counts where possible.
- **Profile overhead** using SageMaker Debugger’s `ProfilerReport` and **network metrics**.
- **Balance compute vs. memory**: Use activation checkpointing/offloading only when memory is the critical bottleneck.
- **Monitor costs**: Multi‑node jobs incur both compute and interconnect costs; choose instance types wisely.
- **Stay within compatibility**: SMDDP and SMMP do **not** work with the deprecated Training Compiler.

---

### 8. Exam‑Focused Quick Triggers

- **AllReduce** = averaging gradients across workers (data parallelism).
- **AllGather** = collecting tensors/metadata among nodes.
- **SMDDP** = SageMaker’s optimized data parallel library.
- **SMMP** = SageMaker’s model parallel library (sharding + checkpointing + offload).
- **Horovod**/**DeepSpeed** = third‑party options for MPI or ZeRO‑based scaling.
- **Single large instance** vs. **multi‑instance**: always try a bigger instance before distributing.

---

With these distributed training techniques, you’ll be ready to architect SageMaker jobs that train the largest modern models—exactly what the exam will test. Good luck!

## Sources

- https://docs.aws.amazon.com/sagemaker/
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain2.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain3.html
- https://docs.aws.amazon.com/aws-certification/latest/machine-learning-engineer-associate-01/machine-learning-engineer-associate-01-domain4.html
