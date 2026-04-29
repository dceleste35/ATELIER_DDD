# **Découpage en sous-domaines**
**Domaine : Circuit des demandes urgentes de dosage anti-Xa**

---

## **1. Tableau récapitulatif des sous-domaines**

| **Sous-domaine** | **Finalité métier** | **Classification stratégique** | **Acteurs principaux** | **Règles métier principales** | **Données / Informations manipulées** |
|------------------|---------------------|-------------------------------|------------------------|--------------------------------|---------------------------------------|
| **Prescription Médicale** | Capturer et valider les demandes de dosage anti-Xa en intégrant les **informations cliniques** essentielles pour une interprétation correcte. | **Core** (cœur stratégique) | Médecins prescripteurs, SIL | - La **prescription médicale** doit inclure les **informations cliniques** obligatoires (anticoagulant, heure de la dernière prise, DFG). <br> - Le SIL doit classer automatiquement la demande en **urgence clinique** ou **urgence vitale** en fonction du motif. <br> - Le SIL doit générer une **alerte** si des champs obligatoires sont manquants. | **Prescription médicale**, **information clinique**, **niveau d'urgence**, **identifiant unique**, **service demandeur** |
| **Gestion des Urgences** | Prioriser et traiter les **demandes urgentes** en fonction de leur niveau de criticité pour garantir un **délai de réponse** optimal. | **Core** (cœur stratégique) | SIL, Techniciens de laboratoire, Médecins prescripteurs | - Les **demandes urgentes** doivent être classées en **urgence vitale** (délai < 30 min) ou **urgence standard** (délai < 1h). <br> - Le SIL doit prioriser automatiquement les demandes en fonction du niveau d'urgence. <br> - Le SIL doit notifier les acteurs concernés en temps réel. | **Prescription médicale**, **niveau d'urgence**, **délai de réponse**, **identifiant unique**, **notification** |
| **Prélèvement et Conformité** | Réaliser l’**acte de prélèvement** et vérifier la **conformité de l’échantillon biologique** pour éviter les erreurs d’analyse. | **Core** (cœur stratégique) | Personnel infirmier, SIL, Biologiste | - L’**échantillon biologique** doit être prélevé dans un **tube de prélèvement** citraté 3,2% avec un volume ≥ 2 mL. <br> - L’étiquetage doit inclure le nom du patient, la date et l’heure de prélèvement. <br> - Le SIL doit vérifier la conformité et rejeter les échantillons non conformes. <br> - Le SIL doit générer une **alerte** en cas de non-conformité. | **Prescription médicale**, **tube de prélèvement**, **échantillon biologique**, **acte de prélèvement**, **conformité**, **alerte** |
| **Analyse Biologique** | Réaliser le **dosage anti-Xa** et valider les résultats en intégrant le **contexte clinique** du patient. | **Core** (cœur stratégique) | Techniciens de laboratoire, Biologiste | - Le **dosage anti-Xa** doit être réalisé dans les délais impartis. <br> - Le **biologiste** doit interpréter les résultats en tenant compte du **contexte clinique** (traitement, fonction rénale, heure de la dernière prise). <br> - Le SIL doit enregistrer les résultats et les associer à la **prescription médicale** correspondante. | **Prescription médicale**, **échantillon biologique**, **dosage anti-Xa**, **contexte clinique**, **résultat du dosage anti-Xa**, **identifiant unique** |
| **Interprétation et Transmission** | Interpréter les résultats du **dosage anti-Xa** et transmettre les informations aux **médecins prescripteurs** pour une **décision thérapeutique** adaptée. | **Core** (cœur stratégique) | Biologiste, SIL, Médecins prescripteurs | - Le **biologiste** doit rédiger une **interprétation du résultat** incluant le **contexte clinique** et des recommandations. <br> - Le SIL doit transmettre les résultats et l’interprétation aux **médecins prescripteurs** dans les délais. <br> - Le SIL doit enregistrer la **transmission des résultats** dans la **traçabilité**. | **Prescription médicale**, **résultat du dosage anti-Xa**, **interprétation du résultat**, **contexte clinique**, **transmission des résultats**, **identifiant unique** |
| **Traçabilité et Sécurité** | Assurer la **traçabilité** complète du circuit et la sécurité des données patients conformément au RGPD. | **Supporting** (support métier) | SIL, Biologiste, Équipe qualité | - Le SIL doit enregistrer chaque étape du circuit (prescription → prélèvement → analyse → transmission) avec horodatage et identifiants uniques. <br> - Les données patients doivent être chiffrées (AES-256) et accessibles uniquement aux personnes autorisées. <br> - Le SIL doit permettre l’export des données de **traçabilité** au format PDF ou Excel. <br> - Les logs d’accès doivent être conservés pendant 20 ans. | **Prescription médicale**, **échantillon biologique**, **dosage anti-Xa**, **résultat du dosage anti-Xa**, **traçabilité**, **identifiant unique**, **logs d’accès** |
| **Gestion des Alertes et Exceptions** | Surveiller les dépassements de délais et gérer les exceptions (ex : **rejet de l’échantillon**, **urgences non prévues**). | **Supporting** (support métier) | SIL, Biologiste, Médecins prescripteurs, Personnel infirmier | - Le SIL doit générer des **alertes** en cas de dépassement des **délais de réponse**. <br> - Le SIL doit gérer les **rejets d’échantillon** et notifier les acteurs concernés. <br> - Le SIL doit permettre de gérer les **urgences non prévues** (ex : ajout manuel d’une priorité). | **Prescription médicale**, **alerte**, **rejet de l’échantillon**, **délai de réponse**, **identifiant unique** |
| **Intégration et Interopérabilité** | Assurer l’intégration du SIL avec les systèmes existants (ex : automates de dosage, logiciels de prescription) et les normes réglementaires. | **Generic** (commodité interchangeable) | Équipe SIL, Équipe informatique | - Le SIL doit s’interfacer avec les automates de dosage via une API sécurisée. <br> - Le SIL doit être compatible avec les logiciels de prescription (ex : DxCare, Cristal). <br> - Le SIL doit respecter les normes ISO 15189, CLSI GP41 et RGPD. | **Prescription médicale**, **dosage anti-Xa**, **résultat du dosage anti-Xa**, **API**, **normes réglementaires** |

---

## **2. Description détaillée des sous-domaines**

---

### **2.1. Sous-domaine : Prescription Médicale**
**Nom canonique** : `prescription_medicale`

#### **Finalité métier**
Capturer et valider les demandes de dosage anti-Xa en intégrant les **informations cliniques** essentielles pour une interprétation correcte des résultats. Ce sous-domaine est le point d’entrée du circuit et doit garantir que les prescriptions sont complètes, priorisées et traçables.

#### **Problématiques regroupées**
- **Complétude des prescriptions** : Les **prescriptions médicales** doivent inclure toutes les **informations cliniques** obligatoires (anticoagulant, heure de la dernière prise, DFG, motif).
- **Priorisation automatique** : Le SIL doit classer les demandes en **urgence clinique** ou **urgence vitale** en fonction du motif.
- **Génération d’alertes** : Le SIL doit alerter en cas de champs manquants ou de données incohérentes.

#### **Acteurs principaux**
- **Médecins prescripteurs** (Urgences, Réanimation, Bloc opératoire) : Saisissent les **prescriptions médicales** et renseignent les **informations cliniques**.
- **SIL** : Valide les prescriptions, classe les urgences et génère des **alertes** si nécessaire.

#### **Règles métier principales**
| **Règle** | **Source** | **Implémentation attendue** |
|-----------|------------|-----------------------------|
| Les **prescriptions médicales** doivent inclure les **informations cliniques** obligatoires : anticoagulant, dose, heure de la dernière prise, DFG, motif. | Étape 2 : 08_regles_metier.md | Champ `informations_cliniques_obligatoires` dans le formulaire de saisie. |
| Le SIL doit classer automatiquement les demandes en **urgence clinique** ou **urgence vitale** en fonction du motif. | Étape 2 : 08_regles_metier.md | Enum `NiveauUrgence` avec valeurs `urgence_vitale` et `urgence_standard`. |
| Le SIL doit générer une **alerte** si des champs obligatoires sont manquants. | Étape 2 : 08_regles_metier.md | Notification automatique dans l’interface SIL. |

#### **Données / Informations manipulées**
- **Prescription médicale** : Contient les informations de base (patient, service demandeur, motif).
- **Information clinique** : Anticoagulant, dose, heure de la dernière prise, DFG, motif.
- **Niveau d'urgence** : `urgence_vitale` ou `urgence_standard`.
- **Identifiant unique** : Identifiant unique pour chaque prescription.
- **Service demandeur** : Service clinique à l’origine de la prescription (ex : Urgences, Réanimation).

#### **Frontières (ce qui en fait partie / ce qui n'en fait pas partie)**
| **Inclus** | **Exclus** |
|------------|------------|
| - Saisie des **prescriptions médicales**. <br> - Validation des **informations cliniques**. <br> - Classification en **urgence clinique** ou **urgence vitale**. <br> - Génération d’**alertes** pour les champs manquants. | - La réalisation de l’**acte de prélèvement** (sous-domaine **Prélèvement et Conformité**). <br> - L’analyse des échantillons (sous-domaine **Analyse Biologique**). <br> - La transmission des résultats (sous-domaine **Interprétation et Transmission**). |

#### **Zones de chevauchement potentielles**
- **Chevauchement avec le sous-domaine "Gestion des Urgences"** :
  - La classification en **urgence clinique** ou **urgence vitale** est réalisée dans ce sous-domaine, mais la priorisation et le traitement des urgences relèvent du sous-domaine **Gestion des Urgences**.
  - **À arbitrer** : Qui est responsable de la mise à jour manuelle des niveaux d’urgence en cas d’évolution de la situation clinique ?

- **Chevauchement avec le sous-domaine "Prélèvement et Conformité"** :
  - Les **informations cliniques** (ex : heure de la dernière prise) sont utilisées pour vérifier la conformité de l’**échantillon biologique**.
  - **À arbitrer** : Faut-il inclure une vérification automatique des **informations cliniques** lors de la saisie de la prescription ?

---

### **2.2. Sous-domaine : Gestion des Urgences**
**Nom canonique** : `gestion_des_urgences`

#### **Finalité métier**
Prioriser et traiter les **demandes urgentes** en fonction de leur niveau de criticité pour garantir un **délai de réponse** optimal. Ce sous-domaine est critique pour la sécurité des patients et doit être hautement réactif.

#### **Problématiques regroupées**
- **Hiérarchisation des urgences** : Distinguer les **urgences vitales** (délai < 30 min) des **urgences standard** (délai < 1h).
- **Priorisation automatique** : Le SIL doit appliquer une logique de priorisation basée sur les critères cliniques.
- **Notification en temps réel** : Les acteurs concernés (techniciens, biologistes, prescripteurs) doivent être notifiés immédiatement.

#### **Acteurs principaux**
- **SIL** : Applique la priorisation et génère les notifications.
- **Techniciens de laboratoire** : Reçoivent les demandes priorisées et réalisent les analyses.
- **Médecins prescripteurs** : Sont notifiés des résultats dans les délais impartis.

#### **Règles métier principales**
| **Règle** | **Source** | **Implémentation attendue** |
|-----------|------------|-----------------------------|
| Les **demandes urgentes** doivent être classées en **urgence vitale** (délai < 30 min) ou **urgence standard** (délai < 1h). | Étape 2 : 08_regles_metier.md | Enum `NiveauUrgence` avec valeurs `urgence_vitale` et `urgence_standard`. |
| Le SIL doit prioriser automatiquement les demandes en fonction du niveau d’urgence. | Étape 2 : 08_regles_metier.md | Algorithme de priorisation intégré au SIL. |
| Le SIL doit notifier les acteurs concernés en temps réel. | Étape 2 : 08_regles_metier.md | Système de notification (interface, email, SMS). |

#### **Données / Informations manipulées**
- **Prescription médicale** : Contient le niveau d’urgence.
- **Niveau d'urgence** : `urgence_vitale` ou `urgence_standard`.
- **Délai de réponse** : Délai cible en fonction du niveau d’urgence.
- **Identifiant unique** : Identifiant unique pour chaque demande.
- **Notification** : Message envoyé aux acteurs concernés.

#### **Frontières (ce qui en fait partie / ce qui n'en fait pas partie)**
| **Inclus** | **Exclus** |
|------------|------------|
| - Classification des urgences. <br> - Priorisation automatique des demandes. <br> - Génération de **notifications** en temps réel. <br> - Surveillance des **délais de réponse**. | - La saisie des **prescriptions médicales** (sous-domaine **Prescription Médicale**). <br> - La réalisation de l’**acte de prélèvement** (sous-domaine **Prélèvement et Conformité**). <br> - L’analyse des échantillons (sous-domaine **Analyse Biologique**). |

#### **Zones de chevauchement potentielles**
- **Chevauchement avec le sous-domaine "Prescription Médicale"** :
  - La classification en **urgence clinique** ou **urgence vitale** est initiée dans **Prescription Médicale**, mais la priorisation et le traitement relèvent de **Gestion des Urgences**.
  - **À arbitrer** : Qui est responsable de la mise à jour manuelle des niveaux d’urgence en cas d’évolution de la situation clinique ?

- **Chevauchement avec le sous-domaine "Analyse Biologique"** :
  - La priorisation impacte l’ordre de traitement des échantillons.
  - **À arbitrer** : Faut-il inclure une logique de priorisation dans le sous-domaine **Analyse Biologique** ?

---

### **2.3. Sous-domaine : Prélèvement et Conformité**
**Nom canonique** : `prelevement_et_conformite`

#### **Finalité métier**
Réaliser l’**acte de prélèvement** et vérifier la **conformité de l’échantillon biologique** pour éviter les erreurs d’analyse. Ce sous-domaine est critique pour la qualité des résultats et doit garantir que les échantillons sont conformes aux normes pré-analytiques.

#### **Problématiques regroupées**
- **Conformité des échantillons** : Vérifier que les **échantillons biologiques** respectent les normes (type de tube, volume, étiquetage).
- **Traçabilité des prélèvements** : Enregistrer chaque **acte de prélèvement** avec horodatage et identifiants uniques.
- **Gestion des rejets** : Rejeter les échantillons non conformes et notifier les acteurs concernés.

#### **Acteurs principaux**
- **Personnel infirmier** : Réalise l’**acte de prélèvement** et vérifie la conformité.
- **SIL** : Vérifie la conformité des échantillons et génère des **alertes** en cas de non-conformité.
- **Biologiste** : Valide les rejets d’échantillons et décide des actions correctives.

#### **Règles métier principales**
| **Règle** | **Source** | **Implémentation attendue** |
|-----------|------------|-----------------------------|
| L’**échantillon biologique** doit être prélevé dans un **tube de prélèvement** citraté 3,2% avec un volume ≥ 2 mL. | Étape 2 : 08_regles_metier.md | Vérification automatique du type de tube et du volume. |
| L’étiquetage doit inclure le nom du patient, la date et l’heure de prélèvement. | Étape 2 : 08_regles_metier.md | Champ obligatoire dans le formulaire de saisie. |
| Le SIL doit vérifier la conformité et rejeter les échantillons non conformes. | Étape 2 : 08_regles_metier.md | Génération d’une **alerte** et enregistrement du rejet dans la **traçabilité**. |
| Le SIL doit générer une **alerte** en cas de non-conformité. | Étape 2 : 08_regles_metier.md | Notification automatique dans l’interface SIL. |

#### **Données / Informations manipulées**
- **Prescription médicale** : Contient les informations nécessaires pour le prélèvement.
- **Tube de prélèvement** : Type de tube (citraté 3,2%) et volume.
- **Échantillon biologique** : Matériel prélevé (sang, plasma).
- **Acte de prélèvement** : Action de prélever avec horodatage et opérateur.
- **Conformité** : Résultat de la vérification (conforme/non conforme).
- **Alerte** : Notification en cas de non-conformité.

#### **Frontières (ce qui en fait partie / ce qui n'en fait pas partie)**
| **Inclus** | **Exclus** |
|------------|------------|
| - Réalisation de l’**acte de prélèvement**. <br> - Vérification de la **conformité de l’échantillon**. <br> - Génération d’**alertes** pour les échantillons non conformes. <br> - Enregistrement de la **traçabilité** des prélèvements. | - La saisie des **prescriptions médicales** (sous-domaine **Prescription Médicale**). <br> - La priorisation des demandes (sous-domaine **Gestion des Urgences**). <br> - L’analyse des échantillons (sous-domaine **Analyse Biologique**). |

#### **Zones de chevauchement potentielles**
- **Chevauchement avec le sous-domaine "Prescription Médicale"** :
  - Les **informations cliniques** (ex : heure de la dernière prise) sont utilisées pour vérifier la conformité de l’**échantillon biologique**.
  - **À arbitrer** : Faut-il inclure une vérification automatique des **informations cliniques** lors de la saisie de la prescription ?

- **Chevauchement avec le sous-domaine "Analyse Biologique"** :
  - La conformité de l’échantillon impacte directement l’analyse.
  - **À arbitrer** : Faut-il inclure une logique de rejet dans le sous-domaine **Analyse Biologique** ?

---

### **2.4. Sous-domaine : Analyse Biologique**
**Nom canonique** : `analyse_biologique`

#### **Finalité métier**
Réaliser le **dosage anti-Xa** et valider les résultats en intégrant le **contexte clinique** du patient. Ce sous-domaine est au cœur du processus analytique et doit garantir la qualité et la rapidité des analyses.

#### **Problématiques regroupées**
- **Réaliser le dosage** : Effectuer le **dosage anti-Xa** dans les délais impartis.
- **Interpréter les résultats** : Intégrer le **contexte clinique** pour une interprétation correcte.
- **Valider les résultats** : Assurer la qualité des analyses et enregistrer les résultats dans le SIL.

#### **Acteurs principaux**
- **Techniciens de laboratoire** : Réalise les **dosages anti-Xa** et valide les résultats.
- **Biologiste** : Supervise les analyses, interprète les résultats et rédige les **interprétations**.
- **SIL** : Enregistre les résultats et les associe aux **prescriptions médicales**.

#### **Règles métier principales**
| **Règle** | **Source** | **Implémentation attendue** |
|-----------|------------|-----------------------------|
| Le **dosage anti-Xa** doit être réalisé dans les délais impartis (30 min pour les **urgences vitales**, 1h pour les **urgences standard**). | Étape 2 : 08_regles_metier.md | Horodatage automatique des étapes dans le SIL. |
| Le **biologiste** doit interpréter les résultats en tenant compte du **contexte clinique** (traitement, fonction rénale, heure de la dernière prise). | Étape 1 : 03_concepts_metier_initiaux.md | Champ `interpretation_resultat` incluant le **contexte clinique**. |
| Le SIL doit enregistrer les résultats et les associer à la **prescription médicale** correspondante. | Étape 2 : 08_regles_metier.md | Intégration automatique des résultats dans le dossier patient. |

#### **Données / Informations manipulées**
- **Prescription médicale** : Contient les informations nécessaires pour l’interprétation.
- **Échantillon biologique** : Matériel analysé.
- **Dosage anti-Xa** : Résultat numérique (UI/mL).
- **Contexte clinique** : Traitement, fonction rénale, heure de la dernière prise.
- **Résultat du dosage anti-Xa** : Valeur numérique et interprétation.
- **Identifiant unique** : Identifiant unique pour chaque analyse.

#### **Frontières (ce qui en fait partie / ce qui n'en fait pas partie)**
| **Inclus** | **Exclus** |
|------------|------------|
| - Réalisation du **dosage anti-Xa**. <br> - Interprétation des résultats en intégrant le **contexte clinique**. <br> - Validation des résultats par le **biologiste**. <br> - Enregistrement des résultats dans le SIL. | - La saisie des **prescriptions médicales** (sous-domaine **Prescription Médicale**). <br> - La priorisation des demandes (sous-domaine **Gestion des Urgences**). <br> - La transmission des résultats (sous-domaine **Interprétation et Transmission**). |

#### **Zones de chevauchement potentielles**
- **Chevauchement avec le sous-domaine "Prélèvement et Conformité"** :
  - La conformité de l’échantillon impacte directement l’analyse.
  - **À arbitrer** : Faut-il inclure une logique de rejet dans le sous-domaine **Analyse Biologique** ?

- **Chevauchement avec le sous-domaine "Interprétation et Transmission"** :
  - L’interprétation des résultats est réalisée dans ce sous-domaine, mais la transmission relève de **Interprétation et Transmission**.
  - **À arbitrer** : Qui est responsable de la rédaction de l’**interprétation du résultat** ?

---
### **2.5. Sous-domaine : Interprétation et Transmission**
**Nom canonique** : `interpretation_et_transmission`

#### **Finalité métier**
Interpréter les résultats du **dosage anti-Xa** et transmettre les informations aux **médecins prescripteurs** pour une **décision thérapeutique** adaptée. Ce sous-domaine est critique pour la prise en charge clinique et doit garantir une communication claire et rapide.

#### **Problématiques regroupées**
- **Interprétation des résultats** : Rédiger une **interprétation du résultat** incluant le **contexte clinique** et des recommandations.
- **Transmission sécurisée** : Transmettre les résultats et l’interprétation aux **médecins prescripteurs** dans les délais.
- **Traçabilité** : Enregistrer la **transmission des résultats** pour assurer la conformité réglementaire.

#### **Acteurs principaux**
- **Biologiste** : Rédige l’**interprétation du résultat** et valide la transmission.
- **SIL** : Transmet les résultats et enregistre la **traçabilité**.
- **Médecins prescripteurs** : Reçoivent les résultats et prennent les **décisions thérapeutiques**.

#### **Règles métier principales**
| **Règle** | **Source** | **Implémentation attendue** |
|-----------|------------|-----------------------------|
| Le **biologiste** doit rédiger une **interprétation du résultat** incluant le **contexte clinique** et des recommandations. | Étape 2 : 07_responsabilites_acteurs.md | Champ structuré `interpretation_resultat` dans le SIL. |
| Le SIL doit transmettre les résultats et l’interprétation aux **médecins prescripteurs** dans les délais (30 min pour les **urgences vitales**, 1h pour les **urgences standard**). | Étape 2 : 08_regles_metier.md | Notification automatique dans l’interface SIL et par email. |
| Le SIL doit enregistrer la **transmission des résultats** dans la **traçabilité**. | Étape 2 : 08_regles_metier.md | Horodatage et identifiant unique dans les logs. |

#### **Données / Informations manipulées**
- **Prescription médicale** : Contient les informations nécessaires pour l’interprétation.
- **Résultat du dosage anti-Xa** : Valeur numérique et interprétation.
- **Interprétation du résultat** : Commentaire structuré incluant le **contexte clinique** et des recommandations.
- **Contexte clinique** : Traitement, fonction rénale, heure de la dernière prise.
- **Transmission des résultats** : Acte de transmettre les résultats aux prescripteurs.
- **Identifiant unique** : Identifiant unique pour chaque transmission.

#### **Frontières (ce qui en fait partie / ce qui n'en fait pas partie)**
| **Inclus** | **Exclus** |
|------------|------------|
| - Rédaction de l’**interprétation du résultat**. <br> - Transmission sécurisée des résultats aux **médecins prescripteurs**. <br> - Enregistrement de la **transmission des résultats** dans la **traçabilité**. | - La réalisation du **dosage anti-Xa** (sous-domaine **Analyse Biologique**). <br> - La gestion des urgences (sous-domaine **Gestion des Urgences**). |

#### **Zones de chevauchement potentielles**
- **Chevauchement avec le sous-domaine "Analyse Biologique"** :
  - L’interprétation des résultats est réalisée dans ce sous-domaine, mais la transmission relève de **Interprétation et Transmission**.
  - **À arbitrer** : Qui est responsable de la rédaction de l’**interprétation du résultat** ?

---
### **2.6. Sous-domaine : Traçabilité et Sécurité**
**Nom canonique** : `tracabilite_et_securite`

#### **Finalité métier**
Assurer la **traçabilité** complète du circuit et la sécurité des données patients conformément au RGPD. Ce sous-domaine est essentiel pour la conformité réglementaire et la sécurité des patients.

#### **Problématiques regroupées**
- **Traçabilité complète** : Enregistrer chaque étape du circuit avec horodatage et identifiants uniques.
- **Sécurité des données** : Chiffrer les données patients et restreindre l’accès aux personnes autorisées.
- **Archivage** : Conserver les données pendant 20 ans et permettre leur restauration en cas de besoin.

#### **Acteurs principaux**
- **SIL** : Enregistre les étapes du circuit et gère la sécurité des données.
- **Biologiste** : Accède aux données pour l’interprétation et la validation.
- **Équipe qualité** : Supervise la conformité réglementaire et les audits.

#### **Règles métier principales**
| **Règle** | **Source** | **Implémentation attendue** |
|-----------|------------|-----------------------------|
| Le SIL doit enregistrer chaque étape du circuit (prescription → prélèvement → analyse → transmission) avec horodatage et identifiants uniques. | Étape 2 : 08_regles_metier.md | Base de données avec logs horodatés et identifiants uniques. |
| Les données patients doivent être chiffrées (AES-256) et accessibles uniquement aux personnes autorisées. | Étape 2 : 08_regles_metier.md | Chiffrement des données et gestion des droits d’accès. |
| Le SIL doit permettre l’export des données de **traçabilité** au format PDF ou Excel. | Étape 2 : 12_user_stories.md (User Story 6) | Fonctionnalité d’export intégrée au SIL. |
| Les logs d’accès doivent être conservés pendant 20 ans. | RGPD | Archivage sécurisé des logs. |

#### **Données / Informations manipulées**
- **Prescription médicale** : Contient les informations de base.
- **Échantillon biologique** : Matériel analysé.
- **Dosage anti-Xa** : Résultat numérique.
- **Résultat du dosage anti-Xa** : Valeur numérique et interprétation.
- **Traçabilité** : Enregistrement de chaque étape avec horodatage et identifiants uniques.
- **Identifiant unique** : Identifiant unique pour chaque demande.
- **Logs d’accès** : Historique des accès aux données.

#### **Frontières (ce qui en fait partie / ce qui n'en fait pas partie)**
| **Inclus** | **Exclus** |
|------------|------------|
| - Enregistrement de la **traçabilité** de chaque étape. <br> - Chiffrement des données et gestion des droits d’accès. <br> - Archivage des données pendant 20 ans. <br> - Export des données de **traçabilité**. | - La saisie des **prescriptions médicales** (sous-domaine **Prescription Médicale**). <br> - La réalisation des analyses (sous-domaine **Analyse Biologique**). |

#### **Zones de chevauchement potentielles**
- **Chevauchement avec tous les sous-domaines** :
  - La **traçabilité** est un aspect transversal qui impacte tous les sous-domaines.
  - **À arbitrer** : Qui est responsable de la maintenance et de la supervision de la **traçabilité** ?

---
### **2.7. Sous-domaine : Gestion des Alertes et Exceptions**
**Nom canonique** : `gestion_des_alertes_et_exceptions`

#### **Finalité métier**
Surveiller les dépassements de délais et gérer les exceptions (ex : **rejet de l’échantillon**, **urgences non prévues**). Ce sous-domaine est essentiel pour la réactivité et la qualité du circuit.

#### **Problématiques regroupées**
- **Surveillance des délais** : Générer des **alertes** en cas de dépassement des **délais de réponse**.
- **Gestion des rejets** : Rejeter les **échantillons non conformes** et notifier les acteurs concernés.
- **Gestion des urgences non prévues** : Permettre l’ajout manuel de priorités pour les situations imprévues.

#### **Acteurs principaux**
- **SIL** : Génère les **alertes** et gère les exceptions.
- **Biologiste** : Valide les rejets d’échantillons et décide des actions correctives.
- **Médecins prescripteurs** : Sont notifiés des alertes et des rejets.
- **Personnel infirmier** : Est notifié en cas de rejet d’échantillon.

#### **Règles métier principales**
| **Règle** | **Source** | **Implémentation attendue** |
|-----------|------------|-----------------------------|
| Le SIL doit générer des **alertes** en cas de dépassement des **délais de réponse** (30 min pour les **urgences vitales**, 1h pour les **urgences standard**). | Étape 2 : 08_regles_metier.md | Système de notification automatique (interface, email, SMS). |
| Le SIL doit gérer les **rejets d’échantillon** et notifier les acteurs concernés. | Étape 2 : 08_regles_metier.md | Génération d’une **alerte** et enregistrement du rejet dans la **traçabilité**. |
| Le SIL doit permettre de gérer les **urgences non prévues** (ex : ajout manuel d’une priorité). | Étape 2 : 09_conflits_objectifs.md | Interface de gestion manuelle des priorités. |

#### **Données / Informations manipulées**
- **Prescription médicale** : Contient les informations nécessaires pour la gestion des alertes.
- **Alerte** : Notification générée en cas de dépassement de délai ou de non-conformité.
- **Rejet de l’échantillon** : Décision de ne pas analyser un échantillon non conforme.
- **Délai de réponse** : Délai cible en fonction du niveau d’urgence.
- **Identifiant unique** : Identifiant unique pour chaque alerte ou rejet.

#### **Frontières (ce qui en fait partie / ce qui n'en fait pas partie)**
| **Inclus** | **Exclus** |
|------------|------------|
| - Génération d’**alertes** en cas de dépassement de délais. <br> - Gestion des **rejets d’échantillon**. <br> - Gestion des **urgences non prévues**. <br> - Enregistrement des alertes et rejets dans la **traçabilité**. | - La saisie des **prescriptions médicales** (sous-domaine **Prescription Médicale**). <br> - La priorisation des demandes (sous-domaine **Gestion des Urgences**). |

#### **Zones de chevauchement potentielles**
- **Chevauchement avec le sous-domaine "Prélèvement et Conformité"** :
  - La gestion des **rejets d’échantillon** est liée à la conformité des échantillons.
  - **À arbitrer** : Faut-il inclure la logique de rejet dans le sous-domaine **Prélèvement et Conformité** ?

- **Chevauchement avec le sous-domaine "Gestion des Urgences"** :
  - La gestion des **urgences non prévues** impacte la priorisation des demandes.
  - **À arbitrer** : Faut-il inclure une logique de gestion manuelle des urgences dans **Gestion des Urgences** ?

---
### **2.8. Sous-domaine : Intégration et Interopérabilité**
**Nom canonique** : `integration_et_interoperabilite`

#### **Finalité métier**
Assurer l’intégration du SIL avec les systèmes existants (ex : automates de dosage, logiciels de prescription) et les normes réglementaires. Ce sous-domaine est essentiel pour l’interopérabilité et la conformité du système.

#### **Problématiques regroupées**
- **Intégration avec les automates de dosage** : S’interfacer avec les automates pour automatiser la transmission des demandes et la réception des résultats.
- **Compatibilité avec les logiciels de prescription** : Assurer la compatibilité avec les systèmes existants (ex : DxCare, Cristal).
- **Respect des normes réglementaires** : Conformer le SIL aux normes ISO 15189, CLSI GP41 et RGPD.

#### **Acteurs principaux**
- **Équipe SIL** : Développe et maintient les interfaces.
- **Équipe informatique** : Supervise l’intégration technique.
- **Fournisseurs d’automates** : Fournissent les API pour l’intégration.

#### **Règles métier principales**
| **Règle** | **Source** | **Implémentation attendue** |
|-----------|------------|-----------------------------|
| Le SIL doit s’interfacer avec les automates de dosage via une API sécurisée. | Étape 2 : 12_user_stories.md (User Story 7) | Développement d’une API REST sécurisée. |
| Le SIL doit être compatible avec les logiciels de prescription (ex : DxCare, Cristal). | Étape 2 : 14_alignement_metier_technique.md | Utilisation de standards d’interopérabilité (ex : HL7, FHIR). |
| Le SIL doit respecter les normes ISO 15189, CLSI GP41 et RGPD. | Étape 2 : 08_regles_metier.md | Audit de conformité et documentation technique. |

#### **Données / Informations manipulées**
- **Prescription médicale** : Contient les informations nécessaires pour l’intégration.
- **Dosage anti-Xa** : Résultat numérique.
- **Résultat du dosage anti-Xa** : Valeur numérique et interprétation.
- **API** : Interface de communication avec les automates et logiciels externes.
- **Normes réglementaires** : ISO 15189, CLSI GP41, RGPD.

#### **Frontières (ce qui en fait partie / ce qui n'en fait pas partie)**
| **Inclus** | **Exclus** |
|------------|------------|
| - Développement des interfaces avec les automates. <br> - Intégration avec les logiciels de prescription. <br> - Audit de conformité aux normes réglementaires. | - La saisie des **prescriptions médicales** (sous-domaine **Prescription Médicale**). <br> - La réalisation des analyses (sous-domaine **Analyse Biologique**). |

#### **Zones de chevauchement potentielles**
- **Chevauchement avec le sous-domaine "Analyse Biologique"** :
  - L’intégration avec les automates impacte directement l’analyse.
  - **À arbitrer** : Faut-il inclure la logique d’intégration dans le sous-domaine **Analyse Biologique** ?

- **Chevauchement avec le sous-domaine "Prescription Médicale"** :
  - L’intégration avec les logiciels de prescription impacte la saisie des prescriptions.
  - **À arbitrer** : Faut-il inclure la logique d’intégration dans le sous-domaine **Prescription Médicale** ?

---

## **3. Hypothèses de découpage et points à valider auprès du métier**

### **3.1. Hypothèses de découpage**
| **Hypothèse** | **Justification** | **Impact potentiel** | **Points à valider** |
|---------------|-------------------|----------------------|-----------------------|
| **La "Prescription Médicale" et la "Gestion des Urgences" sont deux sous-domaines distincts** | - La classification en **urgence clinique** ou **urgence vitale** est initiée lors de la saisie de la prescription, mais la priorisation et le traitement relèvent d’un sous-domaine dédié. <br> - Cela permet une séparation claire des responsabilités entre les acteurs. | Risque de duplication des règles de priorisation. | Valider avec les **médecins prescripteurs** et les **biologistes** si la classification doit être manuelle ou automatique. |
| **Le "Prélèvement et Conformité" est un sous-domaine distinct** | - La vérification de la conformité des échantillons est un processus critique et spécifique, nécessitant des règles et des acteurs dédiés. <br> - Cela permet de séparer les responsabilités entre le personnel infirmier (prélèvement) et les techniciens de laboratoire (analyse). | Risque de chevauchement avec l’analyse biologique. | Valider avec les **techniciens de laboratoire** si la conformité doit être vérifiée avant ou après l’analyse. |
| **L’"Interprétation et Transmission" est un sous-domaine distinct** | - L’interprétation des résultats et la transmission aux prescripteurs sont des processus critiques nécessitant une expertise spécifique (biologiste). <br> - Cela permet de séparer les responsabilités entre l’analyse (techniciens) et l’interprétation (biologistes). | Risque de chevauchement avec l’analyse biologique. | Valider avec les **biologistes** si l’interprétation doit être incluse dans le sous-domaine **Analyse Biologique**. |
| **La "Traçabilité et Sécurité" est un sous-domaine transversal** | - La **traçabilité** est un aspect critique qui impacte tous les sous-domaines. <br> - Cela permet de centraliser la gestion des logs et des données de sécurité. | Risque de surcharge du sous-domaine. | Valider avec l’**équipe SIL** si la traçabilité doit être gérée dans un sous-domaine dédié ou intégrée aux autres sous-domaines. |
| **La "Gestion des Alertes et Exceptions" est un sous-domaine distinct** | - La gestion des **alertes** et des **rejets d’échantillon** est un processus critique nécessitant une réactivité immédiate. <br> - Cela permet de centraliser la logique de notification et de gestion des exceptions. | Risque de chevauchement avec les autres sous-domaines. | Valider avec les **biologistes** et le **personnel infirmier** si la gestion des alertes doit être incluse dans les sous-domaines existants. |
| **L’"Intégration et Interopérabilité" est un sous-domaine générique** | - L’intégration avec les automates et les logiciels externes est une commodité technique qui peut être externalisée ou standardisée. <br> - Cela permet de séparer les préoccupations techniques des processus métier. | Risque de sous-estimation des efforts d’intégration. | Valider avec l’**équipe SIL** et l’**équipe informatique** si l’intégration doit être gérée en interne ou externalisée. |

---
### **3.2. Points à valider auprès du métier**
| **Point à valider** | **Acteurs à consulter** | **Questions clés** | **Impact potentiel** |
|---------------------|--------------------------|--------------------|----------------------|
| **Critères de conformité des échantillons** | Biologiste, Techniciens de laboratoire, Personnel infirmier | - Quels sont les types de tubes acceptés (ex : citraté 3,2%) ? <br> - Quel est le volume minimal requis pour l’analyse ? <br> - Quels sont les protocoles d’étiquetage ? | Définir les règles de **rejet de l’échantillon** et les critères de conformité. |
| **Mécanismes de priorisation des urgences** | Médecins prescripteurs, Biologiste, SIL | - Quels sont les critères de classement des urgences (ex : score clinique, type d’anticoagulant) ? <br> - Quels sont les délais de réponse cibles par niveau de priorité ? | Définir les règles de **priorisation** et les **délais de réponse** cibles. |
| **Protocole standardisé de transmission des informations cliniques** | Médecins prescripteurs, Personnel infirmier, Biologiste | - Quels sont les champs obligatoires à remplir dans la prescription ? <br> - Quel est le format de transmission (ex : champ libre, liste déroulante) ? | Définir les **informations cliniques** obligatoires et leur format. |
| **Intégration avec les systèmes existants** | Équipe SIL, Équipe informatique | - Quels sont les systèmes existants à intégrer (ex : DxCare, Cristal) ? <br> - Quelle est la capacité d’interfaçage avec les automates de dosage ? | Définir les efforts d’intégration et les normes à respecter. |
| **Attentes spécifiques en matière de sécurité et de traçabilité** | Équipe SIL, Équipe qualité, Responsable RGPD | - Quel est le niveau de chiffrement requis pour les données patients ? <br> - Quelles sont les modalités de sauvegarde et d’archivage des données ? <br> - Quels sont les processus de validation des utilisateurs ? | Définir les exigences de sécurité et de traçabilité. |
| **Responsabilités pour la mise à jour manuelle des urgences** | Médecins prescripteurs, Biologiste | - Qui est responsable de la mise à jour manuelle des niveaux d’urgence en cas d’évolution de la situation clinique ? | Clarifier les responsabilités pour la gestion des **urgences non prévues**. |
| **Responsabilités pour la rédaction de l’interprétation des résultats** | Biologiste, Techniciens de laboratoire | - Qui est responsable de la rédaction de l’**interprétation du résultat** ? | Clarifier les responsabilités pour l’**interprétation des résultats**. |
| **Responsabilités pour la maintenance de la traçabilité** | Équipe SIL, Équipe qualité | - Qui est responsable de la maintenance et de la supervision de la **traçabilité** ? | Clarifier les responsabilités pour la **traçabilité**. |

---
### **3.3. Contradictions entre les sources à arbitrer**
| **Contradiction** | **Sources concernées** | **Proposition d’arbitrage** | **Impact potentiel** |
|-------------------|------------------------|-----------------------------|----------------------|
| **Délai de réponse pour les urgences vitales** | - Étape 2 : 08_regles_metier.md : "1 heure" <br> - Étape 2 : 09_conflits_objectifs.md : "30 minutes" | Adopter un délai de **30 minutes** pour les **urgences vitales** (ex : hémorragie intracrânienne) et **1 heure** pour les **urgences standard** (ex : ajustement thérapeutique). | Impact sur la priorisation et la réactivité du SIL. |
| **Critères de conformité des échantillons** | - Étape 1 : 04_contraintes_et_risques.md : "normes strictes" <br> - Étape 2 : 08_regles_metier.md : "non-respect des normes" | Définir une liste explicite des critères de conformité (ex : type de tube, volume, étiquetage) basée sur les normes CLSI GP41. | Impact sur la gestion des **rejets d’échantillon**. |
| **Transmission des informations cliniques** | - Étape 1 : 05_vision_globale_du_domaine.md : "absence de standardisation" <br> - Étape 2 : 08_regles_metier.md : "informations cliniques obligatoires" | Définir une liste standardisée des **informations cliniques** obligatoires (ex : anticoagulant, heure de la dernière prise, DFG). | Impact sur la qualité des prescriptions et des analyses. |

---
## **4. Synthèse des décisions stratégiques**

### **4.1. Classification stratégique des sous-domaines**
| **Sous-domaine** | **Classification** | **Justification** |
|------------------|--------------------|-------------------|
| **Prescription Médicale** | **Core** | Cœur du processus métier : sans prescription, pas de demande de dosage. |
| **Gestion des Urgences** | **Core** | Critique pour la sécurité des patients et la réactivité du circuit. |
| **Prélèvement et Conformité** | **Core** | Essentiel pour la qualité des résultats et la conformité réglementaire. |
| **Analyse Biologique** | **Core** | Au cœur du processus analytique et de la valeur ajoutée du laboratoire. |
| **Interprétation et Transmission** | **Core** | Essentiel pour la prise en charge clinique et la communication des résultats. |
| **Traçabilité et Sécurité** | **Supporting** | Support critique pour la conformité réglementaire et la sécurité des données. |
| **Gestion des Alertes et Exceptions** | **Supporting** | Support essentiel pour la réactivité et la gestion des exceptions. |
| **Intégration et Interopérabilité** | **Generic** | Commodité technique qui peut être externalisée ou standardisée. |

---
### **4.2. Recommandations pour l’étape 5 (modélisation DDD)**
- **Prioriser les sous-domaines "Core"** : Commencer par modéliser les sous-domaines **Prescription Médicale**, **Gestion des Urgences**, **Prélèvement et Conformité**, **Analyse Biologique** et **Interprétation et Transmission**.
- **Définir les bounded contexts** : Pour chaque sous-domaine, identifier les **bounded contexts** en fonction des règles métier et des acteurs.
- **Gérer les chevauchements** : Clarifier les responsabilités pour les zones de chevauchement (ex : **traçabilité**, **gestion des alertes**).
- **Valider les hypothèses** : Consulter les parties prenantes pour valider les hypothèses de découpage et les points à clarifier.
- **Documenter les règles métier** : Formaliser les règles métier pour chaque sous-domaine avant de passer à la modélisation tactique.

---
## **5. Annexe : Sources utilisées**
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
| **11_glossaire_metier.md** | Glossaire du langage commun avec termes canoniques. |
| **12_user_stories.md** | User stories formatées selon les conventions DDD. |
| **13_alignement_metier_technique.md** | Alignement entre vocabulaire métier et technique. |
| **14_exemples_langage_commun.md** | Exemples d’usage du langage commun. |
| **RGPD** | Règlement Général sur la Protection des Données. |
| **Normes ISO 15189** | Normes pour les laboratoires d'analyses de biologie médicale. |
| **Normes CLSI GP41** | Normes pour la gestion pré-analytique des échantillons biologiques. |