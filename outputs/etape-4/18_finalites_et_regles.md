# **Finalités et règles par sous-domaine**
**Domaine : Circuit des demandes urgentes de dosage anti-Xa**

---

## **1. Sous-domaine : Prescription Médicale**
**Nom canonique** : `prescription_medicale`

### **Finalité métier**
Capturer et valider les demandes de dosage anti-Xa en intégrant les **informations cliniques** essentielles pour une interprétation correcte des résultats, tout en garantissant leur priorisation automatique et leur traçabilité.

---

### **Invariants à respecter en permanence**
1. **Existence obligatoire d'une prescription médicale** avant tout prélèvement ou analyse.
2. **Traçabilité intégrale** : toute prescription doit être horodatée et associée à un identifiant unique.
3. **Respect des règles de complétude** : les informations cliniques obligatoires doivent être systématiquement collectées.
4. **Classification automatique** : toute prescription doit être classée en **urgence clinique** ou **urgence vitale** selon des critères prédéfinis.

---

### **Règles métier internes**
| **Règle** | **Source** | **Détail** | **Responsable** |
|-----------|------------|-------------|-----------------|
| **Règle de complétude** | Étape 2 : 08_regles_metier.md | La **prescription médicale** doit inclure obligatoirement : <br> - Nom du patient <br> - Service demandeur <br> - Type d'anticoagulant oral direct (ex : apixaban, rivaroxaban) <br> - Dose et heure de la dernière prise <br> - Fonction rénale (DFG) <br> - Motif de la demande | Médecin prescripteur |
| **Règle de classification** | Étape 2 : 08_regles_metier.md | Le SIL doit classer automatiquement la demande en : <br> - **Urgence vitale** (ex : hémorragie intracrânienne, choc hémorragique) → délai de réponse < 30 min <br> - **Urgence standard** (ex : ajustement thérapeutique) → délai de réponse < 1h | SIL |
| **Règle de génération d'alerte** | Étape 2 : 08_regles_metier.md | Le SIL doit générer une **alerte** si des champs obligatoires sont manquants ou incohérents. | SIL |
| **Règle de validation clinique** | Étape 2 : 07_responsabilites_acteurs.md | Le biologiste peut valider ou rejeter une prescription si les informations cliniques sont manifestement erronées ou incomplètes. | Biologiste |

---

### **Règles partagées avec d'autres sous-domaines**
| **Règle** | **Sous-domaine concerné** | **Détail** |
|-----------|----------------------------|------------|
| **Identifiant unique** | Tous les sous-domaines | Chaque **prescription médicale** doit être associée à un **identifiant unique** qui sera utilisé pour tracer toutes les étapes du circuit. | Traçabilité et Sécurité |
| **Niveau d'urgence** | Gestion des Urgences | Le **niveau d'urgence** attribué à la prescription détermine la priorité de traitement dans le sous-domaine **Gestion des Urgences**. | Gestion des Urgences |
| **Heure de la dernière prise** | Prélèvement et Conformité | L'heure de la dernière prise d'anticoagulant est utilisée pour vérifier la conformité de l'échantillon (délai de transport maximal). | Prélèvement et Conformité |

---
### **Acteurs responsables au sein du sous-domaine**
| **Acteur** | **Rôle** | **Responsabilités spécifiques** |
|------------|----------|----------------------------------|
| **Médecin prescripteur** | Initiateur | - Saisir une **prescription médicale** complète et précise <br> - Classer manuellement l'urgence si le système ne le fait pas automatiquement <br> - Mettre à jour la prescription en cas de nouvelles informations cliniques |
| **SIL** | Orchestrateur | - Valider la complétude des **informations cliniques** <br> - Classer automatiquement la demande en **urgence clinique** ou **urgence vitale** <br> - Générer des **alertes** en cas de champs manquants <br> - Assigner un **identifiant unique** à chaque prescription |
| **Biologiste** | Superviseur | - Valider ou rejeter une prescription si les informations sont manifestement erronées <br> - Contacter le médecin prescripteur en cas d'informations manquantes ou incohérentes |

---
### **Indicateurs de succès métier**
| **Indicateur** | **Cible** | **Source** |
|----------------|-----------|------------|
| Taux de prescriptions complètes | ≥ 95% | Étape 2 : 08_regles_metier.md |
| Délai moyen de classification des urgences | < 2 min | Hypothèse métier |
| Nombre d'alertes générées pour prescriptions incomplètes | < 5% des prescriptions | Étape 2 : 08