# Evolutionary Optimization

## Objectif

Étudier expérimentalement plusieurs méthodes de résolution du **Traveling Salesman Problem (TSP)**.

L'intérêt du projet est de comparer des stratégies ayant des mécanismes différents plutôt que de chercher uniquement une solution.

## Ordre d'implémentation

### 1. Problème
- générer des villes ;
- calculer les distances ;
- représenter une tournée ;
- définir la fonction objectif.

### 2. Baseline
Implémenter une stratégie gloutonne.

Elle servira de référence pour les méthodes plus avancées.

### 3. Simulated Annealing
Implémenter :
- voisinage ;
- température ;
- refroidissement ;
- critère d'acceptation.

### 4. Genetic Algorithm
Implémenter :
- population ;
- fitness ;
- sélection ;
- crossover ;
- mutation ;
- remplacement.

### 5. Expériences
Comparer les méthodes sur :
- 10 villes ;
- 25 villes ;
- 50 villes ;
- 100 villes.

Mesurer :
- distance finale ;
- temps d'exécution ;
- convergence ;
- variabilité entre plusieurs runs.

### 6. Analyse
Étudier notamment le compromis :
- qualité de solution ;
- temps ;
- stabilité ;
- sensibilité aux paramètres.

## Structure cible

```text
evolutionary-optimization/
├── README.md
├── src/
├── tests/
├── experiments/
└── results/
```

Créer chaque sous-dossier uniquement lorsqu'il reçoit son premier contenu utile.

## Definition of Done

- [ ] TSP fonctionnel
- [ ] Baseline fonctionnel
- [ ] Simulated annealing fonctionnel
- [ ] Genetic algorithm fonctionnel
- [ ] Protocole expérimental défini
- [ ] Plusieurs runs réalisés
- [ ] Résultats comparables
- [ ] Analyse documentée
