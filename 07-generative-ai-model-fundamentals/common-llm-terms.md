# Common LLM Terms and Model Parameters

- **Tokens** – Numerical representations of words or parts of words. These are the fundamental units processed by the model.

- **Embeddings** – Dense vector representations that encode the semantic meaning of tokens.

- **Top P (nucleus sampling)** – A probability threshold for token inclusion. Tokens are sampled from the smallest possible set whose cumulative probability exceeds P. Higher values = more randomness.

- **Top K** – Limits the sampling pool to the top K most likely tokens. A higher K increases randomness.

- **Temperature** – Controls randomness in output generation:

  - High temperature → more varied and creative outputs.
  - Low temperature → more deterministic and consistent responses.

- **Context Window** – The maximum number of tokens the model can consider in a single inference pass.

- **Max Tokens** – The combined limit for input and output tokens. Exceeding this limit truncates text.

- **Min Tokens** – The minimum number of tokens to generate.

- **Stop Sequences** – Specifies sequences that terminate generation. Useful for specific tasks like code completion.

- **Decoding Method** – The approach used to generate text:

  - Greedy decoding: Selects the most likely token at each step.
  - Random sampling: Selects tokens randomly based on probability distribution.

- **Top-K sampling**: Limits the pool of choices.
- **Top-P sampling**: Limits the pool of choices based on cumulative probability.

Understanding these parameters is crucial for tuning model behavior, optimizing generation quality, and controlling computational cost.
