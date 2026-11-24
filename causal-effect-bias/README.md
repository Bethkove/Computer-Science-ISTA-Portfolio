**English** | [Français](README.fr.md)

# Causal Effect Bias

How reliable is a causal-effect estimate when the outcome is not measured but predicted by a classifier?

**Related research group:** Causal Learning and Artificial Intelligence (Francesco Locatello, ISTA)

## Context

In a randomized controlled trial, the average treatment effect (ATE) is identified by a simple difference of means between treated and control units. In many scientific experiments, however, the outcome is recorded in high-dimensional observations (images, videos) and is **predicted by a machine-learning model** rather than measured directly.

Cadei et al. (NeurIPS 2024) show that this step can bias the causal conclusion even when the classifier is accurate. Two of their results motivate this study:

- **Theorem 3.1:** thresholding predicted probabilities into hard labels biases the effect estimate, even for a consistent classifier.
- **Lemma 3.1:** the worst-case bias of a classifier with error rate ε scales as ε / min_t P(T = t), so it can grow when the treatment is imbalanced.

Their illustrative simulation (Example 1, Appendix B.1) uses a balanced treatment.

## Research question

> How does treatment imbalance affect the bias and the variability of causal-effect estimates computed from raw versus thresholded classifier predictions?

## Approach

1. Reproduce the simulation of Example 1: a structural causal model in which T is a binary treatment, X = T + W + noise, and Y = 1[X + noise ≥ 0]; a logistic regression predicts Y from X, and the effect is estimated from raw and from thresholded predictions.
2. Derive the population-level values of the true and thresholded effects analytically, and check them against simulation.
3. Vary the treatment probability P(T = 1) and measure, over many random seeds, both the average deviation from the true effect and its spread.
4. Study a setting in which the classifier's errors are not shared equally between the two treatment groups, the situation described by the worst case of Lemma 3.1.

## Setting

Python, NumPy, SciPy and scikit-learn, on CPU. All data is simulated.

## Reference

R. Cadei, L. Lindorfer, S. Cremer, C. Schmid, F. Locatello. *Smoke and Mirrors in Causal Downstream Tasks.* NeurIPS 2024. Code: https://github.com/CausalLearningAI/ISTAnt
