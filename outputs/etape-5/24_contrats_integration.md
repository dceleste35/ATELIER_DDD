# **Contrats d'intégration entre Bounded Contexts**
**Domaine : Circuit des demandes urgentes de dosage anti-Xa**
*Document de référence pour l'étape 5 (Strategic Design)*

---

## **1. Table des matières**
1. [Contexte général](#1-contexte-général)
2. [Commandes acceptées par chaque Bounded Context](#2-commandes-acceptées-par-chaque-bounded-context)
3. [Événements de domaine émis par chaque Bounded Context](#3-événements-de-domaine-émis-par-chaque-bounded-context)
4. [Données de référence partagées](#4-données-de-référence-partagées)
5. [Politiques d'idempotence, d'ordre et de cohérence](#5-politiques-didempotence-dordre-et-de-cohérence)
6. [Implications pour l'organisation des équipes (Conway's Law)](#6-implications-pour-lorganisation-des-équipes-conways-law)
7. [Annexes](#7-annexes)

---

## **1. Contexte général**

### **1.1. Objectif du document**
Ce document spécifie les **contrats d'échange** entre les Bounded Contexts du domaine "Circuit des demandes urgentes de dosage anti-Xa", en se concentrant sur :
- Les **commandes** acceptées par chaque contexte (entrées).
- Les **événements de domaine** émis par chaque contexte (sorties).
- Les **données de référence** partagées.
- Les **politiques d'intégration** (synchrone/asynchrone, idempotence, ordre, cohérence).
- Les **implications organisationnelles** (Conway's Law).

### **1.2. Périmètre**
Les Bounded Contexts concernés sont :
- **PrescriptionMédicale** (Core)
- **PrélèvementBiologique** (Core)
- **AnalyseBiologique** (Core)
- **ValidationClinique** (Core)
- **TransmissionRésultats** (Supporting)
- **GestionUrgences** (Supporting)
- **TraçabilitéSécurisée** (Supporting)
- **GestionNonConformités** (Generic)

### **1.3. Principes directeurs**
- **Langage commun** : Tous les termes utilisés sont issus du glossaire métier (étape 3).
- **Séparation des responsabilités** : Chaque Bounded Context a une finalité métier claire et distincte.
- **Patterns DDD** : Les relations inter-contextes sont qualifiées selon les patterns canoniques (Partnership, Customer/Supplier, Shared Kernel).
- **Contrats métier** : Les formats d'échange sont décrits au niveau métier (pas de détails techniques comme JSON/Avro).

---

## **2. Commandes acceptées par chaque Bounded Context**

### **2.1. PrescriptionMédicale**
| **Commande** | **Description métier** | **Données d'entrée** | **Source** | **Garanties attendues** |
|--------------|------------------------|----------------------|------------|-------------------------|
| `SaisirPrescription` | Permettre au médecin prescripteur de saisir une nouvelle prescription médicale. | - `patient_id` (UUID) <br> - `service_demandeur` (enum : Urgences, Réanimation, Bloc) <br> - `anticoagulant` (enum : apixaban, rivaroxaban, dabigatran, etc.) <br> - `dose` (float) <br> - `heure_derniere_prise` (datetime) <br> - `dfg` (float) <br> - `motif` (string) | Médecin prescripteur | - La prescription est enregistrée avec un **identifiant unique** (`prescription_id`). <br> - Le **niveau d'urgence** est déterminé automatiquement. <br> - Une **alerte** est générée si des champs obligatoires sont manquants. |
| `ValiderPrescription` | Valider une prescription médicale saisie. | - `prescription_id` (UUID) | SIL (automatisé) | - La prescription passe au statut `validee`. <br> - Un événement `PrescriptionValidee` est émis. |
| `ModifierPrescription` | Modifier une prescription médicale existante (ex : correction de la dose). | - `prescription_id` (UUID) <br> - `champs_modifiés` (objet partiel) | Médecin prescripteur | - La modification est horodatée et tracée. <br> - Le **niveau d'urgence** est recalculé si nécessaire. |
| `AnnulerPrescription` | Annuler une prescription médicale. | - `prescription_id` (UUID) <br> - `motif_annulation` (string) | Médecin prescripteur | - La prescription passe au statut `rejetee`. <br> - Un événement `PrescriptionAnnulee` est émis. |

---

### **2.2. PrélèvementBiologique**
| **Commande** | **Description métier** | **Données d'entrée** | **Source** | **Garanties attendues** |
|--------------|------------------------|----------------------|------------|-------------------------|
| `EnregistrerActePrelevement` | Enregistrer l'acte de prélèvement réalisé par le personnel infirmier. | - `prescription_id` (UUID) <br> - `operateur_id` (UUID) <br> - `heure_prelevement` (datetime) <br> - `type_tube` (enum : citrate_3.2%) <br> - `volume` (float) <br> - `et