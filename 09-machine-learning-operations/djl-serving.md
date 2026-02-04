# DJL Serving (Deep Java Library)

## Overview
- DJL Serving is a high‑performance, universal model server powered by the Deep Java Library (DJL).
- It exposes models (and workflows) over HTTP with both **inference** and **management** APIs.
- Designed for multi‑model, multi‑engine serving with strong throughput and batching.

## Core Capabilities
- Serve multiple model formats out of the box (TorchScript, TensorFlow SavedModel, ONNX CPU, Python script).
- Extend with plugins for additional model types (XGBoost, LightGBM, SentencePiece, fastText/BlazingText).
- Dynamic batching and auto‑scaling of workers.
- Multi‑engine support so different models can use different engines in one server.
- Model versioning with optional version in inference path.

## Architecture (High Level)
- **Frontend**: Netty HTTP server handling requests.
- **Workflows**: Chain multiple models and glue logic.
- **WorkLoadManager (WLM)**: Manages workers, batching, routing, and threads.
- **Model Store**: Directory of models loaded on startup or dynamically.

## APIs
- **Inference API**: `POST /predictions/{model_name}` (optional `{version}`) for predictions.
- **Management API**: Load/unload/scale models at runtime.
- Default binding is localhost on port 8080 (configurable).

## Serving Modes
- **Java mode**: Use DJL Translators for pre/post‑processing.
- **Python mode**: Use Python handler for custom logic.
- **Binary mode**: Raw NDList/NumPy input/output, no pre/post‑processing.

## Configuration Layers
- **Global config** (`config.properties`, CLI flags, env vars): ports, model store, models/workflows on startup.
- **Model config** (`serving.properties` in each model folder/zip): engine, devices, queues, memory, translator, and engine‑specific `option.*` settings.
- **Workflow config** (`workflow.json` / `workflow.yml`) to compose multi‑model pipelines.

## Batching and Scaling
- Dynamic batching increases throughput and GPU utilization.
- Worker auto‑scaling adjusts concurrency to load.
- LLM serving commonly uses **rolling/continuous batching** in LMI containers (see LMI docs).

## Engines and Compatibility
- DJL supports multiple engines (MXNet, PyTorch, TensorFlow, ONNX Runtime, XGBoost, LightGBM).
- Hybrid engine mode can supplement limited NDArray functionality in some engines.

## Typical Deployment Flow
1. Package model artifacts in a model directory or archive.
2. Add `serving.properties` for per‑model settings (optional but recommended).
3. Configure `config.properties` or CLI flags (model store, ports, startup models).
4. Start DJL Serving and call inference/management endpoints.

## When to Use
- You want a Java‑native, high‑performance inference server.
- You need multi‑model or multi‑engine serving from one endpoint.
- You need workflow orchestration without writing your own server.

## Exam Tips
- DJL Serving exposes **inference + management** APIs and supports **dynamic batching**.
- `serving.properties` is the per‑model configuration entry point.
- WLM handles worker management, batching, and threading.

## Sources
- https://docs.djl.ai/master/docs/serving/index.html
- https://docs.djl.ai/master/docs/serving/serving/docs/architecture.html
- https://docs.djl.ai/master/docs/serving/serving/docs/inference.html
- https://docs.djl.ai/master/docs/serving/serving/docs/configuration.html
- https://docs.djl.ai/master/docs/serving/serving/docs/configurations_global.html
- https://docs.djl.ai/master/docs/serving/serving/docs/configurations_model.html
- https://docs.djl.ai/master/docs/serving/wlm/index.html
- https://docs.djl.ai/master/docs/serving/serving/docs/lmi/user_guides/lmi_input_output_schema.html
- https://docs.djl.ai/master/docs/serving/serving/docs/lmi/deployment_guide/configurations.html
- https://github.com/deepjavalibrary/djl-serving
