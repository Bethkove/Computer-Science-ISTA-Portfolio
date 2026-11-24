**English** | [Français](README.fr.md)

# Federated k-Means

Clustering data spread across many clients that cannot share their raw data, when noise is added to protect privacy.

**Related research group:** Machine Learning and Computer Vision (Christoph Lampert, ISTA)

## Context

Data is often distributed across many devices or institutions and cannot be centralized. In **federated** k-means, each client only sends aggregated statistics (per-cluster sums and counts) to a server, which updates the cluster centers. To protect privacy, noise is added to these aggregates, as in differentially private algorithms.

Scott, Lampert and Saulpic (ICML 2025) point out that, in this setting, **initializing the centers** is the hard part, and propose to use a small dataset held by the server, possibly drawn from a different distribution than the clients' data.

## Research question

> Under noise added to the aggregated statistics, when does initializing from a small server-side dataset make federated k-means succeed where random initialization fails, and how does this change when the server data does not resemble the clients' data?

## Approach

1. Implement k-means (Lloyd's algorithm) and its federated version, in which clients send per-cluster sums and counts, and the server adds Gaussian noise to the totals.
2. Simulate clients with non-identically distributed data drawn from a Gaussian mixture.
3. Compare several initializations: random, k-means++ on in-distribution server data, and k-means++ on shifted, out-of-distribution server data.
4. Measure the clustering cost and the fraction of true clusters recovered, as a function of the noise level, over many random seeds.

## Scope

The noise level is studied as a parameter. Formal privacy guarantees (ε, δ) require the privacy accounting of the original paper, which is outside the scope of this study unless stated otherwise in the results.

## Setting

Python and NumPy (scikit-learn only for data generation and reference results), on CPU. All data is simulated.

## Reference

J. Scott, C. H. Lampert, D. Saulpic. *Differentially Private Federated k-Means Clustering with Server-Side Data.* ICML 2025. https://arxiv.org/abs/2506.05408
