from utilities import *

X_train, y_train, X_test, y_test = load_data()

print(X_train.shape)
print(y_train.shape)
print(np.unique(y_train, return_counts=True))