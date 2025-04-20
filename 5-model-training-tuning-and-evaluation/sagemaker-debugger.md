---
## Amazon SageMaker Debugger
---

### 1. Service Name

**Amazon SageMaker Debugger**

---

### 2. Category

- **Machine Learning → Training Monitoring & Debugging**

---

### 3. Overview

SageMaker Debugger automatically captures internal training state—tensors, gradients, system metrics—periodically during a SageMaker training job. It helps you **profile**, **monitor**, and **debug** your models in real time or after training, without manually instrumenting your training code.

---

### 4. Key Features

- **Automatic Data Capture**
  - Captures tensors (weights, activations, gradients) and system metrics (CPU/GPU utilization, memory) at user-defined intervals.
- **Built‑in Rules & Profiling**
  - Predefined rules for:
    1. **System Bottlenecks** (e.g., CPU/GPU overutilization)
    2. **Framework Profiling** (e.g., TensorFlow op latency, MXNet operator metrics)
    3. **Model Parameter Checks** (e.g., weight saturation, gradient anomalies)
- **Custom Rules & Hooks**
  - Use the **SMDEBUG** Python library to configure custom data capture “hooks” and write your own rules.
- **Real‑time Alerts & Automated Actions**
  - On rule triggers, emits **CloudWatch Events**
  - Configurable actions:
    - **StopTraining** (automatically halt the job)
    - **PublishMetric** (to CloudWatch)
    - **SNS notifications** (Email/SMS via SNS)
- **SageMaker Studio Debugger Dashboard**
  - Visualize captured tensors and metrics over time
  - View generated **profiler reports** and **training summaries**
- **Training Reports**
  - One‑click generation of a detailed HTML report showing hardware utilization and model performance trends.

---

### 5. Supported Frameworks & Estimators

- **Deep Learning Frameworks**:
  - TensorFlow, PyTorch, MXNet
- **Boosted Trees**:
  - XGBoost
- **Generic Estimator**:
  - Any custom training container using the SMDEBUG hooks

---

### 6. How It Works

1. **Instrument Training Job**
   - Pass a **DebuggerHookConfig** when calling `CreateTrainingJob` (SDK/CLI/Studio).
2. **Capture Intervals**
   - Configure collection frequency (e.g., every N steps or seconds).
3. **Rule Evaluation**
   - For each enabled rule, SageMaker Debugger runs a separate “debug job” in parallel, evaluating tensors/metrics.
4. **Event Emission**
   - On rule violation, emits a CloudWatch Event with metadata (rule name, tensor snapshot).
5. **Action Execution**
   - SNS notification, stop training, or CloudWatch metric published.

---

### 7. Built‑in Rule Categories

| Category                | Example Rules                                       | Purpose                                                                          |
| ----------------------- | --------------------------------------------------- | -------------------------------------------------------------------------------- |
| **System Profiling**    | ProfilerReport, HardwareUtilization, CPUUtilization | Detect hardware bottlenecks (CPU/GPU/memory saturation)                          |
| **Framework Profiling** | TfOperatorTime (TensorFlow op latency), StepOutlier | Identify slow ops or anomalous step durations                                    |
| **Model Profiling**     | LossNotDecreasing, WeightUpdate, GradientClipping   | Alert on training anomalies (no loss improvement, exploding/vanishing gradients) |

---

### 8. New & Noteworthy

- **Debugger Insights Dashboard** (2021+)
  - Enhanced visuals in SageMaker Studio for interactive drill-down on captured data.
- **Profiler Rules**
  - Automatically generate and display system-level profiling reports.
- **Enhanced Actions**
  - Now supports automatic **StopTraining** action to conserve compute if model misbehaves.

---

### 9. Integration & Extensibility

- **SMDEBUG Python Library**
  - `smdebug.pytorch`, `smdebug.tensorflow`, `smdebug.mxnet` modules
  - Programmatically define hooks and custom rule sets.
- **CloudWatch & SNS**
  - Leverage standard AWS services for alert routing and notification workflows.
- **SageMaker Studio**
  - Full visual interface for configuring, monitoring, and post‑mortem analysis.

---

### 10. Pricing Model

- **Capturing Overhead**: Minimal extra cost for storing debug data in S3.
- **Compute for Debug Jobs**: Debug jobs incur additional SageMaker compute charges.
- **Data Transfer & Storage**: Charges for S3 PUT and storage of tensor snapshots.

---

### 11. Best Practices

- **Tune Collection Frequency**
  - Balance granularity vs. storage/compute overhead.
- **Enable Only Needed Rules**
  - Focus on critical issues to reduce debug-job costs.
- **Use StopTraining Smartly**
  - Prevent wasted compute when major training anomalies occur.
- **Visualize Early**
  - Use Studio dashboard during early epochs to catch misconfigurations fast.
- **Combine with CloudWatch Alarms**
  - Route rule triggers into existing operational dashboards and incident workflows.

---

### 12. Exam‑Focused Quick Tips

- **SMDEBUG** is the client library; configure via `DebuggerHookConfig` in training job API.
- **Built‑in rules** fire separate debug jobs—each can trigger SNS or StopTraining actions.
- **ProfilerReport** rule auto‑generates a hardware & framework profiling report.
- **StopTraining action** is distinct from job failure—you explicitly configure it via rules.
- **Debugger Insights dashboard** in Studio provides graphical time‑series of tensors & metrics.
