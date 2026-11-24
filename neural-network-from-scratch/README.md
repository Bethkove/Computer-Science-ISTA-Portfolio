# Neural Network from Scratch

## Objectif

Construire un petit réseau de neurones en **Python + NumPy**, sans PyTorch ni TensorFlow, pour comprendre de bout en bout le forward, la rétropropagation et la descente de gradient.

Ce projet est la **base technique** du portfolio : l'étude `quantized-sgd/` réutilise directement l'entraînement par descente de gradient écrit ici.

## État actuel

| Fichier | Contenu | État |
|---|---|---|
| `neuron.py` | Un neurone artificiel (régression logistique) sur des données 2D (`make_blobs`) | Écrit, contient des bugs (voir plus bas) |
| `catdogneuron.py` | Le même neurone sur le jeu chat/chien | En cours, ne tourne pas encore |
| `utilities.py` | Chargement des données chat/chien (HDF5) | Fonctionnel |
| `datasets/` | 1000 images d'entraînement et 200 de test, 64×64, niveaux de gris, classes équilibrées | Présent |

Si ces données viennent d'un tutoriel, cite la source ici.

## À corriger avant d'aller plus loin

Ces problèmes sont à corriger **par toi** ; chacun est un petit exercice.

1. **`neuron.py`, lignes 68-75** : `W` et `b` sont utilisés avant d'être définis (`artificial_neuron` n'est appelé qu'à la ligne 77). Que se passe-t-il à l'exécution, et comment réordonner le script ?
2. **`plt.show` sans parenthèses** (`neuron.py` ligne 65, `catdogneuron.py` ligne 70) : la courbe de perte ne s'affiche pas. Pourquoi ?
3. **`catdogneuron.py`** : `X_train` a la forme `(1000, 64, 64)`. Quelle forme doit avoir `X` pour que `X.dot(W)` fonctionne avec un `W` de forme `(n_features, 1)` ?
4. **Normalisation** : les pixels vont de 0 à 254. Que devient `np.exp(-Z)` avec des entrées de cet ordre ? Que faut-il faire avant l'entraînement ?
5. **`log_loss`** : que vaut `np.log(A)` si `A` vaut exactement 0 ou 1 ? Ajoute une petite constante `epsilon` et explique ton choix.
6. **`catdogneuron.py`, ligne 8** : le chemin Windows écrit en dur empêche quiconque d'autre de lancer le script. Comment s'en passer ?
7. **Code dupliqué** : `catdogneuron.py` recopie toutes les fonctions de `neuron.py`. Regroupe-les dans un module importé par les deux scripts.

## Étapes suivantes (version réduite, compatible avec le calendrier)

1. Corriger les 7 points ci-dessus.
2. Vérifier `gradients` par **gradient checking** (comparer à des différences finies) dans un premier test `pytest`.
3. Passer du neurone unique à un réseau à **une couche cachée** : `input → Dense → ReLU/Sigmoid → Dense → Sigmoid`, avec rétropropagation écrite à la main.
4. Entraîner sur chat/chien, puis sur `sklearn.datasets.load_digits` (10 classes, nécessite Softmax + Cross-Entropy).
5. Exposer une fonction d'entraînement qui reçoit les gradients et applique la mise à jour : c'est l'endroit où `quantized-sgd/` branchera la quantification.

Le reste du plan initial (MNIST complet, nombreuses expériences d'hyperparamètres) passe après les candidatures.

## Structure cible

```text
neural-network-from-scratch/
├── README.md
├── neuron.py
├── catdogneuron.py
├── utilities.py
├── datasets/
└── tests/            ← à créer avec le premier test de gradient
```

Créer chaque dossier uniquement lorsqu'il reçoit son premier contenu utile.

## Definition of Done

- [ ] Les 7 points corrigés
- [ ] Gradient checking réussi (test `pytest`)
- [ ] Réseau à une couche cachée entraînable
- [ ] Courbe de perte et précision test sur chat/chien
- [ ] Fonction d'entraînement réutilisable par `quantized-sgd/`
- [ ] Analyse courte : ce qui marche, ce qui ne marche pas, pourquoi
