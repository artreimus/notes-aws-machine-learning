# Feature Engineering Techniques

## 1. Feature Splitting

**What it is:**  
Breaking a single composite feature into two or more atomic features.

**When to use it:**

- Your data combines multiple pieces of information into one field.
- You suspect each sub‑c
  omponent carries distinct predictive signal.

**Example (building_type_year):**

- **Raw:** `"Office–2005"`, `"Retail–1990"`
- **Split into:**
  - `building_type` → `"Office"`, `"Retail"`
  - `year_constructed` → `2005`, `1990`

This lets the model learn separate effects of **type** and **age**.

---

## 2. Binning (Discretization)

**What it is:**  
Grouping a continuous or ordinal variable into discrete “bins” or categories.

**When to use it:**

- You want to capture **non‑linear** relationships.
- To reduce the impact of noise or outliers.
- To create ordinal categories (e.g. “old”, “mid‑age”, “new”).

**Example (year_constructed):**

- After splitting, raw years (`1950–2020`) → bins like:
  - `“Pre‑1980”`, `“1980–2000”`, `“Post‑2000”`
- Binning can help the model detect era‑based pricing tiers instead of fitting a linear effect of year.

---

## 3. One‑Hot Encoding

**What it is:**  
Converting a categorical variable with _k_ distinct values into _k_ binary (0/1) features.

**When to use it:**

- Your feature is nominal (no inherent order).
- Models can’t ingest string labels directly, and you want to avoid implying ordinal relationships.

**Example (city):**

- **Raw:** `"New York"`, `"San Francisco"`, `"Chicago"`
- **One‑hot** → three columns:
  - `city_NY` = 1/0
  - `city_SF` = 1/0
  - `city_CHI` = 1/0

This lets the model learn a separate intercept (price adjustment) for each city.

---

## 4. Standardization (Z‑score Scaling)

**What it is:**  
Transforming a numeric feature to have **mean = 0** and **standard deviation = 1**:  
\[
x\_{\text{scaled}} = \frac{x - \mu}{\sigma}
\]

**When to use it:**

- Your model relies on gradient‑based optimization (e.g. linear regression, neural nets).
- Features have very different scales or units.
- You want to ensure each numeric feature contributes proportionally.

**Example (building_size):**

- **Raw:** `50 m²`, `300 m²`, `1 200 m²`
- **Standardized:**  
  \[
  \text{size}\_\text{std} = \frac{\text{size} - \overline{\text{size}}}{\text{std(size)}}  
  \]
- Prevents large‐scale features from dominating model updates.

---

## Mapping Features → Techniques

| Feature                      | Technique         | Why / Benefit                                                |
| ---------------------------- | ----------------- | ------------------------------------------------------------ |
| **building_type_year**       | Feature Splitting | Separates “type” vs “year” so each contributes individually  |
| **year_constructed** (child) | Binning           | Captures era‑based pricing tiers with discrete age bins      |
| **city**                     | One‑Hot Encoding  | Avoids arbitrary ordering; lets model learn per‑city effects |
| **building_size**            | Standardization   | Puts sizes on common scale; speeds convergence and stability |
