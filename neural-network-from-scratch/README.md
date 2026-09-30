# Neural Network from Scratch

## Objectif

Construire un petit framework de réseau neuronal en **Python + NumPy**, sans utiliser PyTorch/TensorFlow pour les mécanismes fondamentaux.

Le but n'est pas de produire une librairie industrielle : le but est de comprendre et démontrer les mécanismes fondamentaux d'un réseau neuronal.

## Ordre d'implémentation

### 1. Structure minimale
Commencer par définir comment un réseau est construit et comment les couches communiquent.

### 2. Layers
Implémenter :
- Dense / Linear
- stockage des paramètres ;
- stockage des gradients ;
- forward ;
- backward.

### 3. Activations
Implémenter :
- ReLU ;
- Sigmoid ;
- Softmax.

Pour chaque activation : dérivée + tests numériques.

### 4. Losses
Implémenter :
- MSE ;
- Cross-Entropy.

Vérifier les gradients avec gradient checking.

### 5. Optimisation
Implémenter SGD :
- learning rate ;
- mise à jour des paramètres ;
- boucle d'entraînement.

### 6. Réseau complet
Le réseau doit pouvoir effectuer :

`input → Dense → ReLU → Dense → Softmax`

puis :

`loss → backward → SGD`

### 7. Expériences
Utiliser MNIST et mesurer :
- loss ;
- accuracy ;
- temps ;
- influence du learning rate ;
- influence de la taille de la couche cachée.

### 8. Analyse
Ne pas seulement afficher les chiffres. Expliquer :
- pourquoi les résultats changent ;
- quelles hypothèses sont confirmées ou non ;
- quelles limites possède l'implémentation.

## Structure cible

```text
neural-network-from-scratch/
├── README.md
├── src/
├── tests/
├── experiments/
└── results/
```

Créer chaque sous-dossier uniquement lorsqu'il reçoit son premier contenu utile.

## Definition of Done

- [ ] Forward pass correct
- [ ] Backpropagation vérifiée
- [ ] Gradient checking réussi
- [ ] Tests présents
- [ ] MNIST entraînable
- [ ] Expériences reproductibles
- [ ] Graphiques générés
- [ ] Analyse écrite
