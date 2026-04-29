Voici une **proposition structurée de découpage en sous-domaines** pour le circuit des demandes urgentes de dosage anti-Xa, en appliquant les principes de Strategic Design (Eric Evans, Vaughn Vernon). Chaque sous-domaine est défini selon sa finalité métier, ses règles spécifiques, ses acteurs et ses interactions, puis classé en **Core**, **Supporting** ou **Generic** pour éclairer la priorisation des efforts.

---

---

## **1. Tableau récapitulatif des sous-domaines**

| **Sous-domaine** | **Type** | **Finalité métier** | **Règles spécifiques** | **Acteurs principaux** | **Interactions clés** |
|------------------|----------|---------------------|------------------------|------------------------|------------------------|
| **PrescriptionMédicale** | Core | Capturer et structurer les demandes de dosage anti-Xa en intégrant les informations cliniques critiques pour une interprétation fiable. | - Prescription obligatoire pour tout prélèvement. <br> - Champs obligatoires : anticoagulant, dose, heure dernière prise, DFG. <br> - Classification automatique en urgence vitale/standard. <br> - Alertes en cas de données manquantes ou incohérentes. | Médecins prescripteurs, SIL | → PrélèvementBiologique (prescription validée) <br> → GestionUrgences (niveau d'urgence) |
| **PrélèvementBiologique** | Core | Garantir la qualité et la traçabilité des échantillons biologiques depuis la collecte jusqu’au transport vers le laboratoire. | - Tubes citratés 3,2% ≥ 2 mL. <br> - Étiquetage complet (patient, heure, service). <br> - Délai de transport < 30 min. <br> - Rejet des échantillons non conformes. | Personnel infirmier, Biologiste, SIL | → AnalyseBiologique (échantillon conforme) <br> → GestionNonConformités (rejets) |
| **AnalyseBiologique** | Core | Réaliser les dosages anti-Xa en priorisant les demandes urgentes et en garantissant la qualité des résultats. | - Priorisation automatique des urgences. <br> - Délais de réponse : <30 min (vital), <1h (standard). <br> - Rejet des échantillons non conformes. | Techniciens de laboratoire, Biologiste, SIL | → ValidationClinique (résultats bruts) |
| **ValidationClinique** | Core | Interpréter les résultats des dosages anti-Xa en intégrant le contexte clinique pour formuler des recommandations thérapeutiques. | - Intégration du contexte clinique (traitement, DFG, heure dernière prise). <br> - Recommandations thérapeutiques claires. <br> - Transmission sécurisée des résultats. | Biologiste, Médecins prescripteurs | → TransmissionRésultats (résultats interprétés) |
| **TransmissionRésultats** | Supporting | Assurer la transmission sécurisée et traçable des résultats et interprétations aux acteurs concernés. | - Transmission en temps réel. <br> - Alertes en cas de dépassement des délais. <br> - Archivage conforme au RGPD. | SIL, Médecins prescripteurs | → TraçabilitéSécurisée (logs) |
| **GestionUrgences** | Supporting | Automatiser la priorisation et la gestion des demandes urgentes pour garantir une réactivité maximale. | - Classification automatique des urgences. <br> - Notifications en temps réel (SMS, email, interface SIL). <br> - Surveillance des délais de réponse. | SIL, Médecins prescripteurs, Biologiste | → AnalyseBiologique (priorisation) <br> → PrescriptionMédicale (niveau d'urgence) |
| **TraçabilitéSécurisée** | Supporting | Assurer la traçabilité complète et sécurisée de chaque étape du circuit, de la prescription à la transmission des résultats. | - Enregistrement systématique de toutes les étapes. <br> - Protection des données patients (RGPD). <br> - Génération d’alertes en cas de non-respect des règles. | SIL, Tous les acteurs | → Tous les sous-domaines (logs) |
| **GestionNonConformités** | Generic | Gérer les rejets d’échantillons et les alertes pour améliorer la qualité pré-analytique. | - Détection des non-conformités (tube, volume, étiquetage). <br> - Notifications aux acteurs concernés. <br> - Analyse des causes racines. | Biologiste, SIL | → PrélèvementBiologique (rejets) |

---

---

## **2. Description détaillée des sous-domaines**

---

### **2.1. Sous-domaine : PrescriptionMédicale**
**Nom canonique** : `PrescriptionMédicale`
**Type** : Core

#### **Finalité métier**
Centraliser la **création**, la **validation** et la **priorisation** des demandes de dosage anti-Xa en intégrant les **informations cliniques critiques** (anticoagulant, dose, heure de la dernière prise, DFG). Ce sous-domaine est le point d’entrée du circuit et déclenche toutes les étapes ultérieures.

#### **Règles spécifiques**
1. **Prescription obligatoire** :
   - Toute demande de dosage anti-Xa doit être précédée d’une **prescription médicale validée**.
   - *Source* : Étape 2 : 08_regles_metier.md (Règle de validation).

2. **Champs obligatoires** :
   - **Anticoagulant** (ex : apixaban, rivaroxaban).
   - **Dose** (en mg ou UI).
   - **Heure de la dernière prise**.
   - **DFG** (Débit de Filtration Glomérulaire, en mL/min).
   - *Source* : Étape 2 : 08_regles_metier.md (Contraintes d'information clinique).

3. **Classification automatique des urgences** :
   - **Urgence vitale** : Exemples : hémorragie intracrânienne, choc hémorragique → **délai de réponse < 30 min**.
   - **Urgence standard** : Exemples : ajustement thérapeutique → **délai de réponse < 1h**.
   - *Source* : Étape 2 : 08_regles_metier.md (Règles de priorité), Étape 3 : 13_alignement_metier_technique.md.

4. **Alertes automatiques** :
   - Le SIL génère une **alerte** si :
     - Un champ obligatoire est manquant.
     - Les données saisies sont incohérentes (ex : heure de la dernière prise dans le futur).
   - *Source* : Étape 2 : 08_regles_metier.md (Règles de validation).

#### **Acteurs principaux**
- **Médecins prescripteurs** (Urgences, Réanimation, Bloc opératoire).
- **SIL** (centralisation et validation des prescriptions).

#### **Interactions clés**
| **Cible** | **Type d'interaction** | **Données échangées** | **Format** |
|-----------|------------------------|-----------------------|------------|
| **PrélèvementBiologique** | Asynchrone (événement) | Prescription validée (avec niveau d'urgence) | JSON/XML |
| **GestionUrgences** | Synchrone | Niveau d'urgence (vital/standard) | Enum |

#### **Données manipulées**
| **Donnée** | **Description** | **Format** |
|------------|-----------------|------------|
| `prescription_medicale` | Demande de dosage anti-Xa avec informations cliniques. | Objet structuré (JSON/XML) |
| `identifiant_unique` | Identifiant unique de la prescription (UUID). | UUID |
| `niveau_urgence` | Niveau d'urgence (urgence_vitale, urgence_standard). | Enum |
| `statut_prescription` | Statut de la prescription (en_attente, validee, rejetee). | Enum |

#### **Frontières**
**Inclus** :
- Saisie des prescriptions médicales.
- Classification automatique des urgences.
- Génération d’alertes pour les erreurs de saisie.
- Intégration avec les systèmes de prescription existants (ex : DxCare).

**Exclus** :
- La vérification de la conformité des échantillons (géré par `PrélèvementBiologique`).
- L’analyse des dosages (géré par `AnalyseBiologique`).
- L’interprétation des résultats (géré par `ValidationClinique`).

---

### **2.2. Sous-domaine : PrélèvementBiologique**
**Nom canonique** : `PrélèvementBiologique`
**Type** : Core

#### **Finalité métier**
Garantir la **qualité** et la **traçabilité** des **échantillons biologiques** depuis la collecte jusqu’au transport vers le laboratoire, en vérifiant la conformité des tubes et en respectant les délais de transport.

#### **Règles spécifiques**
1. **Conformité des tubes** :
   - Type de tube : **citraté 3,2%**.
   - Volume ≥ **2 mL**.
   - *Source* : Étape 2 : 08_regles_metier.md (Contraintes de qualité pré-analytique).

2. **Étiquetage complet** :
   - Nom du patient.
   - Heure de prélèvement.
   - Service demandeur.
   - *Source* : Étape 2 : 08_regles_metier.md (Règles de validation).

3. **Délai de transport** :
   - Délai entre prélèvement et réception au laboratoire : **< 30 min**.
   - *Source* : Étape 2 : 08_regles_metier.md (Contraintes temporelles).

4. **Gestion des rejets** :
   - Si l’échantillon est non conforme, le SIL génère une **alerte** et notifie le personnel infirmier et le médecin prescripteur.
   - *Source* : Étape 2 : 08_regles_metier.md (Règles de rejet).

#### **Acteurs principaux**
- **Personnel infirmier** (réalisation des prélèvements).
- **Biologiste** (décision de rejet).
- **SIL** (vérification de la conformité, enregistrement des actes).

#### **Interactions clés**
| **Cible** | **Type d'interaction** | **Données échangées** | **Format** |
|-----------|------------------------|-----------------------|------------|
| **AnalyseBiologique** | Asynchrone (événement) | Échantillon conforme (avec identifiant unique) | JSON/XML |
| **GestionNonConformités** | Synchrone | Rejet d’échantillon (motif) | Objet structuré |

#### **Données manipulées**
| **Donnée** | **Description** | **Format** |
|------------|-----------------|------------|
| `echantillon_biologique` | Matériel biologique prélevé (sang) dans un tube. | Objet structuré |
| `tube_prelevement` | Type de tube (citrate_3.2%, volume, étiquetage). | Enum |
| `acte_prelevement` | Action de prélèvement (opérateur, heure, lieu). | Objet structuré |
| `statut_conformite` | Statut de conformité (conforme, non_conforme). | Enum |

#### **Frontières**
**Inclus** :
- Vérification de la conformité des tubes.
- Enregistrement des actes de prélèvement.
- Gestion des rejets d’échantillons non conformes.
- Respect des délais de transport.

**Exclus** :
- La prescription médicale (géré par `PrescriptionMédicale`).
- L’analyse des échantillons (géré par `AnalyseBiologique`).
- L’interprétation des résultats (géré par `ValidationClinique`).

---

### **2.3. Sous-domaine : AnalyseBiologique**
**Nom canonique** : `AnalyseBiologique`
**Type** : Core

#### **Finalité métier**
Réaliser les **dosages anti-Xa** en priorisant les demandes urgentes et en garantissant la qualité des résultats, tout en respectant les délais de réponse définis.

#### **Règles spécifiques**
1. **Priorisation automatique** :
   - Les demandes urgentes sont priorisées en fonction du niveau d’urgence (`urgence_vitale` ou `urgence_standard`).
   - *Source* : Étape 2 : 08_regles_metier.md (Règles de priorité).

2. **Délais de réponse** :
   - **Urgence vitale** : < 30 min.
   - **Urgence standard** : < 1h.
   - *Source* : Étape 2 : 08_regles_metier.md (Contraintes temporelles).

3. **Gestion des rejets** :
   - Les échantillons non conformes sont rejetés, et une **alerte** est générée.
   - *Source* : Étape 2 : 08_regles_metier.md (Règles de rejet).

4. **Traçabilité** :
   - Le SIL enregistre chaque analyse avec :
     - Identifiant unique de la demande.
     - Horodatage de début et de fin.
     - Nom du technicien responsable.
   - *Source* : Étape 2 : 08_regles_metier.md (Règles de traçabilité).

#### **Acteurs principaux**
- **Techniciens de laboratoire** (réalisation des analyses).
- **Biologiste** (validation des résultats).
- **SIL** (priorisation, enregistrement des résultats).

#### **Interactions clés**
| **Cible** | **Type d'interaction** | **Données échangées** | **Format** |
|-----------|------------------------|-----------------------|------------|
| **ValidationClinique** | Asynchrone (événement) | Résultat du dosage anti-Xa (valeur en UI/mL) | Nombre décimal |

#### **Données manipulées**
| **Donnée** | **Description** | **Format** |
|------------|-----------------|------------|
| `demande_priorisee` | Demande de dosage anti-Xa priorisée par le SIL. | Objet structuré |
| `resultat_dosage_anti_xa` | Résultat du dosage anti-Xa (valeur en UI/mL). | Nombre décimal |
| `statut_analyse` | Statut de l’analyse (en_cours, terminee, rejetee). | Enum |

#### **Frontières**
**Inclus** :
- Priorisation automatique des demandes urgentes.
- Réalisation des dosages anti-Xa.
- Gestion des rejets d’échantillons non conformes.
- Enregistrement des résultats dans le SIL.

**Exclus** :
- La prescription médicale (géré par `PrescriptionMédicale`).
- Le prélèvement biologique (géré par `PrélèvementBiologique`).
- L’interprétation des résultats (géré par `ValidationClinique`).

---

### **2.4. Sous-domaine : ValidationClinique**
**Nom canonique** : `ValidationClinique`
**Type** : Core

#### **Finalité métier**
Interpréter les **résultats des dosages anti-Xa** en intégrant le **contexte clinique** (traitement, fonction rénale, heure de la dernière prise) pour formuler des **recommandations thérapeutiques** claires et actionnables, et transmettre ces résultats aux **médecins prescripteurs** de manière sécurisée.

#### **Règles spécifiques**
1. **Intégration du contexte clinique** :
   - L’interprétation du résultat doit inclure :
     - Le contexte clinique (traitement, DFG, heure de la dernière prise).
     - La valeur du dosage anti-Xa.
     - Une recommandation thérapeutique (ex : "Sous-dosage probable, envisager une transfusion").
   - *Source* : Étape 1 : 03_concepts_metier_initiaux.md (Interprétation des résultats).

2. **Transmission sécurisée** :
   - Les résultats doivent être transmis aux **médecins prescripteurs** dans les délais de réponse définis.
   - *Source* : Étape 2 : 08_regles_metier.md (Règles de priorité).

3. **Traçabilité** :
   - Le SIL enregistre chaque interprétation avec :
     - Identifiant unique de la demande.
     - Horodatage de l’interprétation.
     - Nom du biologiste responsable.
   - *Source* : Étape 2 : 08_regles_metier.md (Règles de traçabilité).

#### **Acteurs principaux**
- **Biologiste** (réalisation des interprétations).
- **Médecins prescripteurs** (réception des résultats).
- **SIL** (transmission des résultats, traçabilité).

#### **Interactions clés**
| **Cible** | **Type d'interaction** | **Données échangées** | **Format** |
|-----------|------------------------|-----------------------|------------|
| **TransmissionRésultats** | Asynchrone (événement) | Résultat interprété (avec recommandation thérapeutique) | Texte structuré (JSON/XML) |

#### **Données manipulées**
| **Donnée** | **Description** | **Format** |
|------------|-----------------|------------|
| `contexte_clinique` | Informations médicales pertinentes pour l’interprétation. | Objet structuré |
| `resultat_dosage_anti_xa` | Résultat du dosage anti-Xa (valeur en UI/mL). | Nombre décimal |
| `interpretation_resultat` | Commentaire et recommandation thérapeutique du biologiste. | Texte structuré |
| `statut_transmission` | Statut de transmission des résultats (envoye, recue, lu). | Enum |

#### **Frontières**
**Inclus** :
- Intégration du contexte clinique dans l’interprétation.
- Rédaction d’interprétations claires et standardisées.
- Transmission sécurisée des résultats aux prescripteurs.
- Enregistrement des interprétations dans le SIL.

**Exclus** :
- La prescription médicale (géré par `PrescriptionMédicale`).
- Le prélèvement biologique (géré par `PrélèvementBiologique`).
- L’analyse biologique (géré par `AnalyseBiologique`).

---

### **2.5. Sous-domaine : TransmissionRésultats**
**Nom canonique** : `TransmissionRésultats`
**Type** : Supporting

#### **Finalité métier**
Assurer la **transmission sécurisée** et **traçable** des résultats et interprétations aux acteurs concernés (médecins prescripteurs), en respectant les délais de réponse et les exigences de confidentialité.

#### **Règles spécifiques**
1. **Transmission en temps réel** :
   - Les résultats interprétés sont transmis aux **médecins prescripteurs** dès validation par le biologiste.
   - *Source* : Étape 2 : 08_regles_metier.md (Règles de transmission).

2. **Alertes en cas de dépassement** :
   - Le SIL génère une **alerte** si le délai de réponse est dépassé.
   - *Source* : Étape 2 : 08_regles_metier.md (Règles de traçabilité).

3. **Archivage conforme au RGPD** :
   - Les données sont archivées pendant **20 ans** avec accès restreint.
   - *Source* : Étape 2 : 08_regles_metier.md (Contraintes réglementaires).

#### **Acteurs principaux**
- **SIL** (centralisation des données).
- **Médecins prescripteurs** (réception des résultats).

#### **Interactions clés**
| **Cible** | **Type d'interaction** | **Données échangées** | **Format** |
|-----------|------------------------|-----------------------|------------|
| **TraçabilitéSécurisée** | Asynchrone (événement) | Logs de transmission (destinataire, horodatage) | Objet structuré |

#### **Données manipulées**
| **Donnée** | **Description** | **Format** |
|------------|-----------------|------------|
| `resultat_interprete` | Résultat interprété avec recommandation thérapeutique. | Texte structuré |
| `statut_transmission` | Statut de transmission (envoye, recue, lu). | Enum |

#### **Frontières**
**Inclus** :
- Transmission sécurisée des résultats.
- Génération d’alertes en cas de dépassement des délais.
- Archivage conforme au RGPD.

**Exclus** :
- La prescription médicale (géré par `PrescriptionMédicale`).
- L’analyse biologique (géré par `AnalyseBiologique`).

---

### **2.6. Sous-domaine : GestionUrgences**
**Nom canonique** : `GestionUrgences`
**Type** : Supporting

#### **Finalité métier**
Automatiser la **priorisation** et la **gestion** des **demandes urgentes** pour garantir une réactivité maximale, en notifiant les acteurs concernés en temps réel et en surveillant les délais de réponse.

#### **Règles spécifiques**
1. **Classification automatique des urgences** :
   - Les demandes sont classées en :
     - **Urgence vitale** (ex : hémorragie intracrânienne) → **délai de réponse < 30 min**.
     - **Urgence standard** (ex : ajustement thérapeutique) → **délai de réponse < 1h**.
   - *Source* : Étape 2 : 08_regles_metier.md (Règles de priorité).

2. **Notifications en temps réel** :
   - Le SIL notifie les acteurs concernés via :
     - Interface SIL.
     - Email.
     - SMS (si configuré).
   - *Source* : Étape 2 : 09_conflits_objectifs.md (Conflit : Communication des informations vs. Délai de réponse).

3. **Surveillance des délais** :
   - Le SIL génère une **alerte** si :
     - Un délai de réponse est dépassé.
     - Une demande prioritaire n’est pas traitée dans les temps.
   - *Source* : Étape 2 : 08_regles_metier.md (Règles de traçabilité).

#### **Acteurs principaux**
- **SIL** (priorisation, notifications).
- **Médecins prescripteurs** (réception des alertes).
- **Biologiste** (réception des alertes).
- **Techniciens de laboratoire** (réception des alertes).

#### **Interactions clés**
| **Cible** | **Type d'interaction** | **Données échangées** | **Format** |
|-----------|------------------------|-----------------------|------------|
| **AnalyseBiologique** | Synchrone | Niveau d'urgence (priorisation) | Enum |
| **PrescriptionMédicale** | Synchrone | Niveau d'urgence (classification) | Enum |

#### **Données manipulées**
| **Donnée** | **Description** | **Format** |
|------------|-----------------|------------|
| `niveau_urgence` | Niveau d'urgence (urgence_vitale, urgence_standard). | Enum |
| `delai_reponse` | Délai de réponse cible (en minutes). | Entier |
| `notification` | Notification envoyée aux acteurs concernés. | Objet structuré |

#### **Frontières**
**Inclus** :
- Classification automatique des urgences.
- Notification en temps réel des acteurs.
- Surveillance des délais de réponse.
- Gestion dynamique des priorités.

**Exclus** :
- La prescription médicale (géré par `PrescriptionMédicale`).
- L’analyse biologique (géré par `AnalyseBiologique`).

---
### **2.7. Sous-domaine : TraçabilitéSécurisée**
**Nom canonique** : `TraçabilitéSécurisée`
**Type** : Supporting

#### **Finalité métier**
Assurer la **traçabilité complète** et **sécurisée** de chaque étape du circuit, de la **prescription médicale** à la **transmission des résultats**, tout en garantissant la protection des données patients conformément au RGPD.

#### **Règles spécifiques**
1. **Enregistrement systématique** :
   - Le SIL enregistre chaque étape du circuit avec :
     - Un **identifiant unique**.
     - Un horodatage précis.
     - Le nom de l’acteur responsable.
     - Le statut de l’étape (ex : "prescription validée", "échantillon conforme").
   - *Source* : Étape 2 : 08_regles_metier.md (Règles de traçabilité).

2. **Protection des données patients** :
   - Les données patients sont **chiffrées** (AES-256).
   - Les accès sont **restreints** et **tracés** (logs d’audit).
   - *Source* : Étape 2 : 08_regles_metier.md (Contraintes réglementaires).

3. **Génération d’alertes** :
   - Le SIL génère une **alerte** si :
     - Un délai de réponse est dépassé.
     - Une étape du circuit n’est pas enregistrée dans les délais.
     - Une non-conformité est détectée.
   - *Source* : Étape 2 : 08_regles_metier.md (Règles de traçabilité).

4. **Archivage** :
   - Les données sont archivées pendant **20 ans** avec accès restreint.
   - *Source* : Étape 2 : 08_regles_metier.md (Contraintes réglementaires).

#### **Acteurs principaux**
- **SIL** (centralisation des données).
- **Tous les acteurs** (consultation de la traçabilité).

#### **Interactions clés**
| **Cible** | **Type d'interaction** | **Données échangées** | **Format** |
|-----------|------------------------|-----------------------|------------|
| **Tous les sous-domaines** | Asynchrone (événement) | Logs de traçabilité (étapes, horodatages) | Objet structuré |

#### **Données manipulées**
| **Donnée** | **Description** | **Format** |
|------------|-----------------|------------|
| `traçabilité` | Historique complet des étapes du circuit. | Liste d’objets structurés |
| `alerte` | Notification automatique en cas de non-respect des règles. | Objet structuré |
| `logs_accès` | Journal des accès au SIL (qui, quand, quoi). | Fichier log structuré |

#### **Frontières**
**Inclus** :
- Enregistrement systématique de toutes les étapes du circuit.
- Génération d’alertes en cas de non-respect des règles.
- Archivage sécurisé des données.
- Protection des données patients (RGPD).

**Exclus** :
- La réalisation des analyses (géré par `AnalyseBiologique`).
- L’interprétation des résultats (géré par `ValidationClinique`).

---
### **2.8. Sous-domaine : GestionNonConformités**
**Nom canonique** : `GestionNonConformités`
**Type** : Generic

#### **Finalité métier**
Gérer les **rejets d’échantillons** et les **alertes** pour améliorer la qualité pré-analytique, en détectant les non-conformités (tube, volume, étiquetage) et en notifiant les acteurs concernés.

#### **Règles spécifiques**
1. **Détection des non-conformités** :
   - Le SIL vérifie :
     - Type de tube (citraté 3,2%).
     - Volume ≥ 2 mL.
     - Étiquetage complet (nom du patient, heure de prélèvement).
   - *Source* : Étape 2 : 08_regles_metier.md (Règles de validation).

2. **Gestion des rejets** :
   - Si un échantillon est non conforme, le SIL :
     - Génère une **alerte** pour le biologiste.
     - Notifie le personnel infirmier et le médecin prescripteur.
     - Enregistre le rejet dans la traçabilité.
   - *Source* : Étape 2 : 08_regles_metier.md (Règles de rejet).

3. **Amélioration continue** :
   - Le SIL fournit des rapports de qualité pour identifier les causes récurrentes de non-conformité.
   - *Source* : Étape 2 : 09_conflits_objectifs.md (Conflit : Charge du personnel infirmier vs. Traçabilité).

#### **Acteurs principaux**
- **Biologiste** (décision de rejet).
- **SIL** (enregistrement des rejets, génération d’alertes).

#### **Interactions clés**
| **Cible** | **Type d'interaction** | **Données échangées** | **Format** |
|-----------|------------------------|-----------------------|------------|
| **PrélèvementBiologique** | Synchrone | Rejet d’échantillon (motif) | Objet structuré |

#### **Données manipulées**
| **Donnée** | **Description** | **Format** |
|------------|-----------------|------------|
| `conformite_echantillon` | Résultat de la vérification de conformité. | Enum |
| `motif_rejet` | Motif du rejet (ex : tube EDTA, volume insuffisant). | Texte structuré |
| `alerte_qualite` | Alerte générée en cas de non-conformité. | Objet structuré |

#### **Frontières**
**Inclus** :
- Vérification de la conformité des échantillons.
- Gestion des rejets d’échantillons non conformes.
- Génération de rapports de qualité.

**Exclus** :
- La prescription médicale (géré par `PrescriptionMédicale`).
- L’analyse biologique (géré par `AnalyseBiologique`).

---

---

## **3. Zones de chevauchement et couplages**

| **Sous-domaines en chevauchement** | **Points de chevauchement** | **Risques identifiés** | **Proposition d'arbitrage** |
|------------------------------------|-----------------------------|------------------------|-----------------------------|
| **PrescriptionMédicale** ↔ **GestionUrgences** | - La **prescription médicale** inclut le niveau d’urgence, qui influence la priorisation dans **GestionUrgences**. | - Risque de désynchronisation entre les deux sous-domaines. | **Solution** : **PrescriptionMédicale** classe l’urgence lors de la saisie, et **GestionUrgences** applique la priorisation automatique. Utiliser un **identifiant unique** commun pour lier les deux sous-domaines. |
| **PrélèvementBiologique** ↔ **GestionNonConformités** | - La conformité de l’**échantillon biologique** (vérifiée dans **PrélèvementBiologique**) impacte directement **GestionNonConformités**. | - Risque de rejet tardif si la non-conformité n’est pas détectée rapidement. | **Solution** : **PrélèvementBiologique** vérifie la conformité et transmet le statut à **GestionNonConformités**, qui gère les rejets et les alertes. |
| **AnalyseBiologique** ↔ **ValidationClinique** | - Le résultat du **dosage anti-Xa** (généré dans **AnalyseBiologique**) est utilisé pour l’**interprétation des résultats** (dans **ValidationClinique**). | - Risque de perte de données si le résultat n’est pas correctement transmis. | **Solution** : Utiliser un **identifiant unique** pour lier le résultat de l’analyse à son interprétation. Le SIL garantit que le résultat est disponible dans **ValidationClinique** avant que le biologiste ne commence son travail. |
| **TraçabilitéSécurisée** ↔ **Tous les sous-domaines** | - Tous les sous-domaines doivent enregistrer leurs actions dans la **traçabilité**. | - Risque de duplication des données si chaque sous-domaine enregistre sa propre traçabilité. | **Solution** : **TraçabilitéSécurisée** est le **sous-domaine unique** responsable de la traçabilité globale. Tous les autres sous-domaines envoient leurs événements à **TraçabilitéSécurisée** via une interface dédiée. |
| **GestionUrgences** ↔ **PrescriptionMédicale** | - La **priorisation des urgences** (dans **GestionUrgences**) dépend du niveau d’urgence défini dans la **prescription médicale** (dans **PrescriptionMédicale**). | - Risque de classification incorrecte des urgences. | **Solution** : **GestionUrgences** s’abonne aux événements de **PrescriptionMédicale** pour mettre à jour automatiquement la priorisation. Utiliser un **événement métier** (ex : `PrescriptionValidee`) pour déclencher la priorisation. |

---

---

## **4. Classification stratégique et priorisation**

### **4.1. Sous-domaines Core (Cœur stratégique)**
| **Sous-domaine** | **Justification** | **Acteurs clés** | **Priorité de conception** |
|------------------|-------------------|------------------|----------------------------|
| **PrescriptionMédicale** | - Point d’entrée du circuit. <br> - Déclenche toutes les étapes ultérieures. <br> - Impact direct sur la sécurité des patients. | Médecins prescripteurs, SIL | **Élevée** (à concevoir en premier) |
| **AnalyseBiologique** | - Réalise les dosages anti-Xa. <br> - Doit respecter les délais critiques. <br> - Impact direct sur la prise en charge des patients. | Techniciens de laboratoire, Biologiste, SIL | **Élevée** |
| **ValidationClinique** | - Fournit des recommandations thérapeutiques. <br> - Doit être claire et actionnable. <br> - Impact direct sur la décision médicale. | Biologiste, Médecins prescripteurs | **Élevée** |
| **GestionUrgences** | - Améliore la réactivité. <br> - Doit être intégré aux autres sous-domaines. <br> - Critique pour la sécurité des patients. | SIL, Médecins prescripteurs, Biologiste | **Élevée** |

---
### **4.2. Sous-domaines Supporting (Support métier)**
| **Sous-domaine** | **Justification** | **Acteurs clés** | **Priorité de conception** |
|------------------|-------------------|------------------|----------------------------|
| **PrélèvementBiologique** | - Garantit la qualité des échantillons. <br> - Évite les rejets inutiles. <br> - Impacte directement la sécurité des patients. | Personnel infirmier, Biologiste, SIL | **Moyenne** (à concevoir après les Core) |
| **TransmissionRésultats** | - Assure la transmission sécurisée des résultats. <br> - Doit respecter les délais et la confidentialité. | SIL, Médecins prescripteurs | **Moyenne** |
| **TraçabilitéSécurisée** | - Nécessaire pour la conformité réglementaire. <br> - Doit être centralisé et sécurisé. | SIL, Tous les acteurs | **Moyenne** |

---
### **4.3. Sous-domaine Generic (Commodité interchangeable)**
| **Sous-domaine** | **Justification** | **Acteurs clés** | **Priorité de conception** |
|------------------|-------------------|------------------|----------------------------|
| **GestionNonConformités** | - Peut être partiellement externalisé. <br> - Moins critique pour la sécurité des patients. | Biologiste, SIL | **Faible** (à externaliser ou standardiser) |

---

---
## **5. Hypothèses de découpage et points à valider**

### **5.1. Hypothèses de découpage**
| **Hypothèse** | **Justification** | **Risques** | **Points à valider** |
|---------------|-------------------|-------------|----------------------|
| **Séparation claire entre PrescriptionMédicale et AnalyseBiologique** | - Les deux sous-domaines ont des finalités et des acteurs distincts. <br> - La prescription est un acte médical, tandis que l’analyse est un acte technique. | - Risque de désynchronisation entre les deux sous-domaines. | Valider avec les **médecins prescripteurs** et les **techniciens de laboratoire** que la séparation est pertinente et ne complique pas leur travail. |
| **Centralisation de la traçabilité dans TraçabilitéSécurisée** | - La traçabilité est un besoin transverse à tous les sous-domaines. <br> - Un sous-domaine dédié évite la duplication des données. | - Risque de goulot d’étranglement si TraçabilitéSécurisée devient trop sollicité. | Valider avec l’**équipe SIL** que cette centralisation est techniquement réalisable et performante. |
| **Séparation entre GestionNonConformités et PrélèvementBiologique** | - GestionNonConformités se concentre sur la gestion des rejets, tandis que PrélèvementBiologique se concentre sur l’enregistrement de l’acte. <br> - Évite la redondance des vérifications. | - Risque de manque de coordination entre les deux sous-domaines. | Valider avec les **techniciens de laboratoire** et les **biologistes** que cette séparation est claire et ne crée pas de confusion. |

---
### **5.2. Points à valider auprès du métier**
| **Point à valider** | **Contexte** | **Questions à poser** | **Acteurs à consulter** |
|---------------------|--------------|-----------------------|-------------------------|
| **Critères de conformité des tubes de prélèvement** | Aucune liste explicite des normes de tubes ou de volumes n’est fournie dans le corpus. | - Quels sont les types de tubes acceptés (ex : tube citraté 3,2%) ? <br> - Quel est le volume minimal requis pour l’analyse ? <br> - Quels sont les protocoles d’étiquetage (ex : étiquette machine-readable, nom du patient, heure de prélèvement) ? | Biologiste, Techniciens de laboratoire, Personnel infirmier |
| **Mécanismes de priorisation des demandes urgentes** | Le corpus mentionne des délais de *"1 heure"* et *"30 minutes"* pour les urgences, mais aucune définition claire des critères pour distinguer une urgence vitale d’une urgence standard. | - Quels sont les critères de classement des urgences (ex : score clinique, type d’anticoagulant, fonction rénale) ? <br> - Quels sont les délais de réponse cibles par niveau de priorité ? | Médecins prescripteurs (Urgences, Réanimation), Biologiste |
| **Protocole standardisé de transmission des informations cliniques** | Aucune standardisation n’est décrite dans le corpus, bien que cela soit identifié comme un irritant métier. | - Quels sont les champs obligatoires à remplir dans la prescription (ex : nom de l’anticoagulant, dose, heure de la dernière prise, DFG) ? <br> - Quel est le format de transmission (ex : champ libre, liste déroulante, intégration automatique depuis le dossier patient) ? | Médecins prescripteurs, Personnel infirmier, Biologiste |
| **Intégration avec les systèmes existants** | Aucune information n’est fournie sur la compatibilité du SIL avec les logiciels de prescription (ex : DxCare, Cristal) ou les automates de dosage anti-Xa. | - Quels sont les systèmes existants à intégrer (ex : DxCare, Cristal) ? <br> - Quelle est la capacité d’interfaçage avec les automates de dosage anti-Xa ? | Équipe SIL, Biologiste, Équipe informatique |

---
## **6. Synthèse des décisions stratégiques**

### **6.1. Sous-domaines Core (prioritaires pour la conception)**
- **PrescriptionMédicale** : À concevoir en premier, car c’est le point d’entrée du circuit.
- **AnalyseBiologique** : Critique pour la réalisation des dosages et le respect des délais.
- **ValidationClinique** : Essentielle pour l’interprétation des résultats et les recommandations thérapeutiques.
- **GestionUrgences** : Améliore la réactivité et doit être intégré aux autres sous-domaines.

### **6.2. Sous-domaines Supporting (à concevoir après les Core)**
- **PrélèvementBiologique** : Garantit la qualité des échantillons.
- **TransmissionRésultats** : Assure la transmission sécurisée des résultats.
- **TraçabilitéSécurisée** : Nécessaire pour la conformité réglementaire.

### **6.3. Sous-domaine Generic (à externaliser ou standardiser)**
- **GestionNonConformités** : Peut être partiellement externalisé (ex : outils de vision par ordinateur pour la détection des étiquettes).

---
## **7. Annexe : Sources et références**

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
| **11_glossaire_metier.md** | Glossaire du langage commun (termes canoniques). |
| **12_ambiguites_resolues.md** | Arbitrages terminologiques et résolution des ambiguïtés. |
| **13_alignement_metier_technique.md** | Alignement entre vocabulaire métier et technique. |
| **14_exemples_langage_commun.md** | Exemples d’usage du langage commun. |
| **Normes ISO 15189** | Normes pour les laboratoires d'analyses de biologie médicale. |
| **Normes CLSI GP41** | Normes pour la gestion pré-analytique des échantillons biologiques. |
| **RGPD** | Règlement Général sur la Protection des Données. |

---
## **8. Conclusion**
Ce découpage en sous-domaines permet de :
1. **Prioriser les efforts de conception** en se concentrant sur les sous-domaines **Core** (PrescriptionMédicale, AnalyseBiologique, ValidationClinique, GestionUrgences).
2. **Réduire la complexité globale** en isolant les préoccupations métiers dans des sous-domaines cohérents.
3. **Clarifier les interactions** entre sous-domaines pour éviter les couplages forts inutiles.
4. **Préparer la phase de tactical design (Step 5)** en définissant des frontières claires et des responsabilités métiers.

**Prochaine étape** : Valider ce découpage avec les parties prenantes (médecins, biologistes, équipe SIL) avant de passer à la modélisation tactique (bounded contexts, agrégats, événements).