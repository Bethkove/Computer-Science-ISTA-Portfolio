**English** | [Français](README.fr.md)

# Neural Network from Scratch

A neural network written in **Python and NumPy** from first principles, without PyTorch or TensorFlow, to understand the forward pass, backpropagation and gradient descent end to end.

This project is the technical foundation of the portfolio: [`quantized-training`](../quantized-training/) reuses its training code.

## Content

| File | Description |
|---|---|
| `neuron.py` | A single artificial neuron (logistic regression) trained by gradient descent on two-dimensional synthetic data (`sklearn.datasets.make_blobs`) |
| `catdogneuron.py` | The same neuron applied to binary image classification (cats versus dogs) |
| `utilities.py` | Loading of the cat/dog dataset from HDF5 files |
| `datasets/` | 1,000 training and 200 test grayscale images, 64×64 pixels, balanced between the two classes |

## Scope

The project progresses from a single neuron to a network with one hidden layer, then to multiclass classification:

1. a single neuron with sigmoid activation and log loss;
2. gradients checked against finite differences;
3. a network with one hidden layer and hand-written backpropagation;
4. softmax output and cross-entropy loss for the 10-class digits dataset (`sklearn.datasets.load_digits`);
5. a reusable training function, on which quantization-aware training is built.

## Setting

Python, NumPy, h5py and Matplotlib, on CPU.
