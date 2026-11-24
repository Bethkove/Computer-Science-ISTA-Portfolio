# Computer Science & AI — Research Portfolio

Portfolio de travail orienté **Machine Learning et recherche**, construit en vue d'un stage de recherche de licence (L3 Informatique, Université de Reims Champagne-Ardenne), notamment à l'ISTA.

## Objectif

Montrer, à l'échelle d'un étudiant de licence, une capacité à :

- comprendre les fondements mathématiques et algorithmiques ;
- implémenter des méthodes sans dépendre entièrement de bibliothèques haut niveau ;
- lire un article de recherche et en reproduire une idée à petite échelle ;
- poser une question précise et concevoir une expérience contrôlée ;
- analyser des résultats en distinguant observation, interprétation et conclusion ;
- documenter un travail reproductible, limites comprises.

Tous les projets tournent sur un ordinateur portable (**CPU uniquement**).

---

## Graphe du portfolio

```text
                     Neural Network from Scratch
               (descente de gradient, rétropropagation)
                                 │
                                 ▼
                    Lecture d'articles (research-notes)
                                 │
          ┌──────────────────────┼──────────────────────┐
          │                      │                      │
          ▼                      ▼                      ▼
   Smoke and Mirrors           QSGD                 KS(conf)
   (Locatello)             (Alistarh)              (Lampert)
          │                      │                      │
          ▼                      ▼                      ▼
  causal-effect-bias       quantized-sgd     classifier-shift-detection
  Le seuillage des        Combien de bits    Un test simple détecte-t-il
  prédictions biaise-t-il  faut-il pour       qu'un classifieur est hors
  un effet causal ?        apprendre ?         de ses conditions d'usage ?
          │                      │                      │
          └──────────────────────┼──────────────────────┘
                                 ▼
             Question → hypothèses → expériences → limites
                                 │
                                 ▼
                    Rapport (report/research-report.md)
```

`quantized-sgd/` réutilise directement le code de `neural-network-from-scratch/`.

## Projets

| Projet | Question | Groupe lié | Statut |
|---|---|---|---|
| [neural-network-from-scratch](neural-network-from-scratch/) | Construire et vérifier un réseau de neurones en NumPy | — (base technique) | En cours |
| [causal-effect-bias](causal-effect-bias/) | Le biais dû au seuillage change-t-il quand le traitement est déséquilibré ? | Locatello | À démarrer |
| [quantized-sgd](quantized-sgd/) | Combien de niveaux de quantification du gradient suffisent pour apprendre ? | Alistarh | À démarrer |
| [classifier-shift-detection](classifier-shift-detection/) | KS(conf) détecte-t-il bruit, rotation et classes inconnues ? | Lampert | À démarrer |

Chaque projet indique dans son README la question, la méthode, une **première action** de 30 minutes, et une Definition of Done.

## Arborescence

```text
.
├── README.md
├── ROADMAP.md
├── requirements.txt
├── .gitignore
│
├── neural-network-from-scratch/
│   ├── README.md
│   ├── neuron.py
│   ├── catdogneuron.py
│   ├── utilities.py
│   └── datasets/
│
├── causal-effect-bias/
│   └── README.md
├── quantized-sgd/
│   └── README.md
├── classifier-shift-detection/
│   └── README.md
│
├── research-notes/
│   ├── README.md
│   ├── smoke-and-mirrors.md
│   ├── qsgd.md
│   ├── ks-conf.md
│   └── causal-representation-learning.md
│
└── report/
    └── research-report.md
```

Les dossiers `src/`, `tests/`, `experiments/` et `results/` de chaque projet seront créés **au moment où ils deviennent nécessaires**. Aucun fichier vide ou placeholder n'est ajouté uniquement pour faire apparaître une arborescence.

## Installation

```bash
python -m venv .venv
# Windows : .venv\Scripts\activate    —    Linux/macOS : source .venv/bin/activate
pip install -r requirements.txt
```

## Definition of Done

Un projet est considéré comme terminé lorsqu'il possède :

- une question et des hypothèses écrites **avant** les résultats ;
- une implémentation compréhensible, avec des tests sur des cas calculables à la main ;
- des expériences répétées sur plusieurs graines ;
- des résultats sauvegardés et des figures ;
- une section « limites » honnête ;
- un README qui permet de tout reproduire.
