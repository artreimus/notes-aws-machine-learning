# Amazon Bedrock Model Evaluations

## Overview
- Bedrock Model Evaluations helps you compare and select foundation models (including custom/imported ones) for your use case.
- Supports automatic, human, and LLM-as-a-judge evaluation modes.
- Also evaluates RAG systems, including Bedrock Knowledge Bases or custom pipelines.

## Evaluation Types
- Models: LLM-as-a-judge
  - A judge model scores a generator model’s outputs using metrics like correctness, completeness, and harmfulness.
- Models: Programmatic
  - Traditional metrics (e.g., BERTScore, F1) against built-in or custom datasets.
- Models: Human-based
  - Human reviewers score outputs for subjective or custom metrics.
- RAG: Retrieval
  - Measures retrieval quality (context relevance, coverage).
- RAG: Retrieve & Generate
  - Evaluates end-to-end RAG outputs for faithfulness, correctness, and safety.

## Key Concepts
- Evaluation job
  - A configured run against a dataset with chosen metrics.
- Prompt dataset
  - Built-in datasets or your own prompts and expected outputs.
- Metrics
  - Built-in metrics (accuracy, robustness, toxicity) or custom metrics.
- Results
  - Console visualizations plus full reports in S3.

## How It Works (High Level)
1. Choose evaluation type and task (generation, summarization, Q&A, classification, RAG).
2. Select dataset (built-in or custom).
3. Choose evaluation method (programmatic, human, LLM-as-judge).
4. Run the evaluation job.
5. Review scores and reports; compare across models.

## When to Use
- Picking the best FM for a specific task.
- Comparing prompt versions or fine-tuned models.
- Validating RAG pipelines before production.
- Monitoring safety or bias risks across models.

## Best Practices
- Use custom datasets that match your production distribution.
- Combine LLM-as-judge with programmatic metrics for a balanced view.
- Re-run evaluations when prompts or models change.
- Store reports in S3 for audit and governance.

## Exam Tips
- Bedrock supports automatic, human, and LLM-as-a-judge evaluations.
- Evaluations can cover both models and RAG pipelines.
- Results are viewable in console and exported to S3.

## Sources
- https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-tasks.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-metrics.html
- https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-judge.html
- https://aws.amazon.com/bedrock/evaluations/
- https://aws.amazon.com/about-aws/whats-new/2025/03/amazon-bedrock-model-evaluation-llm-as-a-judge/
- https://aws.amazon.com/about-aws/whats-new/2024/10/amazon-bedrock-model-evaluation-evaluating-custom-models/
