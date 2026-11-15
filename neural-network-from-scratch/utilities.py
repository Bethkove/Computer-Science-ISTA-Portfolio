from pathlib import Path
import numpy as np
import h5py

BASE_DIR = Path(__file__).resolve().parent

def load_data():

    train_dataset = h5py.File(BASE_DIR / "trainset.hdf5", "r")
    test_dataset = h5py.File(BASE_DIR / "testset.hdf5", "r")

    X_train = np.array(train_dataset["X_train"][:])
    y_train = np.array(train_dataset["Y_train"][:])

    X_test = np.array(test_dataset["X_test"][:])
    y_test = np.array(test_dataset["Y_test"][:])

    train_dataset.close()
    test_dataset.close()

    return X_train, y_train, X_test, y_test