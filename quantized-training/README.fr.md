[English](README.md) | **Français**

# Quantized Training

Entraîner un petit réseau de neurones dont les poids sont limités à très peu de bits.

**Groupe de recherche lié :** Distributed Algorithms and Systems Lab (Dan Alistarh, ISTA)

## Contexte

Les grands modèles coûtent cher à entraîner et à faire tourner. **L'entraînement quantifié** (quantization-aware training) entraîne un réseau dont les poids sont arrondis sur quelques bits lors de la passe avant, tandis que des copies en pleine précision reçoivent les mises à jour. QuEST (Panferov et al., 2025) rend cet entraînement stable jusqu'à une très faible précision. L'un de ses ingrédients consiste à appliquer une **transformation de Hadamard**, une matrice orthogonale qui mélange les coordonnées, avant la quantification, afin d'étaler les valeurs extrêmes, et à choisir l'échelle de quantification qui minimise l'erreur.

Cette étude examine cet ingrédient sur un réseau assez petit pour s'entraîner sur un ordinateur portable.

## Question de recherche

> Lorsqu'un petit perceptron multicouche est entraîné avec des poids quantifiés sur 8, 4, 2 et 1 bits, appliquer une transformation de Hadamard avant la quantification réduit-il l'erreur de quantification et améliore-t-il la précision en test par rapport à une quantification directe des poids ?

## Démarche

1. Implémenter un quantificateur uniforme symétrique, avec une échelle fixée soit par le plus grand poids en valeur absolue, soit en minimisant l'erreur quadratique de quantification.
2. Entraîner un perceptron multicouche, écrit à partir de zéro dans [`neural-network-from-scratch`](../neural-network-from-scratch/README.fr.md), sur le jeu de chiffres de scikit-learn, avec un entraînement quantifié et l'estimateur de gradient straight-through.
3. Comparer trois variantes : pleine précision, quantification directe, et quantification après une transformation de Hadamard normalisée.
4. Mesurer la précision en test, les courbes d'entraînement et l'erreur de quantification pour chaque nombre de bits, sur de nombreuses graines aléatoires.

Une lecture complémentaire sur la parcimonie, *Accurate Neural Network Pruning Requires Rethinking Sparse Optimization*, encadre une extension possible vers l'élagage par magnitude.

## Cadre

Python, NumPy et SciPy, sur CPU. Seuls les poids sont quantifiés, sauf mention contraire dans les résultats.

## Références

A. Panferov, J. Chen, S. Tabesh, R. L. Castro, M. Nikdan, D. Alistarh. *QuEST: Stable Training of LLMs with 1-Bit Weights and Activations.* arXiv:2502.05003, 2025.

D. Kuznedelev, E. Kurtic, E. Iofinova, E. Frantar, A. Peste, D. Alistarh. *Accurate Neural Network Pruning Requires Rethinking Sparse Optimization.* TMLR 2024.
