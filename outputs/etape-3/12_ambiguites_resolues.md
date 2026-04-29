# **Ambiguïtés terminologiques résolues**
**Domaine : Circuit des demandes urgentes de dosage anti-Xa**

---

## **Introduction**
Ce document identifie les termes ambigus, synonymes implicites, homonymes, traductions divergentes et expressions floues présents dans le corpus métier. Pour chaque cas, un arbitrage terminologique est proposé avec une justification métier, afin de fixer un **terme canonique unique** dans le langage commun. Les ambiguïtés non tranchables sans expertise métier sont listées en fin de document pour validation.

---

## **1. Ambiguïtés identifiées et arbitrages proposés**

---

### **1.1. "Demande urgente" vs. "Urgence clinique" vs. "Urgence vitale"**

| **Termes problématiques** | Type de problème | Acteurs concernés et interprétations divergentes | Terme canonique retenu | Définition | Justification métier | Termes à proscrire |
|---------------------------|------------------|--------------------------------------------------|------------------------|-----------|----------------------|--------------------|
| **Demande urgente** (Étape 1 : 03_concepts_metier_initiaux.md) | **Synonymie implicite** / **Expression floue** | - Médecins prescripteurs : utilisent *"demande urgente"* pour toute demande nécessitant une réponse rapide. <br> - Biologiste : associe *"urgence"* à des critères cliniques stricts (ex : hémorragie). <br> - SIL : traite toutes les demandes urgentes de la même manière, sans distinction de gravité. | **Urgence clinique** | Situation où le délai d’obtention du résultat du dosage anti-Xa est critique pour la prise en charge immédiate du patient (ex : suspicion de surdosage, hémorragie, chirurgie urgente). | - Clarifie la distinction entre une simple priorité et une situation vitale. <br> - Aligne le vocabulaire sur les pratiques cliniques (ex : classification des urgences en médecine). <br> - Évite la confusion avec *"demande prioritaire"* (qui n’implique pas nécessairement une urgence vitale). | *"Demande urgente"*, *"Urgence"* (trop générique) |
| **Urgence clinique** (Étape 1 : 01_reformulation_du_besoin.md) | **Homonymie partielle** | - Certains acteurs utilisent *"urgence clinique"* pour désigner toute situation nécessitant un dosage rapide, y compris les ajustements thérapeutiques non critiques. | **Urgence vitale** | Sous-catégorie d’**urgence clinique** où le délai de réponse est critique pour la survie du patient (ex : hémorragie intracrânienne, choc hémorragique). | - Permet de hiérarchiser les priorités dans le SIL. <br> - Justifie des délais de réponse plus stricts (<30 min). <br> - Aligné sur les normes de soins urgents (ex : protocoles de réanimation). | *"Urgence absolue"* (trop subjectif) |
| **Urgence vitale** (Étape 2 : 09_conflits_objectifs.md) | **Expression floue** | - Le corpus mentionne des délais de *"30 minutes"* pour les urgences vitales (Étape 2 : 09_conflits_objectifs.md) et *"1 heure"* pour les urgences standard (Étape 2 : 08_regles_metier.md). <br> - Aucune définition claire des critères pour distinguer une urgence vitale d’une urgence clinique standard. | **Urgence vitale** | Situation où le délai de réponse est critique pour la survie du patient (ex : hémorragie massive, chirurgie en urgence, arrêt cardiaque sous anticoagulant). | - Standardise la classification des urgences. <br> - Permet au SIL de prioriser automatiquement les demandes critiques. <br> - Réduit les risques de sous-estimation des situations vitales. | *"Urgence absolue"*, *"Situation critique"* (trop vague) |

**Exemple d’emploi validé :**
> *"Ce patient en réanimation présente une hémorragie intracrânienne sous apixaban : c’est une **urgence vitale** nécessitant un dosage anti-Xa en moins de 30 minutes."*

---

### **1.2. "Prescription médicale" vs. "Ordonnance" vs. "Demande de dosage"**

| **Termes problématiques** | Type de problème | Acteurs concernés et interprétations divergentes | Terme canonique retenu | Définition | Justification métier | Termes à proscrire |
|---------------------------|------------------|--------------------------------------------------|------------------------|-----------|----------------------|--------------------|
| **Prescription médicale** (Étape 1 : 03_concepts_metier_initiaux.md) | **Synonymie implicite** | - Médecins prescripteurs : utilisent *"prescription"* ou *"ordonnance"* indifféremment. <br> - Personnel infirmier : parle de *"demande de dosage"*. <br> - SIL : utilise *"demande"* dans son interface. | **Prescription médicale** | Acte par lequel un médecin prescrit un dosage anti-Xa pour un patient sous anticoagulant oral direct, incluant les informations cliniques nécessaires (traitement, heure de la dernière prise, fonction rénale). | - Aligné sur le vocabulaire réglementaire (Code de la santé publique). <br> - Distingue clairement l’acte médical (prescription) de l’acte de prélèvement (demande). <br> - Évite la confusion avec les *"demandes urgentes"* (qui sont des instances de prescriptions). | *"Ordonnance"*, *"Demande de dosage"* (trop générique) |
| **Ordonnance** | **Traduction divergente** | - Utilisé par certains médecins pour désigner une prescription écrite. <br> - Risque de confusion avec les ordonnances de sortie (hors contexte d’urgence). | **Prescription médicale** | Voir ci-dessus. | - Le terme *"ordonnance"* est trop large et peut prêter à confusion. <br> - *"Prescription médicale"* est le terme légal et métier précis. | *"Ordonnance"* |
| **Demande de dosage** | **Synonymie implicite** | - Utilisé par le SIL et certains acteurs pour désigner la prescription. <br> - Risque de confusion avec la *"demande urgente"* (qui est une instance de prescription). | **Prescription médicale** | Voir ci-dessus. | - *"Demande de dosage"* est trop générique et peut inclure des demandes non médicales (ex : relance administrative). <br> - *"Prescription médicale"* insiste sur l’acte médical et la responsabilité du prescripteur. | *"Demande de dosage"*, *"Demande"* |

**Exemple d’emploi validé :**
> *"Le médecin a saisi une **prescription médicale** pour un dosage anti-Xa urgent, incluant l’heure de la dernière prise de rivaroxaban et la clairance de la créatinine du patient."*

---

### **1.3. "Échantillon biologique" vs. "Prélèvement" vs. "Tube de prélèvement"**

| **Termes problématiques** | Type de problème | Acteurs concernés et interprétations divergentes | Terme canonique retenu | Définition | Justification métier | Termes à proscrire |
|---------------------------|------------------|--------------------------------------------------|------------------------|-----------|----------------------|--------------------|
| **Échantillon biologique** (Étape 1 : 03_concepts_metier_initiaux.md) | **Synonymie implicite** | - Personnel infirmier : utilise *"prélèvement"*. <br> - Biologiste : parle d’*"échantillon"* ou de *"tube"*. <br> - SIL : utilise *"échantillon"* dans ses logs. | **Échantillon biologique** | Matériel biologique (sang total, plasma) prélevé pour réaliser un dosage anti-Xa, conditionné dans un tube spécifique. | - *"Échantillon biologique"* est le terme le plus précis et inclut implicitement le tube. <br> - Évite la confusion avec *"prélèvement"* (qui peut désigner l’acte ou le matériel). <br> - Aligné sur les normes de laboratoire (ex : ISO 15189). | *"Prélèvement"* (trop ambigu) |
| **Prélèvement** | **Homonymie** | - Peut désigner l’acte de prélever ou le matériel prélevé. <br> - Risque de confusion avec *"prescription"* (ex : *"prélèvement urgent"* vs. *"prescription urgente"*). | **Échantillon biologique** (pour le matériel) <br> **Acte de prélèvement** (pour l’action) | Voir ci-dessus. | - Distingue clairement l’objet (échantillon) de l’action (prélèvement). <br> - Permet de préciser les responsabilités (ex : *"l’IDE réalise l’acte de prélèvement"*). | *"Prélèvement"* (sauf pour désigner l’action) |
| **Tube de prélèvement** (Étape 2 : 08_regles_metier.md) | **Glissement de sens** | - Certains acteurs utilisent *"tube"* pour désigner l’échantillon entier. <br> - Risque de confusion avec le *"tube citraté"* (type spécifique de tube). | **Tube de prélèvement** | Récipient stérile utilisé pour collecter le sang veineux, conforme aux normes de laboratoire pour le dosage anti-Xa (ex : tube citraté 3,2%, volume minimal requis). | - *"Tube de prélèvement"* est précis et évite les ambiguïtés. <br> - Permet de distinguer le contenant (tube) du contenu (échantillon). <br> - Aligné sur les normes pré-analytiques (ex : CLSI GP41). | *"Tube"* (sauf dans *"tube de prélèvement"*) |

**Exemple d’emploi validé :**
> *"L’IDE a réalisé l’**acte de prélèvement** et a transmis l’**échantillon biologique** (tube citraté 3,2%) au laboratoire pour dosage anti-Xa."*

---

### **1.4. "Contexte clinique" vs. "Situation clinique" vs. "Contexte thérapeutique"**

| **Termes problématiques** | Type de problème | Acteurs concernés et interprétations divergentes | Terme canonique retenu | Définition | Justification métier | Termes à proscrire |
|---------------------------|------------------|--------------------------------------------------|------------------------|-----------|----------------------|--------------------|
| **Contexte clinique** (Étape 1 : 03_concepts_metier_initiaux.md) | **Synonymie implicite** | - Biologiste : utilise *"contexte clinique"* pour désigner l’ensemble des données médicales pertinentes. <br> - Médecins prescripteurs : parlent de *"situation clinique"*. <br> - SIL : utilise *"contexte thérapeutique"* dans ses champs de saisie. | **Contexte clinique** | Ensemble des éléments médicaux pertinents pour interpréter un dosage anti-Xa : traitement en cours, heure de la dernière prise, fonction rénale, antécédents thrombotiques ou hémorragiques, signes cliniques actuels. | - *"Contexte clinique"* est le terme le plus complet et inclut le traitement (aspect thérapeutique). <br> - Évite la confusion avec *"contexte thérapeutique"* (trop restrictif). <br> - Aligné sur les pratiques d’interprétation biologique. | *"Situation clinique"*, *"Contexte thérapeutique"* |
| **Situation clinique** | **Traduction divergente** | - Utilisé par certains médecins pour désigner l’état actuel du patient. <br> - Risque de confusion avec *"urgence clinique"*. | **Contexte clinique** | Voir ci-dessus. | - *"Situation clinique"* est trop vague et peut exclure des éléments clés (ex : traitement). <br> - *"Contexte clinique"* est le terme standard en biologie médicale. | *"Situation clinique"* |
| **Contexte thérapeutique** | **Expression floue** | - Utilisé par le SIL pour désigner uniquement le traitement en cours. <br> - Risque d’exclure d’autres éléments clés (ex : fonction rénale, antécédents). | **Contexte clinique** | Voir ci-dessus. | - *"Contexte thérapeutique"* est trop restrictif et peut conduire à des interprétations erronées. <br> - *"Contexte clinique"* est plus large et inclut tous les éléments nécessaires. | *"Contexte thérapeutique"* |

**Exemple d’emploi validé :**
> *"L’interprétation du **dosage anti-Xa** doit intégrer le **contexte clinique** du patient, incluant son traitement par apixaban, sa fonction rénale (DFG à 30 mL/min) et ses antécédents de saignement."*

---

### **1.5. "Traçabilité" vs. "Documentation" vs. "Historique"**

| **Termes problématiques** | Type de problème | Acteurs concernés et interprétations divergentes | Terme canonique retenu | Définition | Justification métier | Termes à proscrire |
|---------------------------|------------------|--------------------------------------------------|------------------------|-----------|----------------------|--------------------|
| **Traçabilité** (Étape 1 : 03_concepts_metier_initiaux.md) | **Synonymie implicite** | - SIL : utilise *"traçabilité"* pour désigner l’enregistrement systématique des étapes. <br> - Biologiste : parle de *"documentation"*. <br> - Techniciens de laboratoire : utilisent *"historique"*. | **Traçabilité** | Capacité à suivre et enregistrer toutes les étapes du circuit d’une demande de dosage anti-Xa : prescription, prélèvement, transport, analyse, transmission des résultats. | - *"Traçabilité"* est le terme réglementaire et métier standard (ex : ISO 15189, RGPD). <br> - Inclut implicitement la *"documentation"* et l’*"historique"*. <br> - Évite la confusion avec *"archivage"* (qui est une sous-partie de la traçabilité). | *"Documentation"*, *"Historique"* (trop restrictifs) |
| **Documentation** | **Traduction divergente** | - Utilisé pour désigner l’enregistrement des étapes. <br> - Risque de confusion avec la *"documentation médicale"* (dossier patient). | **Traçabilité** | Voir ci-dessus. | - *"Documentation"* est trop générique et peut inclure des documents non traçables (ex : notes manuscrites non enregistrées dans le SIL). <br> - *"Traçabilité"* insiste sur l’enregistrement systématique et horodaté. | *"Documentation"* (sauf dans *"traçabilité documentaire"*) |
| **Historique** | **Expression floue** | - Utilisé pour désigner l’ensemble des enregistrements passés. <br> - Risque de confusion avec l’*"historique médical"* du patient. | **Traçabilité** | Voir ci-dessus. | - *"Historique"* est trop vague et peut inclure des données non pertinentes. <br> - *"Traçabilité"* est le terme précis pour le circuit des demandes. | *"Historique"* |

**Exemple d’emploi validé :**
> *"Le SIL doit assurer la **traçabilité** de chaque demande de dosage anti-Xa, depuis la prescription jusqu’à la transmission des résultats, avec horodatage et identifiants uniques."*

---

### **1.6. "Délai de réponse" vs. "Temps de rendu" vs. "Délai d’analyse"**

| **Termes problématiques** | Type de problème | Acteurs concernés et interprétations divergentes | Terme canonique retenu | Définition | Justification métier | Termes à proscrire |
|---------------------------|------------------|--------------------------------------------------|------------------------|-----------|----------------------|--------------------|
| **Délai de réponse** (Étape 2 : 08_regles_metier.md) | **Synonymie implicite** | - Médecins prescripteurs : utilisent *"délai de réponse"* pour désigner le temps entre la demande et la réception des résultats. <br> - Biologiste : parle de *"temps de rendu"*. <br> - SIL : utilise *"délai d’analyse"*. | **Délai de réponse** | Temps maximal autorisé entre la réception de la demande de dosage anti-Xa par le laboratoire et la transmission des résultats au prescripteur. | - *"Délai de réponse"* est le terme le plus clair et inclut implicitement le *"temps de rendu"* et le *"délai d’analyse"*. <br> - Évite la confusion avec *"délai de transport"* (qui est un sous-ensemble du délai de réponse). <br> - Aligné sur les attentes des prescripteurs (ex : *"nous avons besoin d’une réponse rapide"*). | *"Temps de rendu"*, *"Délai d’analyse"* |
| **Temps de rendu** | **Traduction divergente** | - Utilisé pour désigner le temps nécessaire pour obtenir les résultats. <br> - Risque de confusion avec *"délai de transport"*. | **Délai de réponse** | Voir ci-dessus. | - *"Temps de rendu"* est trop restrictif et peut exclure le délai de transport. <br> - *"Délai de réponse"* est plus complet. | *"Temps de rendu"* |
| **Délai d’analyse** | **Expression floue** | - Utilisé pour désigner le temps passé par le laboratoire à analyser l’échantillon. <br> - Risque d’exclure le délai de transport et de transmission. | **Délai de réponse** | Voir ci-dessus. | - *"Délai d’analyse"* est trop restrictif et ne reflète pas la réalité du circuit (qui inclut le transport et la transmission). <br> - *"Délai de réponse"* est le terme global. | *"Délai d’analyse"* |

**Exemple d’emploi validé :**
> *"Pour les **urgences vitales**, le **délai de réponse** ne doit pas excéder 30 minutes, incluant le transport et l’analyse de l’échantillon."*

---
### **1.7. "Information clinique" vs. "Données patient" vs. "Contexte thérapeutique"**

| **Termes problématiques** | Type de problème | Acteurs concernés et interprétations divergentes | Terme canonique retenu | Définition | Justification métier | Termes à proscrire |
|---------------------------|------------------|--------------------------------------------------|------------------------|-----------|----------------------|--------------------|
| **Information clinique** (Étape 1 : 04_contraintes_et_risques.md) | **Synonymie implicite** | - Médecins prescripteurs : utilisent *"données patient"* ou *"contexte thérapeutique"*. <br> - SIL : utilise *"information clinique"* dans ses champs de saisie. | **Information clinique** | Donnée médicale essentielle transmise avec la demande de dosage anti-Xa : traitement en cours, heure de la dernière prise, fonction rénale, antécédents, signes cliniques. | - *"Information clinique"* est le terme le plus précis et inclut tous les éléments nécessaires à l’interprétation. <br> - Évite la confusion avec *"données patient"* (trop large) ou *"contexte thérapeutique"* (trop restrictif). <br> - Aligné sur les normes de laboratoire (ex : ISO 15189). | *"Données patient"*, *"Contexte thérapeutique"* |
| **Données patient** | **Traduction divergente** | - Utilisé pour désigner l’ensemble des informations du dossier médical. <br> - Risque d’inclure des données non pertinentes pour le dosage anti-Xa (ex : antécédents familiaux). | **Information clinique** | Voir ci-dessus. | - *"Données patient"* est trop large et peut inclure des informations inutiles. <br> - *"Information clinique"* est ciblé sur les éléments nécessaires au dosage. | *"Données patient"* |
| **Contexte thérapeutique** | **Expression floue** | - Utilisé pour désigner uniquement le traitement en cours. <br> - Risque d’exclure d’autres éléments clés (ex : fonction rénale). | **Information clinique** | Voir ci-dessus. | - *"Contexte thérapeutique"* est trop restrictif. <br> - *"Information clinique"* est plus complet. | *"Contexte thérapeutique"* |

**Exemple d’emploi validé :**
> *"La **prescription médicale** doit inclure les **informations cliniques** obligatoires : nom de l’anticoagulant, dose, heure de la dernière prise, clairance de la créatinine et motif de la demande."*

---
### **1.8. "Circuit informatisé" vs. "Workflow numérique" vs. "Système sécurisé"**

| **Termes problématiques** | Type de problème | Acteurs concernés et interprétations divergentes | Terme canonique retenu | Définition | Justification métier | Termes à proscrire |
|---------------------------|------------------|--------------------------------------------------|------------------------|-----------|----------------------|--------------------|
| **Circuit informatisé** (Étape 1 : 03_concepts_metier_initiaux.md) | **Synonymie implicite** | - Biologiste : utilise *"circuit informatisé"* pour désigner le processus numérique. <br> - SIL : parle de *"workflow numérique"*. <br> - Médecins prescripteurs : utilisent *"système sécurisé"*. | **Circuit informatisé** | Processus numérique sécurisé et tracé, géré par le SIL, pour la gestion des demandes urgentes de dosage anti-Xa, incluant la priorisation et la transmission des résultats. | - *"Circuit informatisé"* est le terme le plus complet et inclut la sécurité, la traçabilité et la priorisation. <br> - Évite la confusion avec *"workflow numérique"* (trop technique) ou *"système sécurisé"* (trop vague). <br> - Aligné sur les attentes des biologistes (ex : *"nous avons besoin d’un circuit informatisé pour gérer les urgences"*). | *"Workflow numérique"*, *"Système sécurisé"* |
| **Workflow numérique** | **Traduction divergente** | - Utilisé par les techniciens pour désigner la séquence des étapes dans le SIL. <br> - Risque de confusion avec les processus manuels. | **Circuit informatisé** | Voir ci-dessus. | - *"Workflow numérique"* est trop technique et peut exclure des aspects clés (ex : sécurité, traçabilité). <br> - *"Circuit informatisé"* est plus global. | *"Workflow numérique"* |
| **Système sécurisé** | **Expression floue** | - Utilisé pour désigner la protection des données. <br> - Risque d’exclure la traçabilité et la priorisation. | **Circuit informatisé** | Voir ci-dessus. | - *"Système sécurisé"* est trop restrictif et ne reflète pas la complexité du processus. <br> - *"Circuit informatisé"* est plus complet. | *"Système sécurisé"* |

**Exemple d’emploi validé :**
> *"Le **circuit informatisé** doit prioriser automatiquement les **demandes urgentes**, assurer la **traçabilité** de chaque étape et transmettre les résultats en temps réel aux prescripteurs."*

---
### **1.9. "Rejet d’échantillon" vs. "Refus d’analyse" vs. "Échantillon non conforme"**

| **Termes problématiques** | Type de problème | Acteurs concernés et interprétations divergentes | Terme canonique retenu | Définition | Justification métier | Termes à proscrire |
|---------------------------|------------------|--------------------------------------------------|------------------------|-----------|----------------------|--------------------|
| **Rejet d’échantillon** (Étape 2 : 08_regles_metier.md) | **Synonymie implicite** | - Biologiste : utilise *"rejet d’échantillon"*. <br> - Techniciens de laboratoire : parlent de *"refus d’analyse"*. <br> - SIL : utilise *"échantillon non conforme"*. | **Rejet d’échantillon** | Décision de ne pas analyser un échantillon biologique en raison de sa non-conformité (ex : tube inadapté, volume insuffisant, étiquetage incorrect, délai de transport dépassé). | - *"Rejet d’échantillon"* est le terme le plus clair et inclut toutes les raisons de rejet. <br> - Évite la confusion avec *"refus d’analyse"* (qui peut inclure des rejets pour d’autres raisons, ex : erreur technique). <br> - Aligné sur les pratiques de laboratoire (ex : *"l’échantillon a été rejeté pour non-conformité"*). | *"Refus d’analyse"*, *"Échantillon non conforme"* |
| **Refus d’analyse** | **Traduction divergente** | - Utilisé pour désigner le rejet pour non-conformité ou pour d’autres raisons (ex : erreur technique). <br> - Risque de confusion avec le *"rejet d’échantillon"*. | **Rejet d’échantillon** | Voir ci-dessus. | - *"Refus d’analyse"* est trop large et peut inclure des rejets non liés à la conformité. <br> - *"Rejet d’échantillon"* est plus précis. | *"Refus d’analyse"* |
| **Échantillon non conforme** | **Expression floue** | - Utilisé pour désigner un échantillon rejeté. <br> - Risque de confusion avec les échantillons simplement *"non optimaux"* (qui peuvent être analysés avec une mention). | **Rejet d’échantillon** | Voir ci-dessus. | - *"Échantillon non conforme"* est trop vague et peut inclure des cas où l’analyse est possible avec une réserve. <br> - *"Rejet d’échantillon"* est clair et définitif. | *"Échantillon non conforme"* |

**Exemple d’emploi validé :**
> *"Le biologiste a décidé du **rejet de l’échantillon** en raison d’un tube mal étiqueté et d’un volume insuffisant, conformément aux règles de validation du laboratoire."*

---
### **1.10. "Priorisation" vs. "Classement des priorités" vs. "Tri des demandes"**

| **Termes problématiques** | Type de problème | Acteurs concernés et interprétations divergentes | Terme canonique retenu | Définition | Justification métier | Termes à proscrire |
|---------------------------|------------------|--------------------------------------------------|------------------------|-----------|----------------------|--------------------|
| **Priorisation** (Étape 2 : 08_regles_metier.md) | **Synonymie implicite** | - SIL : utilise *"priorisation"*. <br> - Techniciens de laboratoire : parlent de *"classement des priorités"*. <br> - Médecins prescripteurs : utilisent *"tri des demandes"*. | **Priorisation** | Mécanisme permettant de classer les demandes de dosage anti-Xa par ordre d’urgence, en fonction de critères cliniques (ex : urgence vitale) et organisationnels (ex : disponibilité du personnel). | - *"Priorisation"* est le terme le plus clair et inclut implicitement le *"classement"* et le *"tri"*. <br> - Évite la confusion avec *"priorité"* (qui est un état, pas un mécanisme). <br> - Aligné sur les pratiques des SIL (ex : *"le SIL doit appliquer une priorisation automatique"*). | *"Classement des priorités"*, *"Tri des demandes"* |
| **Classement des priorités** | **Traduction divergente** | - Utilisé pour désigner la hiérarchisation des demandes. <br> - Risque de confusion avec *"priorité"* (qui est un état). | **Priorisation** | Voir ci-dessus. | - *"Classement des priorités"* est trop descriptif et peut inclure des étapes manuelles. <br> - *"Priorisation"* est plus dynamique et inclut les mécanismes automatiques. | *"Classement des priorités"* |
| **Tri des demandes** | **Expression floue** | - Utilisé pour désigner la sélection des demandes à traiter en premier. <br> - Risque de confusion avec le *"tri"* manuel (ex : tri par ordre alphabétique). | **Priorisation** | Voir ci-dessus. | - *"Tri des demandes"* est trop vague et peut inclure des méthodes non standardisées. <br> - *"Priorisation"* est le terme métier standard. | *"Tri des demandes"* |

**Exemple d’emploi validé :**
> *"Le SIL doit appliquer une **priorisation** automatique des **demandes urgentes**, avec un délai de réponse maximal de 1 heure pour les cas critiques."*

---

## **2. Points à valider auprès du métier**
Les ambiguïtés suivantes **ne peuvent pas être tranchées sans expertise métier** et doivent être clarifiées avec les parties prenantes :

| **Ambiguïté** | **Description** | **Acteurs à consulter** | **Questions à poser** |
|---------------|-----------------|-------------------------|-----------------------|
| **Critères de conformité des tubes de prélèvement** | Aucune liste explicite des normes de tubes ou de volumes n’est fournie dans le corpus. Les mentions sont génériques (ex : *"normes strictes"* dans Étape 1 : 04_contraintes_et_risques.md). | - Biologiste <br> - Techniciens de laboratoire <br> - Personnel infirmier | - Quels sont les types de tubes acceptés (ex : tube citraté 3,2%) ? <br> - Quel est le volume minimal requis pour l’analyse ? <br> - Quels sont les protocoles d’étiquetage (ex : étiquette machine-readable, nom du patient, heure de prélèvement) ? |
| **Mécanismes de priorisation des demandes urgentes** | Le corpus mentionne des délais de *"1 heure"* (Étape 2 : 08_regles_metier.md) et *"30 minutes"* (Étape 2 : 09_conflits_objectifs.md) pour les urgences vitales, mais aucune définition claire des critères pour distinguer une urgence vitale d’une urgence clinique standard. | - Médecins prescripteurs (Urgences, Réanimation) <br> - Biologiste | - Quels sont les critères de classement des urgences (ex : score clinique, type d’anticoagulant, fonction rénale) ? <br> - Quels sont les délais de réponse cibles par niveau de priorité (ex : <30 min pour les urgences vitales, <1h pour les urgences standard) ? |
| **Protocole standardisé de transmission des informations cliniques** | Aucune standardisation n’est décrite dans le corpus, bien que cela soit identifié comme un irritant métier (Étape 1 : 05_vision_globale_du_domaine.md). | - Médecins prescripteurs <br> - Personnel infirmier <br> - Biologiste | - Quels sont les champs obligatoires à remplir dans la prescription (ex : nom de l’anticoagulant, dose, heure de la dernière prise, DFG) ? <br> - Quel est le format de transmission (ex : champ libre, liste déroulante, intégration automatique depuis le dossier patient) ? |
| **Intégration avec les systèmes existants** | Aucune information n’est fournie sur la compatibilité du SIL avec les logiciels de prescription (ex : DxCare, Cristal) ou les automates de dosage anti-Xa. | - Équipe SIL <br> - Biologiste <br> - Équipe informatique | - Quels sont les systèmes existants à intégrer (ex : DxCare, Cristal) ? <br> - Quelle est la capacité d’interfaçage avec les automates de dosage anti-Xa ? |
| **Attentes spécifiques en matière de sécurité et de traçabilité** | Aucune précision n’est donnée sur le niveau de chiffrement requis, les modalités de sauvegarde ou les processus de validation des utilisateurs. | - Équipe SIL <br> - Équipe informatique <br> - Responsable qualité | - Quel est le niveau de chiffrement requis pour les données patients (ex : AES-256) ? <br> - Quelles sont les modalités de sauvegarde et d’archivage des données (ex : durée de conservation, accès restreint) ? <br> - Quels sont les processus de validation des utilisateurs (ex : authentification forte, logs d’audit) ? |

---
## **3. Synthèse des arbitrages terminologiques**
| **Catégorie** | **Termes problématiques** | **Terme canonique retenu** | **Justification** |
|---------------|---------------------------|----------------------------|-------------------|
| **Urgences** | *"Demande urgente"*, *"Urgence clinique"*, *"Urgence vitale"* | **Urgence clinique** (général) / **Urgence vitale** (sous-catégorie) | Clarifie la hiérarchie des priorités et aligne le vocabulaire sur les pratiques cliniques. |
| **Prescriptions** | *"Prescription médicale"*, *"Ordonnance"*, *"Demande de dosage"* | **Prescription médicale** | Distingue l’acte médical des actes de prélèvement et évite les confusions avec les *"demandes urgentes"*. |
| **Échantillons** | *"Échantillon biologique"*, *"Prélèvement"*, *"Tube de prélèvement"* | **Échantillon biologique** (matériel) / **Tube de prélèvement** (contenant) / **Acte de prélèvement** (action) | Évite les ambiguïtés entre l’objet, le contenant et l’action. |
| **Contexte** | *"Contexte clinique"*, *"Situation clinique"*, *"Contexte thérapeutique"* | **Contexte clinique** | Inclut tous les éléments nécessaires à l’interprétation (traitement, fonction rénale, antécédents). |
| **Traçabilité** | *"Traçabilité"*, *"Documentation"*, *"Historique"* | **Traçabilité** | Terme réglementaire et métier standard pour l’enregistrement systématique des étapes. |
| **Délais** | *"Délai de réponse"*, *"Temps de rendu"*, *"Délai d’analyse"* | **Délai de réponse** | Inclut implicitement le transport, l’analyse et la transmission des résultats. |
| **Informations** | *"Information clinique"*, *"Données patient"*, *"Contexte thérapeutique"* | **Information clinique** | Ciblé sur les éléments nécessaires à l’interprétation du dosage anti-Xa. |
| **Processus numérique** | *"Circuit informatisé"*, *"Workflow numérique"*, *"Système sécurisé"* | **Circuit informatisé** | Inclut la sécurité, la traçabilité et la priorisation. |
| **Rejets** | *"Rejet d’échantillon"*, *"Refus d’analyse"*, *"Échantillon non conforme"* | **Rejet d’échantillon** | Définitif et clair, évite les confusions avec des rejets partiels. |
| **Hiérarchisation** | *"Priorisation"*, *"Classement des priorités"*, *"Tri des demandes"* | **Priorisation** | Mécanisme dynamique incluant les critères cliniques et organisationnels. |

---
## **4. Règles de nommage pour les ateliers, la documentation et le code**
Pour garantir la cohérence du langage commun dans les ateliers, la documentation et le code, les règles suivantes doivent être appliquées :

### **4.1. Termes canoniques obligatoires**
Utiliser **exclusivement** les termes du glossaire ci-dessus dans :
- Les ateliers (Event Storming, Domain Storytelling).
- Les user stories.
- La documentation technique (spécifications, manuels utilisateurs).
- Le code (noms de classes, méthodes, variables).

**Exemples :**
| **Contexte** | **À éviter** | **À utiliser** |
|--------------|---------------|----------------|
| **User story** | *"En tant que médecin, je veux une ordonnance urgente pour un dosage anti-Xa."* | *"En tant que médecin prescripteur, je souhaite saisir une **prescription médicale** pour un **dosage anti-Xa** en situation d’**urgence clinique**, incluant les **informations cliniques** obligatoires."* |
| **Nom de classe (code)** | `PrescriptionUrgent` | `PrescriptionMedicale` |
| **Nom de méthode (code)** | `getTempsRendu()` | `getDelaiReponse()` |
| **Nom de variable (code)** | `tubeNonConforme` | `rejetEchantillon` |

---

### **4.2. Formes grammaticales**
- **Privilégier les noms** pour les concepts :
  - *"La **priorisation** des demandes urgentes est automatique."*
  - *"Le **rejet de l’échantillon** est décidé par le biologiste."*
- **Utiliser des verbes d’action** pour les processus :
  - *"Le SIL doit **prioriser** les demandes urgentes."*
  - *"Le personnel infirmier doit **vérifier la conformité** du tube."*

---
### **4.3. Identifiants uniques (snake_case)**
Pour les concepts clés, utiliser des identifiants en **snake_case** :
- `prescription_medicale`
- `echantillon_biologique`
- `delai_reponse`
- `rejet_echantillon`
- `contexte_clinique`

---
### **4.4. Éviter le jargon technique**
- Remplacer les termes techniques par leur équivalent métier :
  - Utiliser *"SIL"* plutôt que *"LIS"* (Laboratory Information System).
  - Utiliser *"DFG"* (Débit de Filtration Glomérulaire) plutôt que *"clairance de la créatinine"* (sauf à la première occurrence).
- Éviter les acronymes non expliqués :
  - *"RGPD"* doit être défini à sa première occurrence (*Règlement Général sur la Protection des Données*).

---
### **4.5. Exemples de phrases types**
#### **Pour les user stories :**
1. *"En tant que **médecin prescripteur**, je souhaite saisir une **prescription médicale** avec les **informations cliniques** obligatoires (traitement, heure de la dernière prise, fonction rénale) afin que le **dosage anti-Xa** soit interprété correctement."*
2. *"En tant que **biologiste**, je souhaite recevoir une **alerte** si un **échantillon biologique** est **non conforme** (tube inadapté, volume insuffisant) afin de **rejeter l’échantillon** et éviter une erreur d’interprétation."*
3. *"En tant que **technicien de laboratoire**, je souhaite que le **SIL** **priorise automatiquement** les **demandes urgentes** afin de garantir un **délai de réponse** inférieur à 1 heure pour les cas critiques."*

#### **Pour la documentation technique :**
- *"Le **circuit informatisé** doit assurer la **traçabilité** de chaque **prescription médicale**, depuis la saisie jusqu’à la transmission des résultats."*
- *"Le **SIL** doit appliquer une **priorisation** basée sur les niveaux d’**urgence clinique** (urgence vitale, urgence standard)."*

#### **Pour le code :**
```python
class PrescriptionMedicale:
    def __init__(self, patient_id: str, anticoagulant: str, dose: float, heure_derniere_prise: datetime, dfg: float):
        self.patient_id = patient_id
        self.anticoagulant = anticoagulant  # ex: "apixaban"
        self.dose = dose
        self.heure_derniere_prise = heure_derniere_prise
        self.dfg = dfg  # Débit de Filtration Glomérulaire
        self.urgence = self._determiner_urgence()

    def _determiner_urgence(self) -> str:
        if self._est_urgence_vitale():
            return "urgence_vitale"
        else:
            return "urgence_standard"

    def _est_urgence_vitale(self) -> bool:
        # Logique métier pour déterminer si la prescription est une urgence vitale
        pass
```

---
## **5. Annexe : Sources des arbitrages**
| **Ambiguïté** | **Sources principales** | **Termes canoniques retenus** |
|---------------|--------------------------|-------------------------------|
| *"Demande urgente"* vs. *"Urgence clinique"* | Étape 1 : 01_reformulation_du_besoin.md, Étape 2 : 08_regles_metier.md, Étape 2 : 09_conflits_objectifs.md | **Urgence clinique** / **Urgence vitale** |
| *"Prescription médicale"* vs. *"Ordonnance"* | Étape 1 : 03_concepts_metier_initiaux.md, Étape 2 : 07_responsabilites_acteurs.md | **Prescription médicale** |
| *"Échantillon biologique"* vs. *"Prélèvement"* | Étape 1 : 03_concepts_metier_initiaux.md, Étape 2 : 08_regles_metier.md | **Échantillon biologique** / **Tube de prélèvement** / **Acte de prélèvement** |
| *"Contexte clinique"* vs. *"Situation clinique"* | Étape 1 : 03_concepts_metier_initiaux.md, Étape 2 : 07_responsabilites_acteurs.md | **Contexte clinique** |
| *"Traçabilité"* vs. *"Documentation"* | Étape 1 : 03_concepts_metier_initiaux.md, Étape 2 : 08_regles_metier.md | **Traçabilité** |
| *"Délai de réponse"* vs. *"Temps de rendu"* | Étape 2 : 08_regles_metier.md | **Délai de réponse** |
| *"Information clinique"* vs. *"Données patient"* | Étape 1 : 04_contraintes_et_risques.md, Étape 2 : 08_regles_metier.md | **Information clinique** |
| *"Circuit informatisé"* vs. *"Workflow numérique"* | Étape 1 : 03_concepts_metier_initiaux.md, Étape 2 : 08_regles_metier.md | **Circuit informatisé** |
| *"Rejet d’échantillon"* vs. *"Refus d’analyse"* | Étape 2 : 08_regles_metier.md | **Rejet d’échantillon** |
| *"Priorisation"* vs. *"Classement des priorités"* | Étape 2 : 08_regles_metier.md | **Priorisation** |