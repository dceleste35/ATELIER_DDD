# Exemples d'usage du langage commun
**Domaine : Circuit des demandes urgentes de dosage anti-Xa**

---

## Introduction

Ce document illustre l'usage concret du langage commun à travers :
- **Narrations métier** (Domain Narratives) : récits métiers illustrant le parcours des acteurs
- **User Stories** : formulations standardisées des besoins fonctionnels
- **Scénarios Gherkin** : tests comportementaux en Given/When/Then
- **Exemples de dialogues** : échanges reformulés avec le vocabulaire canonique

Tous les exemples sont strictement basés sur les livrables des étapes 1 et 2, sans anticipation sur la modélisation DDD.

---

## 1. Narrations métier (Domain Narratives)

### **Narration 1 : Parcours d'une demande urgente depuis les Urgences**

**Contexte** : Un patient de 68 ans est admis aux Urgences pour une hémorragie digestive sous apixaban (anticoagulant oral direct). Le médecin urgentiste identifie une **urgence clinique** nécessitant un **dosage anti-Xa** immédiat.

**Séquence d'événements** :
1. Le **Médecin prescripteur** (Urgences) rédige une **prescription médicale** incluant :
   - Le **contexte clinique** : hémorragie digestive sous apixaban, fonction rénale à 45 mL/min
   - L'**heure de la dernière prise** : 10h30
   - La **priorité** : urgente

2. Le **Personnel infirmier** valide la **prescription médicale** et effectue le **prélèvement** dans un **tube de prélèvement** citrate 3.2% à 11h15 (**heure de prélèvement**). Il vérifie la **conformité de l'échantillon** et transmet les **informations cliniques** au SIL.

3. Le **SIL** enregistre la **demande urgente** et applique une **priorisation** automatique. Il génère un identifiant unique pour le **circuit informatisé** et transmet la demande aux **Techniciens de laboratoire**.

4. Les **Techniciens de laboratoire** reçoivent la demande prioritaire et analysent l'**échantillon biologique** immédiatement. Ils respectent le **délai critique** de 1 heure pour les urgences.

5. Le **Biologiste** interprète le **résultat du dosage anti-Xa** (0,1 UI/mL) en tenant compte du **contexte clinique** (hémorragie, fonction rénale, heure de la dernière prise). Il rédige une **interprétation du résultat** et transmet le tout au **Médecin prescripteur** via le SIL.

6. Le **Médecin prescripteur** ajuste le traitement en fonction de l'**interprétation du résultat** et du **contexte clinique**.

**Traçabilité** : Le SIL documente chaque étape :
- Heure de réception de la **prescription médicale** : 10h45
- Heure de réception de l'**échantillon biologique** : 11h30
- Heure de transmission du **résultat du dosage anti-Xa** : 12h15

---

### **Narration 2 : Gestion d'un échantillon non conforme**

**Contexte** : Un patient en réanimation nécessite un **dosage anti-Xa** pour surveiller son traitement par rivaroxaban. Le **Personnel infirmier** effectue le prélèvement mais utilise un **tube de prélèvement** EDTA au lieu du citrate 3.2% requis.

**Séquence d'événements** :
1. Le **Personnel infirmier** transmet l'**échantillon biologique** au laboratoire avec les **informations cliniques**.

2. Les **Techniciens de laboratoire** vérifient la **conformité de l'échantillon** et constatent qu'il n'est pas conforme (tube EDTA non acceptable pour le dosage anti-Xa).

3. Le **Biologiste** prend la décision de **rejet d'échantillon** et notifie le **Personnel infirmier** via le SIL.

4. Le **Personnel infirmier** doit effectuer un nouveau prélèvement avec un **tube de prélèvement** citrate 3.2% valide.

5. Le **SIL** met à jour la **traçabilité des données** avec le motif du rejet et l'heure du nouveau prélèvement.

**Conséquence** : Le **délai de réponse** est prolongé, mais la **sécurité des données** et la **qualité de l'analyse** sont préservées.

---

### **Narration 3 : Standardisation des informations cliniques**

**Contexte** : Le **SIL** actuel ne permet pas de standardiser la transmission des **informations cliniques** entre les services. Les **Médecins prescripteurs** omettent parfois la **fonction rénale** ou l'**heure de la dernière prise**, ce qui complique l'**interprétation du résultat** par le **Biologiste**.

**Séquence d'événements** :
1. Le **SIL** impose désormais un formulaire standardisé pour les **prescriptions médicales** urgentes, incluant obligatoirement :
   - Le **traitement en cours** (anticoagulant oral direct)
   - La **fonction rénale**
   - L'**heure de la