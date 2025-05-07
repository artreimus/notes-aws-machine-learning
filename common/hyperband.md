## Hyperband

**Definition:** Hyperband is an efficient hyperparameter optimization algorithm that adapts the concept of multi-armed bandits to allocate resources (e.g., training epochs, data subsets) to randomly sampled hyperparameter configurations. It incorporates early stopping to quickly discard poor performers, focusing computational budget on promising candidates.

---

### Motivation

* Traditional hyperparameter search methods (grid search, random search) can be inefficient, wasting resources on unpromising configurations.
* Hyperband balances exploration (trying many configurations) and exploitation (allocating more resources to promising ones) to speed up tuning.

### Key Components

1. **Budget (R):** Total resource allocated to each configuration (e.g., max epochs).
2. **Brackets:** Each bracket corresponds to a different tradeoff between number of configurations and amount of resource per configuration.
3. **Successive Halving:** Within each bracket, Hyperband repeatedly trains all current configurations for a fixed resource increment, evaluates performance, and only keeps the top-performing fraction.

### Algorithm Outline

1. **Initialization:** Choose the maximum resource per configuration $R$ and the proportion of configurations to keep $\eta$ (commonly $\eta = 3$).
2. **Bracket Loop:** For each bracket $s = \lfloor \log_\eta{R}
   floor, \lfloor \log_\eta{R}
   floor - 1, \dots, 0$:

   * Compute:

     * $n = \lceil \frac{\log_\eta{R}}{s + 1} \rceil \cdot \eta^s$ (number of configurations)
     * $r = R \eta^{-s}$ (initial resource per config)
   * Run **Successive Halving** with $n$ configurations and starting budget $r$.
3. **Successive Halving:** Given $n$ configurations and resource $r$:

   * For $i = 0 \ldots s$:

     * Train each of the $n$ configurations for $r$ resources.
     * Evaluate their performance.
     * Keep the top $\lceil n/\eta \rceil$ configurations.
     * Increase $r \leftarrow r \times \eta$ and update $n \leftarrow \lceil n/\eta \rceil$.
4. **Selection:** Return the best hyperparameter configuration found across all brackets.

### Advantages

* **Resource Efficiency:** Quickly discards bad configurations, saving compute.
* **Scalability:** Effective for large-scale problems with high-dimensional hyperparameter spaces.
* **Flexibility:** Works with any algorithm where resource allocation and performance evaluation are defined.

### Considerations

* **Choice of η:** Affects aggressiveness of pruning; higher η prunes more heavily.
* **Compute Overhead:** Managing multiple brackets and evaluations can add complexity.
* **Randomness:** Being based on random sampling, results can vary; consider multiple runs.

---

**References:**

* Li, L., Jamieson, K., DeSalvo, G., Rostamizadeh, A., & Talwalkar, A. (2017). Hyperband: A Novel Bandit-Based Approach to Hyperparameter Optimizat
