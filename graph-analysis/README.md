# Graph Analysis

## Objectif

Construire une petite base algorithmique permettant de représenter et analyser des graphes.

Le projet doit privilégier les implémentations compréhensibles et l'analyse de complexité.

## Ordre d'implémentation

### 1. Structure
Créer une classe Graph avec une représentation par listes d'adjacence.

Décider explicitement :
- graphe orienté ou non orienté ;
- graphe pondéré ou non pondéré ;
- représentation des sommets.

### 2. Parcours
Implémenter :
- BFS ;
- DFS.

Pour chacun, documenter la complexité.

### 3. Chemins
Implémenter les shortest paths adaptés au modèle de graphe choisi.

### 4. Analyse
Implémenter :
- connected components ;
- degree centrality ;
- PageRank.

### 5. Expériences
Construire plusieurs graphes :
- petit graphe manuel ;
- graphe aléatoire ;
- graphe avec structure claire.

Observer comment les algorithmes se comportent selon la structure.

### 6. Visualisation
Produire des visualisations utiles pour :
- les graphes ;
- les chemins ;
- les scores de centralité ;
- PageRank.

## Structure cible

```text
graph-analysis/
├── README.md
├── src/
├── tests/
├── experiments/
└── results/
```

Créer chaque sous-dossier uniquement lorsqu'il reçoit son premier contenu utile.

## Definition of Done

- [ ] Graph fonctionnel
- [ ] BFS testé
- [ ] DFS testé
- [ ] Shortest paths testé
- [ ] Connected components
- [ ] Degree centrality
- [ ] PageRank
- [ ] Tests
- [ ] Analyse de complexité
- [ ] Visualisations
