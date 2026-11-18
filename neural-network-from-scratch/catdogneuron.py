import sys
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.metrics import accuracy_score
import plotly.graph_objects as go

sys.path.append(r"C:\Users\const\Documents\Licence 3\stage\Computer-Science-ISTA-Portfolio\neural-network-from-scratch")

from utilities import *

X_train, y_train, X_test, y_test = load_data()

print(X_train.shape)
print(y_train.shape)
print(np.unique(y_train, return_counts=True))

plt.figure(figsize=(16, 8))
for i in range(1, 10):
    plt.subplot(4, 5, i)
    plt.imshow(X_train[i], cmap='gray')
    plt.title(y_train[i])
    plt.tight_layout()
plt.show()

def initializer(X):
    W = np.random.randn(X.shape[1], 1)
    b = np.random.randn(1)
    return(W,b)

def model(X, W, b):
    Z = X.dot(W) + b
    A = 1 / (1+ np.exp(-Z))
    return A

def log_loss(A, y):
    return 1/len(y) * np.sum(-y* np.log(A) - (1 - y) * np.log(1-A))


def gradients(A, X, y):
    dW = 1/len(y) * np.dot(X.T, A - y)
    db = 1/len(y) * np.sum(A - y)
    return (dW, db)

def update(dW, db, W, b, learning_rate):
    W = W - learning_rate * dW
    b = b - learning_rate * db
    return (W, b)

def predict(X, W, b):
    A = model(X, W, b)
    #print(A)
    return A >= 0.5

def artificial_neuron(X, y, learning_rate = 0.1, n_iter = 100):
    #Initialisation of W,b
    W, b = initializer(X)
    Loss = [] #cost visualisation

    for i in range(n_iter):
        A = model(X, W, b)
        Loss.append(log_loss(A, y))
        dW, db = gradients(A, X, y)
        W, b = update(dW, db, W, b, learning_rate)

    y_pred = predict(X, W, b)
    print(accuracy_score(y, y_pred))

    plt.plot(Loss)
    plt.show
    return (W, b)