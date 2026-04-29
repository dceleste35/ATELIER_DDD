# ATELIER DDD - Processus général de la démarche DDD
<img width="1024" height="1536" alt="Processus_DDD" src="https://github.com/user-attachments/assets/e24f9027-e444-457a-98d5-9742973f1da3" />

Ce projet est un prototype de programmation d'Agents IA destiné à produire les livrables successifs d'une démarche **Domain-Driven Design**.

Le cas étudié concerne l'évolution d'un SIL pour améliorer la gestion des demandes urgentes de dosage anti-Xa chez les patients sous anticoagulants oraux directs.

Le runner est paramétrable par étape via l'option `--step`. Chaque étape s'appuie automatiquement sur les livrables des étapes précédentes.

---

## Étape 1 : Comprendre le domaine métier

### Objectif

Produire une connaissance globale du domaine, sans encore concevoir le modèle DDD détaillé, les bounded contexts, les agrégats ou l'architecture technique.

### Livrables produits

Générés dans `outputs/etape-1/` :

```text
01_reformulation_du_besoin.md
02_acteurs_du_domaine.md
03_concepts_metier_initiaux.md
04_contraintes_et_risques.md
05_vision_globale_du_domaine.md
```

Livrable principal : `05_vision_globale_du_domaine.md`.

### Exécution

```bash
python src/runner.py --step 1
```

(Équivalent à `python src/runner.py` — étape 1 par défaut.)

---

## Étape 2 : Structurer la connaissance du domaine

### Objectif

Approfondir la compréhension acquise en étape 1 en identifiant **qui agit**, **pourquoi**, **quelles décisions sont prises**, **quelles informations sont manipulées** et **quelles règles métier** encadrent le circuit. Rendre explicites les logiques implicites et repérer les conflits d'objectifs entre acteurs.

L'agent IA reçoit en contexte :
- la demande métier d'origine (`data/input/`) ;
- l'ensemble des livrables produits en étape 1 (`outputs/etape-1/`).

Aucun modèle DDD détaillé (entités, agrégats, value objects, événements) n'est encore produit — c'est le rôle de l'étape 4.

### Livrables produits

Générés dans `outputs/etape-2/` :

```text
06_cartographie_acteurs.md
07_responsabilites_acteurs.md
08_regles_metier.md
09_conflits_objectifs.md
10_synthese_etape2.md
```

Livrable principal : `10_synthese_etape2.md`.

### Exécution

```bash
python src/runner.py --step 2
```

> Pré-requis : les livrables de l'étape 1 doivent être présents dans `outputs/etape-1/`.

---

## Étape 3 : Établir le langage commun (Ubiquitous Language)


### Objectif

Construire un **langage commun partagé** par toutes les parties prenantes du projet (experts métier, cliniciens, biologistes, IDE, analystes, développeurs, décideurs) afin de supprimer les ambiguïtés, les interprétations divergentes et les traductions permanentes entre vocabulaire métier et vocabulaire technique.

Chaque concept important du domaine est nommé de manière **claire, unique et cohérente**, puis réutilisé dans les ateliers, la documentation, les user stories, les tests et le code à venir.

L'agent IA reçoit en contexte :
- la demande métier d'origine (`data/input/`) ;
- les livrables des étapes 1 et 2 (`outputs/etape-1/`, `outputs/etape-2/`).

Aucun modèle DDD détaillé (bounded contexts, agrégats, entités, value objects, événements) n'est encore produit — c'est le rôle de l'étape 4.

### Livrables produits

Générés dans `outputs/etape-3/` :

```text
11_glossaire_metier.md
12_ambiguites_resolues.md
13_alignement_metier_technique.md
14_exemples_langage_commun.md
15_synthese_langage_commun.md
```

Livrable principal : `15_synthese_langage_commun.md`.

### Exécution

```bash
python src/runner.py --step 3
```

> Pré-requis : les livrables des étapes 1 et 2 doivent être présents dans `outputs/etape-1/` et `outputs/etape-2/`.

---

## Étape 4 : Découper le domaine en sous-domaines

### Objectif

Structurer la complexité du domaine global en le **découpant en sous-domaines cohérents**, chacun regroupant un ensemble homogène de problématiques métier. Identifier leurs finalités propres, leurs règles spécifiques et leurs interactions, puis classifier chaque sous-domaine selon sa valeur stratégique :

- **Core** : cœur métier différenciant — investissement et conception sur mesure ;
- **Supporting** : support nécessaire mais non différenciant ;
- **Generic** : commodité interchangeable, candidate à des solutions du marché.

Ce découpage clarifie où se situe la valeur métier principale, oriente la priorisation des efforts de conception, l'organisation des équipes et la modularité du futur système.

L'agent IA reçoit en contexte :
- la demande métier d'origine (`data/input/`) ;
- les livrables des étapes 1, 2 et 3 (`outputs/etape-1/`, `outputs/etape-2/`, `outputs/etape-3/`).

Aucun bounded context détaillé ni modèle tactique (entités, agrégats, value objects, événements) n'est encore produit — c'est le rôle de l'étape 5 et au-delà.

### Livrables produits

Générés dans `outputs/etape-4/` :

```text
16_decoupage_sous_domaines.md
17_classification_strategique.md
18_finalites_et_regles.md
19_interactions_sous_domaines.md
20_synthese_sous_domaines.md
```

Livrable principal : `20_synthese_sous_domaines.md`.

### Exécution

```bash
python src/runner.py --step 4
```

> Pré-requis : les livrables des étapes 1, 2 et 3 doivent être présents dans `outputs/etape-1/`, `outputs/etape-2/` et `outputs/etape-3/`.

---

## Étape 5 : Délimiter les Bounded Contexts

### Objectif

Transformer le découpage en sous-domaines de l'étape 4 en **frontières explicites de responsabilité** : les Bounded Contexts. Au sein de chaque contexte, un modèle métier, un vocabulaire et des règles conservent un sens stable et non ambigu.

Pour chaque Bounded Context : périmètre, responsabilités, modèle propre, vocabulaire (issu du langage commun), règles internes, variations sémantiques. Construction de la **Context Map** qualifiant chaque relation inter-contextes selon les patterns DDD canoniques :

- **Partnership** — coopération étroite et synchronisée ;
- **Shared Kernel** — modèle partagé minimal ;
- **Customer / Supplier** — dépendance fournisseur asymétrique ;
- **Conformist** — adhésion forcée au modèle amont ;
- **Anticorruption Layer (ACL)** — couche de traduction protectrice ;
- **Open Host Service (OHS)** + **Published Language (PL)** — interface publiée stable ;
- **Separate Ways** — pas d'intégration ;
- **Big Ball of Mud** — zone non maîtrisée à isoler.

L'agent IA reçoit en contexte :
- la demande métier d'origine (`data/input/`) ;
- les livrables des étapes 1, 2, 3 et 4.

Aucun modèle tactique (entités, agrégats, value objects, événements détaillés) n'est encore produit — c'est le rôle de l'étape 6.

### Livrables produits

Générés dans `outputs/etape-5/` :

```text
21_identification_bounded_contexts.md
22_frontieres_et_responsabilites.md
23_context_map_relations.md
24_contrats_integration.md
25_synthese_context_map.md       # schéma Mermaid uniquement
```

Livrable principal : `25_synthese_context_map.md` (Context Map sous forme de diagramme Mermaid).

### Exécution

```bash
python src/runner.py --step 5
```

> Pré-requis : les livrables des étapes 1, 2, 3 et 4 doivent être présents dans leurs dossiers `outputs/etape-N/`.

---

## Les inputs

Les inputs (demandes utilisateurs) sont à déposer dans le répertoire `data/input/`. Dans cet exemple, vous trouverez la demande d'évolution d'un SI émise par un biologiste.

Extensions acceptées : `.md`, `.txt`, `.log`, `.csv`.

---

## Installation

### 1) Lancer le projet dans Codespaces

- Faites un Fork de ce repository GitHub (bouton **Fork** en haut à droite).
- Créez, dans votre repository, le secret Codespaces suivant :
  **`MISTRAL_API_KEY`** qui contiendra l'API key de votre compte Mistral.
- Cliquez ensuite sur **[Code]** → **Create codespace on main**.
- Dans le terminal du Codespace :

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2) Lancer le projet en local (macOS / Linux)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Crée un fichier `.env` à la racine. Le projet utilise **Mistral** via [LiteLLM](https://docs.litellm.ai/) :

```
MISTRAL_API_KEY=...
LLM_MODEL=mistral/mistral-small-latest   # optionnel — défaut : mistral-small-latest
```

Le modèle peut être changé pour `mistral/mistral-large-latest`, `mistral/mistral-tiny`, etc. Voir [Mistral models](https://docs.mistral.ai/getting-started/models/models_overview/).

> **Important** : Mistral n'est pas un provider natif de CrewAI. Le package `litellm` est requis pour l'intégration et est inclus dans `requirements.txt`. Si tu rencontres l'erreur *"Unable to initialize LLM ... LiteLLM fallback package is not installed"*, installe-le manuellement :
>
> ```bash
> pip install litellm
> ```

---

## Exécution complète de la chaîne

```bash
# Étape 1 : compréhension du domaine
python src/runner.py --step 1

# Étape 2 : structuration (lit auto les livrables étape 1)
python src/runner.py --step 2

# Étape 3 : langage commun (lit auto les livrables étapes 1 + 2)
python src/runner.py --step 3

# Étape 4 : découpage en sous-domaines (lit auto les livrables étapes 1 + 2 + 3)
python src/runner.py --step 4

# Étape 5 : Bounded Contexts + Context Map (lit auto les livrables étapes 1 à 4)
python src/runner.py --step 5
```

Variable d'environnement équivalente : `DDD_STEP=5 python src/runner.py`.

---

## Structure du projet

```text
ATELIER_DDD/
├── config/
│   ├── agents_step1.yaml    # agent compréhension
│   ├── tasks_step1.yaml     # 5 tâches étape 1
│   ├── agents_step2.yaml    # agent structuration
│   ├── tasks_step2.yaml     # 5 tâches étape 2
│   ├── agents_step3.yaml    # agent langage commun
│   ├── tasks_step3.yaml     # 5 tâches étape 3
│   ├── agents_step4.yaml    # agent stratège sous-domaines
│   ├── tasks_step4.yaml     # 5 tâches étape 4
│   ├── agents_step5.yaml    # agent designer Bounded Contexts
│   └── tasks_step5.yaml     # 5 tâches étape 5
├── data/
│   └── input/               # demandes métier (entrées)
├── outputs/
│   ├── etape-1/             # livrables étape 1
│   ├── etape-2/             # livrables étape 2
│   ├── etape-3/             # livrables étape 3
│   ├── etape-4/             # livrables étape 4
│   └── etape-5/             # livrables étape 5
├── src/
│   └── runner.py            # orchestrateur multi-étapes
├── .env                     # secrets locaux (non versionné)
├── requirements.txt
└── README.md
```

---

## Remarque

Ce projet couvre actuellement les étapes **1**, **2**, **3**, **4** et **5** de la méthode DDD. Les étapes suivantes — modélisation tactique (agrégats, entités, value objects, événements de domaine, services, repositories), cas d'usage et architecture applicative — ne sont pas encore incluses.
