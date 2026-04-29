# **Synthèse du langage commun**
**Domaine : Circuit des demandes urgentes de dosage anti-Xa**
*Document de référence pour l'étape 4 (modélisation DDD)*

---

## **1. Vue d'ensemble du langage commun**

### **1.1. Structure et volumétrie**
Le langage commun est organisé en **5 catégories** couvrant l'ensemble du domaine métier :

| **Catégorie** | **Nombre de termes** | **Description** |
|---------------|----------------------|-----------------|
| **Clinique** | 7 | Concepts liés aux patients, traitements et contextes médicaux |
| **Biologique** | 7 | Concepts liés aux analyses, échantillons et résultats |
| **Organisationnel** | 7 | Concepts liés aux processus, acteurs et systèmes |
| **Temporel** | 5 | Concepts liés aux délais et horodatages |
| **Informationnel** | 6 | Concepts liés à la communication et documentation |

**Total : 32 termes canoniques** définis et alignés entre acteurs métier et technique.

---

## **2. Décisions terminologiques majeures et justifications**

### **2.1. Choix stratégiques**

| **Décision terminologique** | **Justification métier** | **Impact sur la modélisation** |
|-----------------------------|--------------------------|---------------------------------|
| **Anticoagulant oral direct** (vs AOD) | Évite la confusion avec les anticoagulants injectables (héparine, AVK) et clarifie le mode d'administration | Permet une distinction claire dans les prescriptions et analyses |
| **Contexte clinique** (vs contexte patient) | Inclut explicitement les éléments critiques pour l'interprétation : traitement, fonction rénale, heure de dernière prise | Essentiel pour l'interprétation des résultats par le Biologiste |
| **Prescription médicale** (vs ordonnance) | Insiste sur l'acte médical et l'inclusion des informations cliniques obligatoires | Base pour la standardisation des demandes dans le SIL |
| **Échantillon biologique** (vs prélèvement) | Couvre à la fois le matériel et l'acte, évite l'ambiguïté | Permet de documenter les exigences de conformité |
| **Conformité de l'échantillon** (vs qualité) | Met l'accent sur le respect des normes comme condition préalable | Critère de rejet formel par le Biologiste |
| **Dosage anti-Xa** (vs mesure/test) | Standard dans le domaine biologique, évite les confusions avec d'autres tests | Aligné sur les pratiques des laboratoires |
| **Résultat du dosage anti-Xa** (vs valeur) | Insiste sur l'interprétation nécessaire par le Biologiste | Intègre le processus d'analyse et d'interprétation |
| **Traçabilité** (vs suivi/historique) | Couvre l'enregistrement systématique de toutes les étapes | Essentiel pour la conformité réglementaire |
| **Délai critique** (vs délai d'urgence) | Met l'accent sur l'impact direct sur la sécurité patient | Permet de définir des seuils clairs pour les urgences |
| **Priorisation** (vs classement/tri) | Insiste sur le processus systématique et objectif | Base pour l'automatisation dans le SIL |

---

### **2.2. Alignement métier ↔ technique**

**Principes d'alignement appliqués** :
1. **Unicité** : Un seul terme métier pour chaque concept
2. **Traçabilité** : Correspondance claire entre termes métier et techniques
3. **Exhaustivité** : Tous les concepts critiques sont couverts
4. **Standardisation** : Alignement sur les pratiques des sociétés savantes (HAS, SFBC, SFAR)

**Exemples d'alignement** :
- `prescription_medicale` (métier) ↔ `prescription_medicale` (SIL)
- `contexte_clinique` (métier) ↔ `contexte_clinique` (SIL)
- `echantillon_biologique` (m