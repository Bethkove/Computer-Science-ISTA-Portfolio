[English](README.md) | **Français**

# Quantized Training — avec combien de bits un petit réseau peut-il apprendre ?

**Groupe lié :** Distributed Algorithms and Systems Lab (Dan Alistarh, ISTA)
**Article de départ :** Panferov, Chen, Tabesh, Castro, Nikdan, Alistarh, *QuEST: Stable Training of LLMs with 1-Bit Weights and Activations*, prépublication arXiv, 2025 — https://arxiv.org/abs/2502.05003
**Lecture complémentaire :** Kuznedelev, Kurtic, Iofinova, Frantar, Peste, Alistarh, *Accurate Neural Network Pruning Requires Rethinking Sparse Optimization*, TMLR 2024
**Calcul :** CPU uniquement (NumPy, SciPy). Réutilise `neural-network-from-scratch/`.

## Contexte

Les grands modèles coûtent cher à entraîner et à faire tourner. **L'entraînement quantifié** (quantization-aware training) entraîne un réseau dont les poids sont arrondis sur très peu de bits lors de la passe avant, tout en gardant des copies en pleine précision pour les mises à jour. QuEST fait fonctionner cela jusqu'à une très faible précision. L'un de ses ingrédients consiste à appliquer une **transformation de Hadamard** (une matrice orthogonale qui « mélange » les valeurs) avant de quantifier, pour étaler les valeurs extrêmes, puis à ajuster l'échelle de quantification en minimisant l'erreur.

Cette étude teste cet ingrédient sur un **petit** réseau qui s'entraîne sur un portable.

## Question de recherche

> Lors de l'entraînement d'un petit MLP dont les poids sont quantifiés sur 4, 2 et 1 bits, appliquer une transformation de Hadamard avant la quantification réduit-il l'erreur de quantification et améliore-t-il la précision en test par rapport à une quantification directe ?

## Hypothèses (à écrire et dater par toi AVANT les expériences)

- H1 : <...>
- H2 : <...>

## Méthode

1. **Modèle de base :** ton réseau de `neural-network-from-scratch/`, sur `sklearn.datasets.load_digits` (chiffres 8×8 ; la taille de la couche cachée doit être une puissance de 2, par exemple 64 ou 128, pour que la matrice de Hadamard existe).
2. **Quantificateur :** quantification uniforme symétrique sur b bits avec une échelle par matrice de poids ; d'abord une échelle fixée par la valeur absolue maximale, puis une échelle choisie pour minimiser l'erreur quadratique.
3. **Entraînement quantifié :** passe avant avec les poids quantifiés ; passe arrière avec l'**estimateur straight-through** (l'arrondi est traité comme l'identité) ; mise à jour des poids en pleine précision.
4. **Variante Hadamard :** quantifier `H W` au lieu de `W` (H : matrice de Hadamard normalisée, `scipy.linalg.hadamard(n) / sqrt(n)`), puis revenir en arrière avec `Hᵀ`.
5. **Comparaison :** pleine précision, quantification directe, Hadamard + quantification ; b ∈ {8, 4, 2, 1} ; plusieurs graines.
6. **Mesures :** précision en test, courbes de perte d'entraînement, erreur de quantification ‖W − Q(W)‖.
7. L'estimateur de gradient « de confiance » de QuEST : l'ajouter **seulement** si tu le comprends à la lecture de l'article.

**Extension optionnelle (issue de la lecture complémentaire) :** élagage par magnitude à forte parcimonie (80 à 95 %) du même réseau, avec un réentraînement court ou plus long.

## Première action (30 min, sans coder)

Lis le résumé, l'introduction et la vue d'ensemble de la méthode de QuEST. Puis, sur papier, prends le vecteur v = (0,9 ; −0,1 ; 0,05 ; −0,02) :

1. Quantifie-le sur 2 bits avec une échelle fixée par la valeur absolue maximale, et calcule l'erreur quadratique.
2. Multiplie-le d'abord par la matrice de Hadamard normalisée 4×4, quantifie le résultat de la même façon, reviens en arrière, et calcule à nouveau l'erreur quadratique.
3. Refais les deux calculs sur 3 bits.

Quelle erreur est la plus petite dans chaque cas ? La réponse est-elle la même sur 2 et sur 3 bits, et pourquoi ? Ce calcul deviendra ton premier test, et il devrait orienter tes hypothèses.

## Reproduire

```bash
pip install -r ../requirements.txt
python -m pytest
# <commande pour lancer chaque expérience>
```

## Résultats

<figures et chiffres réellement obtenus, avec leur dispersion>

## Ce que les résultats soutiennent / ne soutiennent pas

## Limites

Très petits modèle et jeu de données ; poids seulement (pas de quantification des activations, sauf si tu l'ajoutes) ; aucun gain de vitesse matériel mesuré. À écrire honnêtement à la fin.

## Definition of Done

- [ ] Hypothèses écrites et datées avant les résultats
- [ ] Tests : quantificateur et transformation de Hadamard vérifiés sur des cas calculés à la main
- [ ] Précision et erreur de quantification pour chaque nombre de bits, avec et sans Hadamard, sur plusieurs graines
- [ ] README complété (résultats, limites)
