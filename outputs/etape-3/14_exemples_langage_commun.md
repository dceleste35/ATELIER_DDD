# **Exemples d'usage du langage commun**
**Domaine : Circuit des demandes urgentes de dosage anti-Xa**

---

## **Introduction**
Ce document illustre l'application concrète du **langage commun** (Ubiquitous Language) à travers :
- Des **narrations métier** (Domain Narratives)
- Des **user stories** formatées selon les conventions DDD
- Des **scénarios Gherkin** (Given/When/Then) pour les tests d'acceptation
- Des **exemples de dialogues** entre acteurs (cliniciens, biologistes, IDE, SIL)

Tous les exemples sont strictement alignés sur le **glossaire du langage commun** et les livrables des étapes 1 et 2, sans anticiper la modélisation DDD détaillée.

---

## **1. Narrations métier (Domain Narratives)**

### **Narration 1 : Parcours d'une prescription médicale en urgence vitale**
**Contexte** : Un patient de 68 ans sous apixaban 5 mg/jour est admis aux Urgences pour une hémorragie digestive aiguë. Le médecin prescripteur identifie une **urgence vitale** nécessitant un **dosage anti-Xa** immédiat.

```markdown
## **Scénario : Gestion d'une urgence vitale**
1. **Prescription médicale** :
   - Le **médecin prescripteur** des Urgences saisit une **prescription médicale** dans le SIL.
   - Il classe la demande en **urgence vitale** et renseigne les **informations cliniques** obligatoires :
     - Anticoagulant : apixaban 5 mg
     - Heure de la dernière prise : 10h00
     - Fonction rénale : DFG = 35 mL/min
     - Motif : "Hémorragie digestive sous AOD"

2. **Acte de prélèvement** :
   - Le **personnel infirmier** vérifie la conformité du **tube de prélèvement** (citraté 3,2%, volume ≥ 2 mL).
   - Il étiquette l’**échantillon biologique** avec :
     - Nom du patient
     - Heure de prélèvement : 10h30
     - Service demandeur : Urgences

3. **Transport** :
   - L’IDE transmet l’**échantillon biologique** au laboratoire dans un délai de 15 minutes (respect du **délai de transport** < 30 min).

4. **Analyse** :
   - Le **technicien de laboratoire** priorise la demande (niveau **urgence vitale**).
   - Il réalise le **dosage anti-Xa** et obtient un résultat à 0,1 UI/mL.

5. **Interprétation et transmission** :
   - Le **biologiste** interprète le résultat en tenant compte du **contexte clinique** (apixaban, DFG, heure de la dernière prise).
   - Il rédige une **interprétation du résultat** avec recommandation : "Sous-dosage probable, envisager une transfusion et ajuster le traitement anticoagulant".
   - Le SIL transmet les résultats au **médecin prescripteur** en moins de 30 minutes (respect du **délai de réponse**).

6. **Décision thérapeutique** :
   - Le **médecin prescripteur** ajuste le traitement en fonction de l’**interprétation du résultat** et du **contexte clinique**.
```

**Points clés** :
- Utilisation exclusive des termes canoniques.
- Respect des règles métier (ex : **délai de réponse** < 30 min pour les **urgences vitales**).
- Traçabilité de chaque étape (prescription → prélèvement → transport → analyse → transmission).

---

### **Narration 2 : Gestion d'un échantillon non conforme**
**Contexte** : Un **échantillon biologique** prélevé en Réanimation est rejeté pour non-conformité.

```markdown
## **Scénario : Rejet d'un échantillon non conforme**
1. **Prescription médicale** :
   - Le **médecin prescripteur** de Réanimation saisit une **prescription médicale** pour un **dosage anti-Xa** de routine.

2. **Acte de prélèvement** :
   - Le **personnel infirmier** prélève l’**échantillon biologique** dans un tube EDTA (non conforme pour le dosage anti-Xa).
   - Il oublie de renseigner l’heure de prélèvement sur l’étiquette.

3. **Contrôle de conformité** :
   - Le **technicien de laboratoire** vérifie la **conformité de l’échantillon** :
     - Type de tube : EDTA ❌ (doit être citraté 3,2%)
     - Volume : 1,5 mL ❌ (insuffisant, volume minimal requis : 2 mL)
     - Étiquetage : Heure manquante ❌

4. **Rejet de l'échantillon** :
   - Le **biologiste** décide du **rejet de l’échantillon** et génère une **alerte** dans le SIL.
   - Le SIL notifie le **médecin prescripteur** et le **personnel infirmier** :
     *"L'échantillon a été rejeté pour non-conformité : tube EDTA et volume insuffisant. Veuillez prélever un nouvel échantillon."*

5. **Nouveau prélèvement** :
   - Le **personnel infirmier** réalise un nouvel **acte de prélèvement** avec un tube citraté 3,2% et un volume suffisant.
   - Le **technicien de laboratoire** valide la conformité et lance l’analyse.

6. **Transmission des résultats** :
   - Le **dosage anti-Xa** est réalisé et les résultats sont transmis au **médecin prescripteur** dans les délais.
```

**Points clés** :
- Respect des **règles de validation** (type de tube, volume, étiquetage).
- Utilisation du terme **rejet de l’échantillon** (et non "refus d'analyse").
- Génération d’une **alerte** automatique par le SIL.

---

### **Narration 3 : Priorisation des demandes urgentes**
**Contexte** : Le SIL doit prioriser automatiquement les **demandes urgentes** en fonction de leur niveau d’urgence.

```markdown
## **Scénario : Priorisation automatique des demandes**
1. **Saisie des prescriptions** :
   - Deux **prescriptions médicales** sont saisies dans le SIL :
     - **Prescription 1** : Urgence vitale (hémorragie intracrânienne sous dabigatran).
     - **Prescription 2** : Urgence standard (ajustement thérapeutique pour un patient sous rivaroxaban).

2. **Priorisation** :
   - Le **SIL** applique la **priorisation** automatique :
     - **Prescription 1** : Niveau **urgence vitale** → **délai de réponse** < 30 min.
     - **Prescription 2** : Niveau **urgence standard** → **délai de réponse** < 1h.

3. **Ordre de traitement** :
   - Le **technicien de laboratoire** reçoit les demandes priorisées :
     1. **Prescription 1** (urgence vitale) en premier.
     2. **Prescription 2** (urgence standard) ensuite.

4. **Transmission des résultats** :
   - Le **dosage anti-Xa** de la **Prescription 1** est transmis au **médecin prescripteur** en 25 minutes.
   - Le **dosage anti-Xa** de la **Prescription 2** est transmis en 50 minutes.

5. **Traçabilité** :
   - Le SIL enregistre chaque étape de la **priorisation** et de la **transmission des résultats** pour assurer la **traçabilité**.
```

**Points clés** :
- Distinction claire entre **urgence vitale** et **urgence standard**.
- Respect des **délais de réponse** cibles.
- Enregistrement de la **priorisation** dans la **traçabilité**.

---

## **2. User Stories (format standard)**

### **User Story 1 : Saisie d'une prescription médicale avec informations cliniques**
```markdown
**Titre** : Saisir une prescription médicale avec les informations cliniques obligatoires

**En tant que** médecin prescripteur
**Je souhaite** saisir une **prescription médicale** pour un **dosage anti-Xa** en situation d’**urgence clinique**
**Afin de** garantir une interprétation correcte des résultats par le **biologiste**

**Critères d'acceptation** :
1. Le formulaire de saisie doit inclure les champs obligatoires :
   - Nom du patient
   - Service demandeur (ex : Urgences, Réanimation)
   - Type d’**anticoagulant oral direct** (ex : apixaban, rivaroxaban)
   - Dose et **heure de la dernière prise**
   - Fonction rénale (DFG)
   - Motif de la demande (ex : suspicion de surdosage, hémorragie)
2. Le **SIL** doit classer automatiquement la demande en **urgence clinique** ou **urgence vitale** en fonction du motif.
3. Le **SIL** doit générer une **alerte** si des champs obligatoires sont manquants.
```

---

### **User Story 2 : Vérification de la conformité d'un échantillon biologique**
```markdown
**Titre** : Vérifier la conformité d'un échantillon biologique avant analyse

**En tant que** technicien de laboratoire
**Je souhaite** que le **SIL** vérifie automatiquement la **conformité de l’échantillon** avant analyse
**Afin de** éviter les erreurs d’interprétation et les rejets inutiles

**Critères d'acceptation** :
1. Le **SIL** doit vérifier les critères de conformité :
   - Type de **tube de prélèvement** (citraté 3,2%)
   - Volume ≥ 2 mL
   - Étiquetage complet (nom du patient, heure de prélèvement)
   - Délai de transport < 30 min
2. Si l’échantillon est non conforme, le **SIL** doit :
   - Générer une **alerte** pour le **biologiste**.
   - Notifier le **personnel infirmier** et le **médecin prescripteur**.
3. Le **SIL** doit enregistrer la décision de **rejet de l’échantillon** dans la **traçabilité**.
```

---

### **User Story 3 : Priorisation automatique des demandes urgentes**
```markdown
**Titre** : Prioriser automatiquement les demandes urgentes

**En tant que** technicien de laboratoire
**Je souhaite** que le **SIL** priorise automatiquement les **demandes urgentes**
**Afin de** garantir un **délai de réponse** optimal pour les patients critiques

**Critères d'acceptation** :
1. Le **SIL** doit classer les demandes en :
   - **Urgence vitale** (ex : hémorragie massive) → **délai de réponse** < 30 min.
   - **Urgence standard** (ex : ajustement thérapeutique) → **délai de réponse** < 1h.
2. Le **SIL** doit afficher les demandes priorisées dans un tableau dédié.
3. Le **SIL** doit notifier les acteurs concernés (techniciens, biologistes) en temps réel.
4. Le **SIL** doit enregistrer la **priorisation** dans la **traçabilité**.
```

---
### **User Story 4 : Transmission sécurisée des résultats**
```markdown
**Titre** : Transmettre les résultats du dosage anti-Xa de manière sécurisée

**En tant que** biologiste
**Je souhaite** que le **SIL** transmette les **résultats du dosage anti-Xa** de manière sécurisée
**Afin de** garantir la confidentialité et la rapidité de la prise en charge

**Critères d'acceptation** :
1. Le **SIL** doit transmettre les résultats :
   - Au **médecin prescripteur** via une interface sécurisée.
   - Avec une **interprétation du résultat** incluant le **contexte clinique**.
2. Le **SIL** doit générer une **alerte** si le **délai de réponse** dépasse les seuils définis.
3. Le **SIL** doit enregistrer la **transmission des résultats** dans la **traçabilité**.
```

---
### **User Story 5 : Rejet d'un échantillon non conforme**
```markdown
**Titre** : Rejeter un échantillon biologique non conforme

**En tant que** biologiste
**Je souhaite** que le **SIL** me notifie automatiquement les **échantillons non conformes**
**Afin de** prendre une décision de **rejet de l’échantillon** et éviter une erreur d’interprétation

**Critères d'acceptation** :
1. Le **SIL** doit détecter les non-conformités :
   - Type de **tube de prélèvement** incorrect.
   - Volume insuffisant.
   - Étiquetage incomplet.
   - Délai de transport dépassé.
2. Le **SIL** doit générer une **alerte** pour le **biologiste** avec les motifs de rejet.
3. Le **SIL** doit permettre au **biologiste** de valider le **rejet de l’échantillon**.
4. Le **SIL** doit notifier le **personnel infirmier** et le **médecin prescripteur**.
5. Le **SIL** doit enregistrer la décision dans la **traçabilité**.
```

---
### **User Story 6 : Consultation de la traçabilité**
```markdown
**Titre** : Consulter la traçabilité d'une demande de dosage anti-Xa

**En tant que** médecin prescripteur / biologiste / personnel infirmier
**Je souhaite** consulter l’historique complet d’une **prescription médicale**
**Afin de** vérifier le respect des délais et la conformité du processus

**Critères d'acceptation** :
1. Le **SIL** doit afficher une vue détaillée de la **traçabilité** incluant :
   - Date et heure de la **prescription médicale**.
   - Heure de l’**acte de prélèvement**.
   - Heure de réception au laboratoire.
   - Heure de l’analyse et du résultat.
   - Heure de la **transmission des résultats**.
2. Le **SIL** doit permettre de filtrer par :
   - **Identifiant unique** de la demande.
   - **Service demandeur**.
   - **Niveau d’urgence**.
3. Le **SIL** doit exporter la **traçabilité** au format PDF ou Excel.
```

---
### **User Story 7 : Intégration avec les automates de dosage**
```markdown
**Titre** : Intégrer le SIL avec les automates de dosage anti-Xa

**En tant que** technicien de laboratoire
**Je souhaite** que le **SIL** s’interface automatiquement avec les automates de dosage
**Afin de** éviter les erreurs de saisie et accélérer le processus

**Critères d'acceptation** :
1. Le **SIL** doit envoyer les demandes de **dosage anti-Xa** aux automates via une API sécurisée.
2. Les automates doivent retourner les **résultats du dosage anti-Xa** au **SIL** automatiquement.
3. Le **SIL** doit associer les résultats aux **prescriptions médicales** correspondantes.
4. Le **SIL** doit enregistrer les résultats dans la **traçabilité**.
```

---
### **User Story 8 : Gestion des alertes pour les délais dépassés**
```markdown
**Titre** : Générer des alertes en cas de dépassement des délais

**En tant que** biologiste / médecin prescripteur
**Je souhaite** recevoir une **alerte** si le **délai de réponse** est dépassé
**Afin de** prendre les mesures correctives nécessaires

**Critères d'acceptation** :
1. Le **SIL** doit surveiller les **délais de réponse** pour chaque demande.
2. Si le **délai de réponse** dépasse :
   - 30 min pour une **urgence vitale** → **alerte rouge**.
   - 1h pour une **urgence standard** → **alerte orange**.
3. Le **SIL** doit notifier les acteurs concernés (biologiste, médecin prescripteur) par :
   - Notification dans l’interface.
   - Email.
   - SMS (si configuré).
4. Le **SIL** doit enregistrer l’**alerte** dans la **traçabilité**.
```

---
### **User Story 9 : Archivage sécurisé des données**
```markdown
**Titre** : Archiver les données des patients conformément au RGPD

**En tant que** responsable qualité / équipe SIL
**Je souhaite** que le **SIL** archive les données des patients de manière sécurisée
**Afin de** respecter les exigences réglementaires

**Critères d'acceptation** :
1. Le **SIL** doit archiver les données pendant 20 ans (conformément au RGPD).
2. L’archivage doit être :
   - Chiffré (AES-256).
   - Accessible uniquement aux personnes autorisées.
3. Le **SIL** doit permettre de restaurer les données en cas de besoin.
4. Le **SIL** doit enregistrer les accès aux archives dans les logs.
```

---
### **User Story 10 : Formation des équipes aux nouveaux processus**
```markdown
**Titre** : Former les équipes aux nouveaux processus du circuit informatisé

**En tant que** chef de projet
**Je souhaite** organiser des sessions de formation pour les équipes
**Afin de** garantir l’adoption du nouveau **circuit informatisé**

**Critères d'acceptation** :
1. Organiser 3 sessions de formation :
   - Pour les **médecins prescripteurs**.
   - Pour le **personnel infirmier**.
   - Pour les **techniciens de laboratoire** et **biologistes**.
2. Les formations doivent couvrir :
   - La saisie des **prescriptions médicales**.
   - La vérification de la **conformité de l’échantillon**.
   - La gestion des **alertes** et des **rejets**.
   - La consultation de la **traçabilité**.
3. Fournir des supports de formation (PDF, vidéos).
4. Évaluer la compréhension des équipes via un quiz.
```

---

## **3. Scénarios Gherkin (Given/When/Then)**

### **Scénario 1 : Saisie d'une prescription médicale en urgence vitale**
```gherkin
Scénario : Saisie d'une prescription médicale pour une urgence vitale
  Contexte :
    Etant donné un médecin prescripteur connecté au SIL
    Et un patient sous apixaban 5 mg/jour admis aux Urgences pour une hémorragie digestive

  Quand le médecin saisit une prescription médicale avec :
    | Champ                     | Valeur                          |
    |---------------------------|---------------------------------|
    | Anticoagulant             | apixaban 5 mg                   |
    | Heure de la dernière prise| 10h00                           |
    | Fonction rénale (DFG)     | 35 mL/min                       |
    | Motif                     | Hémorragie digestive sous AOD  |
    | Niveau d'urgence          | urgence vitale                  |

  Alors le SIL :
    - Classe la demande en "urgence vitale"
    - Affiche un message de confirmation : "Prescription enregistrée avec succès"
    - Génère un identifiant unique pour la demande
    - Envoie une notification au personnel infirmier pour prélèvement
```

---
### **Scénario 2 : Rejet d'un échantillon non conforme**
```gherkin
Scénario : Rejet d'un échantillon biologique non conforme
  Contexte :
    Etant donné un technicien de laboratoire qui reçoit un échantillon biologique
    Et un SIL configuré pour vérifier la conformité

  Quand le technicien scanne l'étiquette de l'échantillon
  Et le SIL vérifie les critères suivants :
    | Critère                  | Valeur attendue       | Valeur réelle       |
    |--------------------------|-----------------------|---------------------|
    | Type de tube             | citraté 3,2%          | EDTA                |
    | Volume                   | ≥ 2 mL                | 1,5 mL              |
    | Heure de prélèvement     | Renseignée            | Manquante           |

  Alors le SIL :
    - Affiche un message : "Échantillon non conforme : tube EDTA et volume insuffisant"
    - Génère une alerte pour le biologiste
    - Notifie le personnel infirmier et le médecin prescripteur
    - Enregistre le rejet dans la traçabilité
```

---
### **Scénario 3 : Priorisation automatique des demandes**
```gherkin
Scénario : Priorisation automatique des demandes urgentes
  Contexte :
    Etant donné deux prescriptions médicales saisies dans le SIL :
      - Prescription 1 : Urgence vitale (hémorragie intracrânienne)
      - Prescription 2 : Urgence standard (ajustement thérapeutique)

  Quand le SIL traite les demandes
  Alors le SIL :
    - Classe la Prescription 1 en "urgence vitale" avec un délai de réponse < 30 min
    - Classe la Prescription 2 en "urgence standard" avec un délai de réponse < 1h
    - Affiche les demandes priorisées dans un tableau dédié
    - Notifie les techniciens de laboratoire en temps réel
```

---
### **Scénario 4 : Transmission des résultats en cas d'urgence vitale**
```gherkin
Scénario : Transmission des résultats pour une urgence vitale
  Contexte :
    Etant donné une prescription médicale classée en "urgence vitale"
    Et un dosage anti-Xa réalisé avec un résultat à 0,1 UI/mL

  Quand le biologiste valide l'interprétation du résultat
  Alors le SIL :
    - Transmet les résultats au médecin prescripteur en moins de 30 min
    - Inclut l'interprétation : "Sous-dosage probable, envisager une transfusion"
    - Enregistre la transmission dans la traçabilité
    - Génère une notification de confirmation
```

---
### **Scénario 5 : Consultation de la traçabilité**
```gherkin
Scénario : Consulter la traçabilité d'une demande
  Contexte :
    Etant donné une prescription médicale avec identifiant unique "DEM-2023-001"
    Et le SIL a enregistré toutes les étapes (prescription → prélèvement → analyse → transmission)

  Quand un acteur (médecin, biologiste, IDE) consulte la traçabilité
  Alors le SIL affiche :
    - La liste des étapes avec horodatage :
      | Étape                  | Date/Heure          | Acteur               |
      |------------------------|---------------------|----------------------|
      | Prescription médicale  | 10/10/2023 10h00   | Médecin prescripteur |
      | Acte de prélèvement    | 10/10/2023 10h30   | Personnel infirmier  |
      | Réception au labo      | 10/10/2023 10h45   | Technicien           |
      | Analyse terminée       | 10/10/2023 11h10   | Technicien           |
      | Transmission des résultats | 10/10/2023 11h15 | SIL                  |
    - La possibilité d'exporter les données au format PDF
```

---

## **4. Exemples de dialogues entre acteurs**

### **Dialogue 1 : Échange entre médecin prescripteur et biologiste (urgence vitale)**
**Contexte** : Un médecin prescripteur des Urgences contacte le biologiste pour une **urgence vitale**.

```markdown
**Médecin prescripteur** (Urgences) :
*"Bonjour, je suis le Dr Martin des Urgences. Nous avons un patient de 68 ans sous apixaban qui présente une hémorragie digestive aiguë. C’est une **urgence vitale**, je viens de saisir une **prescription médicale** dans le SIL avec les **informations cliniques** suivantes :
- Anticoagulant : apixaban 5 mg
- Heure de la dernière prise : 10h00
- Fonction rénale : DFG = 35 mL/min
Pouvez-vous prioriser cette demande ? Le **délai de réponse** doit être inférieur à 30 minutes."*

**Biologiste** :
*"Bonjour Dr Martin, je vois votre **prescription médicale** dans le SIL. Elle est bien classée en **urgence vitale**. Je vais transmettre l’info à l’équipe du labo pour un **dosage anti-Xa** immédiat. Je vous tiens au courant dès que j’ai les résultats avec une **interprétation du résultat** intégrant le **contexte clinique**."*

**Médecin prescripteur** :
*"Parfait, merci pour votre réactivité. Je reste en attente des résultats pour ajuster la **décision thérapeutique**."*
```

**Points clés** :
- Utilisation des termes canoniques (**urgence vitale**, **prescription médicale**, **informations cliniques**, **dosage anti-Xa**, **interprétation du résultat**, **contexte clinique**).
- Respect des **règles métier** (priorisation, **délai de réponse** < 30 min).

---

### **Dialogue 2 : Échange entre personnel infirmier et technicien de laboratoire (échantillon non conforme)**
**Contexte** : Une IDE contacte le technicien de laboratoire pour signaler un **échantillon non conforme**.

```markdown
**Personnel infirmier** (Réanimation) :
*"Bonjour, je suis l’IDE Dupont. J’ai prélevé un **échantillon biologique** pour un **dosage anti-Xa** il y a 20 minutes, mais le **SIL** vient de m’envoyer une **alerte** : l’échantillon est non conforme. Pouvez-vous vérifier ?"*

**Technicien de laboratoire** :
*"Bonjour Mme Dupont, je vois l’**alerte** dans le SIL. Pouvez-vous me préciser les motifs de non-conformité ?"*

**Personnel infirmier** :
*"Oui, le **tube de prélèvement** est en EDTA au lieu de citraté 3,2%, et le volume est de 1,5 mL alors qu’il faut au moins 2 mL."*

**Technicien de laboratoire** :
*"Merci pour ces précisions. Je vais enregistrer un **rejet de l’échantillon** dans le SIL et notifier le **biologiste**. Pouvez-vous prélever un nouvel **échantillon biologique** avec un tube citraté 3,2% et un volume suffisant ?"*

**Personnel infirmier** :
*"Bien sûr, je m’en occupe immédiatement. Je vous transmets le nouvel échantillon dans les 10 minutes."*
```

**Points clés** :
- Utilisation des termes canoniques (**échantillon biologique**, **tube de prélèvement**, **alerte**, **rejet de l’échantillon**).
- Respect des **règles de validation** (type de tube, volume).

---
### **Dialogue 3 : Échange entre SIL et médecin prescripteur (transmission des résultats)**
**Contexte** : Le SIL notifie le médecin prescripteur que les résultats sont disponibles.

```markdown
**SIL** (notification automatique) :
*"Bonjour Dr Martin,
Les résultats du **dosage anti-Xa** pour votre patient (DEM-2023-001) sont disponibles.
- Résultat : 0,1 UI/mL
- **Interprétation du résultat** : Sous-dosage probable, envisager une transfusion et ajuster le traitement anticoagulant.
- **Contexte clinique** : Apixaban 5 mg, DFG = 35 mL/min, dernière prise à 10h00.
Merci de consulter le SIL pour plus de détails.
Cordialement,
Votre **circuit informatisé**"*

**Médecin prescripteur** :
*"Merci pour cette notification rapide. Je vais ajuster la **décision thérapeutique** en fonction de l’**interprétation du résultat** et du **contexte clinique**. Je consulte les détails dans le SIL."*
```

**Points clés** :
- Utilisation des termes canoniques (**dosage anti-Xa**, **interprétation du résultat**, **contexte clinique**, **circuit informatisé**).
- Transmission sécurisée des résultats avec **interprétation** et **contexte clinique**.

---
### **Dialogue 4 : Réunion de revue entre biologiste et équipe SIL**
**Contexte** : Le biologiste et l’équipe SIL font un point sur les performances du **circuit informatisé**.

```markdown
**Biologiste** :
*"Bonjour à tous. Je fais un point sur le **circuit informatisé** depuis son déploiement il y a 3 mois. Voici les constats :
1. Le **délai de réponse** moyen pour les **urgences vitales** est de 28 minutes, ce qui est conforme à nos attentes.
2. Le taux de **rejet de l’échantillon** a diminué de 15% grâce à la vérification automatique de la **conformité de l’échantillon**.
3. La **traçabilité** est bien respectée, mais nous avons quelques soucis avec l’export des données en PDF.

Avez-vous des suggestions pour améliorer ces points ?"*

**Équipe SIL** :
*"Bonjour. Voici nos propositions :
1. Pour réduire le **délai de réponse**, nous pourrions optimiser l’interface entre le **SIL** et les automates de dosage.
2. Pour les **rejets d’échantillon**, nous allons ajouter un champ 'motif du rejet' dans la **traçabilité** pour mieux analyser les causes.
3. Pour l’export PDF, nous allons corriger le bug signalé et ajouter un filtre par **niveau d’urgence**.

Qu’en pensez-vous ?"*

**Biologiste** :
*"Cela me semble pertinent. Je valide ces améliorations. Pouvez-vous les prioriser et me donner un échéancier ?"*

**Équipe SIL** :
*"Oui, nous prévoyons de déployer ces corrections dans les 2 prochaines semaines."*
```

**Points clés** :
- Utilisation des termes canoniques (**circuit informatisé**, **délai de réponse**, **rejet de l’échantillon**, **conformité de l’échantillon**, **traçabilité**, **niveau d’urgence**).
- Focus sur l’amélioration continue du processus.

---
### **Dialogue 5 : Formation du personnel infirmier aux nouveaux processus**
**Contexte** : Une IDE pose des questions lors d’une session de formation sur le **circuit informatisé**.

```markdown
**Personnel infirmier** :
*"Bonjour, je suis nouvelle dans le service et je n’ai pas encore l’habitude du nouveau **circuit informatisé**. Pouvez-vous me rappeler les étapes à suivre pour un **acte de prélèvement** ?"*

**Formateur** :
*"Bien sûr. Voici les étapes clés :
1. Vérifiez que le **médecin prescripteur** a bien saisi une **prescription médicale** dans le SIL.
2. Prélevez l’**échantillon biologique** dans un **tube de prélèvement** citraté 3,2% avec un volume ≥ 2 mL.
3. Étiquetez l’échantillon avec le nom du patient, la date et l’heure de prélèvement.
4. Transmettez l’échantillon au laboratoire dans un délai de 30 minutes maximum.
5. Vérifiez que le SIL a bien enregistré votre **acte de prélèvement** et généré un identifiant unique.

Y a-t-il des points que vous souhaitez approfondir ?"*

**Personnel infirmier** :
*"Non, c’est très clair. Merci pour ces précisions !"*
```

**Points clés** :
- Utilisation des termes canoniques (**circuit informatisé**, **acte de prélèvement**, **prescription médicale**, **échantillon biologique**, **tube de prélèvement**).
- Clarification des responsabilités et des étapes du processus.

---

## **5. Annexe : Checklist pour l'application du langage commun**

| **Étape** | **Action** | **Critères de validation** | **Exemple** |
|-----------|------------|-----------------------------|-------------|
| **1. Rédaction de narrations métier** | Utiliser les termes canoniques | - Tous les termes sont ceux du glossaire <br> - Respect des règles métier | *"Le **médecin prescripteur** saisit une **prescription médicale** en **urgence vitale**."* |
| **2. Rédaction de user stories** | Formuler avec le format "En tant que... Je souhaite... Afin de..." | - Inclure les critères d'acceptation <br> - Utiliser les termes canoniques | *"En tant que **biologiste**, je souhaite recevoir une **alerte** si un **échantillon biologique** est **non conforme** afin de **rejeter l’échantillon**."* |
| **3. Rédaction de scénarios Gherkin** | Structurer en Given/When/Then | - Couvrir les cas critiques (urgence, qualité, traçabilité) <br> - Utiliser les termes canoniques | ```gherkin Quand le SIL vérifie la **conformité de l’échantillon** Alors il génère une **alerte** si l’échantillon est non conforme ``` |
| **4. Dialogues entre acteurs** | Reformuler les échanges avec le langage commun | - Remplacer les termes techniques par les termes canoniques <br> - Respecter le vocabulaire métier | *"Le **SIL** a généré une **alerte** pour signaler un **rejet de l’échantillon**."* |
| **5. Revue de code** | Vérifier la cohérence avec le glossaire | - Noms de classes/méthodes/variables alignés sur le glossaire <br> - Commentaires explicatifs | ```python class PrescriptionMedicale: # Gère les **prescriptions médicales** ``` |
| **6. Tests d'acceptation** | Rédiger les tests avec les termes canoniques | - Scénarios clairs et reproductibles <br> - Couverture des règles métier | ```gherkin Étant donné une **prescription médicale** en **urgence vitale** Quand le SIL priorise la demande Alors le **délai de réponse** est < 30 min ``` |

---
## **6. Annexe : Sources et références**

| **Source** | **Description** |
|------------|-----------------