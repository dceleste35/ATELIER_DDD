# Ambiguïtés terminologiques résolues
**Domaine : Circuit des demandes urgentes de dosage anti-Xa**

---

## Introduction

Ce document identifie et résout les ambiguïtés terminologiques présentes dans le corpus métier. Pour chaque cas, nous précisons :
- Les termes problématiques et leur type d'ambiguïté
- Les acteurs concernés et leurs interprétations divergentes
- Le terme canonique retenu avec sa définition
- La justification métier de l'arbitrage
- Les termes à proscrire

Les ambiguïtés non tranchables sans expertise métier sont listées en section "Points à valider auprès du métier".

---

## 1. Ambiguïtés terminologiques identifiées et résolues

---

### **1.1. "Anticoagulant oral direct" vs. "AOD" vs. "anticoagulant direct oral"**

| **Problème** | **Type** | **Acteurs concernés et leurs interprétations** |
|--------------|----------|------------------------------------------------|
| **Termes problématiques** : "Anticoagulant oral direct", "AOD", "anticoagulant direct oral" | **Synonymie + traduction divergente** | - **Médecins prescripteurs** : Utilisent indifféremment "AOD" ou "anticoagulant oral direct".<br>- **Biologiste** : Préfère "anticoagulant oral direct" pour éviter toute confusion avec les anticoagulants injectables (ex : héparine).<br>- **Techniciens de laboratoire** : Utilisent "AOD" dans les protocoles internes.<br>- **SIL** : Le terme "AOD" est souvent utilisé dans les interfaces techniques. |

| **Terme canonique retenu** | **Définition** | **Justification métier** | **Termes à proscrire** |
|----------------------------|----------------|---------------------------|-------------------------|
| **Anticoagulant oral direct** | Médicament antithrombotique agissant directement sur un facteur de coagulation (ex : apixaban, rivaroxaban, dabigatran, édoxaban) administré par voie orale. | - **Clarté** : Évite toute confusion avec les anticoagulants injectables (héparine, AVK).<br>- **Précision** : Le terme "oral" est essentiel pour distinguer ces molécules des autres anticoagulants.<br>- **Standardisation** : Aligné sur les recommandations de la HAS (Haute Autorité de Santé) et des sociétés savantes (ex : GEHT). | AOD, anticoagulant direct oral |

| **Exemple d'emploi** |
|----------------------|
| *"Le patient est sous anticoagulant oral direct (apixaban), il faut vérifier le dosage anti-Xa en urgence."* |

| **Source** |
|------------|
| Étape 1 (03_concepts_metier_initiaux.md), Étape 2 (06_cartographie_acteurs.md), Corpus initial (demande_biologiste.md) |

---

### **1.2. "Contexte clinique" vs. "situation clinique" vs. "contexte thérapeutique"**

| **Problème** | **Type** | **Acteurs concernés et leurs interprétations** |
|--------------|----------|------------------------------------------------|
| **Termes problématiques** : "Contexte clinique", "situation clinique", "contexte thérapeutique" | **Synonymie + glissement de sens** | - **Médecins prescripteurs** : Utilisent "situation clinique" pour décrire l'état général du patient.<br>- **Biologiste** : Préfère "contexte clinique" pour insister sur les éléments pertinents pour l'interprétation du dosage anti-Xa (traitement, fonction rénale, heure de la dernière prise).<br>- **Personnel infirmier** : Utilise "contexte thérapeutique" pour désigner les traitements en cours.<br>- **SIL** : Le terme "contexte clinique" est utilisé dans les champs de saisie. |

| **Terme canonique retenu** | **Définition** | **Justification métier** | **Termes à proscrire** |
|----------------------------|----------------|---------------------------|-------------------------|
| **Contexte clinique** | Ensemble des informations médicales pertinentes pour interpréter un dosage anti-Xa : traitement en cours (anticoagulant oral direct), fonction rénale, heure de la dernière prise, antécédents thrombotiques ou hémorragiques, et autres éléments influençant l'interprétation (ex : insuffisance hépatique). | - **Précision** : Le terme "clinique" est plus large que "thérapeutique" et inclut tous les éléments nécessaires à l'interprétation.<br>- **Standardisation** : Aligné sur les pratiques des biologistes et des sociétés savantes (ex : SFBC).<br>- **Exhaustivité** : Inclut explicitement la fonction rénale et l'heure de la dernière prise, critiques pour l'interprétation. | Situation clinique, contexte thérapeutique |

| **Exemple d'emploi** |
|----------------------|
| *"Le contexte clinique montre une insuffisance rénale aiguë et un traitement par rivaroxaban, ce qui influence l'interprétation du résultat anti-Xa."* |

| **Source** |
|------------|
| Étape 1 (03_concepts_metier_initiaux.md), Étape 2 (07_responsabilites_acteurs.md) |

---

### **1.3. "Prescription médicale" vs. "ordonnance" vs. "demande de dosage"**

| **Problème** | **Type** | **Acteurs concernés et leurs interprétations** |
|--------------|----------|------------------------------------------------|
| **Termes problématiques** : "Prescription médicale", "ordonnance", "demande de dosage" | **Synonymie + traduction divergente** | - **Médecins prescripteurs** : Utilisent "ordonnance" ou "prescription médicale" indifféremment.<br>- **Personnel infirmier** : Utilise "demande de dosage" pour désigner l'acte de prescription.<br>- **Biologiste** : Préfère "prescription médicale" pour insister sur l'acte médical.<br>- **SIL** : Le terme "demande de dosage" est utilisé dans les interfaces techniques. |

| **Terme canonique retenu** | **Définition** | **Justification métier** | **Termes à proscrire** |
|----------------------------|----------------|---------------------------|-------------------------|
| **Prescription médicale** | Acte par lequel un médecin ordonne un dosage anti-Xa pour un patient, incluant les informations cliniques nécessaires (traitement en cours, fonction rénale, heure de la dernière prise). | - **Précision** : Insiste sur l'acte médical et l'inclusion des informations cliniques.<br>- **Standardisation** : Aligné sur les pratiques des médecins et des sociétés savantes (ex : CNOM).<br>- **Exhaustivité** : Inclut explicitement les informations nécessaires à l'analyse. | Ordonnance, demande de dosage, prescription thérapeutique |

| **Exemple d'emploi** |
|----------------------|
| *"La prescription médicale pour un dosage anti-Xa urgent a été transmise aux infirmiers du service de réanimation, incluant le traitement par apixaban et une fonction rénale à 30 mL/min."* |

| **Source** |
|------------|
| Étape 1 (03_concepts_metier_initiaux.md), Étape 2 (09_conflits_objectifs.md) |

---
### **1.4. "Échantillon biologique" vs. "prélèvement" vs. "tube sanguin"**

| **Problème** | **Type** | **Acteurs concernés et leurs interprétations** |
|--------------|----------|------------------------------------------------|
| **Termes problématiques** : "Échantillon biologique", "prélèvement", "tube sanguin" | **Synonymie + homonymie** | - **Personnel infirmier** : Utilise "prélèvement" pour désigner l'acte de collecte et "tube sanguin" pour le contenant.<br>- **Techniciens de laboratoire** : Utilisent "échantillon biologique" pour désigner le matériel analysé.<br>- **Biologiste** : Préfère "échantillon biologique" pour insister sur la qualité et la conformité.<br>- **SIL** : Le terme "échantillon" est utilisé dans les interfaces techniques. |

| **Terme canonique retenu** | **Définition** | **Justification métier** | **Termes à proscrire** |
|----------------------------|----------------|---------------------------|-------------------------|
| **Échantillon biologique** | Matériel biologique (sang total ou plasma) prélevé pour réaliser un dosage anti-Xa. Doit être conforme aux normes de prélèvement (type de tube, volume, étiquetage, délai de transport). | - **Précision** : Inclut explicitement le type de matériel (sang total ou plasma) et les exigences de conformité.<br>- **Standardisation** : Aligné sur les pratiques des techniciens de laboratoire et des sociétés savantes (ex : SFBC).<br>- **Exhaustivité** : Couvre à la fois l'acte de prélèvement et le contenant. | Prélèvement, tube sanguin, tube à prélèvement |

| **Exemple d'emploi** |
|----------------------|
| *"L'échantillon biologique a été prélevé dans un tube citrate 3.2% et transporté au laboratoire en moins de 30 minutes pour garantir la fiabilité du dosage anti-Xa."* |

| **Source** |
|------------|
| Étape 1 (03_concepts_metier_initiaux.md), Étape 2 (07_responsabilites_acteurs.md) |

---
### **1.5. "Conformité de l'échantillon" vs. "qualité de l'échantillon"**

| **Problème** | **Type** | **Acteurs concernés et leurs interprétations** |
|--------------|----------|------------------------------------------------|
| **Termes problématiques** : "Conformité de l'échantillon", "qualité de l'échantillon" | **Synonymie + glissement de sens** | - **Biologiste** : Utilise "conformité de l'échantillon" pour désigner le respect des normes de prélèvement (type de tube, volume, étiquetage).<br>- **Techniciens de laboratoire** : Utilisent "qualité de l'échantillon" pour désigner l'intégrité du matériel analysé.<br>- **Personnel infirmier** : Utilise les deux termes de manière interchangeable. |

| **Terme canonique retenu** | **Définition** | **Justification métier** | **Termes à proscrire** |
|----------------------------|----------------|---------------------------|-------------------------|
| **Conformité de l'échantillon** | Respect des normes de prélèvement (type de tube, volume, étiquetage, délai de transport) pour garantir la fiabilité du dosage anti-Xa. | - **Précision** : Insiste sur le respect des normes, qui est une condition préalable à la qualité de l'analyse.<br>- **Standardisation** : Aligné sur les pratiques des biologistes et des sociétés savantes (ex : SFBC).<br>- **Exhaustivité** : Couvre tous les aspects critiques pour la fiabilité de l'analyse. | Qualité de l'échantillon, échantillon conforme |

| **Exemple d'emploi** |
|----------------------|
| *"L'échantillon n'est pas conforme : le tube n'est pas un citrate 3.2%, il doit être rejeté et un nouveau prélèvement doit être effectué."* |

| **Source** |
|------------|
| Étape 1 (04_contraintes_et_risques.md), Étape 2 (08_regles_metier.md) |

---
### **1.6. "Dosage anti-Xa" vs. "mesure anti-Xa" vs. "test anti-Xa"**

| **Problème** | **Type** | **Acteurs concernés et leurs interprétations** |
|--------------|----------|------------------------------------------------|
| **Termes problématiques** : "Dosage anti-Xa", "mesure anti-Xa", "test anti-Xa" | **Synonymie + traduction divergente** | - **Biologiste** : Utilise "dosage anti-Xa" pour désigner l'analyse biologique.<br>- **Techniciens de laboratoire** : Utilisent "mesure anti-Xa" dans les protocoles techniques.<br>- **Médecins prescripteurs** : Utilisent "test anti-Xa" dans les prescriptions.<br>- **SIL** : Le terme "dosage" est utilisé dans les interfaces. |

| **Terme canonique retenu** | **Définition** | **Justification métier** | **Termes à proscrire** |
|----------------------------|----------------|---------------------------|-------------------------|
| **Dosage anti-Xa** | Mesure de l'activité inhibitrice des anticoagulants oraux directs sur le facteur Xa de la coagulation, exprimée en UI/mL ou ng/mL selon l'anticoagulant. | - **Précision** : Le terme "dosage" est standard dans le domaine biologique et médical.<br>- **Standardisation** : Aligné sur les pratiques des biologistes et des sociétés savantes (ex : SFBC).<br>- **Clarté** : Évite toute confusion avec d'autres types de tests (ex : dosage de la créatinine). | Mesure anti-Xa, test anti-Xa, activité anti-Xa |

| **Exemple d'emploi** |
|----------------------|
| *"Le dosage anti-Xa du patient est à 0,5 UI/mL, ce qui correspond à une activité thérapeutique pour l'apixaban."* |

| **Source** |
|------------|
| Étape 1 (03_concepts_metier_initiaux.md), Corpus initial (demande_biologiste.md) |

---
### **1.7. "Résultat du dosage anti-Xa" vs. "valeur anti-Xa"**

| **Problème** | **Type** | **Acteurs concernés et leurs interprétations** |
|--------------|----------|------------------------------------------------|
| **Termes problématiques** : "Résultat du dosage anti-Xa", "valeur anti-Xa" | **Synonymie** | - **Biologiste** : Utilise "résultat du dosage anti-Xa" pour désigner la valeur numérique ou qualitative issue de l'analyse.<br>- **Médecins prescripteurs** : Utilisent "valeur anti-Xa" dans les échanges cliniques.<br>- **SIL** : Le terme "résultat" est utilisé dans les interfaces techniques. |

| **Terme canonique retenu** | **Définition** | **Justification métier** | **Termes à proscrire** |
|----------------------------|----------------|---------------------------|-------------------------|
| **Résultat du dosage anti-Xa** | Valeur numérique ou qualitative issue de l'analyse biologique, interprétée par le biologiste en fonction du contexte clinique. | - **Précision** : Insiste sur le fait que le résultat est issu d'un dosage et doit être interprété.<br>- **Standardisation** : Aligné sur les pratiques des biologistes et des sociétés savantes (ex : SFBC).<br>- **Exhaustivité** : Couvre à la fois la valeur numérique et son interprétation. | Valeur anti-Xa, résultat anti-Xa |

| **Exemple d'emploi** |
|----------------------|
| *"Le résultat du dosage anti-Xa est de 0,3 UI/mL, ce qui indique une sous-anticoagulation pour l'apixaban. Une adaptation du traitement est nécessaire."* |

| **Source** |
|------------|
| Étape 1 (03_concepts_metier_initiaux.md), Étape 2 (07_responsabilites_acteurs.md) |

---
### **1.8. "Traçabilité" vs. "suivi" vs. "historique"**

| **Problème** | **Type** | **Acteurs concernés et leurs interprétations** |
|--------------|----------|------------------------------------------------|
| **Termes problématiques** : "Traçabilité", "suivi", "historique" | **Synonymie + traduction divergente** | - **Biologiste** : Utilise "traçabilité" pour désigner l'enregistrement systématique de chaque étape du circuit.<br>- **Techniciens de laboratoire** : Utilisent "suivi" pour désigner le suivi des échantillons dans le SIL.<br>- **SIL** : Le terme "traçabilité" est utilisé dans les interfaces techniques.<br>- **Médecins prescripteurs** : Utilisent "historique" pour désigner l'historique des dosages. |

| **Terme canonique retenu** | **Définition** | **Justification métier** | **Termes à proscrire** |
|----------------------------|----------------|---------------------------|-------------------------|
| **Traçabilité** | Capacité à suivre et documenter chaque étape du circuit des demandes urgentes de dosage anti-Xa : de la prescription au résultat, en passant par le prélèvement, le transport et l'analyse. | - **Précision** : Insiste sur l'enregistrement systématique et complet de chaque étape.<br>- **Standardisation** : Aligné sur les pratiques des biologistes et des sociétés savantes (ex : SFBC, HAS).<br>- **Exhaustivité** : Couvre tous les aspects critiques pour la sécurité et la conformité réglementaire. | Suivi, historique, documentation |

| **Exemple d'emploi** |
|----------------------|
| *"La traçabilité du dosage anti-Xa doit inclure l'identité du patient, l'heure de prélèvement, le type de tube utilisé, l'heure de réception au laboratoire, et l'heure de transmission du résultat."* |

| **Source** |
|------------|
| Étape 1 (03_concepts_metier_initiaux.md), Étape 2 (08_regles_metier.md) |

---
### **1.9. "Délai critique" vs. "délai d'urgence" vs. "délai maximal"**

| **Problème** | **Type** | **Acteurs concernés et leurs interprétations** |
|--------------|----------|------------------------------------------------|
| **Termes problématiques** : "Délai critique", "délai d'urgence", "délai maximal" | **Synonymie + traduction divergente** | - **Médecins prescripteurs** : Utilisent "délai d'urgence" pour désigner le temps maximal acceptable pour un dosage urgent.<br>- **Biologiste** : Utilise "délai critique" pour insister sur l'impact sur la sécurité du patient.<br>- **SIL** : Le terme "délai maximal" est utilisé dans les interfaces techniques. |

| **Terme canonique retenu** | **Définition** | **Justification métier** | **Termes à proscrire** |
|----------------------------|----------------|---------------------------|-------------------------|
| **Délai critique** | Temps maximal autorisé pour réaliser un dosage anti-Xa sans compromettre la sécurité du patient. Pour les demandes urgentes, ce délai est généralement de 1 heure après réception de l'échantillon au laboratoire. | - **Précision** : Insiste sur l'impact direct sur la sécurité du patient.<br>- **Standardisation** : Aligné sur les pratiques des cliniciens et des sociétés savantes (ex : SFAR).<br>- **Exhaustivité** : Inclut une valeur par défaut (1 heure) tout en permettant des ajustements selon le contexte clinique. | Délai d'urgence, délai maximal |

| **Exemple d'emploi** |
|----------------------|
| *"Le délai critique pour ce dosage anti-Xa est de 1 heure en raison de l'hémorragie active du patient sous apixaban. Le résultat doit être transmis au prescripteur dans ce délai."* |

| **Source** |
|------------|
| Étape 1 (04_contraintes_et_risques.md), Étape 2 (08_regles_metier.md) |

---
### **1.10. "Priorisation" vs. "classement par urgence" vs. "tri des demandes"**

| **Problème** | **Type** | **Acteurs concernés et leurs interprétations** |
|--------------|----------|------------------------------------------------|
| **Termes problématiques** : "Priorisation", "classement par urgence", "tri des demandes" | **Synonymie** | - **SIL** : Utilise "priorisation" pour désigner le processus d'attribution d'un niveau de priorité aux demandes.<br>- **Techniciens de laboratoire** : Utilisent "classement par urgence" pour désigner l'ordre de traitement des demandes.<br>- **Médecins prescripteurs** : Utilisent "tri des demandes" pour désigner la sélection des demandes urgentes. |

| **Terme canonique retenu** | **Définition** | **Justification métier** | **Termes à proscrire** |
|----------------------------|----------------|---------------------------|-------------------------|
| **Priorisation** | Processus d'attribution d'un niveau de priorité aux demandes de dosage anti-Xa en fonction de l'urgence clinique. Les demandes urgentes (ex : hémorragie, thrombose) sont traitées en priorité. | - **Précision** : Insiste sur le processus systématique et objectif.<br>- **Standardisation** : Aligné sur les pratiques des techniciens de laboratoire et des sociétés savantes (ex : SFBC).<br>- **Exhaustivité** : Couvre tous les aspects critiques pour la réactivité du laboratoire. | Classement par urgence, tri des demandes |

| **Exemple d'emploi** |
|----------------------|
| *"Le SIL applique une priorisation automatique des demandes urgentes de dosage anti-Xa pour réduire les délais d'analyse et garantir la sécurité des patients."* |

| **Source** |
|------------|
| Étape 1 (03_concepts_metier_initiaux.md), Étape 2 (08_regles_metier.md) |

---
### **1.11. "Information clinique" vs. "données patient" vs. "informations thérapeutiques"**

| **Problème** | **Type** | **Acteurs concernés et leurs interprétations** |
|--------------|----------|------------------------------------------------|
| **Termes problématiques** : "Information clinique", "données patient", "informations thérapeutiques" | **Synonymie + traduction divergente** | - **Médecins prescripteurs** : Utilisent "données patient" pour désigner les informations médicales.<br>- **Personnel infirmier** : Utilisent "informations thérapeutiques" pour désigner les traitements en cours.<br>- **Biologiste** : Utilise "information clinique" pour insister sur l'exhaustivité des données nécessaires à l'interprétation. |

| **Terme canonique retenu** | **Définition** | **Justification métier** | **Termes à proscrire** |
|----------------------------|----------------|---------------------------|-------------------------|
| **Information clinique** | Données médicales transmises avec la demande de dosage anti-Xa : traitement en cours (anticoagulant oral direct), fonction rénale, heure de la dernière prise, et contexte clinique (ex : antécédents thrombotiques ou hémorragiques). | - **Précision** : Insiste sur l'exhaustivité des données nécessaires à l'interprétation.<br>- **Standardisation** : Aligné sur les pratiques des biologistes et des sociétés savantes (ex : SFBC).<br>- **Exhaustivité** : Couvre tous les aspects critiques pour l'interprétation du dosage. | Données patient, informations thérapeutiques |

| **Exemple d'emploi** |
|----------------------|
| *"Les informations cliniques transmises avec la demande incluent le traitement par apixaban, une fonction rénale à 30 mL/min, et une heure de dernière prise à 14h."* |

| **Source** |
|------------|
| Étape 1 (04_contraintes_et_risques.md), Étape 2 (07_responsabilites_acteurs.md) |

---
### **1.12. "Rejet d'échantillon" vs. "refus d'analyse" vs. "échantillon non conforme"**

| **Problème** | **Type** | **Acteurs concernés et leurs interprétations** |
|--------------|----------|------------------------------------------------|
| **Termes problématiques** : "Rejet d'échantillon", "refus d'analyse", "échantillon non conforme" | **Synonymie + traduction divergente** | - **Biologiste** : Utilise "rejet d'échantillon" pour désigner la décision de ne pas analyser un échantillon non conforme.<br>- **Techniciens de laboratoire** : Utilisent "refus d'analyse" pour désigner la même décision.<br>- **Personnel infirmier** : Utilise "échantillon non conforme" pour désigner le matériel rejeté. |

| **Terme canonique retenu** | **Définition** | **Justification métier** | **Termes à proscrire** |
|----------------------------|----------------|---------------------------|-------------------------|
| **Rejet d'échantillon** | Décision de ne pas analyser un échantillon en raison de sa non-conformité (ex : tube inadapté, étiquetage incorrect, délai de transport dépassé). | - **Précision** : Insiste sur la décision formelle et ses conséquences.<br>- **Standardisation** : Aligné sur les pratiques des biologistes et des sociétés savantes (ex : SFBC).<br>- **Exhaustivité** : Couvre toutes les raisons de rejet. | Refus d'analyse, échantillon non conforme |

| **Exemple d'emploi** |
|----------------------|
| *"L'échantillon a été rejeté car le tube n'était pas un citrate 3.2% et l'étiquetage était incomplet. Une nouvelle demande doit être faite avec un prélèvement conforme."* |

| **Source** |
|------------|
| Étape 1 (04_contraintes_et_risques.md), Étape 2 (08_regles_metier.md) |

---
### **1.13. "Urgence clinique" vs. "situation critique" vs. "urgence thérapeutique"**

| **Problème** | **Type** | **Acteurs concernés et leurs interprétations** |
|--------------|----------|------------------------------------------------|
| **Termes problématiques** : "Urgence clinique", "situation critique", "urgence thérapeutique" | **Synonymie + glissement de sens** | - **Médecins prescripteurs** : Utilisent "urgence clinique" pour désigner une situation nécessitant une réponse immédiate.<br>- **Biologiste** : Utilise "situation critique" pour insister sur la gravité.<br>- **Personnel infirmier** : Utilise "urgence thérapeutique" pour désigner une situation nécessitant un ajustement du traitement. |

| **Terme canonique retenu** | **Définition** | **Justification métier** | **Termes à proscrire** |
|----------------------------|----------------|---------------------------|-------------------------|
| **Urgence clinique** | Situation où le délai de réponse pour un dosage anti-Xa impacte directement la sécurité du patient (ex : suspicion de surdosage, hémorragie active, thrombose artérielle ou veineuse). | - **Précision** : Insiste sur l'impact direct sur la sécurité du patient.<br>- **Standardisation** : Aligné sur les pratiques des cliniciens et des sociétés savantes (ex : SFAR, HAS).<br>- **Exhaustivité** : Couvre les situations critiques nécessitant une réponse immédiate. | Situation critique, urgence thérapeutique |

| **Exemple d'emploi** |
|----------------------|
| *"Ce patient en réanimation présente une hémorragie sous apixaban : c'est une urgence clinique nécessitant un dosage anti-Xa immédiat et un résultat dans un délai critique de 1 heure."* |

| **Source** |
|------------|
| Étape 1 (03_concepts_metier_initiaux.md), Étape 2 (08_regles_metier.md) |

---
### **1.14. "Transmission des informations" vs. "transmission des données" vs. "communication clinique"**

| **Problème** | **Type** | **Acteurs concernés et leurs interprétations** |
|--------------|----------|------------------------------------------------|
| **Termes problématiques** : "Transmission des informations", "transmission des données", "communication clinique" | **Synonymie + traduction divergente** | - **Médecins prescripteurs** : Utilisent "communication clinique" pour désigner l'échange d'informations entre acteurs.<br>- **Personnel infirmier** : Utilisent "transmission des informations" pour désigner la transmission des données cliniques.<br>- **SIL** : Utilise "transmission des données" dans les interfaces techniques. |

| **Terme canonique retenu** | **Définition** | **Justification métier** | **Termes à proscrire** |
|----------------------------|----------------|---------------------------|-------------------------|
| **Transmission des informations** | Processus de communication des données cliniques entre les acteurs (médecins prescripteurs, personnel infirmier, biologistes) via des canaux sécurisés (ex : SIL, messagerie instantanée). | - **Précision** : Insiste sur le processus et les canaux de communication.<br>- **Standardisation** : Aligné sur les pratiques des acteurs et les exigences de sécurité (ex : RGPD).<br>- **Exhaustivité** : Couvre tous les aspects critiques pour la qualité des échanges. | Transmission des données, communication clinique |

| **Exemple d'emploi** |
|----------------------|
| *"La transmission des informations cliniques doit être complète et précise pour éviter les erreurs d'interprétation du dosage anti-Xa. Les données doivent être transmises via le SIL pour garantir la traçabilité."* |

| **Source** |
|------------|
| Étape 1 (04_contraintes_et_risques.md), Étape 2 (09_conflits_objectifs.md) |

---
### **1.15. "Standardisation" vs. "normalisation" vs. "uniformisation"**

| **Problème** | **Type** | **Acteurs concernés et leurs interprétations** |
|--------------|----------|------------------------------------------------|
| **Termes problématiques** : "Standardisation", "normalisation", "uniformisation" | **Synonymie** | - **SIL** : Utilise "standardisation" pour désigner la définition de formats et protocoles communs.<br>- **Biologiste** : Utilise "normalisation" pour désigner l'application de normes.<br>- **Médecins prescripteurs** : Utilisent "uniformisation" pour désigner l'harmonisation des pratiques. |

| **Terme canonique retenu** | **Définition** | **Justification métier** | **Termes à proscrire** |
|----------------------------|----------------|---------------------------|-------------------------|
| **Standardisation** | Processus de définition de formats et protocoles communs pour la transmission des informations cliniques et la gestion des demandes dans le SIL. | - **Précision** : Insiste sur la définition de règles communes et reproductibles.<br>- **Standardisation** : Aligné sur les pratiques des acteurs et les exigences de qualité (ex : ISO 15189).<br>- **Exhaustivité** : Couvre tous les aspects critiques pour l'interopérabilité et la traçabilité. | Normalisation, uniformisation |

| **Exemple d'emploi** |
|----------------------|
| *"La standardisation des informations cliniques dans le SIL permettra d'améliorer la qualité des demandes de dosage anti-Xa et de réduire les erreurs d'interprétation."* |

| **Source** |
|------------|
| Étape 1 (05_vision_globale_du_domaine.md), Étape 2 (09_conflits_objectifs.md) |

---
### **1.16. "Sécurité des données" vs. "protection des données" vs. "confidentialité"**

| **Problème** | **Type** | **Acteurs concernés et leurs interprétations** |
|--------------|----------|------------------------------------------------|
| **Termes problématiques** : "Sécurité des données", "protection des données", "confidentialité" | **Synonymie + traduction divergente** | - **SIL** : Utilise "sécurité des données" pour désigner la protection des informations patients.<br>- **Biologiste** : Utilise "protection des données" pour insister sur le respect du RGPD.<br>- **Médecins prescripteurs** : Utilisent "confidentialité" pour désigner le respect du secret médical. |

| **Terme canonique retenu** | **Définition** | **Justification métier** | **Termes à proscrire** |
|----------------------------|----------------|---------------------------|-------------------------|
| **Sécurité des données** | Protection des informations patients conformément au RGPD et aux politiques hospitalières, incluant la confidentialité, l'intégrité et la disponibilité des données. | - **Précision** : Insiste sur l'ensemble des mesures de protection (confidentialité, intégrité, disponibilité).<br>- **Standardisation** : Aligné sur les pratiques des acteurs et les exigences réglementaires (ex : RGPD, HDS).<br>- **Exhaustivité** : Couvre tous les aspects critiques pour la protection des données. | Protection des données, confidentialité |

| **Exemple d'emploi** |
|----------------------|
| *"La sécurité des données patients dans le SIL doit être garantie pour éviter les violations de confidentialité et les risques juridiques. Le chiffrement et les accès restreints sont obligatoires."* |

| **Source** |
|------------|
| Étape 1 (04_contraintes_et_risques.md), Étape 2 (08_regles_metier.md) |

---
### **1.17. "Documentation" vs. "archivage" vs. "enregistrement"**

| **Problème** | **Type** | **Acteurs concernés et leurs interprétations** |
|--------------|----------|------------------------------------------------|
| **Termes problématiques** : "Documentation", "archivage", "enregistrement" | **Synonymie + traduction divergente** | - **Techniciens de laboratoire** : Utilisent "documentation" pour désigner l'enregistrement des étapes du circuit.<br>- **SIL** : Utilise "enregistrement" pour désigner la saisie des données dans le système.<br>- **Biologiste** : Utilise "archivage" pour désigner le stockage à long terme des données. |

| **Terme canonique retenu** | **Définition** | **Justification métier** | **Termes à proscrire** |
|----------------------------|----------------|---------------------------|-------------------------|
| **Documentation** | Enregistrement écrit ou numérique de chaque étape du circuit des demandes urgentes de dosage anti-Xa : prescription, prélèvement, transport, analyse, résultat. | - **Précision** : Insiste sur l'enregistrement systématique et complet de chaque étape.<br>- **Standardisation** : Aligné sur les pratiques des acteurs et les exigences réglementaires (ex : HAS, ISO 15189).<br>- **Exhaustivité** : Couvre tous les aspects critiques pour la traçabilité et la conformité. | Archivage, enregistrement |

| **Exemple d'emploi** |
|----------------------|
| *"La documentation de chaque étape du circuit est obligatoire pour assurer la traçabilité et la conformité réglementaire. Elle doit inclure l'identité du patient, l'heure de prélèvement, le type de tube, et l'heure de réception au laboratoire."* |

| **Source** |
|------------|
| Étape 1 (03_concepts_metier_initiaux.md), Étape 2 (08_regles_metier.md) |

---
### **1.18. "Délai de réponse" vs. "temps de réponse" vs. "délai d'analyse"**

| **Problème** | **Type** | **Acteurs concernés et leurs interprétations** |
|--------------|----------|------------------------------------------------|
| **Termes problématiques** : "Délai de réponse", "temps de réponse", "délai d'analyse" | **Synonymie + traduction divergente** | - **SIL** : Utilise "délai de réponse" pour désigner le temps écoulé entre la réception de la demande et la transmission du résultat.<br>- **Biologiste** : Utilise "temps de réponse" pour désigner le même concept.<br>- **Médecins prescripteurs** : Utilisent "délai d'analyse" pour désigner le temps nécessaire à l'analyse en laboratoire. |

| **Terme canonique retenu** | **Définition** | **Justification métier** | **Termes à proscrire** |
|----------------------------|----------------|---------------------------|-------------------------|
| **Délai de réponse** | Temps écoulé entre la réception de la demande de dosage anti-Xa par le laboratoire et la transmission du résultat au prescripteur. Pour les demandes urgentes, ce délai ne doit pas excéder 1 heure. | - **Précision** : Insiste sur le temps total de réponse, incluant l'analyse et la transmission.<br>- **Standardisation** : Aligné sur les pratiques des acteurs et les exigences de qualité (ex : HAS).<br>- **Exhaustivité** : Couvre tous les aspects critiques pour la réactivité du laboratoire. | Temps de réponse, délai d'analyse |

| **Exemple d'emploi** |
|----------------------|
| *"Le délai de réponse pour les demandes urgentes de dosage anti-Xa doit être inférieur à 1 heure pour garantir la sécurité des patients. Ce délai inclut l'analyse en laboratoire et la transmission du résultat au prescripteur."* |

| **Source** |
|------------|
| Étape 1 (04_contraintes_et_risques.md), Étape 2 (08_regles_metier.md) |

---
### **1.19. "Délai de transport" vs. "temps d'acheminement"**

| **Problème** | **Type** | **Acteurs concernés et leurs interprétations** |
|--------------|----------|------------------------------------------------|
| **Termes problématiques** : "Délai de transport", "temps d'acheminement" | **Synonymie** | - **Personnel infirmier** : Utilise "délai de transport" pour désigner le temps d'acheminement de l'échantillon.<br>- **Techniciens de laboratoire** : Utilisent "temps d'acheminement" pour désigner le même concept. |

| **Terme canonique retenu** | **Définition** | **Justification métier** | **Termes à proscrire** |
|----------------------------|----------------|---------------------------|-------------------------|
| **Délai de transport** | Temps maximal autorisé pour acheminer l'échantillon biologique du service de soins au laboratoire, généralement fixé à 30 minutes pour garantir la fiabilité du dosage anti-Xa. | - **Précision** : Insiste sur le temps maximal acceptable pour le transport.<br>- **Standardisation** : Aligné sur les pratiques des acteurs et les exigences de qualité (ex : SFBC).<br>- **Exhaustivité** : Couvre tous les aspects critiques pour l'intégrité de l'échantillon. | Temps d'acheminement |

| **Exemple d'emploi** |
|----------------------|
| *"Le délai de transport de l'échantillon ne doit pas excéder 30 minutes pour garantir la fiabilité du dosage anti-Xa. Un transport plus long peut compromettre l'intégrité de l'échantillon et fausser les résultats."* |

| **Source** |
|------------|
| Étape 1 (04_contraintes_et_risques.md), Étape 2 (08_regles_metier.md) |

---
### **1.20. "Heure de réception" vs. "date de réception"**

| **Problème** | **Type** | **Acteurs concernés et leurs interprétations** |
|--------------|----------|------------------------------------------------|
| **Termes problématiques** : "Heure de réception", "date de réception" | **Synonymie** | - **Techniciens de laboratoire** : Utilisent "heure de réception" pour désigner le moment où l'échantillon est reçu au laboratoire.<br>- **SIL** : Utilise "date de réception" dans les interfaces techniques. |

| **Terme canonique retenu** | **Définition** | **Justification métier** | **Termes à proscrire** |
|----------------------------|----------------|---------------------------|-------------------------|
| **Heure de réception** | Moment où l'échantillon biologique est reçu au laboratoire, enregistré dans le SIL. Cette heure est critique pour le calcul du délai de réponse. | - **Précision** : Insiste sur l'importance de l'heure exacte pour le calcul des délais.<br>- **Standardisation** : Aligné sur les pratiques des acteurs et les exigences de traçabilité (ex : ISO 15189).<br>- **Exhaustivité** : Couvre tous les aspects critiques pour la gestion des délais. | Date de réception |

| **Exemple d'emploi** |
|----------------------|
| *"L'heure de réception de l'échantillon au laboratoire est 15h45. Le délai critique de 1 heure est respecté, car le résultat doit être transmis avant 16h45."* |

| **Source** |
|------------|
| Étape 2 (08_regles_metier.md) |

---
### **1.21. "Heure de prélèvement" vs. "heure de ponction"**

| **Problème** | **Type** | **Acteurs concernés et leurs interprétations** |
|--------------|----------|------------------------------------------------|
| **Termes problématiques** : "Heure de prélèvement", "heure de ponction" | **Synonymie** | - **Personnel infirmier** : Utilise "heure de prélèvement" pour désigner le moment où le sang est prélevé chez le patient.<br>- **Médecins prescripteurs** : Utilisent "heure de ponction" pour désigner le même concept. |

| **Terme canonique retenu** | **Définition** | **Justification métier** | **Termes à proscrire** |
|----------------------------|----------------|---------------------------|-------------------------|
| **Heure de prélèvement** | Moment où le sang est prélevé chez le patient pour le dosage anti-Xa. Cette heure est essentielle pour l'interprétation du résultat, car elle permet de calculer le délai depuis la dernière prise d'anticoagulant oral direct. | - **Précision** : Insiste sur l'importance de l'heure exacte pour l'interprétation.<br>- **Standardisation** : Aligné sur les pratiques des acteurs et les exigences de qualité (ex : SFBC).<br>- **Exhaustivité** : Couvre tous les aspects critiques pour l'interprétation du dosage. | Heure de ponction |

| **Exemple d'emploi** |
|----------------------|
| *"L'heure de prélèvement est 15h15. L'heure de la dernière prise d'apixaban est 14h, ce qui permet de calculer un délai de 1h15 entre la prise et le prélèvement, conforme aux recommandations."* |

| **Source** |
|------------|
| Étape 2 (08_regles_metier.md) |

---
### **1.22. "Tube de prélèvement" vs. "tube à prélèvement" vs. "tube citrate"**

| **Problème** | **Type** | **Acteurs concernés et leurs interprétations** |
|--------------|----------|------------------------------------------------|
| **Termes problématiques** : "Tube de prélèvement", "tube à prélèvement", "tube citrate" | **Synonymie + spécificité technique** | - **Personnel infirmier** : Utilise "tube de prélèvement" ou "tube à prélèvement" pour désigner le contenant.<br>- **Biologiste** : Précise "tube citrate 3.2%" pour insister sur le type de tube requis.<br>- **Techniciens de laboratoire** : Utilisent "tube citrate" dans les protocoles techniques. |

| **Terme canonique retenu** | **Définition** | **Justification métier** | **Termes à proscrire** |
|----------------------------|----------------|---------------------------|-------------------------|
| **Tube de prélèvement** | Récipient spécifique utilisé pour collecter le sang en vue d'un dosage anti-Xa. Le tube doit être de type citrate 3.2% pour éviter la coagulation avant l'analyse. | - **Précision** : Insiste sur le type de tube requis (citrate 3.2%) et son rôle dans la prévention de la coagulation.<br>- **Standardisation** : Aligné sur les pratiques des acteurs et les exigences de qualité (ex : SFBC).<br>- **Exhaustivité** : Couvre tous les aspects critiques pour la conformité de l'échantillon. | Tube à prélèvement, tube citrate |

| **Exemple d'emploi** |
|----------------------|
| *"Le tube de prélèvement doit être un citrate 3.2% pour éviter la coagulation avant l'analyse. L'utilisation d'un autre type de tube (ex : EDTA) compromettrait la fiabilité du dosage anti-Xa."* |

| **Source** |
|------------|
| Étape 1 (03_concepts_metier_initiaux.md), Étape 2 (08_regles_metier.md) |

---
### **1.23. "Interprétation du résultat" vs. "lecture du résultat"**

| **Problème** | **Type** | **Acteurs concernés et leurs interprétations** |
|--------------|----------|------------------------------------------------|
| **Termes problématiques** : "Interprétation du résultat", "lecture du résultat" | **Synonymie** | - **Biologiste** : Utilise "interprétation du résultat" pour désigner l'analyse du résultat du dosage anti-Xa en fonction du contexte clinique.<br>- **Médecins prescripteurs** : Utilisent "lecture du résultat" pour désigner la même activité. |

| **Terme canonique retenu** | **Définition** | **Justification métier** | **Termes à proscrire** |
|----------------------------|----------------|---------------------------|-------------------------|
| **Interprétation du résultat** | Analyse du résultat du dosage anti-Xa par le biologiste, tenant compte du traitement en cours (anticoagulant oral direct), de la fonction rénale, de l'heure de la dernière prise et du contexte clinique. | - **Précision** : Insiste sur l'analyse approfondie du résultat en fonction de multiples paramètres.<br>- **Standardisation** : Aligné sur les pratiques des biologistes et des sociétés savantes (ex : SFBC).<br>- **Exhaustivité** : Couvre tous les aspects critiques pour l'ajustement du traitement. | Lecture du résultat, analyse biologique |

| **Exemple d'emploi** |
|----------------------|
| *"L'interprétation du résultat anti-Xa montre une activité thérapeutique pour l'apixaban, mais la fonction rénale altérée (30 mL/min) nécessite une surveillance accrue et éventuellement une adaptation de la posologie."* |

| **Source** |
|------------|
| Étape 1 (03_concepts_metier_initiaux.md), Étape 2 (07_responsabilites_acteurs.md) |

---
### **1.24. "Service clinique" vs. "unité clinique"**

| **Problème** | **Type** | **Acteurs concernés et leurs interprétations** |
|--------------|----------|------------------------------------------------|
| **Termes problématiques** : "Service clinique", "unité clinique" | **Synonymie** | - **Médecins prescripteurs** : Utilisent "service clinique" pour désigner les unités hospitalières (ex : Urgences, Réanimation).<br>- **SIL** : Utilise "unité clinique" dans les interfaces techniques. |

| **Terme canonique retenu** | **Définition** | **Justification métier** | **Termes à proscrire** |
|----------------------------|----------------|---------------------------|-------------------------|
| **Service clinique** | Unité hospitalière (ex : Urgences, Réanimation, Bloc opératoire) où sont pris en charge les patients sous anticoagulants oraux directs. | - **Précision** : Insiste sur le rôle de l'unité dans la prise en charge des patients.<br>- **Standardisation** : Aligné sur les pratiques des acteurs et les dénominations hospitalières courantes.<br>- **Clarté** : Évite toute confusion avec d'autres types d'unités (ex : unités administratives). | Unité clinique |

| **Exemple d'emploi** |
|----------------------|
| *"La prescription de dosage anti-Xa provient du service clinique de réanimation. Ce service est responsable de la prise en charge des patients sous anticoagulants oraux directs en situation critique."* |

| **Source** |
|------------|
| Étape 1 (02_acteurs_du_domaine.md), Étape 2 (06_cartographie_acteurs.md) |

---
### **1.25. "Circuit informatisé" vs. "circuit digital" vs. "circuit sécurisé"**

| **Problème** | **Type** | **Acteurs concernés et leurs interprétations** |
|--------------|----------|------------------------------------------------|
| **Termes problématiques** : "Circuit informatisé", "circuit digital", "circuit sécurisé" | **Synonymie + traduction divergente** | - **Biologiste** : Utilise "circuit informatisé" pour désigner le processus numérique de gestion des demandes.<br>- **SIL** : Utilise "circuit digital" dans les interfaces techniques.<br>- **Médecins prescripteurs** : Utilisent "circuit sécurisé" pour insister sur la sécurité des données. |

| **Terme canonique retenu** | **Définition** | **Justification métier** | **Termes à proscrire** |
|----------------------------|----------------|---------------------------|-------------------------|
| **Circuit informatisé** | Processus numérique sécurisé et tracé pour la gestion des demandes urgentes de dosage anti-Xa, incluant la priorisation, la transmission des résultats et la traçabilité. | - **Précision** : Insiste sur l'aspect numérique, sécurisé et tracé du processus.<br>- **Standardisation** : Aligné sur les pratiques des acteurs et les exigences de qualité (ex : ISO 15189, HDS).<br>- **Exhaustivité** : Couvre tous les aspects critiques pour la gestion des demandes. | Circuit digital, circuit sécurisé |

| **Exemple d'emploi** |
|----------------------|
| *"Le nouveau circuit informatisé doit garantir la traçabilité, la priorisation et la sécurité des demandes urgentes de dosage anti-Xa. Il doit permettre une transmission rapide des résultats aux prescripteurs."* |

| **Source** |
|------------|
| Étape 1 (03_concepts_metier_initiaux.md), Étape 2 (08_regles_metier.md) |

---
### **1.26. "Demande urgente" vs. "demande prioritaire" vs. "demande critique"**

| **Problème** | **Type** | **Acteurs concernés et leurs interprétations** |
|--------------|----------|------------------------------------------------|
| **Termes problématiques** : "Demande urgente", "demande prioritaire", "demande critique" | **Synonymie** | - **Médecins prescripteurs** : Utilisent "demande urgente" pour désigner une demande nécessitant une réponse immédiate.<br>- **SIL** : Utilise "demande prioritaire" pour désigner les demandes classées comme urgentes.<br>- **Biologiste** : Utilise "demande critique" pour insister sur la gravité de la situation. |

| **Terme canonique retenu** | **Définition** | **Justification métier** | **Termes à proscrire** |
|----------------------------|----------------|---------------------------|-------------------------|
| **Demande urgente** | Demande de dosage anti-Xa classée comme prioritaire en raison de la situation clinique du patient (ex : hémorragie active, thrombose artérielle ou veineuse, suspicion de surdosage). | - **Précision** : Insiste sur la classification de la demande en fonction de l'urgence clinique.<br>- **Standardisation** : Aligné sur les pratiques des acteurs et les exigences de qualité (ex : HAS, SFAR).<br>- **Exhaustivité** : Couvre tous les aspects critiques pour la réactivité du laboratoire. | Demande prioritaire, demande critique |

| **Exemple d'emploi** |
|----------------------|
| *"Cette demande de dosage anti-Xa est classée comme urgente en raison d'une hémorragie active sous apixaban. Le SIL doit la prioriser pour garantir un délai de réponse inférieur à 1 heure."* |

| **Source** |
|------------|
| Étape 1 (03_concepts_metier_initiaux.md), Étape 2 (08_regles_metier.md) |

---
### **1.27. "Traçabilité des données" vs. "historique des données"**

| **Problème** | **Type** | **Acteurs concernés et leurs interprétations** |
|--------------|----------|------------------------------------------------|
| **Termes problématiques** : "Traçabilité des données", "historique des données" | **Synonymie** | - **SIL** : Utilise "traçabilité des données" pour désigner l'enregistrement systématique de chaque étape du circuit.<br>- **Médecins prescripteurs** : Utilisent "historique des données" pour désigner le suivi des dosages antérieurs. |

| **Terme canonique retenu** | **Définition** | **Justification métier** | **Termes à proscrire** |
|----------------------------|----------------|---------------------------|-------------------------|
| **Traçabilité des données** | Enregistrement systématique de toutes les informations liées à une demande de dosage anti-Xa : prescription, prélèvement, transport, analyse, résultat. | - **Précision** : Insiste sur l'enregistrement systématique et complet de chaque étape.<br>- **Standardisation** : Aligné sur les pratiques des acteurs et les exigences de traçabilité (ex : ISO 15189, RGPD).<br>- **Exhaustivité** : Couvre tous les aspects critiques pour la sécurité et la conformité réglementaire. | Historique des données |

| **Exemple d'emploi** |
|----------------------|
| *"La traçabilité des données doit inclure l'identité du patient, l'heure de prélèvement, le type de tube utilisé, l'heure de réception au laboratoire, et l'heure de transmission du résultat. Ces données sont essentielles pour garantir la sécurité du patient et la conformité réglementaire."* |

| **Source** |
|------------|
| Étape 1 (03_concepts_metier_initiaux.md), Étape 2 (08_regles_metier.md) |

---
### **1.28. "Heure de la dernière prise" vs. "délai depuis la dernière dose"**

| **Problème** | **Type** | **Acteurs concernés et leurs interprétations** |
|--------------|----------|------------------------------------------------|
| **Termes problématiques** : "Heure de la dernière prise", "délai depuis la dernière dose" | **Synonymie** | - **Médecins prescripteurs** : Utilisent "heure de la dernière prise" pour désigner le moment où le patient a ingéré sa dernière dose d'anticoagulant oral direct.<br>- **Personnel infirmier** : Utilisent "délai depuis la dernière dose" pour désigner le temps écoulé depuis cette prise. |

| **Terme canonique retenu** | **Définition** | **Justification métier** | **Termes à proscrire** |
|----------------------------|----------------|---------------------------|-------------------------|
| **Heure de la dernière prise** | Moment auquel le patient a ingéré sa dernière dose d'anticoagulant oral direct. Cette information est essentielle pour l'interprétation du dosage anti-Xa, car elle permet de calculer le délai entre la prise et le prélèvement. | - **Précision** : Insiste sur l'importance de l'heure exacte pour l'interprétation.<br>- **Standardisation** : Aligné sur les pratiques des acteurs et les exigences de qualité (ex : SFBC).<br>- **Exhaustivité** : Couvre tous les aspects critiques pour l'interprétation du dosage. | Délai depuis la dernière dose |

| **Exemple d'emploi** |
|----------------------|
| *"L'heure de la dernière prise d'apixaban est à 14h. Le prélèvement doit être fait à 16h pour un dosage anti-Xa fiable, ce qui permet de calculer un délai de 2 heures entre la prise et le prélèvement, conforme aux recommandations."* |

| **Source