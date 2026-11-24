[English](README.md) | **Français**

# Causal Effect Bias

Quelle est la fiabilité d'une estimation d'effet causal quand le résultat n'est pas mesuré mais prédit par un classifieur ?

**Groupe de recherche lié :** Causal Learning and Artificial Intelligence (Francesco Locatello, ISTA)

## Contexte

Dans un essai contrôlé randomisé, l'effet moyen du traitement (ATE) s'identifie par une simple différence de moyennes entre unités traitées et unités témoins. Dans de nombreuses expériences scientifiques, cependant, le résultat est enregistré dans des observations de grande dimension (images, vidéos) et il est **prédit par un modèle d'apprentissage automatique** au lieu d'être mesuré directement.

Cadei et al. (NeurIPS 2024) montrent que cette étape peut biaiser la conclusion causale même lorsque le classifieur est précis. Deux de leurs résultats motivent cette étude :

- **Théorème 3.1 :** seuiller les probabilités prédites en étiquettes binaires biaise l'estimation de l'effet, même pour un classifieur cohérent.
- **Lemme 3.1 :** le pire biais d'un classifieur de taux d'erreur ε varie comme ε / min_t P(T = t) ; il peut donc grandir quand le traitement est déséquilibré.

Leur simulation d'illustration (exemple 1, annexe B.1) utilise un traitement équilibré.

## Question de recherche

> Comment le déséquilibre du traitement affecte-t-il le biais et la variabilité des estimations d'effet causal calculées à partir des prédictions brutes ou seuillées d'un classifieur ?

## Démarche

1. Reproduire la simulation de l'exemple 1 : un modèle causal structurel où T est un traitement binaire, X = T + W + bruit, et Y = 1[X + bruit ≥ 0] ; une régression logistique prédit Y à partir de X, et l'effet est estimé à partir des prédictions brutes et des prédictions seuillées.
2. Calculer analytiquement les valeurs, au niveau de la population, de l'effet réel et de l'effet seuillé, et les confronter à la simulation.
3. Faire varier la probabilité de traitement P(T = 1) et mesurer, sur de nombreuses graines aléatoires, à la fois l'écart moyen à l'effet réel et sa dispersion.
4. Étudier un cadre où les erreurs du classifieur ne sont pas réparties de la même façon entre les deux groupes de traitement, la situation décrite par le pire cas du lemme 3.1.

## Cadre

Python, NumPy, SciPy et scikit-learn, sur CPU. Toutes les données sont simulées.

## Référence

R. Cadei, L. Lindorfer, S. Cremer, C. Schmid, F. Locatello. *Smoke and Mirrors in Causal Downstream Tasks.* NeurIPS 2024. Code : https://github.com/CausalLearningAI/ISTAnt
