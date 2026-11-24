[English](README.md) | **Français**

# Federated k-Means

Regrouper des données réparties entre de nombreux clients qui ne peuvent pas partager leurs données brutes, quand un bruit est ajouté pour protéger la confidentialité.

**Groupe de recherche lié :** Machine Learning and Computer Vision (Christoph Lampert, ISTA)

## Contexte

Les données sont souvent réparties entre de nombreux appareils ou établissements et ne peuvent pas être centralisées. Dans un k-means **fédéré**, chaque client n'envoie au serveur que des statistiques agrégées (sommes et effectifs par cluster), et le serveur met à jour les centres des clusters. Pour protéger la confidentialité, un bruit est ajouté à ces agrégats, comme dans les algorithmes à confidentialité différentielle.

Scott, Lampert et Saulpic (ICML 2025) soulignent que, dans ce cadre, **l'initialisation des centres** est la partie difficile, et proposent d'utiliser un petit jeu de données détenu par le serveur, éventuellement tiré d'une distribution différente de celle des clients.

## Question de recherche

> Avec un bruit ajouté aux statistiques agrégées, quand une initialisation à partir d'un petit jeu de données du serveur permet-elle au k-means fédéré de réussir là où une initialisation aléatoire échoue, et comment cela change-t-il quand les données du serveur ne ressemblent pas à celles des clients ?

## Démarche

1. Implémenter le k-means (algorithme de Lloyd) et sa version fédérée, dans laquelle les clients envoient les sommes et effectifs par cluster, et le serveur ajoute un bruit gaussien aux totaux.
2. Simuler des clients dont les données, tirées d'un mélange de gaussiennes, ne sont pas identiquement distribuées.
3. Comparer plusieurs initialisations : aléatoire, k-means++ sur des données du serveur de même distribution, et k-means++ sur des données du serveur décalées (hors distribution).
4. Mesurer le coût du clustering et la proportion de vrais clusters retrouvés, en fonction du niveau de bruit, sur de nombreuses graines aléatoires.

## Périmètre

Le niveau de bruit est étudié comme un paramètre. Les garanties formelles de confidentialité (ε, δ) demandent le calcul de confidentialité de l'article original, qui sort du périmètre de cette étude sauf mention contraire dans les résultats.

## Cadre

Python et NumPy (scikit-learn seulement pour générer les données et obtenir des résultats de référence), sur CPU. Toutes les données sont simulées.

## Référence

J. Scott, C. H. Lampert, D. Saulpic. *Differentially Private Federated k-Means Clustering with Server-Side Data.* ICML 2025. https://arxiv.org/abs/2506.05408
