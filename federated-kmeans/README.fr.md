[English](README.md) | **Français**

# Federated k-Means — regrouper des données privées réparties sur plusieurs appareils

**Groupe lié :** Machine Learning and Computer Vision (Christoph Lampert, ISTA)
**Article de départ :** Scott, Lampert, Saulpic, *Differentially Private Federated k-Means Clustering with Server-Side Data*, ICML 2025 — https://arxiv.org/abs/2506.05408
**Calcul :** CPU uniquement (NumPy, scikit-learn pour générer les données). Chaque run prend quelques secondes.

## Contexte

Les données sont souvent réparties sur de nombreux appareils (téléphones, hôpitaux) et ne peuvent pas être centralisées pour des raisons de confidentialité. Dans un k-means **fédéré**, chaque client n'envoie au serveur que des statistiques agrégées (sommes et effectifs par cluster), et le serveur met à jour les centres. Pour protéger la confidentialité, on ajoute du **bruit** à ces agrégats. L'article souligne qu'avec ce bruit, la partie difficile est **l'initialisation** des centres, et utilise pour cela un petit jeu de données détenu par le serveur (éventuellement différent des données des clients).

## Question de recherche

> Dans un k-means fédéré où l'on ajoute un bruit gaussien aux statistiques agrégées, à partir de quel niveau de bruit une initialisation à partir d'un petit jeu de données du serveur bat-elle nettement une initialisation aléatoire, et que se passe-t-il quand les données du serveur ne ressemblent pas à celles des clients ?

## Hypothèses (à écrire et dater par toi AVANT les expériences)

- H1 : <...>
- H2 : <...>

## Méthode

1. **Données :** un mélange de gaussiennes à k clusters (`sklearn.datasets.make_blobs`), réparti entre une dizaine de clients de façon **non IID** (chaque client voit surtout quelques clusters).
2. **Itération de Lloyd fédérée :** chaque client calcule, pour ses propres points, les sommes et effectifs par cluster ; le serveur ajoute un bruit gaussien d'échelle σ aux totaux, puis recalcule les centres.
3. **Initialisations :**
   - aléatoire ;
   - k-means++ sur un petit jeu de données du serveur tiré de la même distribution ;
   - la même, avec des données du serveur tirées d'une distribution **décalée** (hors distribution).
4. **Grille :** plusieurs niveaux de bruit σ, plusieurs graines.
5. **Mesures :** coût du k-means sur toutes les données des clients ; proportion de vrais clusters retrouvés.
6. Comparer ensuite avec l'initialisation réellement proposée dans l'article, une fois que tu l'auras lu.

**Important :** sauf si tu implémentes le calcul de confidentialité de l'article, cette étude ne donne **aucune garantie formelle de confidentialité** (ε, δ). Écris-le dans les limites : ici, σ est un réglage de bruit, pas un niveau de confidentialité.

## Première action (30 min, sans coder)

Lis le résumé, l'introduction et la vue d'ensemble de l'algorithme. Puis, sur papier : deux clients en 1D, deux centres. Le client A possède les points {0, 1, 2}, le client B possède {10, 11}. En partant des centres 1 et 9, fais **une** étape de Lloyd fédérée à la main (sommes, effectifs, nouveaux centres). Ajoute ensuite +2 de bruit à l'effectif du second cluster : de combien son centre se déplace-t-il ? Qu'est-ce que cela t'apprend sur les petits clusters bruités ? Ce calcul deviendra ton premier test.

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

Données synthétiques ; bruit sans calcul formel de confidentialité ; clients simulés sur une seule machine. À écrire honnêtement à la fin.

## Definition of Done

- [ ] Hypothèses écrites et datées avant les résultats
- [ ] Test : l'étape de Lloyd calculée à la main est retrouvée par le code
- [ ] Coût et clusters retrouvés en fonction de σ, pour chaque initialisation, sur plusieurs graines
- [ ] Cas des données du serveur hors distribution
- [ ] README complété (résultats, limites)
