Voici une synthèse structurée et actionnable pour finaliser l'étape 4 (découpage en sous-domaines) et préparer l'étape 5 (modélisation tactique DDD), en intégrant les éléments clés des échanges précédents et en respectant le langage commun établi.

---

# **Découpage en Sous-domaines Stratégiques**
**Domaine** : Circuit des demandes urgentes de dosage anti-Xa
**Étape** : 4 (Modélisation stratégique DDD)
**Date** : [À compléter]

---

## **1. Tableau Récapitulatif des Sous-domaines**

| **Sous-domaine**               | **Finalité Métier**                                                                                     | **Stratégie** | **Acteurs Principaux**                     | **Règles Métier Clés**                                                                                     | **Données/Informations Manipulées**                                                                                     | **Frontières**                                                                                     |
|---------------------------------|---------------------------------------------------------------------------------------------------------|---------------|--------------------------------------------|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| **Prescription Médicale**       | Capturer et valider les prescriptions médicales avec informations cliniques obligatoires.               | **Core**      | Médecins prescripteurs, SIL                | - Prescription complète : anticoagulant, dose, heure dernière prise, DFG, motif. <br> - Classification automatique en **urgence vitale**/**urgence standard**. <br> - Alertes pour champs manquants. | `prescription_medicale`, `niveau_urgence`, `identifiant_unique`, `informations_cliniques_obligatoires` | **Inclus** : Saisie, validation, classification. <br> **Exclus** : Prélèvement, analyse, interprétation. |
| **Gestion des Urgences**        | Prioriser et gérer les demandes urgentes en fonction de leur criticité.                                | **Core**      | SIL, Techniciens de laboratoire             | - **Urgence vitale** : réponse < 30 min (ex : hémorragie intracrânienne). <br> - **Urgence standard** : réponse < 1h. <br> - Génération d’alertes en cas de dépassement. | `niveau_urgence`, `delai_reponse`, `alerte`, `identifiant_unique`                                                      | **Inclus** : Priorisation, suivi des délais. <br> **Exclus** : Saisie des prescriptions, transmission des résultats. |
| **Prélèvement et Conformité**   | Réaliser le prélèvement des échantillons et vérifier leur conformité avant analyse.                     | **Core**      | Personnel infirmier, SIL, Biologiste       | - Tube citraté 3,2%, volume ≥ 2 mL. <br> - Étiquetage complet (nom patient, date, heure). <br> - Rejet des échantillons non conformes + notification. | `echantillon_biologique`, `conformite_echantillon`, `motif_rejet`, `identifiant_unique`                                | **Inclus** : Prélèvement, vérification de conformité. <br> **Exclus** : Prescription (amont), analyse (aval). |
| **Analyse Biologique**          | Réaliser le dosage anti-Xa et valider les résultats techniques.                                        | **Core**      | Techniciens de laboratoire, Biologiste     | - Dosage anti-Xa selon normes du laboratoire. <br> - Validation technique de l’échantillon. <br> - Rejet si non conforme. | `resultat_dosage_anti_xa`, `statut_conformite`, `motif_rejet`, `identifiant_unique`                                      | **Inclus** : Réalisation du dosage, validation technique. <br> **Exclus** : Interprétation clinique (aval). |
| **Interprétation et Transmission** | Interpréter les résultats du dosage et les transmettre aux prescripteurs de manière sécurisée.      | **Core**      | Biologiste, SIL, Médecins prescripteurs    | - Interprétation incluant **contexte clinique** (traitement, DFG, heure dernière prise). <br> - Transmission sécurisée dans les délais. <br> - Archivage des résultats. | `interpretation_resultat`, `contexte_clinique`, `resultat_dosage_anti_xa`, `delai_transmission`                          | **Inclus** : Validation, interprétation, transmission. <br> **Exclus** : Analyse technique (aval). |
| **Traçabilité et Sécurité**     | Assurer la traçabilité complète et la sécurité des données patients (RGPD, ISO 15189).                | **Supporting**| SIL, Équipe qualité                        | - Enregistrement systématique de chaque étape avec horodatage et identifiant unique. <br> - Chiffrement AES-256. <br> - Archivage 20 ans. | `traçabilité`, `logs_securite`, `identifiant_unique`, `données_patients_chiffrées`                                      | **Inclus** : Enregistrement, archivage, consultation des historiques. <br> **Exclus** : Actions métiers (prescription, analyse). |
| **Gestion des Alertes**         | Surveiller les dépassements de délais et gérer les exceptions (ex : rejets d’échantillons).             | **Supporting**| SIL, Biologiste, Médecins prescripteurs    | - Alertes pour échantillons non conformes ou délais dépassés. <br> - Gestion manuelle des urgences non prévues. | `alerte`, `motif_alerte`, `statut_exception`, `identifiant_unique`                                                     | **Inclus** : Surveillance, gestion des exceptions. <br> **Exclus** : Transmission des résultats (aval). |
| **Intégration et Interopérabilité** | Assurer l’intégration avec les systèmes externes (automates, logiciels de prescription).              | **Generic**   | Équipe SIL, Équipe informatique             | - Interface avec automates via API sécurisée. <br> - Compatibilité avec DxCare, Cristal. <br> - Conformité HL7/FHIR. | `api_automate`, `fichier_hl7`, `données_patients`                                                                       | **Inclus** : Intégration technique. <br> **Exclus** : Fonctionnalités métiers. |

---

## **2. Classification Stratégique Détaillée**

### **2.1. Sous-domaines Core (Cœur Métier)**
**Critères** :
- Valeur clinique directe (sécurité patient, différenciation concurrentielle).
- Fréquence d’usage élevée (quotidienne).
- Risque réglementaire élevé (ISO 15189, CLSI GP41).
- Difficile à externaliser (processus métier unique).

| **Sous-domaine**               | **Investissement Recommandé** | **Justification**                                                                                     | **Risques en Cas de Négligence**                                                                                     |
|---------------------------------|-------------------------------|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| **Prescription Médicale**       | 30-40% du budget              | Point d’entrée critique pour le circuit. Une prescription incomplète entraîne des erreurs d’interprétation. | Prescriptions erronées → risques pour le patient, non-conformité RGPD.                                                  |
| **Gestion des Urgences**        | 25-35% du budget              | Priorisation automatique des urgences vitales (<30 min) et standard (<1h).                          | Retards dans les traitements critiques → risques médico-légaux.                                                       |
| **Prélèvement et Conformité**   | 20-30% du budget              | Garantit la qualité des échantillons pour des résultats fiables.                                     | Échantillons non conformes → résultats erronés, rejets répétés.                                                      |
| **Analyse Biologique**          | 20-25% du budget              | Réalisation du dosage anti-Xa, cœur du processus analytique.                                         | Dosages erronés → décisions thérapeutiques incorrectes.                                                               |
| **Interprétation et Transmission** | 15-20% du budget           | Interprétation clinique des résultats et transmission sécurisée.                                    | Résultats mal interprétés ou non transmis → risques pour le patient.                                                  |

---

### **2.2. Sous-domaines Supporting (Support Métier)**
**Critères** :
- Valeur clinique indirecte (support aux processus Core).
- Risque réglementaire élevé (RGPD, traçabilité).
- Peut être externalisé partiellement.

| **Sous-domaine**               | **Investissement Recommandé** | **Justification**                                                                                     | **Risques en Cas de Négligence**                                                                                     |
|---------------------------------|-------------------------------|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| **Traçabilité et Sécurité**     | 10-15% du budget              | Conformité RGPD et ISO 15189 (archivage 20 ans, chiffrement).                                         | Non-conformité → sanctions légales, perte de confiance des patients.                                                   |
| **Gestion des Alertes**         | 5-10% du budget               | Surveillance des délais et gestion des exceptions (ex : rejets d’échantillons).                      | Alertes ignorées → retards dans la prise en charge.                                                                  |

---

### **2.3. Sous-domaine Generic (Commodité)**
**Critères** :
- Processus technique standardisable.
- Solutions du marché disponibles (SaaS, middleware).

| **Sous-domaine**               | **Investissement Recommandé** | **Justification**                                                                                     | **Solutions du Marché**                                                                                                |
|---------------------------------|-------------------------------|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| **Intégration et Interopérabilité** | 5-10% du budget           | Intégration avec automates (ex : Sysmex, Stago) et logiciels de prescription (DxCare, Cristal).       | MuleSoft, Apache Camel, Epic/Cerner (HL7/FHIR).                                                                       |

---

## **3. Interactions entre Sous-domaines**

### **3.1. Tableau des Interactions Clés**

| **Source**                  | **Cible**                     | **Information/Decision Échangée**                                                                     | **Trigger**                          | **Mode**       | **Format**               | **Criticité** | **Risque de Couplage** | **Points d'Attention**                                                                                     |
|-----------------------------|-------------------------------|-------------------------------------------------------------------------------------------------------|--------------------------------------|----------------|--------------------------|----------------|-------------------------|-------------------------------------------------------------------------------------------------------------|
| **Prescription Médicale**   | **Gestion des Urgences**      | `prescription_medicale` + `niveau_urgence`                                                          | Saisie de la prescription            | Asynchrone     | JSON/XML                 | Critique       | Fort                    | Validation des champs obligatoires, classification automatique de l’urgence.                              |
| **Prescription Médicale**   | **Traçabilité et Sécurité**   | `identifiant_unique` + horodatage                                                                   | Validation de la prescription        | Synchrone      | Événement                | Critique       | Faible                  | Enregistrement immédiat pour traçabilité.                                                                   |
| **Gestion des Urgences**    | **Prélèvement et Conformité** | `niveau_urgence` + `identifiant_unique`                                                              | Priorisation validée                 | Asynchrone     | JSON/XML                 | Critique       | Moyen                   | Transmission des priorités au personnel infirmier.                                                          |
| **Prélèvement et Conformité** | **Analyse Biologique**       | `echantillon_biologique` + `conformite_echantillon` + `identifiant_unique`                          | Validation de l’échantillon          | Asynchrone     | JSON/XML                 | Critique       | Fort                    | Rejet immédiat si non conforme.                                                                             |
| **Analyse Biologique**      | **Interprétation et Transmission** | `resultat_dosage_anti_xa` + `statut_conformite`                                                  | Dosage terminé                       | Asynchrone     | JSON/XML                 | Critique       | Moyen                   | Intégration du contexte clinique dans l’interprétation.                                                    |
| **Interprétation et Transmission** | **Gestion des Urgences** | `delai_transmission` + `alerte` (si dépassement)                                                    | Transmission des résultats           | Asynchrone     | Événement                | Critique       | Faible                  | Génération d’alertes en cas de retard.                                                                     |
| **Traçabilité et Sécurité** | Tous les sous-domaines       | `traçabilité` (horodatage, identifiant unique) + `logs_securite`                                    | Toute action métier                  | Synchrone      | Événement                | Critique       | Faible                  | Centralisation des logs pour RGPD et ISO 15189.                                                            |
| **Gestion des Alertes**     | **Prescription Médicale**     | `alerte` (ex : prescription incomplète) + `motif_alerte`                                            | Détection d’une exception            | Asynchrone     | Notification             | Élevé          | Moyen                   | Notification en temps réel aux prescripteurs.                                                              |
| **Intégration et Interopérabilité** | **Analyse Biologique** | `api_automate` (données pour dosage)                                                                | Lancement de l’analyse               | Synchrone      | API REST/JSON            | Critique       | Faible                  | Compatibilité avec les automates (ex : Sysmex).                                                            |

---

### **3.2. Flux Métier Global (Séquentiel)**
1. **Prescription Médicale** :
   - Médecin prescripteur saisit une `prescription_medicale` avec les `informations_cliniques_obligatoires`.
   - SIL valide la complétude et classe l’urgence (`urgence_vitale`/**urgence_standard**).
   - Enregistrement synchrone dans **Traçabilité et Sécurité**.

2. **Gestion des Urgences** :
   - Transmission asynchrone du `niveau_urgence` à **Prélèvement et Conformité**.

3. **Prélèvement et Conformité** :
   - Personnel infirmier réalise l’`acte_prelevement`.
   - Vérification de la `conformite_echantillon` (tube citraté 3,2%, volume ≥ 2 mL, étiquetage complet).
   - Rejet immédiat si non conforme + notification via **Gestion des Alertes**.

4. **Analyse Biologique** :
   - Technicien de laboratoire réalise le `dosage_anti_xa`.
   - Validation technique de l’échantillon (lien avec **Prélèvement et Conformité**).

5. **Interprétation et Transmission** :
   - Biologiste interprète les résultats avec le `contexte_clinique` (traitement, DFG, heure dernière prise).
   - Transmission sécurisée des résultats aux prescripteurs dans les délais.

6. **Traçabilité et Sécurité** :
   - Enregistrement de chaque étape (prescription → prélèvement → analyse → transmission).
   - Archivage sécurisé des données (RGPD, 20 ans).

7. **Gestion des Alertes** :
   - Surveillance des délais et gestion des exceptions (ex : rejets, dépassements).

8. **Intégration et Interopérabilité** :
   - Interface avec les automates (ex : Sysmex) via API sécurisée.

---

## **4. Zones de Chevauchement et Conflits à Arbitrer**

| **Sous-domaines Concernés**       | **Problème de Chevauchement**                                                                         | **Proposition d'Arbitrage**                                                                                     | **Points à Valider**                                                                                     |
|------------------------------------|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| **Prescription Médicale ↔ Gestion des Urgences** | Qui met à jour manuellement le `niveau_urgence` en cas d’évolution clinique ?                        | - **Prescription Médicale** : Saisie initiale et validation. <br> - **Gestion des Urgences** : Priorisation automatique et suivi des délais. | Faut-il une validation manuelle par le biologiste en cas de changement de situation ?                   |
| **Prélèvement et Conformité ↔ Analyse Biologique** | Où placer la logique de rejet des échantillons non conformes ?                                        | - **Prélèvement et Conformité** : Vérification initiale par l’IDE. <br> - **Analyse Biologique** : Validation technique finale. | Peut-on centraliser la logique de rejet dans **Prélèvement et Conformité** ?                             |
| **Traçabilité et Sécurité**        | Faut-il fusionner avec **Gestion des Alertes** ou garder séparé ?                                     | - **Traçabilité et Sécurité** : Enregistrement des logs. <br> - **Gestion des Alertes** : Surveillance et notifications. | La traçabilité est transverse → à garder séparé pour la clarté.                                          |
| **Interprétation et Transmission ↔ Gestion des Urgences** | Qui gère les alertes en cas de retard de transmission ?                                              | - **Interprétation et Transmission** : Transmission des résultats. <br> - **Gestion des Urgences** : Surveillance des délais. | Clarifier les responsabilités entre biologiste et SIL.                                                   |

---

## **5. Hypothèses et Points à Valider avec les Parties Prenantes**

| **Hypothèse**                                                                                     | **Sous-domaine Concerné**       | **Impact Potentiel**                                                                                     | **Méthode de Validation**                                                                                     |
|--------------------------------------------------------------------------------------------------|----------------------------------|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Les **urgences vitales** doivent avoir un délai de réponse < 30 min.                              | Gestion des Urgences            | Risque de non-conformité si délai non respecté.                                                          | Valider avec les médecins prescripteurs et biologistes.                                                      |
| Les **échantillons biologiques** doivent être prélevés dans des tubes citratés 3,2%.             | Prélèvement et Conformité       | Risque de rejet des échantillons si tube incorrect.                                                      | Valider avec le personnel infirmier et les techniciens de laboratoire.                                       |
| Le **contexte clinique** (traitement, DFG, heure dernière prise) doit être intégré dans l’interprétation. | Interprétation et Transmission | Risque d’interprétation erronée sans contexte.                                                           | Valider avec les biologistes.                                                                                 |
| Le **SIL** doit générer une alerte en cas de prescription incomplète.                            | Prescription Médicale            | Risque de non-respect des champs obligatoires.                                                           | Valider avec l’équipe SIL et les prescripteurs.                                                              |
| Les **données patients** doivent être chiffrées (AES-256) et archivées 20 ans.                    | Traçabilité et Sécurité         | Risque de non-conformité RGPD.                                                                           | Valider avec l’équipe qualité et le responsable RGPD.                                                       |
| L’**intégration avec les automates** doit se faire via une API REST/JSON sécurisée.               | Intégration et Interopérabilité | Risque de blocage du processus analytique.                                                              | Valider avec l’équipe informatique et les fournisseurs d’automates (ex : Sysmex).                            |

---

## **6. Recommandations pour l'Étape 5 (Modélisation Tactique DDD)**

### **6.1. Priorités pour la Modélisation**
1. **Sous-domaines Core** :
   - **Prescription Médicale** : Modéliser un **bounded context** `prescription_validation` avec :
     - **Agrégat** : `PrescriptionMedicale` (racine).
     - **Entités** : `Patient`, `Prescripteur`, `InformationClinique`.
     - **Value Objects** : `NiveauUrgence`, `IdentifiantUnique`.
     - **Domain Events** : `PrescriptionValidee`, `UrgenceClassee`.
   - **Gestion des Urgences** : Modéliser un **bounded context** `urgence_priorisation` avec :
     - **Agrégat** : `DemandeUrgente` (racine).
     - **Entités** : `NiveauUrgence`, `DelaiCible`.
     - **Domain Events** : `UrgenceVitaleDetectee`, `DelaiDepasse`.
   - **Prélèvement et Conformité** : Modéliser un **bounded context** `prelevement_conformite` avec :
     - **Agrégat** : `EchantillonBiologique` (racine).
     - **Entités** : `TubePrelevement`, `ActePrelevement`.
     - **Value Objects** : `StatutConformite`, `MotifRejet`.
     - **Domain Events** : `EchantillonRejete`, `ConformiteValidee`.
   - **Analyse Biologique** : Modéliser un **bounded context** `analyse_biologique` avec :
     - **Agrégat** : `DosageAntiXa` (racine).
     - **Entités** : `ResultatDosage`, `Automate`.
     - **Domain Events** : `DosageTermine`, `ResultatValide`.
   - **Interprétation et Transmission** : Modéliser un **bounded context** `interpretation_transmission` avec :
     - **Agrégat** : `InterpretationResultat` (racine).
     - **Entités** : `Biologiste`, `Prescripteur`.
     - **Value Objects** : `ContexteClinique`, `DelaiTransmission`.
     - **Domain Events** : `ResultatTransmis`, `InterpretationValidee`.

2. **Sous-domaines Supporting** :
   - **Traçabilité et Sécurité** : Modéliser un **bounded context** `tracabilite_securite` avec :
     - **Agrégat** : `Trace` (racine).
     - **Entités** : `Horodatage`, `LogSecurite`.
     - **Domain Events** : `EtapeEnregistree`, `DonneeArchivee`.
   - **Gestion des Alertes** : Modéliser un **bounded context** `gestion_alertes` avec :
     - **Agrégat** : `Alerte` (racine).
     - **Entités** : `MotifAlerte`, `Destinataire`.
     - **Domain Events** : `AlerteGeneree`, `AlerteResolue`.

3. **Sous-domaine Generic** :
   - **Intégration et Interopérabilité** : Externaliser à un middleware (ex : MuleSoft) ou utiliser des **anti-corruption layers** dans le SIL.

---

### **6.2. Modèle d'Intégration Événementielle**
Pour éviter les couplages forts entre sous-domaines, utiliser un **bus d’événements** (ex : Kafka, RabbitMQ) pour :
- **Prescription Médicale** → Publie `PrescriptionValidee` → **Gestion des Urgences** s’abonne.
- **Prélèvement et Conformité** → Publie `EchantillonRejete` → **Gestion des Alertes** s’abonne.
- **Analyse Biologique** → Publie `DosageTermine` → **Interprétation et Transmission** s’abonne.

**Exemple d’événement** :
```json
{
  "event_type": "PrescriptionValidee",
  "data": {
    "identifiant_unique": "UUID-1234",
    "niveau_urgence": "urgence_vitale",
    "prescripteur": "Dr. Dupont",
    "patient": "Patient-4567",
    "informations_cliniques": {
      "anticoagulant": "apixaban",
      "dose": "5 mg",
      "heure_derniere_prise": "10:00",
      "dfg": 35,
      "motif": "Hémorragie digestive"
    }
  },
  "timestamp": "2023-11-15T14:30:00Z"
}
```

---

## **7. Contexte à Préserver pour les Étapes Futures**

### **7.1. Termes Canoniques (Langage Commun)**
| **Terme**                     | **Définition**                                                                                     | **Exemple d'Usage**                                                                                     |
|-------------------------------|---------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| `prescription_medicale`       | Acte par lequel un médecin prescrit un dosage anti-Xa avec informations cliniques obligatoires.   | *"Le médecin saisit une `prescription_medicale` pour un patient sous apixaban."*                        |
| `urgence_vitale`              | Situation clinique critique nécessitant une réponse < 30 min.                                    | *"La `prescription_medicale` est classée en `urgence_vitale` en raison d’une hémorragie intracrânienne."* |
| `echantillon_biologique`      | Matériel prélevé (sang, plasma) pour dosage anti-Xa.                                              | *"L’`echantillon_biologique` est prélevé dans un tube citraté 3,2%."*                                   |
| `contexte_clinique`           | Informations complémentaires (traitement, DFG, heure dernière prise) pour interpréter les résultats. | *"L’`interpretation_resultat` intègre le `contexte_clinique` du patient."*                              |
| `traçabilité`                 | Enregistrement systématique de chaque étape avec horodatage et identifiant unique.               | *"Le SIL assure la `traçabilité` de chaque étape du circuit."*                                          |
| `alerte`                      | Notification générée en cas de non-conformité ou dépassement de délai.                            | *"Une `alerte` est envoyée si le délai de réponse est dépassé."*                                         |

---

### **7.2. Règles Métier Critiques à Conserver**
| **Règle**                                                                                     | **Source**                                                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| Les prescriptions doivent inclure : anticoagulant, dose, heure dernière prise, DFG, motif.   | Étape 2 : 08_regles_metier.md                                                                 |
| Les urgences vitales ont un délai de réponse < 30 min.                                        | Étape 2 : 08_regles_metier.md                                                                 |
| Les échantillons doivent être prélevés dans des tubes citratés 3,2% avec volume ≥ 2 mL.       | Norme CLSI GP41                                                                               |
| Les données patients doivent être chiffrées (AES-256) et archivées 20 ans.                    | RGPD                                                                                          |
| Chaque étape doit être enregistrée avec horodatage et identifiant unique.                     | ISO 15189                                                                                     |

---

### **7.3. Acteurs et Leurs Rôles**
| **Acteur**                     | **Rôle**                                                                                     | **Responsabilités**                                                                                     |
|---------------------------------|---------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| Médecin prescripteur            | Initiateur du circuit.                                                                       | Saisir les `prescriptions_medicales`, mettre à jour les urgences.                                      |
| Personnel infirmier             | Exécuteur du prélèvement.                                                                   | Réaliser l’`acte_prelevement`, vérifier la `conformite_echantillon`.                                   |
| Technicien de laboratoire       | Analyste des échantillons.                                                                  | Réaliser le `dosage_anti_xa`, valider les résultats techniques.                                         |
| Biologiste                      | Superviseur de l’interprétation et de la transmission.                                     | Interpréter les résultats avec le `contexte_clinique`, valider les transmissions.                       |
| SIL                             | Orchestrateur du circuit.                                                                   | Valider les prescriptions, prioriser les urgences, générer les alertes, assurer la `traçabilité`.       |
| Équipe qualité                  | Garante de la conformité réglementaire.                                                     | Vérifier le respect des normes (RGPD, ISO 15189), auditer les processus.                               |

---

### **7.4. Sources et Références à Conserver**
| **Document**                    | **Lien/Emplacement**                                                                         | **Contenu Clé**                                                                                     |
|----------------------------------|---------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| `demande_biologiste.md`          | `data/input/demande_biologiste.md`                                                          | Besoin métier initial et objectifs.                                                                |
| `08_regles_metier.md`            | Étape 2 : 08_regles_metier.md                                                                | Règles de complétude, classification, alertes, sécurité.                                          |
| `11_glossaire_metier.md`         | Étape 3 : 11_glossaire_metier.md                                                             | 50+ termes canoniques et définitions.                                                              |
| `12_user_stories.md`             | Étape 3 : 12_user_stories.md                                                                | Exemples concrets de fonctionnalités attendues.                                                   |
| `13_alignement_metier_technique.md` | Étape 3 : 13_alignement_metier_technique.md                                              | Correspondance entre termes métier et techniques.                                                  |
| Normes                           | RGPD, ISO 15189, CLSI GP41                                                                   | Exigences légales et techniques.                                                                   |

---
## **8. Prochaines Étapes (Checklist)**

### **À Faire Immédiatement**
- [ ] **Valider les hypothèses** avec les parties prenantes (médecins, biologistes, équipe SIL).
- [ ] **Résoudre les conflits** dans les zones de chevauchement (ex : qui met à jour les urgences ?).
- [ ] **Finaliser le tableau des interactions** et le partager avec l’équipe projet.
- [ ] **Préparer un atelier de modélisation tactique (Étape 5)** avec les bounded contexts prioritaires.

### **À Faire Avant l'Étape 5**
- [ ] **Prototyper les bounded contexts** pour **Prescription Médicale** et **Gestion des Urgences**.
- [ ] **Définir les invariants** pour chaque agrégat (ex : `PrescriptionMedicale` doit être complète).
- [ ] **Modéliser les événements du domaine** (ex : `PrescriptionValidee`, `EchantillonRejete`).
- [ ] **Planifier l’intégration** avec les automates et les logiciels de prescription.

---
**Document à transmettre** :
- Ce document structuré (`decoupage_sous_domaines.md`).
- Le tableau des interactions (`interactions_sous_domaines.md`).
- Les user stories et scénarios Gherkin pour validation (`user_stories_validation.md`).

Ce livrable servira de **référence unique** pour les étapes 5 (modélisation tactique) et 6 (implémentation), en garantissant la cohérence avec le langage commun et les règles métier.