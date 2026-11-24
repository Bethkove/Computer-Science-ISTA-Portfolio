**English** | [Français](README.fr.md)

# Neural Network from Scratch

## Goal

Build a small neural network in **Python + NumPy**, without PyTorch or TensorFlow, to understand the forward pass, backpropagation and gradient descent end to end.

This project is the **technical foundation** of the portfolio: `quantized-training/` reuses the training code written here.

## Current state

| File | Content | State |
|---|---|---|
| `neuron.py` | A single artificial neuron (logistic regression) on 2D data (`make_blobs`) | Written, contains bugs (see below) |
| `catdogneuron.py` | The same neuron on the cat/dog dataset | In progress, does not run yet |
| `utilities.py` | Loading the cat/dog data (HDF5) | Working |
| `datasets/` | 1000 training and 200 test images, 64×64, grayscale, balanced classes | Present |

If this data comes from a tutorial, cite the source here.

## To fix before going further

Fix these yourself; each one is a small exercise.

1. **`neuron.py`, lines 68-75:** `W` and `b` are used before being defined (`artificial_neuron` is only called on line 77). What happens when the script runs, and how should it be reordered?
2. **`plt.show` without parentheses** (`neuron.py` line 65, `catdogneuron.py` line 70): the loss curve is never displayed. Why?
3. **`catdogneuron.py`:** `X_train` has shape `(1000, 64, 64)`. What shape must `X` have for `X.dot(W)` to work with a `W` of shape `(n_features, 1)`?
4. **Normalization:** pixel values range from 0 to 254. What happens to `np.exp(-Z)` with inputs of that size? What should be done before training?
5. **`log_loss`:** what is `np.log(A)` when `A` is exactly 0 or 1? Add a small constant `epsilon` and explain your choice.
6. **`catdogneuron.py`, line 8:** the hard-coded Windows path prevents anyone else from running the script. How can you avoid it?
7. **Duplicated code:** `catdogneuron.py` copies every function from `neuron.py`. Move them into one module imported by both scripts.

## Next steps (reduced scope, compatible with the schedule)

1. Fix the 7 points above.
2. Check `gradients` with **gradient checking** (compare with finite differences) in a first `pytest` test.
3. Go from a single neuron to a network with **one hidden layer**: `input → Dense → ReLU/Sigmoid → Dense → Sigmoid`, with hand-written backpropagation.
4. Train on cat/dog, then on `sklearn.datasets.load_digits` (10 classes, needs Softmax + Cross-Entropy).
5. Expose a training function that takes the weights through a function before the forward pass: this is where `quantized-training/` will plug in quantization.

The rest of the original plan (full MNIST, many hyperparameter experiments) comes after the applications.

## Target layout

```text
neural-network-from-scratch/
├── README.md / README.fr.md
├── neuron.py
├── catdogneuron.py
├── utilities.py
├── datasets/
└── tests/            ← create with the first gradient test
```

Create each folder only when it receives its first useful content.

## Definition of Done

- [ ] The 7 points fixed
- [ ] Gradient checking passes (`pytest` test)
- [ ] One-hidden-layer network trains
- [ ] Loss curve and test accuracy on cat/dog
- [ ] Training function reusable by `quantized-training/`
- [ ] Short analysis: what works, what does not, and why
