[English](README.md) | **Français**

# Neural Network from Scratch

Un réseau de neurones écrit en **Python et NumPy** à partir des principes de base, sans PyTorch ni TensorFlow, pour comprendre de bout en bout la passe avant, la rétropropagation et la descente de gradient.

Ce projet est la base technique du portfolio : [`quantized-training`](../quantized-training/README.fr.md) réutilise son code d'entraînement.

## Contenu

| Fichier | Description |
|---|---|
| `neuron.py` | Un neurone artificiel (régression logistique) entraîné par descente de gradient sur des données synthétiques en deux dimensions (`sklearn.datasets.make_blobs`) |
| `catdogneuron.py` | Le même neurone appliqué à une classification d'images binaire (chats contre chiens) |
| `utilities.py` | Chargement du jeu de données chats/chiens depuis des fichiers HDF5 |
| `datasets/` | 1 000 images d'entraînement et 200 images de test en niveaux de gris, 64×64 pixels, réparties à égalité entre les deux classes |

## Périmètre

Le projet progresse d'un neurone unique vers un réseau à une couche cachée, puis vers la classification multiclasse :

1. un neurone unique avec activation sigmoïde et perte logistique ;
2. des gradients vérifiés par différences finies ;
3. un réseau à une couche cachée avec une rétropropagation écrite à la main ;
4. une sortie softmax et une perte d'entropie croisée pour le jeu de chiffres à 10 classes (`sklearn.datasets.load_digits`) ;
5. une fonction d'entraînement réutilisable, sur laquelle est construit l'entraînement quantifié.

## Cadre

Python, NumPy, h5py et Matplotlib, sur CPU.
