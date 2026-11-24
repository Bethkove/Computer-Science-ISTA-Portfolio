# Quantized SGD — combien de bits faut-il pour apprendre ?

**Groupe lié :** Distributed Algorithms and Systems Lab (Dan Alistarh, ISTA)
**Article de départ :** Alistarh, Grubic, Li, Tomioka, Vojnovic, *QSGD: Communication-Efficient SGD via Gradient Quantization and Encoding*, NeurIPS 2017 — https://arxiv.org/abs/1610.02132

**Calcul :** CPU uniquement (NumPy). Réutilise `neural-network-from-scratch/`.

## Contexte

Quand plusieurs machines entraînent un modèle ensemble, elles s'envoient leurs gradients, ce qui coûte cher en communication. QSGD **compresse chaque gradient** en ne gardant que quelques niveaux, avec un arrondi aléatoire choisi pour que le gradient compressé reste **sans biais** (en moyenne égal au vrai gradient). En contrepartie, sa variance augmente.

Cette étude simule l'effet de cette compression **sur une seule machine** : on quantifie le gradient avant chaque mise à jour, sans réseau ni calcul distribué.

## Question de recherche

> À partir de combien de niveaux de quantification s l'entraînement d'un petit modèle converge-t-il presque aussi bien que la descente de gradient sans compression ? Et l'arrondi aléatoire sans biais fait-il mieux qu'un arrondi déterministe au plus proche ?

## Hypothèses (à écrire et dater par toi AVANT les expériences)

- H1 : <...>
- H2 : <...>

## Méthode

1. **Quantificateur** : implémenter la quantification stochastique de QSGD (section 3 de l'article) pour un vecteur `v` et un nombre de niveaux `s`.
2. **Tests d'abord** :
   - sans biais : la moyenne de `Q(v)` sur un grand nombre de tirages s'approche de `v` ;
   - borne de variance : comparer la variance empirique à la borne du lemme 3.1 de l'article.
3. **Variante de comparaison** : arrondi déterministe au niveau le plus proche (biaisé).
4. **Entraînement** : le neurone (ou le petit réseau) de `neural-network-from-scratch/`, sur chat/chien ou `load_digits`, avec s ∈ {1, 2, 4, 8, 16} et sans quantification.
5. **Mesures** : perte et précision au fil des itérations, nombre de bits transmis par gradient (approximatif, sans le codage d'Elias de l'article : le dire dans les limites), plusieurs graines.

## Première action (30 min, sans coder)

Lis l'abstract, l'introduction et la section 3 jusqu'au lemme 3.1. Puis, sur papier, prends `v = (0,3 ; −0,8 ; 0,5)` et `s = 2` : quels sont les niveaux possibles pour chaque coordonnée, avec quelles probabilités ? Vérifie à la main que l'espérance de `Q(v)` vaut bien `v`. Ce calcul deviendra ton premier test.

## Reproduire

```bash
pip install -r ../requirements.txt
python -m pytest
# <commande pour lancer chaque expérience>
```

## Résultats

<figures et chiffres réellement obtenus, avec leur dispersion>

## Limites

Une seule machine (pas de communication réelle) ; petit modèle ; pas de codage entropique. À écrire honnêtement à la fin.

## Definition of Done

- [ ] Quantificateur testé (sans biais, variance)
- [ ] Courbes d'entraînement pour plusieurs s, plusieurs graines
- [ ] Comparaison avec l'arrondi déterministe
- [ ] README complété (résultats, limites)
