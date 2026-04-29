# **Découpage en sous-domaines**
**Domaine : Circuit des demandes urgentes de dosage anti-Xa**
*Document de référence pour l'étape 4 (Strategic Design)*

---

## **1. Tableau récapitulatif des sous-domaines**

| **Sous-domaine** | **Classification** | **Finalité métier** | **Acteurs principaux** | **Règles métier principales** | **Données / Informations manipulées** |
|------------------|--------------------|---------------------|------------------------|--------------------------------|---------------------------------------|
| **Prescription Médicale** | Core | Gérer la saisie, la validation et la priorisation des **prescriptions médicales** pour les dosages anti-Xa, en intégrant les **informations cliniques** obligatoires. | Médecins prescripteurs, SIL | - Une **prescription médicale** est obligatoire pour tout **acte de prélèvement**. <br> - Les **informations cliniques** (anticoagulant, heure de la dernière prise, DFG) sont obligatoires. <br> - Le **niveau d’urgence** (urgence vitale / urgence standard) est déterminé automatiquement ou manuellement. <br> - Le **SIL** génère une **alerte** si des champs obligatoires sont manquants. | - **Prescription médicale** (patient, service, anticoagulant, dose, heure de la dernière prise, DFG, motif, niveau d’urgence) <br> - **Identifiant unique** de la demande <br> - Statut de la prescription (en attente, validée, rejetée) |
| **Prélèvement Biologique** | Supporting | Organiser et tracer l’**acte de prélèvement** et la gestion des **échantillons biologiques**, en garantissant leur conformité avant analyse. | Personnel infirmier, SIL | - Le **tube de prélèvement** doit être citraté 3,2% avec un volume ≥ 2 mL. <br> - L’étiquetage doit inclure le nom du patient, l’heure de prélèvement et le service demandeur. <br> - Le **délai de transport** de l’échantillon au laboratoire doit être < 30 min. <br> - Le **SIL** vérifie la conformité et génère une **alerte** en cas de non-conformité. | - **Acte de prélèvement** (opérateur, heure, service, conformité) <br> - **Échantillon biologique** (identifiant, type de tube, volume, étiquetage) <br> - Statut de conformité (conforme / non conforme) <br> - **Identifiant unique** de l’échantillon |
| **Analyse Biologique** | Core | Réaliser les **dosages anti-Xa** et valider les résultats en fonction des **informations cliniques** et des **règles de qualité**. | Techniciens de laboratoire, Biologiste, SIL | - Les **échantillons non conformes** sont **rejetés** par le biologiste. <br> - Les **dosages anti-Xa** sont priorisés selon le **niveau d’urgence**. <br> - Le **délai de réponse** doit être < 30 min pour les urgences vitales et < 1h pour les urgences standard. <br> - Le **biologiste** interprète les résultats en intégrant le **contexte clinique**. | - **Résultat du dosage anti-Xa** (valeur en UI/mL) <br> - **Interprétation du résultat** (commentaire biologique, recommandation) <br> - Statut de l’analyse (en cours, terminée, rejetée) <br> - **Traçabilité** des étapes d’analyse |
| **Validation Clinique** | Core | Valider les **interprétations des résultats** et formuler des **décisions thérapeutiques** en fonction du **contexte clinique**. | Biologiste, Médecins prescripteurs | - Le **biologiste** valide l’**interprétation du résultat** avant transmission. <br> - Les **décisions thérapeutiques** sont ajustées en fonction des résultats et du **contexte clinique**. <br> - Le **SIL** transmet les résultats avec l’interprétation au médecin prescripteur. | - **Interprétation du résultat** (commentaire, recommandation) <br> - **Décision thérapeutique** (ajustement de dose, arrêt du traitement) <br> - Statut de validation (validé, en attente) |
| **Transmission des Résultats** | Supporting | Assurer la **transmission sécurisée et traçable** des résultats et des interprétations aux acteurs concernés. | SIL, Médecins prescripteurs, Biologiste | - Les résultats sont transmis en temps réel au médecin prescripteur. <br> - Le **SIL** génère une **alerte** si le **délai de réponse** est dépassé. <br> - Les données sont archivées conformément au RGPD. | - **Résultat du dosage anti-Xa** <br> - **Interprétation du résultat** <br> - **Décision thérapeutique** <br> - **Traçabilité** des transmissions |
| **Gestion des Urgences** | Core | Prioriser et gérer les **demandes urgentes** en fonction de leur **niveau d’urgence** et des ressources disponibles. | SIL, Techniciens de laboratoire, Médecins prescripteurs | - Les **demandes urgentes** sont classées en **urgence vitale** ou **urgence standard**. <br> - Le **SIL** applique une **priorisation automatique** des demandes. <br> - Les **alertes** sont générées en cas de dépassement des **délais de réponse**. | - **Niveau d’urgence** (urgence vitale / urgence standard) <br> - **Délai de réponse** cible <br> - Statut de priorisation (prioritaire, en attente) <br> - **Alertes** pour les dépassements de délai |
| **Traçabilité et Conformité** | Supporting | Enregistrer et auditer l’ensemble des étapes du circuit pour garantir la **traçabilité** et la **conformité réglementaire**. | SIL, Biologiste, Équipe qualité | - Chaque étape est horodatée et associée à un **identifiant unique**. <br> - Les données sont conservées pendant 20 ans (RGPD). <br> - Les accès aux données sont tracés et sécurisés. | - **Traçabilité** (étapes, horodatages, acteurs) <br> - **Identifiants uniques** (demande, échantillon) <br> - Logs d’audit (accès, modifications) |
| **Gestion des Non-Conformités** | Supporting | Gérer les **rejets d’échantillons** et les **alertes** pour améliorer la qualité pré-analytique. | Biologiste, Techniciens de laboratoire, SIL | - Les **échantillons non conformes** sont **rejetés** et une **alerte** est générée. <br> - Le **SIL** notifie les acteurs concernés (IDE, médecin prescripteur). <br> - Les motifs de rejet sont enregistrés dans la **traçabilité**. | - **Motifs de rejet** (type de tube, volume, étiquetage, délai de transport) <br> - **Alertes** pour les non-conformités <br> - Statut de l’échantillon (rejeté, à reprendre) |

---

## **2. Détail des sous-domaines**

---

### **2.1. Sous-domaine : Prescription Médicale**
**Nom canonique** : `PrescriptionMedicale`
**Classification** : **Core** (cœur stratégique du domaine)

#### **Finalité métier**
- Permettre aux **médecins prescripteurs** de saisir, valider et prioriser les **prescriptions médicales** pour les **dosages anti-Xa**, en intégrant les **informations cliniques** obligatoires.
- Automatiser la classification des demandes en **niveau d’urgence** (urgence vitale / urgence standard) pour faciliter la **priorisation** par le SIL.
- Garantir que chaque **prescription médicale** est traçable et associée à un **identifiant unique**.

#### **Problématiques regroupées**
- **Saisie des informations cliniques** : Les médecins doivent renseigner des champs obligatoires (anticoagulant, heure de la dernière prise, DFG).
- **Classification des urgences** : Distinction entre **urgence vitale** (ex : hémorragie massive) et **urgence standard** (ex : ajustement thérapeutique).
- **Validation des prescriptions** : Le SIL doit vérifier la complétude des **informations cliniques** et générer des **alertes** en cas d’omission.
- **Intégration avec les systèmes existants** : Compatibilité avec les logiciels de prescription (ex : DxCare, Cristal).

#### **Acteurs principaux**
| **Acteur** | **Rôle** | **Interactions** |
|------------|----------|------------------|
| **Médecin prescripteur** | Saisit et valide la **prescription médicale**. | - Interagit avec le **SIL** pour la saisie. <br> - Reçoit des **alertes** en cas d’omission. |
| **SIL** | Centralise les **prescriptions médicales** et applique les règles de validation. | - Génère des **alertes** pour les champs manquants. <br> - Transmet les **prescriptions validées** au **Prélèvement Biologique**. |
| **Personnel infirmier** | Reçoit la notification pour réaliser l’**acte de prélèvement**. | - Reçoit une alerte du SIL pour prélever l’échantillon. |

#### **Règles métier principales**
| **Règle** | **Source** | **Impact** |
|-----------|------------|------------|
| Une **prescription médicale** est obligatoire pour tout **acte de prélèvement**. | Étape 2 : 08_regles_metier.md | Garantit la traçabilité et la légalité de l’acte. |
| Les **informations cliniques** (anticoagulant, heure de la dernière prise, DFG) sont obligatoires. | Étape 2 : 08_regles_metier.md | Essentielles pour l’interprétation du **dosage anti-Xa**. |
| Le **niveau d’urgence** est déterminé automatiquement ou manuellement. | Étape 2 : 08_regles_metier.md | Permet la **priorisation** des demandes. |
| Le SIL génère une **alerte** si des champs obligatoires sont manquants. | Étape 2 : 08_regles_metier.md | Réduit les erreurs de saisie. |

#### **Données / Informations manipulées**
| **Donnée** | **Type** | **Description** | **Exemple** |
|------------|----------|-----------------|-------------|
| **Prescription médicale** | Objet | Contient les informations cliniques et le niveau d’urgence. | `{ patient_id: "PAT123", anticoagulant: "apixaban", dose: 5, heure_derniere_prise: "10:00", dfg: 35, niveau_urgence: "urgence_vitale" }` |
| **Identifiant unique** | UUID | Identifiant unique de la demande. | `"DEM-2023-001"` |
| **Statut de la prescription** | Enum | Statut de la prescription (en attente, validée, rejetée). | `"validée"` |

#### **Frontières du sous-domaine**
**Ce qui en fait partie** :
- Saisie des **prescriptions médicales** dans le SIL.
- Validation des **informations cliniques**.
- Classification en **niveau d’urgence**.
- Génération d’**alertes** pour les champs manquants.

**Ce qui n’en fait pas partie** :
- La réalisation de l’**acte de prélèvement** (géré par le sous-domaine **Prélèvement Biologique**).
- L’analyse des échantillons (gérée par le sous-domaine **Analyse Biologique**).
- La transmission des résultats (gérée par le sous-domaine **Transmission des Résultats**).

---

### **2.2. Sous-domaine : Prélèvement Biologique**
**Nom canonique** : `PrelevementBiologique`
**Classification** : **Supporting** (support métier critique)

#### **Finalité métier**
- Organiser et tracer l’**acte de prélèvement** et la gestion des **échantillons biologiques**, en garantissant leur conformité avant analyse.
- Assurer que les **échantillons biologiques** sont prélevés, étiquetés et transportés dans des conditions optimales pour éviter les **rejets** et les erreurs d’analyse.
- Intégrer la vérification de conformité dans le **SIL** pour automatiser les contrôles.

#### **Problématiques regroupées**
- **Conformité des tubes de prélèvement** : Respect des normes (citraté 3,2%, volume ≥ 2 mL).
- **Étiquetage des échantillons** : Inclusion du nom du patient, de l’heure de prélèvement et du service demandeur.
- **Délai de transport** : Respect du **délai de transport** < 30 min pour éviter la dégradation des échantillons.
- **Traçabilité des actes de prélèvement** : Enregistrement systématique des étapes (qui, quand, où).

#### **Acteurs principaux**
| **Acteur** | **Rôle** | **Interactions** |
|------------|----------|------------------|
| **Personnel infirmier** | Réalise l’**acte de prélèvement** et vérifie la conformité. | - Reçoit une alerte du SIL pour prélever l’échantillon. <br> - Transmet l’échantillon au laboratoire. |
| **SIL** | Vérifie la conformité de l’échantillon et génère des **alertes** en cas de non-conformité. | - Valide le type de **tube de prélèvement** et le volume. <br> - Enregistre l’**acte de prélèvement** dans la **traçabilité**. |
| **Technicien de laboratoire** | Reçoit l’échantillon et vérifie sa conformité avant analyse. | - Reçoit une alerte si l’échantillon est non conforme. |

#### **Règles métier principales**
| **Règle** | **Source** | **Impact** |
|-----------|------------|------------|
| Le **tube de prélèvement** doit être citraté 3,2% avec un volume ≥ 2 mL. | Étape 2 : 08_regles_metier.md | Garantit la qualité de l’analyse. |
| L’étiquetage doit inclure le nom du patient, l’heure de prélèvement et le service demandeur. | Étape 2 : 08_regles_metier.md | Évite les erreurs d’identification. |
| Le **délai de transport** de l’échantillon au laboratoire doit être < 30 min. | Étape 2 : 08_regles_metier.md | Préserve l’intégrité de l’échantillon. |
| Le SIL génère une **alerte** en cas de non-conformité. | Étape 2 : 08_regles_metier.md | Réduit les rejets d’échantillons. |

#### **Données / Informations manipulées**
| **Donnée** | **Type** | **Description** | **Exemple** |
|------------|----------|-----------------|-------------|
| **Acte de prélèvement** | Objet | Enregistre l’opérateur, l’heure, le service et la conformité. | `{ operateur_id: "IDE456", heure_prelevement: "10:30", service: "Urgences", conforme: true }` |
| **Échantillon biologique** | Objet | Contient le type de tube, le volume, l’étiquetage et l’identifiant unique. | `{ id: "ECH-2023-001", type_tube: "citrate_3.2%", volume: 2.5, etiquetage: { nom_patient: "Dupont", heure: "10:30", service: "Urgences" } }` |
| **Statut de conformité** | Enum | Statut de l’échantillon (conforme / non conforme). | `"conforme"` |

#### **Frontières du sous-domaine**
**Ce qui en fait partie** :
- Réalisation de l’**acte de prélèvement**.
- Vérification de la conformité du **tube de prélèvement** et du volume.
- Enregistrement de l’**échantillon biologique** dans le SIL.
- Génération d’**alertes** en cas de non-conformité.

**Ce qui n’en fait pas partie** :
- La prescription médicale (gérée par le sous-domaine **Prescription Médicale**).
- L’analyse des échantillons (gérée par le sous-domaine **Analyse Biologique**).
- L’interprétation des résultats (gérée par le sous-domaine **Validation Clinique**).

---

### **2.3. Sous-domaine : Analyse Biologique**
**Nom canonique** : `AnalyseBiologique`
**Classification** : **Core** (cœur stratégique du domaine)

#### **Finalité métier**
- Réaliser les **dosages anti-Xa** et valider les résultats en fonction des **informations cliniques** et des **règles de qualité**.
- Prioriser les analyses en fonction du **niveau d’urgence** pour garantir des **délais de réponse** optimaux.
- Rejeter les **échantillons non conformes** et générer des **alertes** pour les acteurs concernés.

#### **Problématiques regroupées**
- **Priorisation des demandes** : Classer les demandes en **urgence vitale** ou **urgence standard**.
- **Contrôle qualité** : Valider la conformité des **échantillons biologiques** avant analyse.
- **Réalisation des dosages** : Effectuer les **dosages anti-Xa** avec des automates ou des méthodes manuelles.
- **Validation des résultats** : Assurer la qualité des résultats avant transmission au biologiste.

#### **Acteurs principaux**
| **Acteur** | **Rôle** | **Interactions** |
|------------|----------|------------------|
| **Technicien de laboratoire** | Réalise les **dosages anti-Xa** et priorise les demandes. | - Reçoit les **prescriptions médicales** priorisées du SIL. <br> - Transmet les résultats au **biologiste**. |
| **Biologiste** | Valide les résultats et interprète les **dosages anti-Xa**. | - Reçoit les résultats du technicien. <br> - Rédige une **interprétation du résultat**. |
| **SIL** | Centralise les demandes et applique la **priorisation**. | - Transmet les demandes priorisées au technicien. <br> - Enregistre les résultats dans la **traçabilité**. |

#### **Règles métier principales**
| **Règle** | **Source** | **Impact** |
|-----------|------------|------------|
| Les **échantillons non conformes** sont **rejetés** par le biologiste. | Étape 2 : 08_regles_metier.md | Évite les erreurs d’analyse. |
| Les **dosages anti-Xa** sont priorisés selon le **niveau d’urgence**. | Étape 2 : 08_regles_metier.md | Garantit des **délais de réponse** optimaux. |
| Le **délai de réponse** doit être < 30 min pour les urgences vitales et < 1h pour les urgences standard. | Étape 2 : 08_regles_metier.md | Répond aux exigences cliniques. |
| Le **biologiste** interprète les résultats en intégrant le **contexte clinique**. | Étape 2 : 07_responsabilites_acteurs.md | Assure une interprétation correcte. |

#### **Données / Informations manipulées**
| **Donnée** | **Type** | **Description** | **Exemple** |
|------------|----------|-----------------|-------------|
| **Résultat du dosage anti-Xa** | Objet | Valeur numérique du dosage en UI/mL. | `{ valeur: 0.5, unite: "UI/mL" }` |
| **Interprétation du résultat** | Texte structuré | Commentaire biologique et recommandation. | `"Sous-dosage probable, envisager une transfusion."` |
| **Statut de l’analyse** | Enum | Statut de l’analyse (en cours, terminée, rejetée). | `"terminée"` |

#### **Frontières du sous-domaine**
**Ce qui en fait partie** :
- Priorisation des demandes en fonction du **niveau d’urgence**.
- Réalisation des **dosages anti-Xa**.
- Validation de la conformité des **échantillons biologiques**.
- Génération d’**alertes** pour les **rejets d’échantillons**.

**Ce qui n’en fait pas partie** :
- La prescription médicale (gérée par le sous-domaine **Prescription Médicale**).
- La transmission des résultats (gérée par le sous-domaine **Transmission des Résultats**).
- La prise de décision thérapeutique (gérée par le sous-domaine **Validation Clinique**).

---

### **2.4. Sous-domaine : Validation Clinique**
**Nom canonique** : `ValidationClinique`
**Classification** : **Core** (cœur stratégique du domaine)

#### **Finalité métier**
- Valider les **interprétations des résultats** et formuler des **décisions thérapeutiques** en fonction du **contexte clinique**.
- Assurer que les résultats des **dosages anti-Xa** sont correctement interprétés et associés à des recommandations cliniques.
- Faciliter la communication entre le **biologiste** et le **médecin prescripteur** pour ajuster les traitements.

#### **Problématiques regroupées**
- **Interprétation des résultats** : Intégrer le **contexte clinique** (traitement, fonction rénale, heure de la dernière prise) pour formuler une interprétation.
- **Validation des interprétations** : Vérifier que l’interprétation est cohérente avec les données cliniques.
- **Transmission des recommandations** : Communiquer les **décisions thérapeutiques** au médecin prescripteur.
- **Traçabilité des validations** : Enregistrer les étapes de validation pour la **traçabilité**.

#### **Acteurs principaux**
| **Acteur** | **Rôle** | **Interactions** |
|------------|----------|------------------|
| **Biologiste** | Valide l’**interprétation du résultat** et formule des recommandations. | - Reçoit les résultats du technicien. <br> - Transmet l’interprétation au SIL. |
| **Médecin prescripteur** | Reçoit les **décisions thérapeutiques** et ajuste le traitement. | - Reçoit les résultats et les recommandations du SIL. |
| **SIL** | Transmet les **interprétations** et les **décisions thérapeutiques** au médecin prescripteur. | - Enregistre les validations dans la **traçabilité**. |

#### **Règles métier principales**
| **Règle** | **Source** | **Impact** |
|-----------|------------|------------|
| Le **biologiste** valide l’**interprétation du résultat** avant transmission. | Étape 2 : 07_responsabilites_acteurs.md | Garantit la qualité de l’interprétation. |
| Les **décisions thérapeutiques** sont ajustées en fonction des résultats et du **contexte clinique**. | Étape 2 : 07_responsabilites_acteurs.md | Assure un traitement adapté. |
| Le SIL transmet les résultats avec l’interprétation au médecin prescripteur. | Étape 2 : 07_responsabilites_acteurs.md | Facilite la prise de décision. |

#### **Données / Informations manipulées**
| **Donnée** | **Type** | **Description** | **Exemple** |
|------------|----------|-----------------|-------------|
| **Interprétation du résultat** | Texte structuré | Commentaire biologique et recommandation. | `"Sous-dosage probable, envisager une transfusion."` |
| **Décision thérapeutique** | Objet | Ajustement de dose ou arrêt du traitement. | `{ action: "ajuster_dose", nouvelle_dose: 2.5, commentaire: "Surveillance renforcée" }` |
| **Statut de validation** | Enum | Statut de la validation (validé, en attente). | `"validé"` |

#### **Frontières du sous-domaine**
**Ce qui en fait partie** :
- Validation de l’**interprétation du résultat**.
- Formulation des **décisions thérapeutiques**.
- Transmission des résultats au médecin prescripteur.

**Ce qui n’en fait pas partie** :
- La réalisation des dosages (gérée par le sous-domaine **Analyse Biologique**).
- La prescription médicale (gérée par le sous-domaine **Prescription Médicale**).
- La traçabilité des étapes (gérée par le sous-domaine **Traçabilité et Conformité**).

---
### **2.5. Sous-domaine : Transmission des Résultats**
**Nom canonique** : `TransmissionResultats`
**Classification** : **Supporting** (support métier critique)

#### **Finalité métier**
- Assurer la **transmission sécurisée et traçable** des **résultats du dosage anti-Xa**, des **interprétations** et des **décisions thérapeutiques** aux acteurs concernés.
- Garantir que les résultats sont disponibles en temps réel pour les médecins prescripteurs.
- Notifier les acteurs en cas de dépassement des **délais de réponse**.

#### **Problématiques regroupées**
- **Transmission en temps réel** : Envoyer les résultats aux médecins prescripteurs dès leur validation.
- **Sécurité des données** : Chiffrer les transmissions et respecter le RGPD.
- **Notification des acteurs** : Générer des **alertes** en cas de dépassement des délais.
- **Traçabilité des transmissions** : Enregistrer chaque étape de transmission pour la **traçabilité**.

#### **Acteurs principaux**
| **Acteur** | **Rôle** | **Interactions** |
|------------|----------|------------------|
| **SIL** | Transmet les résultats et génère des **alertes** en cas de dépassement. | - Envoie les résultats au médecin prescripteur. <br> - Enregistre la transmission dans la **traçabilité**. |
| **Médecin prescripteur** | Reçoit les résultats et les **décisions thérapeutiques**. | - Consulte les résultats dans le SIL. |
| **Biologiste** | Valide les résultats avant transmission. | - Transmet les résultats validés au SIL. |

#### **Règles métier principales**
| **Règle** | **Source** | **Impact** |
|-----------|------------|------------|
| Les résultats sont transmis en temps réel au médecin prescripteur. | Étape 2 : 07_responsabilites_acteurs.md | Permet une prise en charge rapide. |
| Le SIL génère une **alerte** si le **délai de réponse** est dépassé. | Étape 2 : 08_regles_metier.md | Réduit les risques pour le patient. |
| Les données sont archivées conformément au RGPD. | Étape 2 : 08_regles_metier.md | Garantit la conformité réglementaire. |

#### **Données / Informations manipulées**
| **Donnée** | **Type** | **Description** | **Exemple** |
|------------|----------|-----------------|-------------|
| **Résultat du dosage anti-Xa** | Objet | Valeur numérique du dosage. | `{ valeur: 0.5, unite: "UI/mL" }` |
| **Interprétation du résultat** | Texte structuré | Commentaire biologique. | `"Sous-dosage probable."` |
| **Décision thérapeutique** | Objet | Ajustement de dose ou arrêt du traitement. | `{ action: "ajuster_dose", nouvelle_dose: 2.5 }` |
| **Statut de transmission** | Enum | Statut de la transmission (envoyé, reçu, lu). | `"envoyé"` |

#### **Frontières du sous-domaine**
**Ce qui en fait partie** :
- Transmission des **résultats** au médecin prescripteur.
- Génération d’**alertes** en cas de dépassement des délais.
- Archivage sécurisé des données (RGPD).

**Ce qui n’en fait pas partie** :
- La validation des résultats (gérée par le sous-domaine **Validation Clinique**).
- La réalisation des dosages (gérée par le sous-domaine **Analyse Biologique**).
- La traçabilité des étapes (gérée par le sous-domaine **Traçabilité et Conformité**).

---
### **2.6. Sous-domaine : Gestion des Urgences**
**Nom canonique** : `GestionUrgences`
**Classification** : **Core** (cœur stratégique du domaine)

#### **Finalité métier**
- Prioriser et gérer les **demandes urgentes** en fonction de leur **niveau d’urgence** (urgence vitale / urgence standard) et des ressources disponibles.
- Automatiser la **priorisation** des demandes pour garantir des **délais de réponse** optimaux.
- Générer des **alertes** en cas de dépassement des délais pour permettre une intervention rapide.

#### **Problématiques regroupées**
- **Classification des urgences** : Distinguer les **urgences vitales** (ex : hémorragie massive) des **urgences standard** (ex : ajustement thérapeutique).
- **Priorisation automatique** : Appliquer des règles de priorisation dans le SIL.
- **Gestion des ressources** : Allouer les ressources (techniciens, automates) en fonction des priorités.
- **Notification des acteurs** : Informer les acteurs concernés des urgences et des dépassements de délai.

#### **Acteurs principaux**
| **Acteur** | **Rôle** | **Interactions** |
|------------|----------|------------------|
| **SIL** | Applique la **priorisation automatique** et génère des **alertes**. | - Classe les demandes en **niveau d’urgence**. <br> - Transmet les alertes aux acteurs. |
| **Technicien de laboratoire** | Reçoit les demandes priorisées et réalise les analyses. | - Traite les demandes en fonction de leur priorité. |
| **Médecin prescripteur** | Reçoit les notifications en cas de dépassement de délai. | - Est informé des urgences et des retards. |

#### **Règles métier principales**
| **Règle** | **Source** | **Impact** |
|-----------|------------|------------|
| Les **demandes urgentes** sont classées en **urgence vitale** ou **urgence standard**. | Étape 2 : 08_regles_metier.md | Permet une **priorisation** efficace. |
| Le SIL applique une **priorisation automatique** des demandes. | Étape 2 : 08_regles_metier.md | Réduit les erreurs humaines. |
| Les **alertes** sont générées en cas de dépassement des **délais de réponse**. | Étape 2 : 08_regles_metier.md | Permet une intervention rapide. |

#### **Données / Informations manipulées**
| **Donnée** | **Type** | **Description** | **Exemple** |
|------------|----------|-----------------|-------------|
| **Niveau d’urgence** | Enum | Classification de la demande (urgence vitale / urgence standard). | `"urgence_vitale"` |
| **Délai de réponse** | Int | Délai cible en minutes. | `30` |
| **Statut de priorisation** | Enum | Statut de la priorisation (prioritaire, en attente). | `"prioritaire"` |
| **Alertes** | Objet | Notification de dépassement de délai. | `{ type: "alerte_rouge", message: "Délai dépassé pour la demande DEM-2023-001" }` |

#### **Frontières du sous-domaine**
**Ce qui en fait partie** :
- Classification des demandes en **niveau d’urgence**.
- **Priorisation automatique** des demandes.
- Génération d’**alertes** en cas de dépassement des délais.

**Ce qui n’en fait pas partie** :
- La prescription médicale (gérée par le sous-domaine **Prescription Médicale**).
- La réalisation des dosages (gérée par le sous-domaine **Analyse Biologique**).
- La transmission des résultats (gérée par le sous-domaine **Transmission des Résultats**).

---
### **2.7. Sous-domaine : Traçabilité et Conformité**
**Nom canonique** : `TracabiliteConformite`
**Classification** : **Supporting** (support métier critique)

#### **Finalité métier**
- Enregistrer et auditer l’ensemble des étapes du circuit pour garantir la **traçabilité** et la **conformité réglementaire**.
- Assurer que chaque étape est horodatée, associée à un **identifiant unique** et accessible pour les audits.
- Archiver les données conformément au RGPD et aux normes de laboratoire.

#### **Problématiques regroupées**
- **Enregistrement systématique** : Horodater et associer chaque étape à un **identifiant unique**.
- **Conservation des données** : Archiver les données pendant 20 ans (RGPD).
- **Sécurité des accès** : Restreindre l’accès aux données sensibles.
- **Audits** : Permettre la consultation des logs pour les contrôles qualité.

#### **Acteurs principaux**
| **Acteur** | **Rôle** | **Interactions** |
|------------|----------|------------------|
| **SIL** | Enregistre les étapes et génère les logs. | - Horodate chaque étape. <br> - Associe un **identifiant unique** à chaque demande. |
| **Équipe qualité** | Consulte les logs pour les audits. | - Vérifie la conformité des processus. |
| **Biologiste / Médecin prescripteur** | Consulte la **traçabilité** pour vérifier les étapes. | - Vérifie le respect des délais et des règles. |

#### **Règles métier principales**
| **Règle** | **Source** | **Impact** |
|-----------|------------|------------|
| Chaque étape est horodatée et associée à un **identifiant unique**. | Étape 2 : 08_regles_metier.md | Garantit la traçabilité. |
| Les données sont conservées pendant 20 ans (RGPD). | Étape 2 : 08_regles_metier.md | Respecte la réglementation. |
| Les accès aux données sont tracés et sécurisés. | Étape 2 : 08_regles_metier.md | Protège la confidentialité. |

#### **Données / Informations manipulées**
| **Donnée** | **Type** | **Description** | **Exemple** |
|------------|----------|-----------------|-------------|
| **Traçabilité** | Liste d’étapes | Enregistre chaque étape avec horodatage et acteur. | `[ { etape: "prescription", heure: "10:00", acteur: "Dr Martin" }, { etape: "prelevement", heure: "10:30", acteur: "IDE Dupont" } ]` |
| **Identifiants uniques** | UUID | Identifiant unique de la demande, de l’échantillon, etc. | `"DEM-2023-001"` |
| **Logs d’audit** | Liste d’accès | Enregistre les accès aux données sensibles. | `[ { utilisateur: "Dr Martin", action: "consulter_resultat", heure: "11:00" } ]` |

#### **Frontières du sous-domaine**
**Ce qui en fait partie** :
- Enregistrement des étapes avec horodatage.
- Archivage sécurisé des données (RGPD).
- Génération des logs d’audit.

**Ce qui n’en fait pas partie** :
- La prescription médicale (gérée par le sous-domaine **Prescription Médicale**).
- La réalisation des dosages (gérée par le sous-domaine **Analyse Biologique**).
- La transmission des résultats (gérée par le sous-domaine **Transmission des Résultats**).

---
### **2.8. Sous-domaine : Gestion des Non-Conformités**
**Nom canonique** : `GestionNonConformites`
**Classification** : **Supporting** (support métier critique)

#### **Finalité métier**
- Gérer les **rejets d’échantillons** et les **alertes** pour améliorer la qualité pré-analytique.
- Identifier les causes des non-conformités et mettre en place des actions correctives.
- Notifier les acteurs concernés (IDE, médecin prescripteur) pour éviter les récidives.

#### **Problématiques regroupées**
- **Détection des non-conformités** : Vérifier la conformité des **échantillons biologiques** avant analyse.
- **Génération d’alertes** : Notifier les acteurs en cas de rejet.
- **Enregistrement des motifs** : Conserver les motifs de rejet pour analyse.
- **Actions correctives** : Mettre en place des mesures pour réduire les rejets (ex : formation des IDE).

#### **Acteurs principaux**
| **Acteur** | **Rôle** | **Interactions** |
|------------|----------|------------------|
| **Biologiste** | Décide du **rejet de l’échantillon** et génère une **alerte**. | - Valide la non-conformité. <br> - Notifie les acteurs concernés. |
| **Technicien de laboratoire** | Vérifie la conformité de l’échantillon. | - Transmet l’échantillon au biologiste si non conforme. |
| **SIL** | Génère des **alertes** et enregistre les motifs de rejet. | - Notifie les acteurs. <br> - Enregistre les motifs dans la **traçabilité**. |

#### **Règles métier principales**
| **Règle** | **Source** | **Impact** |
|-----------|------------|------------|
| Les **échantillons non conformes** sont **rejetés** par le biologiste. | Étape 2 : 08_regles_metier.md | Évite les erreurs d’analyse. |
| Le SIL génère une **alerte** pour les non-conformités. | Étape 2 : 08_regles_metier.md | Réduit les risques de récidive. |
| Les motifs de rejet sont enregistrés dans la **traçabilité**. | Étape 2 : 08_regles_metier.md | Permet l’analyse des causes. |

#### **Données / Informations manipulées**
| **Donnée** | **Type** | **Description** | **Exemple** |
|------------|----------|-----------------|-------------|
| **Motifs de rejet** | Liste | Liste des raisons de non-conformité (type de tube, volume, étiquetage, délai de transport). | `[ "type_tube_incorrect", "volume_insuffisant" ]` |
| **Alertes** | Objet | Notification de rejet envoyée aux acteurs. | `{ type: "alerte", message: "Échantillon rejeté : type de tube incorrect" }` |
| **Statut de l’échantillon** | Enum | Statut de l’échantillon (rejeté, à reprendre). | `"rejeté"` |

#### **Frontières du sous-domaine**
**Ce qui en fait partie** :
- Détection des **non-conformités**.
- Génération d’**alertes** pour les rejets.
- Enregistrement des motifs de rejet.

**Ce qui n’en fait pas partie** :
- La prescription médicale (gérée par le sous-domaine **Prescription Médicale**).
- La réalisation des dosages (gérée par le sous-domaine **Analyse Biologique**).
- La transmission des résultats (gérée par le sous-domaine **Transmission des Résultats**).

---

## **3. Zones de chevauchement potentielles entre sous-domaines**

| **Sous-domaines concernés** | **Zone de chevauchement** | **Risque** | **Proposition d'arbitrage** |
|-----------------------------|---------------------------|------------|-----------------------------|
| **Prescription Médicale** ↔ **Gestion des Urgences** | La **classification des urgences** peut être faite soit dans **Prescription Médicale** (lors de la saisie) soit dans **Gestion des Urgences** (lors de la priorisation). | Double responsabilité ou omission. | **Prescription Médicale** est responsable de la classification initiale (lors de la saisie). **Gestion des Urgences** applique la priorisation automatique et génère des alertes. |
| **Prélèvement Biologique** ↔ **Gestion des Non-Conformités** | La **vérification de conformité** peut être faite soit dans **Prélèvement Biologique** (lors de la saisie de l’acte) soit dans **Gestion des Non-Conformités** (lors de la réception au laboratoire). | Double contrôle ou omission. | **Prélèvement Biologique** vérifie la conformité lors de la saisie de l’acte. **Gestion des Non-Conformités** gère les rejets et les alertes en aval. |
| **Analyse Biologique** ↔ **Validation Clinique** | L’**interprétation des résultats** peut être faite soit par le technicien (dans **Analyse Biologique**) soit par le biologiste (dans **Validation Clinique**). | Confusion sur les responsabilités. | **Analyse Biologique** réalise le dosage et transmet les résultats bruts. **Validation Clinique** est responsable de l’interprétation et de la validation finale. |
| **Transmission des Résultats** ↔ **Traçabilité et Conformité** | La **transmission des résultats** doit être tracée, ce qui peut chevaucher **Traçabilité et Conformité**. | Double enregistrement. | **Transmission des Résultats** enregistre les étapes de transmission. **Traçabilité et Conformité** archive les données et génère les logs d’audit. |
| **Gestion des Urgences** ↔ **Gestion des Non-Conformités** | Les **alertes** pour les urgences et les non-conformités peuvent être gérées par le même module. | Complexité de la logique d’alertes. | **Gestion des Urgences** gère les alertes pour les dépassements de délai. **Gestion des Non-Conformités** gère les alertes pour les rejets d’échantillons. |

---
## **4. Hypothèses de découpage et points à valider auprès du métier**

### **4.1. Hypothèses de découpage**
| **Hypothèse** | **Justification** | **Points à valider** |
|---------------|-------------------|----------------------|
| **Séparation claire entre "Prescription Médicale" et "Gestion des Urgences"** | La classification des urgences est faite lors de la saisie de la prescription, puis priorisée automatiquement. | - Valider que la classification initiale est suffisante. <br> - Vérifier que la priorisation automatique est acceptée par les métiers. |
| **Séparation entre "Analyse Biologique" et "Validation Clinique"** | Le technicien réalise le dosage, tandis que le biologiste interprète les résultats. | - Valider que les techniciens ne sont pas autorisés à interpréter les résultats. <br> - Vérifier que le biologiste a bien accès à toutes les **informations cliniques** pour l’interprétation. |
| **Centralisation de la traçabilité dans "Traçabilité et Conformité"** | Toutes les étapes sont enregistrées dans un module dédié. | - Valider que les autres sous-domaines n’ont pas besoin de gérer leur propre traçabilité. <br> - Vérifier que les logs d’audit sont conformes au RGPD. |
| **Gestion des alertes dans plusieurs sous-domaines** | Les alertes sont générées par **Gestion des Urgences** (délais) et **Gestion des Non-Conformités** (rejets). | - Valider que les acteurs reçoivent bien les alertes pertinentes. <br> - Vérifier que les notifications sont configurables (email, SMS, interface SIL). |

---
### **4.2. Points à clarifier auprès du métier**
| **Point à clarifier** | **Acteurs à consulter** | **Questions** |
|-----------------------|-------------------------|---------------|
| **Critères précis de conformité des tubes de prélèvement** | Biologiste, Techniciens de laboratoire, Personnel infirmier | - Quels sont les types de tubes acceptés (ex : citraté 3,2%) ? <br> - Quel est le volume minimal requis ? <br> - Quels sont les protocoles d’étiquetage ? |
| **Mécanismes de priorisation des urgences** | Médecins prescripteurs, Biologiste, Équipe SIL | - Quels sont les critères de classement des urgences (ex : score clinique) ? <br> - Quels sont les délais de réponse cibles par niveau d’urgence ? |
| **Protocole standardisé de transmission des informations cliniques** | Médecins prescripteurs, Personnel infirmier, Biologiste | - Quels sont les champs obligatoires à remplir dans la prescription ? <br> - Quel est le format de transmission (champ libre, liste déroulante) ? |
| **Intégration avec les automates de dosage** | Équipe SIL, Biologiste, Techniciens de laboratoire | - Quelle est la capacité d’interfaçage avec les automates ? <br> - Faut-il une validation manuelle des résultats avant transmission ? |
| **Attentes spécifiques en matière de sécurité** | Équipe SIL, Équipe qualité, Responsable RGPD | - Quel est le niveau de chiffrement requis pour les données patients ? <br> - Quelles sont les modalités de sauvegarde et d’archivage ? |
| **Processus de rejet d’échantillon** | Biologiste, Techniciens de laboratoire | - Faut-il une validation manuelle du rejet ou une automatisation totale ? <br> - Comment notifier les acteurs concernés (IDE, médecin prescripteur) ? |

---
### **4.3. Contradictions ou ambiguïtés identifiées dans les sources**
| **Élément** | **Contradiction / Ambiguïté** | **Source** | **Proposition de résolution** |
|-------------|-------------------------------|------------|-------------------------------|
| **Délai de réponse pour les urgences vitales** | Le corpus mentionne à la fois *"30 minutes"* (Étape 2 : 09_conflits_objectifs.md) et *"1 heure"* (Étape 2 : 08_regles_metier.md). | Étape 2 : 08_regles_metier.md vs. Étape 2 : 09_conflits_objectifs.md | **Hypothèse** : Les urgences vitales critiques (ex : hémorragie intracrânienne) ont un délai de 30 min, tandis que les urgences vitales standard (ex : ajustement thérapeutique urgent) ont un délai de 1h. À valider avec les cliniciens. |
| **Critères de conformité des échantillons** | Aucune liste explicite des normes de tubes ou de volumes n’est fournie. Les mentions sont génériques (ex : *"normes strictes"* dans Étape 1 : 04_contraintes_et_risques.md). | Étape 1 : 04_contraintes_et_risques.md | **Hypothèse** : Utiliser les normes ISO 15189 et CLSI GP41 comme référence (tube citraté 3,2%, volume ≥ 2 mL). À valider avec le laboratoire. |
| **Transmission des informations cliniques** | Aucune standardisation n’est décrite dans le corpus, bien que cela soit identifié comme un irritant métier (Étape 1 : 05_vision_globale_du_domaine.md). | Étape 1 : 05_vision_globale_du_domaine.md | **Hypothèse** : Créer un formulaire standardisé avec les champs obligatoires (anticoagulant, dose, heure de la dernière prise, DFG). À valider avec les médecins prescripteurs. |

---
## **5. Synthèse des décisions stratégiques**

### **5.1. Sous-domaines Core (cœur stratégique)**
Ces sous-domaines sont critiques pour la différenciation métier et doivent être conçus sur mesure :
- **Prescription Médicale** : Gère la saisie des **prescriptions médicales** et la classification des urgences.
- **Analyse Biologique** : Réalise les **dosages anti-Xa** et priorise les demandes.
- **Validation Clinique** : Valide les interprétations et formule les **décisions thérapeutiques**.
- **Gestion des Urgences** : Priorise les demandes et génère des **alertes** en cas de dépassement de délai.

**Justification** :
- Ces sous-domaines sont au cœur de la valeur métier (rapidité, qualité, sécurité).
- Ils nécessitent une intégration fine avec les processus cliniques et une automatisation poussée.

---
### **5.2. Sous-domaines Supporting (support métier critique)**
Ces sous-domaines sont essentiels mais ne sont pas différenciateurs stratégiques. Ils peuvent être externalisés ou réutilisés :
- **Prélèvement Biologique** : Gère l’**acte de prélèvement** et la conformité des **échantillons biologiques**.
- **Transmission des Résultats** : Assure la transmission sécurisée des résultats.
- **Traçabilité et Conformité** : Enregistre les étapes et archive les données.
- **Gestion des Non-Conformités** : Gère les rejets d’échantillons et les alertes associées.

**Justification** :
- Ces sous-domaines sont critiques pour la qualité et la conformité, mais peuvent être standardisés (ex : utilisation d’un SIL existant).
- Ils nécessitent une intégration avec les sous-domaines Core.

---
### **5.3. Sous-domaines Generic (commodité interchangeable)**
Aucun sous-domaine n’est classé comme **Generic** dans ce découpage, car tous les processus sont spécifiques au domaine hospitalier et biologique. Cependant, certains composants pourraient être externalisés :
- **Archivage des données** : Peut être externalisé vers un prestataire cloud conforme RGPD.
- **Génération d’alertes** : Peut utiliser un service externe (ex : Twilio pour les SMS).

---
## **6. Recommandations pour l'étape 5 (modélisation DDD tactique)**

### **6.1. Priorités de conception**
1. **Sous-domaines Core** :
   - **Prescription Médicale** : Modéliser les **prescriptions médicales** avec les **informations cliniques** et le **niveau d’urgence**.
   - **Analyse Biologique** : Modéliser les **dosages anti-Xa** et la **priorisation** des demandes.
   - **Validation Clinique** : Modéliser les **interprétations des résultats** et les **décisions thérapeutiques**.
   - **Gestion des Urgences** : Modéliser la **priorisation automatique** et les **alertes**.

2. **Sous-domaines Supporting** :
   - **Prélèvement Biologique** : Modéliser les **actes de prélèvement** et la **conformité des échantillons**.
   - **Traçabilité et Conformité** : Modéliser les **logs d’audit** et l’archivage des données.

### **6.2. Intégrations à prévoir**
- **SIL** : Doit intégrer tous les sous-domaines et assurer la communication entre eux.
- **Automates de dosage** : Doit s’interfacer avec le sous-domaine **Analyse Biologique**.
- **Logiciels de prescription** (ex : DxCare) : Doit s’interfacer avec le sous-domaine **Prescription Médicale**.

### **6.3. Points d'attention pour l'étape 5**
- **Éviter les fuites de domaine** : Ne pas mélanger la logique métier entre sous-domaines.
- **Gérer les événements** : Prévoir des événements pour notifier les changements d’état (ex : `PrescriptionValidee`, `EchantillonRejete`).
- **Sécurité** : Implémenter des mécanismes d’authentification forte et de chiffrement pour les sous-domaines Core.

---
## **7. Annexe : Sources utilisées**

| **Source** | **Description** |
|------------|-----------------|
| **demande_biologiste.md** | Demande initiale du biologiste pour l’évolution du SIL. |
| **01_reformulation_du_besoin.md** | Reformulation claire du besoin et objectifs opérationnels. |
| **02_acteurs_du_domaine.md** | Cartographie des acteurs et leurs interactions. |
| **03_concepts_metier_initiaux.md** | Liste des concepts métier initiaux. |
| **04_contraintes_et_risques.md** | Contraintes temporelles, de qualité et réglementaires. |
| **05_vision_globale_du_domaine.md** | Synthèse des enjeux et objectifs du futur circuit. |
| **06_cartographie_acteurs.md** | Détail des acteurs et leurs rôles. |
| **07_responsabilites_acteurs.md** | Responsabilités opérationnelles et décisions clés par acteur. |
| **08_regles_metier.md** | Règles de validation, priorité, sécurité et documentation. |
| **09_conflits_objectifs.md** | Conflits d’objectifs et pistes d’arbitrage. |
| **10_synthese_etape2.md** | Synthèse des acteurs, règles et conflits. |
| **11_glossaire_metier.md** | Glossaire du langage commun. |
| **12_ambiguites_resolues.md** | Ambiguïtés terminologiques résolues. |
| **13_alignement_metier_technique.md** | Alignement du vocabulaire métier et technique. |
| **14_exemples_langage_commun.md** | Exemples d’usage du langage commun. |