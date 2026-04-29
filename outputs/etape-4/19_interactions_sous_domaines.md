# **Interactions entre sous-domaines**
**Domaine : Circuit des demandes urgentes de dosage anti-Xa**

---

## **1. Vue d'ensemble du parcours métier**

Le circuit des demandes urgentes de dosage anti-Xa suit un parcours linéaire et séquentiel à travers les sous-domaines, avec des interactions critiques aux interfaces entre chaque étape. Le parcours commence par la **Prescription Médicale** et se termine par la **Transmission des résultats**, en passant par la conformité, l'analyse et l'interprétation.

**Schéma du parcours métier :**
```
Prescription Médicale → Gestion des Urgences → Prélèvement et Conformité → Analyse Biologique → Interprétation et Transmission → Traçabilité et Sécurité
```

Chaque sous-domaine joue un rôle spécifique dans la chaîne de valeur, avec des interactions formalisées entre eux. Les échanges d'informations sont principalement **asynchrones** (sauf exceptions critiques), avec des notifications en temps réel pour les alertes et les urgences.

---

## **2. Tableau des interactions entre sous-domaines**

| **Sous-domaine source** | **Sous-domaine cible** | **Information ou décision échangée** | **Déclencheur** | **Mode** | **Format** | **Criticité** | **Risque de couplage** | **Points d'attention** |
|-------------------------|------------------------|--------------------------------------|-----------------|----------|------------|---------------|------------------------|-------------------------|
| **Prescription Médicale** | **Gestion des Urgences** | **Prescription médicale** + **niveau d'urgence** | Saisie de la prescription | Asynchrone | Donnée structurée (JSON/XML) | **Critique** | **Fort** (dépendances directes) | Assurer la classification automatique correcte |
| **Prescription Médicale** | **Prélèvement et Conformité** | **Prescription médicale** + **heure de la dernière prise** | Validation de la prescription | Asynchrone | Donnée structurée | **Critique** | **Moyen** (dépend des informations cliniques) | Vérifier que les informations cliniques sont transmises correctement |
| **Prescription Médicale** | **Traçabilité et Sécurité** | **Prescription médicale** + **identifiant unique** | Saisie de la prescription | Synchrone | Donnée + événement | **Critique** | **Faible** (traçabilité passive) | Assurer l'enregistrement immédiat dans les logs |
| **Gestion des Urgences** | **Prélèvement et Conformité** | **Niveau d'urgence** + **délai de réponse cible** | Classification de la prescription | Asynchrone | Donnée structurée | **Critique** | **Fort** (priorité de traitement) | Garantir que la priorité est respectée dans le prélèvement |
| **Gestion des Urgences** | **Analyse Biologique** | **Niveau d'urgence** + **identifiant unique** | Priorisation des demandes | Asynchrone | Donnée structurée | **Critique** | **Moyen** (impact sur l'ordre de traitement) | Éviter les conflits de priorité entre urgences |
| **Gestion des Urgences** | **Traçabilité et Sécurité** | **Niveau d'urgence** + **horodatage** | Priorisation des demandes | Synchrone | Événement | **Critique** | **Faible** | Enregistrer la priorisation dans les logs |
| **Gestion des Urgences** | **Gestion des Alertes et Exceptions** | **Niveau d'urgence** + **délai de réponse** | Surveillance des délais | Asynchrone | Notification | **Critique** | **Faible** | Configurer des seuils d'alerte adaptés |
| **Prélèvement et Conformité** | **Analyse Biologique** | **Échantillon biologique** + **conformité** + **identifiant unique** | Validation de l'échantillon | Asynchrone | Donnée structurée | **Critique** | **Fort** (impact direct sur l'analyse) | Rejeter immédiatement les échantillons non conformes |
| **Prélèvement et Conformité** | **Traçabilité et Sécurité** | **Acte de prélèvement** + **conformité** + **horodatage** | Réalisation du prélèvement | Synchrone | Événement | **Critique** | **Faible** | Enregistrer la conformité et le transport |
|