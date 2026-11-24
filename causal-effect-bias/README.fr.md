[English](README.md) | **Français**

# Causal Effect Bias — quand un classifieur fausse un effet causal

**Groupe lié :** Causal Learning and Artificial Intelligence (Francesco Locatello, ISTA)
**Article de départ :** Cadei, Lindorfer, Cremer, Schmid, Locatello, *Smoke and Mirrors in Causal Downstream Tasks*, NeurIPS 2024 — code : https://github.com/CausalLearningAI/ISTAnt
**Calcul :** CPU uniquement (NumPy, scikit-learn). Chaque simulation prend quelques secondes.

## Contexte

Dans un essai randomisé, on veut estimer l'effet moyen d'un traitement (ATE). Quand le résultat n'est pas mesuré directement mais **prédit par un modèle**, les erreurs du modèle peuvent biaiser l'effet estimé, même avec une bonne précision.

L'article montre deux choses que cette étude reprend à petite échelle :

- **Théorème 3.1** : seuiller les probabilités prédites (les arrondir à 0 ou 1) biaise l'estimation de l'effet.
- **Lemme 3.1** : le pire biais possible grandit quand le traitement est **déséquilibré** (borne en ε / min P(T=t)).

Or l'exemple 1 de l'article utilise un traitement équilibré (p_T = 0,5).

## Question de recherche

> Le biais dû au seuillage des prédictions change-t-il quand le traitement devient déséquilibré (P(T=1) de 0,5 à 0,1) ?

## Hypothèses (à écrire et dater par toi AVANT les expériences)

- H1 : <...>
- H2 : <...>

## Méthode

### Étape 1 — Reproduire l'exemple 1 (annexe B.1)

Modèle causal simulé :

- T ~ Bernoulli(p_T), W ~ N(0, 1), bruit n_X ~ N(0, 1), bruit n_Y ~ N(0, σ²_Y)
- X = T + W + n_X
- Y = 1 si X + n_Y ≥ 0, sinon 0

Puis : régression logistique de Y sur X, prédictions brutes `f(X)` et seuillées `1[f(X) ≥ 0,5]`, et différence associationnelle empirique (EAD) calculée avec chacune.

Objectif : reproduire la **figure 3** de l'article (EAD en fonction de n, 50 graines par n, p_T = 0,5, σ²_Y = 1).

### Étape 2 — Faire varier P(T=1)

Mêmes simulations pour p_T ∈ {0,5 ; 0,3 ; 0,2 ; 0,1}. Mesurer l'écart entre l'EAD seuillée et la vraie AD, avec sa dispersion sur les graines.

Vraie AD : calculable analytiquement (annexe B.1, équation 32) ou par une simulation de très grande taille. Indique laquelle tu utilises.

### Étape 3 (si le temps le permet)

Faire varier σ²_Y : l'article affirme que le biais augmente avec la variance du bruit. Le vérifier.

## Première action (30 min, sans coder)

Relis l'annexe B.1. Sur papier, calcule `AD_{Y,T}` pour p_T = 0,5 et σ²_Y = 1 avec les équations 27-28 et 32, puis la valeur seuillée (équation 33). Retrouves-tu un écart d'environ 0,042 (équation 37) ? Ce calcul deviendra ton premier test.

## Reproduire

```bash
pip install -r ../requirements.txt
python -m pytest
# <commande pour lancer chaque expérience>
```

Graines : <liste>. Matériel : <ton portable>.

## Résultats

<figures et chiffres réellement obtenus, avec leur dispersion>

## Ce que les résultats soutiennent / ne soutiennent pas

## Limites

Données entièrement simulées et unidimensionnelles ; modèle bien spécifié (la régression logistique est proche du vrai mécanisme). À écrire honnêtement à la fin.

## Definition of Done

- [ ] Hypothèses écrites et datées avant les résultats
- [ ] Test : la valeur analytique de l'équation 37 est retrouvée
- [ ] Figure 3 reproduite
- [ ] Étude du déséquilibre sur plusieurs graines
- [ ] README complété (résultats, limites)
