**English** | [Français](README.fr.md)

# Causal Effect Bias — when a classifier distorts a causal effect

**Related group:** Causal Learning and Artificial Intelligence (Francesco Locatello, ISTA)
**Starting paper:** Cadei, Lindorfer, Cremer, Schmid, Locatello, *Smoke and Mirrors in Causal Downstream Tasks*, NeurIPS 2024 — code: https://github.com/CausalLearningAI/ISTAnt
**Compute:** CPU only (NumPy, scikit-learn). Each simulation takes seconds.

## Context

In a randomized trial we want the average treatment effect (ATE). When the outcome is not measured directly but **predicted by a model**, the model's errors can bias the estimated effect, even when its accuracy is high.

The paper shows two things this study revisits at small scale:

- **Theorem 3.1:** thresholding predicted probabilities (rounding them to 0 or 1) biases the effect estimate.
- **Lemma 3.1:** the worst-case bias grows when the treatment is **imbalanced** (bound in ε / min P(T=t)).

Yet Example 1 of the paper uses a balanced treatment (p_T = 0.5).

## Research question

> Does the bias caused by thresholding predictions change when the treatment becomes imbalanced (P(T=1) from 0.5 down to 0.1)?

## Hypotheses (write and date them yourself BEFORE running experiments)

- H1: <...>
- H2: <...>

## Method

### Step 1 — Reproduce Example 1 (Appendix B.1)

Simulated causal model:

- T ~ Bernoulli(p_T), W ~ N(0, 1), noise n_X ~ N(0, 1), noise n_Y ~ N(0, σ²_Y)
- X = T + W + n_X
- Y = 1 if X + n_Y ≥ 0, else 0

Then: logistic regression of Y on X, raw predictions `f(X)` and thresholded predictions `1[f(X) ≥ 0.5]`, and the empirical associational difference (EAD) computed with each.

Goal: reproduce **Figure 3** of the paper (EAD as a function of n, 50 seeds per n, p_T = 0.5, σ²_Y = 1).

### Step 2 — Vary P(T=1)

Same simulations for p_T ∈ {0.5, 0.3, 0.2, 0.1}. Measure the gap between the thresholded EAD and the true AD, with its spread across seeds.

True AD: computable analytically (Appendix B.1, Equation 32) or by one very large simulation. State which one you use.

### Step 3 (if time allows)

Vary σ²_Y: the paper states that the bias grows with the noise variance. Check it.

## First step (30 min, no code)

Re-read Appendix B.1. On paper, compute `AD_{Y,T}` for p_T = 0.5 and σ²_Y = 1 with Equations 27-28 and 32, then the thresholded value (Equation 33). Do you get a gap of about 0.042 (Equation 37)? This computation becomes your first test.

## Reproduce

```bash
pip install -r ../requirements.txt
python -m pytest
# <command to run each experiment>
```

Seeds: <list>. Hardware: <your laptop>.

## Results

<figures and numbers actually obtained, with their spread>

## What the results support / do not support

## Limitations

Fully simulated, one-dimensional data; well-specified model (logistic regression is close to the true mechanism). Write this honestly at the end.

## Definition of Done

- [ ] Hypotheses written and dated before the results
- [ ] Test: the analytical value of Equation 37 is recovered
- [ ] Figure 3 reproduced
- [ ] Imbalance study over several seeds
- [ ] README completed (results, limitations)
