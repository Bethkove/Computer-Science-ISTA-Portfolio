# Classifier Shift Detection — mon classifieur est-il hors de ses conditions d'usage ?

**Groupe lié :** Machine Learning and Computer Vision (Christoph Lampert, ISTA)
**Article de départ :** Sun & Lampert, *KS(conf): A Light-Weight Test if a Multiclass Classifier Operates Outside of Its Specifications*, IJCV 2020 — https://arxiv.org/abs/1804.04171

**Calcul :** CPU uniquement (scikit-learn, SciPy). Chaque expérience prend quelques secondes.

## Contexte

Un classifieur entraîné sur certaines données peut être utilisé plus tard sur des données différentes (images bruitées, tournées, classes jamais vues) sans que personne ne s'en rende compte. KS(conf) propose un test statistique simple : comparer la **distribution des scores de confiance** du classifieur sur les nouvelles données à celle mesurée sur des données de validation, avec un **test de Kolmogorov-Smirnov**.

## Question de recherche

> Sur un petit classifieur entraîné sur `load_digits`, KS(conf) détecte-t-il différents types de changements (bruit, rotation, classes inconnues), et combien d'échantillons lui faut-il pour les détecter de façon fiable ?

## Hypothèses (à écrire et dater par toi AVANT les expériences)

- H1 : <...>
- H2 : <...>

## Méthode

1. Entraîner un classifieur probabiliste (`LogisticRegression` ou `MLPClassifier`) sur une partie de `sklearn.datasets.load_digits`. Pour la variante « classes inconnues », l'entraîner sur les chiffres 0 à 7 seulement.
2. Calculer sa confiance maximale (`max(predict_proba)`) sur un jeu de validation propre.
3. Construire des lots de test : propres, bruités (plusieurs niveaux), tournés, ou contenant les chiffres 8 et 9.
4. Comparer chaque lot à la validation avec `scipy.stats.ks_2samp` et un seuil de significativité fixé à l'avance.
5. Mesurer, pour chaque type de changement et chaque taille de lot (10, 25, 50, 100, 200) :
   - le taux de détection (lots modifiés) ;
   - le taux de fausses alertes (lots propres), qui doit rester proche du seuil choisi.

Répéter sur plusieurs tirages aléatoires.

## Première action (30 min, sans coder)

Lis l'abstract, l'introduction et la section qui décrit le test. Puis explique en 5 lignes, avec tes mots : que compare exactement le test, et pourquoi n'a-t-il pas besoin des vraies étiquettes des nouvelles données ? Vérifie ensuite sur papier ce que mesure la statistique de Kolmogorov-Smirnov (écart maximal entre deux fonctions de répartition empiriques).

## Reproduire

```bash
pip install -r ../requirements.txt
python -m pytest
# <commande pour lancer chaque expérience>
```

## Résultats

<figures et chiffres réellement obtenus, avec leur dispersion>

## Limites

Images 8×8 très simples ; un seul type de classifieur ; changements simulés. À écrire honnêtement à la fin.

## Definition of Done

- [ ] Taux de fausses alertes vérifié sur des lots propres
- [ ] Taux de détection pour au moins trois types de changement
- [ ] Courbe détection / taille de lot, plusieurs tirages
- [ ] README complété (résultats, limites)
