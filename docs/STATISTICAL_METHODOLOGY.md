# Statistical Modeling & Business Analytics Methodology

## 1. Overview & Architectural Separation
The **Intelligent Flying School Recommendation System** integrates rigorous statistical modeling and multi-criteria decision analysis (MCDA) to evaluate Directorate General of Civil Aviation (DGCA) approved Flying Training Organisations (FTOs) in India.

The platform provides **four analytical modes**:
1. **Hybrid Analytical Mode (Default / Recommended)**: Synthesizes hard regulatory/budget filtering, user preference weighted normalization, and statistical boosts from Factor Analysis & Clustering.
2. **Logistic Regression Mode**: Classifies FTOs by probability of attaining top-tier operational performance (Category A/A+), displaying model coefficients, odds ratios, ROC curve coordinates, and calibration curves.
3. **Factor Analysis Mode**: Reduces 8 operational, fleet, and pricing attributes into 3 orthogonal latent dimensions using Kaiser-Meyer-Olkin (KMO) test, Bartlett's test of sphericity, Scree plot eigenvalues, and Varimax rotation.
4. **K-Means Clustering Mode**: Unsupervised archetype segmentation sweeping candidate $K \in [2, 5]$, evaluating inertia elbow curves, silhouette coefficients, 2D PCA coordinate projections, and Adjusted Rand Index (ARI) seed stability.

---

## 2. Binary Logistic Regression

### Mathematical Specification
For an FTO characterized by feature vector $\mathbf{x} = [x_1, x_2, \dots, x_p]^T$, the log-odds of achieving top-tier operational classification (DGCA Category A or A+) is given by:

$$\ln\left(\frac{P(Y=1 \mid \mathbf{x})}{1 - P(Y=1 \mid \mathbf{x})}\right) = \beta_0 + \sum_{j=1}^p \beta_j x_j$$

And the predicted probability is:

$$P(Y=1 \mid \mathbf{x}) = \sigma(\beta_0 + \mathbf{\beta}^T \mathbf{x}) = \frac{1}{1 + e^{-(\beta_0 + \sum_{j=1}^p \beta_j x_j)}}$$

The **Odds Ratio (OR)** for feature $x_j$ is given by:

$$\text{OR}_j = \exp(\beta_j)$$

### Features Standardized
- Total fleet size ($z$-scored)
- Multi-engine aircraft count ($z$-scored)
- Base operations count
- Indicative fee in INR (inverted & $z$-scored)
- Night flying availability (binary $0/1$)
- Glass cockpit avionics availability (binary $0/1$)
- Established operational years ($z$-scored)

### Cross-Validation & Metric Tracking
- **Stratified K-Fold Cross Validation** ($k=3$) to preserve minority and majority class distributions.
- **Metrics Tracked**: Accuracy, Precision, Recall, $F_1$-Score, AUC-ROC, and Brier Calibration Score:
  $$\text{Brier} = \frac{1}{N}\sum_{i=1}^N (P_i - y_i)^2$$
- **ROC Curve Coordinates**: True Positive Rate (TPR) vs. False Positive Rate (FPR) across discrimination thresholds $\theta \in [0, 1]$.

---

## 3. Exploratory Factor Analysis (EFA)

### Pre-requisite Diagnostic Tests
1. **Kaiser-Meyer-Olkin (KMO) Measure of Sampling Adequacy**:
   Evaluates partial correlation vs. zero-order correlation among items:
   $$\text{KMO} = \frac{\sum_{i \neq j} r_{ij}^2}{\sum_{i \neq j} r_{ij}^2 + \sum_{i \neq j} a_{ij}^2}$$
   *Rule of Thumb*: $\text{KMO} \ge 0.60$ indicates adequate sampling for factor extraction.
2. **Bartlett's Test of Sphericity**:
   Tests the null hypothesis that the correlation matrix $\mathbf{R}$ is an identity matrix $\mathbf{I}$:
   $$\chi^2 = -\left(N - 1 - \frac{2p + 5}{6}\right) \ln |\mathbf{R}| \sim \chi^2_{\frac{p(p-1)}{2}}$$
   A $p$-value $< 0.05$ rejects the null hypothesis and confirms significant inter-item correlation.

### Factor Extraction & Rotation
- **Extraction**: Principal axis decomposition of the correlation matrix, retaining factors with Kaiser-Guttman eigenvalues $\lambda_k > 1.0$.
- **Varimax Orthogonal Rotation**: Maximizes the variance of squared loadings across variables to achieve clean simple structure:
  $$V = \sum_{k=1}^m \left[ \sum_{j=1}^p \left(\frac{l_{jk}}{h_j}\right)^4 - \frac{1}{p} \left( \sum_{j=1}^p \frac{l_{jk}^2}{h_j^2} \right)^2 \right]$$
- **Identified Latent Dimensions**:
  1. *Fleet Capacity & Modernity* (High loadings on total fleet, multi-engine count, glass cockpit).
  2. *Operational Maturity & Scope* (High loadings on base count, active runways, ATC tower complexity).
  3. *Cost-Efficiency vs. Premium Training* (High negative loading on fee, high loading on duration transparency).

---

## 4. K-Means Clustering

### Optimization Objective
Partitions the $N$ flying schools into $K$ disjoint clusters $S = \{S_1, S_2, \dots, S_K\}$ by minimizing within-cluster sum of squares (Inertia):

$$\min_S \sum_{k=1}^K \sum_{\mathbf{x} \in S_k} \|\mathbf{x} - \mathbf{\mu}_k\|^2$$

Where $\mathbf{\mu}_k$ is the geometric centroid of cluster $S_k$.

### Model Evaluation Sweep
- Evaluates candidate $K \in \{2, 3, 4, 5\}$.
- **Inertia Elbow Point**: Measures rate of variance reduction with increasing $K$.
- **Silhouette Coefficient**:
  $$s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}$$
  Where $a(i)$ is mean intra-cluster distance and $b(i)$ is nearest-cluster distance.
- **PCA 2D Dimensionality Reduction**: Projects standardized 8-dimensional space onto first 2 principal components ($PC_1, PC_2$) for 2D Cartesian scatter visualization.
- **Seed Stability**: Runs K-Means across 10 random seeds ($seed \in [0, 9]$) and computes pairwise Adjusted Rand Index (ARI) to verify reproducibility.

---

## 5. Multi-Criteria Recommendation & Sensitivity Analysis

### Decision Stages
1. **Hard Regulatory & Constraints Filtering**:
   - Verification of active DGCA approval status.
   - User budget threshold (with tolerance flexibility toggle).
   - Mandatory multi-engine requirement check.
   - Relocation willingness vs. base state/region.
2. **Standardized Preference Scoring**:
   $$\text{Score}_{\text{MCDA}} = w_c \cdot S_{\text{cost}} + w_r \cdot S_{\text{rank}} + w_f \cdot S_{\text{fleet}} + w_l \cdot S_{\text{location}} + w_i \cdot S_{\text{infra}}$$
   Where $\sum w = 1.0$.
3. **Statistical Hybrid Synthesis**:
   $$\text{Final Score} = \text{clamp}\left(0.85 \cdot \text{Score}_{\text{MCDA}} + 0.15 \cdot \text{Score}_{\text{Stat}}, 0, 100\right)$$
4. **Sensitivity Simulation ($\pm 20\%$)**:
   The engine perturbs each major weight vector by $\pm 20\%$, renormalizes weights, and recalculates school ranks to display how robust or sensitive each recommendation is to user preference shifts.
