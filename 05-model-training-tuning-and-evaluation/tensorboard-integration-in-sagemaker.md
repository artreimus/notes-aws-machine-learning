### 1. Feature Name

**TensorBoard Integration in SageMaker**

---

### 2. Category

- **Machine Learning → Training Visualization & Debugging**

---

### 3. Overview

TensorBoard is the standard visualization toolkit for TensorFlow (and now supported by PyTorch). In SageMaker, you can launch a hosted TensorBoard instance that points at your training job’s log files, giving you live, interactive access to:

- **Scalars** (loss, accuracy, custom metrics)
- **Graphs** (model architecture)
- **Histograms** (weights, biases over time)
- **Embedding projections** (dimensionality reduction of embedding layers)
- **Profiling data** (kernel, memory, and execution profiling)

---

### 4. Key Benefits

- **Live Monitoring**: View training progress without waiting for job completion.
- **Deep Insights**: Visualize internal model behavior—identify vanishing/exploding gradients, poorly learning layers, or bottlenecks.
- **Cross‑Framework Support**: Works with TensorFlow and PyTorch via native callbacks or hooks.
- **Seamless in Studio**: One‑click launch from SageMaker Studio or via SDK/CLI, with secure access over IAM.

---

### 5. How It Works

1. **Instrument Your Training Script**
   - **TensorFlow**: Add a `TensorBoard` callback in your `model.fit()` call, specifying a log directory under `/opt/ml/output/tensorboard`.
   - **PyTorch**: Use `torch.utils.tensorboard.SummaryWriter` and write logs to the same SageMaker output path.
2. **Configure the Estimator**

   ```python
   from sagemaker.tensorflow import TensorFlow

   estimator = TensorFlow(
       entry_point="train.py",
       role=role,
       instance_count=1,
       instance_type="ml.p3.2xlarge",
       framework_version="2.4",
       py_version="py37",
       hyperparameters={…},
       tensorboard_output_config={
           "LocalPath": "/opt/ml/output/tensorboard",  # where your script writes logs
       }
   )
   ```

3. **Launch the Training Job**
   - SageMaker automatically uploads logs from the specified TensorBoard directory to S3 under the job’s output path.
4. **Open TensorBoard**
   - **In Studio**: Right‑click the training job in the Experiments pane → **Visualize in TensorBoard**.
   - **Via SDK/CLI**: Call `estimator.tensorboard_start()` to get a presigned URL.
5. **Interact & Analyze**
   - Explore the Scalars, Graphs, Histograms, Embeddings, and Profile tabs in your browser.

---

### 6. Required Script Modifications

- **Log Directory**: Write logs to `/opt/ml/output/tensorboard` (or custom path you pass via `tensorboard_output_config`).
- **Callbacks/Hooks**:

  - **TensorFlow**:

    ```python
    from tensorflow.keras.callbacks import TensorBoard

    tb_callback = TensorBoard(log_dir="/opt/ml/output/tensorboard", update_freq="batch")
    model.fit(dataset, epochs=…, callbacks=[tb_callback, …])
    ```

  - **PyTorch**:

    ```python
    from torch.utils.tensorboard import SummaryWriter

    writer = SummaryWriter(log_dir="/opt/ml/output/tensorboard")
    for step, (x, y) in enumerate(loader):
        …
        writer.add_scalar("loss", loss.item(), global_step=step)
    writer.close()
    ```

---

### 7. Best Practices

- **Frequent Logging**: Set `update_freq="batch"` or a small step interval for finer granularity.
- **Manage Storage**: Log only essential metrics to avoid excessive S3 storage.
- **Secure Access**: Use IAM and VPC endpoints so only authorized users can view your TensorBoard.
- **Combine with Debugger**: For deeper insights, use TensorBoard alongside SageMaker Debugger’s system and framework profiling.

---

### 8. Exam‑Focused Tips

- **Directory Convention**: Logs must be in the estimator’s `tensorboard_output_config` path (default `/opt/ml/output/tensorboard`).
- **One‑click in Studio**: You can launch TensorBoard directly from the SageMaker Studio UI.
- **Supported Frameworks**: TensorFlow and PyTorch natively; others via custom logging in the same output path.
- **No Extra Containers**: TensorBoard runs on SageMaker-managed infrastructure—no need to build your own container.
