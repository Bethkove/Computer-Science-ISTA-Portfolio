**English** | [Français](README.fr.md)

# Federated k-Means — clustering private data spread over many devices

**Related group:** Machine Learning and Computer Vision (Christoph Lampert, ISTA)
**Starting paper:** Scott, Lampert, Saulpic, *Differentially Private Federated k-Means Clustering with Server-Side Data*, ICML 2025 — https://arxiv.org/abs/2506.05408
**Compute:** CPU only (NumPy, scikit-learn for data generation). Each run takes seconds.

## Context

Data is often spread over many devices (phones, hospitals) and cannot be centralized for privacy reasons. In **federated** k-means, each client only sends aggregated statistics (per-cluster sums and counts) to a server, which updates the cluster centers. To protect privacy, **noise** is added to these aggregates. The paper points out that, under noise, the **initialization** of the centers is the hard part, and uses a small dataset held by the server (possibly different from the clients' data) to initialize.

## Research question

> In federated k-means with Gaussian noise added to the aggregated statistics, from which noise level does initializing from a small server-side dataset clearly beat random initialization, and what happens when the server data does not resemble the clients' data?

## Hypotheses (write and date them yourself BEFORE running experiments)

- H1: <...>
- H2: <...>

## Method

1. **Data:** a Gaussian mixture with k clusters (`sklearn.datasets.make_blobs`), split across about 10 clients in a **non-IID** way (each client mostly sees a few clusters).
2. **Federated Lloyd iteration:** each client computes, for its own points, the per-cluster sums and counts; the server adds Gaussian noise of scale σ to the totals, then recomputes the centers.
3. **Initializations:**
   - random;
   - k-means++ on a small server-side dataset drawn from the same distribution;
   - the same, with server data drawn from a **shifted** distribution (out-of-distribution).
4. **Grid:** several noise levels σ, several seeds.
5. **Metrics:** k-means cost on all client data; fraction of true clusters recovered.
6. Compare later with the initialization actually proposed in the paper, once you have read it.

**Important:** unless you implement the paper's privacy accounting, this study gives **no formal privacy guarantee** (ε, δ). Say so in the limitations: here σ is a noise knob, not a privacy level.

## First step (30 min, no code)

Read the abstract, the introduction and the overview of the algorithm. Then, on paper: two clients in 1D, two centers. Client A holds points {0, 1, 2}, client B holds {10, 11}. Starting from centers 1 and 9, do **one** federated Lloyd step by hand (sums, counts, new centers). Then add +2 of noise to the count of the second cluster: how far does its center move? What does this tell you about small clusters under noise? This computation becomes your first test.

## Reproduce

```bash
pip install -r ../requirements.txt
python -m pytest
# <command to run each experiment>
```

## Results

<figures and numbers actually obtained, with their spread>

## What the results support / do not support

## Limitations

Synthetic data; noise without formal privacy accounting; simulated clients on one machine. Write this honestly at the end.

## Definition of Done

- [ ] Hypotheses written and dated before the results
- [ ] Test: the hand-computed Lloyd step is recovered by the code
- [ ] Cost and recovered clusters as a function of σ, for each initialization, several seeds
- [ ] Out-of-distribution server data case
- [ ] README completed (results, limitations)
