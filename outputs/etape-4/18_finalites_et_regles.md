# **Finalités et règles par sous-domaine**
**Domaine : Circuit des demandes urgentes de dosage anti-Xa**
*Document de référence pour l'étape 4 (Strategic Design)*

---

## **1. Sous-domaine : Prescription Médicale**

### **1.1. Finalité métier**
Permettre aux **médecins prescripteurs** de saisir, valider et prioriser de manière sécurisée et traçable les **prescriptions médicales** pour les **dosages anti-Xa**, en intégrant systématiquement les **informations cliniques** essentielles (anticoagulant, heure de la dernière prise, fonction rénale) et en classant automatiquement le **niveau d'urgence** (urgence vitale / urgence standard) pour garantir une prise en charge optimale des patients sous anticoagulants oraux directs.

---

### **1.2. Invariants à respecter en permanence**
| **Invariant** | **Description** | **Source** |
|---------------|-----------------|------------|
| **Prescription obligatoire** | Toute demande de **dosage anti-Xa** doit être précédée d'une **prescription médicale** valide et complète. | Étape 2 : 08_regles_metier.md (Enchaînement obligatoire) |
| **Intégrité des informations cliniques** | Les **informations cliniques** (anticoagulant, dose, heure de la dernière prise, DFG) doivent être complètes et cohérentes avant validation. | Étape 2 : 08_regles_metier.md (Validation des informations cliniques) |
| **Identifiant unique** | Chaque **prescription médicale** doit être associée à un **identifiant unique** traçable tout au long du circuit. | Étape 2 : 08_regles_metier.md (Documentation des étapes) |
| **Niveau d'urgence déterminé** | Le **niveau d'urgence** (urgence vitale / urgence standard) doit être déterminé dès la saisie et ne peut être modifié manuellement après validation initiale. | Étape 2 : 08_regles_metier.md (Règles de priorité) |

---

### **1.3. Règles métier internes**
| **Règle** | **Description** | **Source** | **Conséquence en cas de non-respect** |
|-----------|-----------------|------------|----------------------------------------|
| **Champs obligatoires** | Les champs suivants sont obligatoires : nom du patient, service demandeur, type d'anticoagulant oral direct, dose, heure de la dernière prise, DFG, motif de la demande. | Étape 2 : 08_regles_metier.md (Validation des informations cliniques) | Génération d'une **alerte** et blocage de la validation. |
| **Format des données** | L'heure de la dernière prise doit être au format HH:MM, le DFG en mL/min, et le type d'anticoagulant doit être sélectionné dans une liste prédéfinie. | Étape 2 : 08_regles_metier.md (Validation des informations cliniques) | Erreur de format → **alerte** et demande de correction. |
| **Classification automatique** | Le **niveau d'urgence** est déterminé automatiquement en fonction du motif (ex : "hémorragie" → urgence vitale, "ajustement thérapeutique" → urgence standard). | Étape 2 : 08_regles_metier.md (Règles de priorité) | Risque de mauvaise priorisation → impact sur les délais. |
| **Validation croisée** | Le SIL vérifie que le DFG est cohérent avec l'âge et le poids du patient (seuils critiques : DFG < 30 mL/min → urgence vitale). | Étape 2 : 08_regles_metier.md (Seuils et valeurs critiques) | **Alerte** si incohérence détectée. |
| **Historique des modifications** | Toute modification d'une **prescription médicale** doit être horodatée et tracée dans le SIL. | Étape 2 : 08_regles_metier.md (Documentation des étapes) | Non-respect → impossibilité de prouver la conformité en cas d'audit. |

---

### **1.4. Règles métier partagées**
| **Règle** | **Sous-domaine concerné** | **Description** | **Source** |
|-----------|---------------------------|-----------------|------------|
| **Prescription → Prélèvement** | **Prélèvement Biologique** | Une **prescription médicale** validée est une condition sine qua non pour réaliser un **acte de prélèvement**. | Étape 2 : 08_regles_metier.md (Enchaînement obligatoire) |
| **Prescription → Priorisation** | **Gestion des Urgences** | Le **niveau d'urgence** déterminé dans la **prescription médicale** est utilisé pour prioriser la demande dans le SIL. | Étape 2 : 08_regles_metier.md (Règles de priorité) |
| **Prescription → Traçabilité** | **Traçabilité et Conformité** | Chaque **prescription médicale** est horodatée et associée à un **identifiant unique** pour assurer la traçabilité. | Étape 2 : 08_regles_metier.md (Documentation des étapes) |

---
### **1.5. Acteurs responsables au sein du sous-domaine**
| **Acteur** | **Rôle** | **Responsabilités spécifiques** |
|------------|----------|----------------------------------|
| **Médecin prescripteur** | Saisie et validation | - Saisir les **informations cliniques** complètes. <br> - Valider la **prescription médicale**. <br> - Modifier ou annuler une prescription si nécessaire. |
| **SIL** | Validation automatique et traçabilité | - Vérifier la complétude des champs. <br> - Déterminer le **niveau d'urgence**. <br> - Générer des **alertes** en cas d'erreur. <br> - Enregistrer l'historique des modifications. |
| **Équipe qualité** | Audit et conformité | - Vérifier le respect des règles de saisie. <br> - Auditer les **prescriptions médicales** pour détecter les erreurs récurrentes. |

---
### **1.6. Indicateurs de succès métier**
| **Indicateur** | **Cible** | **Fréquence de mesure** | **Source de données** |
|----------------|-----------|-------------------------|-----------------------|
| Taux de saisie complète des **informations cliniques** | ≥ 95% | Mensuelle | SIL (logs de saisie) |
| Délai moyen de saisie d'une **prescription médicale** | < 2 minutes | Hebdomadaire | SIL (horodatages) |
| Taux d'erreurs de classification du **niveau d'urgence** | ≤ 2% | Mensuelle | SIL (logs de validation) |
| Taux de modifications post-validation | ≤ 5% | Mensuelle | SIL (historique des modifications) |
| Temps moyen de validation d'une **prescription médicale** | < 30 secondes | Quotidienne | SIL (temps de traitement) |

---
### **1.7. Modes de défaillance**
| **Mode de défaillance** | **Cause possible** | **Conséquence** | **Mesures de mitigation** |
|-------------------------|--------------------|-----------------|---------------------------|
| **Prescription incomplète** | Oubli de champs obligatoires (ex : DFG non renseigné) | Génération d'une **alerte** et blocage de la validation → retard dans le circuit. | - Formation des prescripteurs. <br> - Vérification automatique des champs avant validation. |
| **Mauvaise classification de l'urgence** | Motif mal interprété (ex : "surveillance" classé en urgence vitale) | Priorisation incorrecte → retard pour les vraies urgences. | - Utilisation de listes déroulantes pour les motifs. <br> - Double vérification par le SIL. |
| **Erreur de saisie du DFG** | Saisie manuelle incorrecte (ex : 35 au lieu de 15) | **Alerte** → correction nécessaire → retard. | - Intégration automatique du DFG depuis le dossier patient. <br> - Seuil critique bloquant (DFG < 30 → urgence vitale). |
| **Modification non tracée** | Suppression ou modification non horodatée d'une prescription. | Impossibilité de prouver la conformité en cas d'audit → risque juridique. | - Journalisation automatique de toutes les modifications. <br> - Accès restreint aux modifications (rôles utilisateurs). |

---

## **2. Sous-domaine : Prélèvement Biologique**

### **2.1. Finalité métier**
Organiser et tracer de manière sécurisée et conforme les **actes de prélèvement** et la gestion des **échantillons biologiques**, en garantissant leur intégrité (type de tube, volume, étiquetage, délai de transport) pour éviter les rejets et assurer des analyses fiables, tout en assurant une **traçabilité** complète de chaque étape.

---

### **2.2. Invariants à respecter en permanence**
| **Invariant** | **Description** | **Source** |
|---------------|-----------------|------------|
| **Conformité du tube** | Le **tube de prélèvement** doit être de type citraté 3,2% avec un volume ≥ 2 mL. | Étape 2 : 08_regles_metier.md (Conformité des tubes) |
| **Étiquetage complet** | L'étiquette doit inclure le nom du patient, l'heure de prélèvement, le service demandeur et l'identifiant unique de l'échantillon. | Étape 2 : 08_regles_metier.md (Conformité de l'échantillon) |
| **Délai de transport** | Le **délai de transport** de l'échantillon au laboratoire doit être < 30 minutes. | Étape 2 : 