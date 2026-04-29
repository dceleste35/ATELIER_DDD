# **Synthèse du langage commun**
**Domaine : Circuit des demandes urgentes de dosage anti-Xa**
*Document de référence pour l'étape 4 (modélisation DDD)*

---

## **1. Vue d'ensemble du langage commun**

### **1.1. Structure et volumétrie**
Ce document synthétise **50 termes canoniques** organisés en **5 catégories** :

| **Catégorie** | **Nombre de termes** | **Acteurs principaux** |
|---------------|---------------------|------------------------|
| **Concepts cliniques** | 5 | Médecins prescripteurs, Biologiste |
| **Concepts biologiques** | 5 | Personnel infirmier, Techniciens de laboratoire, Biologiste |
| **Concepts organisationnels** | 10 | Tous les acteurs |
| **Concepts temporels** | 4 | SIL, Médecins prescripteurs, Biologiste |
| **Concepts informationnels** | 7 | SIL, Biologiste, Médecins prescripteurs |

**Total** : 31 termes canoniques + 19 termes dérivés (ex : `urgence_vitale` dérivé de `urgence_clinique`).

---

### **1.2. Périmètre couvert**
Le langage commun couvre l'intégralité du **parcours métier** identifié dans les étapes 1 et 2 :

1. **Prescription médicale** → **Acte de prélèvement** → **Transport** → **Analyse** → **Transmission des résultats**
2. **Gestion des urgences** (hiérarchisation en `urgence_vitale`/`urgence_standard`)
3. **Contrôle qualité** (conformité des **échantillons biologiques**)
4. **Traçabilité** (enregistrement systématique de chaque étape)
5. **Sécurité** (protection des données, alertes automatiques)

---

### **1.3. Acteurs et interactions clés**
| **Acteur** | **Rôle dans le langage commun** | **Termes canoniques associés** |
|------------|----------------------------------|--------------------------------|
| **Médecin prescripteur** | Initiateur des **prescriptions médicales** | `prescription_medicale`, `urgence_clinique`, `information_clinique` |
| **Personnel infirmier** | Réalise l’**acte de prélèvement** et vérifie la conformité | `acte_prelevement`, `tube_prelevement`, `echantillon_biologique` |
| **Technicien de laboratoire** | Priorise les demandes et réalise les analyses | `priorisation`, `dosage_anti_xa`, `rejet_echantillon` |
| **Biologiste** | Interprète les résultats et valide les échantillons | `interpretation_resultat`, `contexte_clinique`, `traçabilité` |
| **SIL** | Centralise les données et automatise les processus | `circuit_informatise`, `delai_reponse`, `alerte`, `identifiant_unique` |

---

## **2. Décisions terminologiques majeures et justifications**

### **2.1. Hiérarchie des urgences**
| **Décision** | **Justification métier** | **Impact sur la modélisation** |
|--------------|--------------------------|--------------------------------|
| **Distinction entre `urgence_clinique` et `urgence_vitale`** | - Aligné sur les pratiques médicales (classification des urgences) <br> - Permet une **priorisation automatique** dans le SIL <br> - Justifie des **délais de réponse** différents (<1h vs <30 min) | Création d'un **enum** `NiveauUrgence` avec valeurs : <br> - `urgence_vitale` <br> - `urgence_standard` |
| **Suppression de "Demande urgente"** | - Trop générique et source de confusion <br> - Remplacé par `urgence_clinique` (général) et `urgence_vitale` (spécifique) | Utilisation exclusive de `urgence_clinique` pour les cas non vitaux |

---

### **2.2. Clarification des termes liés aux échantillons**
| **Décision** | **Justification métier** | **Impact sur la modélisation** |
|--------------|--------------------------|--------------------------------|
| **Distinction entre `echantillon_biologique`, `tube_prelevement` et `acte_prelevement`** | - Évite les ambiguïtés entre le **matériel** (échantillon), le **contenant** (tube) et l’**action** (prélèvement) <br> - Aligné sur les normes ISO 15189 et CLSI GP41 | Modélisation de 3 entités distinctes : <br> - `EchantillonBiologique` (matériel) <br> - `TubePrelevement` (contenant) <br> - `ActePrelevement` (action) |
| **Suppression de "Prélèvement"** (sauf pour l'action) | - Trop ambigu (peut désigner l'acte ou le matériel) <br> - Remplacé par `echantillon_biologique` (matériel) | Utilisation de `echantillon_biologique` pour désigner le matériel prélevé |

---

### **2.3. Standardisation des termes liés à la traçabilité**
| **Décision** | **Justification métier** | **Impact sur la modélisation** |
|--------------|--------------------------|