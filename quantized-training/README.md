**English** | [Français](README.fr.md)

# Quantized Training — how few bits can a small network train with?

**Related group:** Distributed Algorithms and Systems Lab (Dan Alistarh, ISTA)
**Starting paper:** Panferov, Chen, Tabesh, Castro, Nikdan, Alistarh, *QuEST: Stable Training of LLMs with 1-Bit Weights and Activations*, arXiv preprint, 2025 — https://arxiv.org/abs/2502.05003
**Complementary reading:** Kuznedelev, Kurtic, Iofinova, Frantar, Peste, Alistarh, *Accurate Neural Network Pruning Requires Rethinking Sparse Optimization*, TMLR 2024
**Compute:** CPU only (NumPy, SciPy). Reuses `neural-network-from-scratch/`.

## Context

Large models are expensive to train and run. **Quantization-aware training** trains a network whose weights are rounded to very few bits in the forward pass, while keeping full-precision copies for the updates. QuEST makes this work down to very low precision. One of its ingredients is to apply a **Hadamard transform** (an orthogonal "mixing" matrix) before quantizing, to spread out extreme values, then to fit the quantization scale by minimizing the error.

This study tests that ingredient on a **small** network that trains on a laptop.

## Research question

> When training a small MLP with weights quantized to 4, 2 and 1 bits, does applying a Hadamard transform before quantization reduce the quantization error and improve test accuracy compared with quantizing directly?

## Hypotheses (write and date them yourself BEFORE running experiments)

- H1: <...>
- H2: <...>

## Method

1. **Base model:** your network from `neural-network-from-scratch/`, on `sklearn.datasets.load_digits` (8×8 digits; the hidden layer size should be a power of 2, e.g. 64 or 128, so that the Hadamard matrix exists).
2. **Quantizer:** symmetric uniform quantization with b bits and one scale per weight matrix; first a max-abs scale, then a scale chosen to minimize the squared error.
3. **Quantization-aware training:** forward pass with quantized weights; backward pass with the **straight-through estimator** (the rounding is treated as the identity); update of the full-precision weights.
4. **Hadamard variant:** quantize `H W` instead of `W` (H: normalized Hadamard matrix, `scipy.linalg.hadamard(n) / sqrt(n)`), then transform back with `Hᵀ`.
5. **Comparison:** full precision, direct quantization, Hadamard + quantization; b ∈ {8, 4, 2, 1}; several seeds.
6. **Metrics:** test accuracy, training-loss curves, quantization error ‖W − Q(W)‖.
7. QuEST's "trust" gradient estimator: add it **only** if you understand it from reading the paper.

**Optional extension (from the complementary reading):** magnitude pruning at high sparsity (80-95 %) of the same network, with short versus longer fine-tuning.

## First step (30 min, no code)

Read the abstract, the introduction and the method overview of QuEST. Then, on paper, take the vector v = (0.9, −0.1, 0.05, −0.02):

1. Quantize it to 2 bits with a max-abs scale and compute the squared error.
2. Multiply it first by the normalized 4×4 Hadamard matrix, quantize the result the same way, transform back, and compute the squared error again.
3. Redo both computations with 3 bits.

Which error is smaller in each case? Is the answer the same at 2 and 3 bits, and why? This computation becomes your first test, and it should shape your hypotheses.

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

Tiny model and dataset; weights only (no activation quantization unless you add it); no hardware speed-up measured. Write this honestly at the end.

## Definition of Done

- [ ] Hypotheses written and dated before the results
- [ ] Tests: quantizer and Hadamard transform checked on hand-computed cases
- [ ] Accuracy and quantization error for each bit width, with and without Hadamard, several seeds
- [ ] README completed (results, limitations)
