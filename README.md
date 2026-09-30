# Computer Science & AI — Research Portfolio

Portfolio de travail orienté **Computer Science, Artificial Intelligence et recherche**, construit en vue de candidatures à des stages de recherche, notamment à l'ISTA.

## Objectif

Construire progressivement un portfolio qui montre non seulement des projets fonctionnels, mais surtout une capacité à :

- comprendre les fondements mathématiques et algorithmiques ;
- implémenter des méthodes sans dépendre entièrement de bibliothèques haut niveau ;
- concevoir des expériences contrôlées ;
- analyser des résultats ;
- tester et vérifier ses implémentations ;
- lire et discuter des travaux de recherche ;
- produire une documentation reproductible.

---

## Graphe du portfolio

```text
                         COMPUTER SCIENCE / AI
                                  │
             ┌────────────────────┼────────────────────┐
             │                    │                    │
             ▼                    ▼                    ▼
      Neural Network       Evolutionary          Graph Analysis
       from Scratch         Optimization          & Algorithms
             │                    │                    │
             │                    │                    │
             └────────────────────┼────────────────────┘
                                  │
                                  ▼
                       Experimental Methodology
                                  │
                                  ▼
                         Research Paper Reading
                                  │
             ┌────────────────────┼────────────────────┐
             │                    │                    │
             ▼                    ▼                    ▼
            QSGD                KS(conf)       Causal Representation
             │                    │                    │
             └────────────────────┼────────────────────┘
                                  │
                         ┌────────┴────────┐
                         │                 │
                         ▼                 ▼
                     T1-PILOT     Spurious Correlations
                         │                 │
                         └────────┬────────┘
                                  ▼
                         Research Question
                                  │
                                  ▼
                         Experimental Report
                                  │
                                  ▼
                    Tests + Reproducibility
                                  │
                                  ▼
                         FINAL PORTFOLIO
```

## Parcours de travail

1. **Neural Network from Scratch**
   - construire les briques fondamentales ;
   - comprendre forward/backpropagation ;
   - vérifier les gradients ;
   - entraîner sur un jeu de données réel ;
   - réaliser des expériences contrôlées.

2. **Evolutionary Optimization**
   - établir un baseline ;
   - implémenter une recherche locale ;
   - implémenter un algorithme génétique ;
   - comparer les méthodes expérimentalement.

3. **Graph Analysis**
   - implémenter les structures de graphe ;
   - explorer BFS/DFS et les chemins ;
   - implémenter plusieurs mesures d'analyse ;
   - comparer les comportements sur différents graphes.

4. **Research Notes**
   - lire les cinq articles sélectionnés ;
   - extraire question, méthode, résultats et limites ;
   - relier les idées des articles aux projets.

5. **Research Report**
   - formuler une question ;
   - définir une méthodologie ;
   - présenter les expériences ;
   - analyser les résultats ;
   - discuter les limites et pistes futures.

---

## Arborescence

```text
.
├── README.md
├── ROADMAP.md
│
├── neural-network-from-scratch/
│   └── README.md
│
├── evolutionary-optimization/
│   └── README.md
│
├── graph-analysis/
│   └── README.md
│
├── research-notes/
│   ├── README.md
│   ├── qsgd.md
│   ├── ks-conf.md
│   ├── causal-representation-learning.md
│   ├── t1-pilot.md
│   └── spurious-correlations.md
│
└── report/
    └── research-report.md
```

Les dossiers `src/`, `tests/`, `experiments/` et `results/` seront créés **au moment où ils deviennent nécessaires**. Aucun fichier vide ou placeholder n'est ajouté uniquement pour faire apparaître une arborescence.

## Definition of Done

Le portfolio sera considéré comme prêt lorsque chaque projet possède :

- une implémentation compréhensible ;
- des tests pertinents ;
- des expériences reproductibles ;
- des résultats sauvegardés ;
- une analyse des résultats ;
- une documentation claire.

Et lorsque le rapport final relie les projets et les lectures de recherche en une démarche cohérente.
