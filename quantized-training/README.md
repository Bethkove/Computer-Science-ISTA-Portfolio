**English** | [Français](README.fr.md)

# Quantized Training

Training a small neural network whose weights are restricted to very few bits.

**Related research group:** Distributed Algorithms and Systems Lab (Dan Alistarh, ISTA)

## Context

Large models are expensive to train and to run. **Quantization-aware training** trains a network whose weights are rounded to a few bits in the forward pass, while full-precision copies receive the updates. QuEST (Panferov et al., 2025) makes this stable down to very low precision. One of its ingredients is to apply a **Hadamard transform**, an orthogonal matrix that mixes coordinates, before quantization, in order to spread out extreme values, and to choose the quantization scale that minimizes the error.

This study examines that ingredient on a network small enough to train on a laptop.

## Research question

> When a small multilayer perceptron is trained with weights quantized to 8, 4, 2 and 1 bits, does applying a Hadamard transform before quantization reduce the quantization error and improve test accuracy compared with quantizing the weights directly?

## Approach

1. Implement a symmetric uniform quantizer, with a scale chosen either from the largest absolute weight or by minimizing the squared quantization error.
2. Train a multilayer perceptron, written from scratch in [`neural-network-from-scratch`](../neural-network-from-scratch/), on the scikit-learn digits dataset, with quantization-aware training and the straight-through gradient estimator.
3. Compare three variants: full precision, direct quantization, and quantization after a normalized Hadamard transform.
4. Measure test accuracy, training curves and quantization error for each bit width, over many random seeds.

A complementary reading on sparsity, *Accurate Neural Network Pruning Requires Rethinking Sparse Optimization*, frames a possible extension to magnitude pruning.

## Setting

Python, NumPy and SciPy, on CPU. Weights only are quantized unless stated otherwise in the results.

## References

A. Panferov, J. Chen, S. Tabesh, R. L. Castro, M. Nikdan, D. Alistarh. *QuEST: Stable Training of LLMs with 1-Bit Weights and Activations.* arXiv:2502.05003, 2025.

D. Kuznedelev, E. Kurtic, E. Iofinova, E. Frantar, A. Peste, D. Alistarh. *Accurate Neural Network Pruning Requires Rethinking Sparse Optimization.* TMLR 2024.
