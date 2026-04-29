# **Alignement métier ↔ technique**
**Domaine : Circuit des demandes urgentes de dosage anti-Xa**

---

## **1. Tableau de correspondance : vocabulaire métier vs. vocabulaire technique**

| **Terme métier (canonique)** | **Terme technique actuel / pressenti** | **Écart constaté** | **Terme à privilégier** | **Justification** | **Exemple d'usage technique** |
|-------------------------------|----------------------------------------|--------------------|--------------------------|-------------------|--------------------------------|
| **Prescription médicale** | `Ordonnance`, `Demande de dosage`, `Prescription` (dans le SIH) | - Confusion avec les ordonnances de sortie <br> - Absence de distinction avec l'acte de prélèvement | `prescription_medicale` | - Aligné sur le vocabulaire réglementaire <br> - Distingue l'acte médical de l'acte de prélèvement | Champ `prescription_medicale` dans la base de données SIL |
| **Urgence clinique** | `Demande urgente`, `Urgence` (dans le SIL) | - Pas de distinction entre urgence vitale et urgence standard | `urgence_clinique` | - Permet une hiérarchisation claire <br> - Aligné sur les pratiques cliniques | Enum `urgence_clinique` avec valeurs `urgence_vitale`, `urgence_standard` |
| **Urgence vitale** | `Urgence absolue`, `Situation critique` (dans les interfaces) | - Pas de définition claire des critères | `urgence_vitale` | - Standardise les délais de réponse (<30 min) <br> - Réduit les risques de sous-estimation | Champ `niveau_urgence` avec valeur `urgence_vitale` |
| **Échantillon biologique** | `Prélèvement`, `Tube` (dans les logs SIL) | - Confusion entre l'acte et le matériel <br> - Risque de perte de traçabilité | `echantillon_biologique` | - Inclut implicitement le tube et le matériel <br> - Aligné sur les normes ISO 15189 | Objet `EchantillonBiologique` dans le code SIL |
| **Tube de prélèvement** | `Tube`, `Contenant` (dans les interfaces) | - Pas de distinction entre type de tube (citraté, EDTA, etc.) | `tube_prelevement` | - Permet de vérifier la conformité <br> - Aligné sur les normes pré-analytiques (CLSI GP41) | Champ `type_tube` avec valeurs `citrate_3.2%`, `EDTA`, etc. |
| **Acte de prélèvement** | `Prélèvement` (dans les logs) | - Risque de confusion avec l'échantillon | `acte_prelevement` | - Distingue clairement l'action du matériel <br> - Permet de tracer l'opérateur | Objet `ActePrelevement` avec champs `operateur_id`, `heure_prelevement` |
| **Contexte clinique** | `Contexte thérapeutique`, `Données patient` (dans les formulaires) | - Trop restrictif (exclut la fonction rénale) | `contexte_clinique` | - Inclut tous les éléments nécessaires à l'interprétation <br> - Aligné sur les pratiques de biologie médicale | Champ `contexte_clinique` avec sous-champs `traitement`, `heure_derniere_prise`, `dfg` |
| **Information clinique** | `Données patient`, `Contexte` (dans les interfaces SIL) | - Trop large (inclut des données inutiles) | `information_clinique` | - Ciblé sur les éléments nécessaires au dosage anti-Xa <br> - Aligné sur les normes ISO 15189 | Champ `informations_cliniques_obligatoires` dans le formulaire de prescription |
| **Dosage anti-Xa** | `Mesure FXa`, `Test anti-Xa` (dans les automates) | - Traduction technique non comprise par les cliniciens | `dosage_anti_xa` | - Terme métier clair et précis <br> - Évite les confusions avec d'autres tests | Méthode `calculer_dosage_anti_xa()` dans le code de l'automate |
| **Résultat du dosage anti-Xa** | `Valeur FXa`, `Résultat analyse` (dans les comptes-rendus) | - Pas de distinction avec d'autres résultats | `resultat_dosage_anti_xa` | - Permet une interprétation spécifique <br> - Aligné sur les pratiques de biologie | Champ `resultat` de type `ResultatDosageAntiXa` dans la base de données |
| **Interprétation du résultat** | `Commentaire biologique`, `Analyse des résultats` (dans les rapports) | - Pas de standardisation | `interpretation_resultat` | - Inclut le contexte clinique et les recommandations <br> - Aligné sur les pratiques de biologie | Méthode `interpreter_resultat()` dans le code du biologiste |
| **Traçabilité** | `Documentation`, `Historique` (dans les logs SIL) | - Trop vague (peut inclure des données non pertinentes) | `traçabilité` | - Terme réglementaire et métier standard <br> - Inclut l'horodatage et les identifiants uniques | Champ `traçabilité` avec sous-champs `horodatage`, `identifiant_unique`, `etapes` |
| **Circuit informatisé** | `Workflow numérique`, `Système sécurisé` (dans les spécifications techniques) | - Trop technique ou trop vague | `circuit_informatise` | - Inclut la sécurité, la traçabilité et la priorisation <br> - Aligné sur les attentes des biologistes | Module `CircuitInformatise` dans l'architecture du SIL |
| **Priorisation** | `Classement des priorités`, `Tri des demandes` (dans les interfaces) | - Pas de mécanisme clair | `priorisation` | - Mécanisme dynamique incluant les critères cliniques et organisationnels <br> - Aligné sur les pratiques des SIL | Méthode `prioriser_demandes()` dans le code du SIL |
| **Rejet d’échantillon** | `Refus d’analyse`, `Échantillon non conforme` (dans les logs) | - Pas de distinction entre rejet définitif et analyse avec réserve | `rejet_echantillon` | - Décision claire et définitive <br> - Aligné sur les pratiques de laboratoire | Champ `statut_echantillon` avec valeur `rejet` et motif `non_conforme` |
| **Délai de réponse** | `Temps de rendu`, `Délai d’analyse` (dans les indicateurs) | - Exclut le délai de transport | `delai_reponse` | - Inclut implicitement le transport, l'analyse et la transmission <br> - Aligné sur les attentes des prescripteurs | Champ `delai_reponse` avec valeurs `urgence_vitale:30min`, `urgence_standard:1h` |
| **Transmission des résultats** | `Communication des résultats`, `Rendu des résultats` (dans les processus) | - Pas de standardisation | `transmission_resultats` | - Inclut le format et les destinataires <br> - Aligné sur les pratiques de biologie | Méthode `transmettre_resultats()` dans le code du SIL |
| **Identifiant unique** | `ID demande`, `Numéro de dossier` (dans les bases de données) | - Pas de standardisation | `identifiant_unique` | - Permet une traçabilité sans ambiguïté <br> - Aligné sur les normes RGPD | Champ `id_unique` de type UUID dans la base de données |
| **Alerte** | `Notification`, `Signalement` (dans les interfaces) | - Pas de distinction entre alertes automatiques et manuelles | `alerte` | - Notification automatique générée par le SIL <br> - Aligné sur les besoins de traçabilité | Champ `alerte` avec sous-champs `type`, `niveau`, `message` |

---

## **2. Traductions permanentes à supprimer**

### **2.1. Traductions entre vocabulaire métier et vocabulaire technique à éliminer**

| **Traduction à supprimer** | **Terme métier (canonique)** | **Terme technique actuel** | **Raison** | **Solution proposée** |
|----------------------------|-------------------------------|----------------------------|-------------|-----------------------|
| *"Ordonnance"* → *"Prescription médicale"* | **Prescription médicale** | `Ordonnance` (dans le SIH) | Confusion avec les ordonnances de sortie | Utiliser systématiquement `prescription_medicale` dans le SIL et le SIH |
| *"Demande de dosage"* → *"Prescription médicale"* | **Prescription médicale** | `Demande de dosage` (dans les interfaces SIL) | Risque de confusion avec les demandes non médicales | Remplacer par `prescription_medicale` dans toutes les interfaces |
| *"Prélèvement"* → *"Échantillon biologique"* | **Échantillon biologique** | `Prélèvement` (dans les logs SIL) | Confusion entre l'acte et le matériel | Utiliser `echantillon_biologique` pour désigner le matériel et `acte_prelevement` pour l'action |
| *"Tube"* → *"Tube de prélèvement"* | **Tube de prélèvement** | `Tube` (dans les interfaces) | Pas de distinction entre types de tubes | Utiliser `tube_prelevement` avec un champ `type_tube` |
| *"Contexte thérapeutique"* → *"Contexte clinique"* | **Contexte clinique** | `Contexte thérapeutique` (dans les formulaires) | Trop restrictif (exclut la fonction rénale) | Utiliser `contexte_clinique` avec tous les sous-champs nécessaires |
| *"Données patient"* → *"Information clinique"* | **Information clinique** | `Données patient` (dans les interfaces SIL) | Trop large (inclut des données inutiles) | Utiliser `information_clinique` avec une liste de champs obligatoires |
| *"Mesure FXa"* → *"Dosage anti-Xa"* | **Dosage anti-Xa** | `Mesure FXa` (dans les automates) | Traduction technique non comprise par les cliniciens | Utiliser `dosage_anti_xa` dans toutes les interfaces et le code |
| *"Test anti-Xa"* → *"Dosage anti-Xa"* | **Dosage anti-Xa** | `Test anti-Xa` (dans les rapports) | Traduction technique non standardisée | Utiliser `dosage_anti_xa` dans tous les documents |
| *"Valeur FXa"* → *"Résultat du dosage anti-Xa"* | **Résultat du dosage anti-Xa** | `Valeur FXa` (dans les comptes-rendus) | Pas de distinction avec d'autres résultats | Utiliser `resultat_dosage_anti_xa` dans tous les rapports |
| *"Commentaire biologique"* → *"Interprétation du résultat"* | **Interprétation du résultat** | `Commentaire biologique` (dans les rapports) | Pas de standardisation | Utiliser `interpretation_resultat` avec un format structuré |
| *"Documentation"* → *"Traçabilité"* | **Traçabilité** | `Documentation` (dans les logs SIL) | Trop vague | Utiliser `traçabilité` avec des champs structurés (horodatage, identifiant unique, étapes) |
| *"Workflow numérique"* → *"Circuit informatisé"* | **Circuit informatisé** | `Workflow numérique` (dans les spécifications techniques) | Trop technique | Utiliser `circuit_informatise` dans toutes les spécifications |
| *"Système sécurisé"* → *"Circuit informatisé"* | **Circuit informatisé** | `Système sécurisé` (dans les présentations) | Trop vague | Utiliser `circuit_informatise` pour inclure sécurité, traçabilité et priorisation |
| *"Classement des priorités"* → *"Priorisation"* | **Priorisation** | `Classement des priorités` (dans les interfaces) | Pas de mécanisme clair | Utiliser `priorisation` avec une logique métier explicite |
| *"Tri des demandes"* → *"Priorisation"* | **Priorisation** | `Tri des demandes` (dans les processus) | Pas de standardisation | Utiliser `priorisation` avec des critères cliniques et organisationnels |
| *"Refus d’analyse"* → *"Rejet d’échantillon"* | **Rejet d’échantillon** | `Refus d’analyse` (dans les logs) | Pas de distinction entre rejet définitif et analyse avec réserve | Utiliser `rejet_echantillon` pour une décision claire et définitive |
| *"Échantillon non conforme"* → *"Rejet d’échantillon"* | **Rejet d’échantillon** | `Échantillon non conforme` (dans les interfaces) | Pas de distinction entre rejet et analyse avec réserve | Utiliser `rejet_echantillon` avec un motif clair |
| *"Temps de rendu"* → *"Délai de réponse"* | **Délai de réponse** | `Temps de rendu` (dans les indicateurs) | Exclut le délai de transport | Utiliser `delai_reponse` pour inclure transport, analyse et transmission |
| *"Délai d’analyse"* → *"Délai de réponse"* | **Délai de réponse** | `Délai d’analyse` (dans les processus) | Exclut le délai de transport et de transmission | Utiliser `delai_reponse` pour une vision globale du circuit |
| *"Communication des résultats"* → *"Transmission des résultats"* | **Transmission des résultats** | `Communication des résultats` (dans les processus) | Pas de standardisation | Utiliser `transmission_resultats` avec un format et des destinataires clairs |
| *"ID demande"* → *"Identifiant unique"* | **Identifiant unique** | `ID demande` (dans les bases de données) | Pas de standardisation | Utiliser `identifiant_unique` de type UUID dans toutes les bases de données |
| *"Numéro de dossier"* → *"Identifiant unique"* | **Identifiant unique** | `Numéro de dossier` (dans les interfaces) | Risque de confusion avec d'autres numéros | Utiliser `identifiant_unique` pour une traçabilité sans ambiguïté |
| *"Notification"* → *"Alerte"* | **Alerte** | `Notification` (dans les interfaces) | Pas de distinction entre alertes automatiques et manuelles | Utiliser `alerte` pour les notifications automatiques générées par le SIL |

---

## **3. Règles de nommage pour la documentation technique, les user stories et le code**

### **3.1. Conventions générales**

| **Règle** | **Exemple** | **Justification** |
|------------|-------------|-------------------|
| **Langue** | Utiliser le français dans tous les documents et le code | Aligné sur le langage commun métier |
| **Pluriel** | Utiliser le pluriel pour les noms de collections : `demandes_urgentes`, `echantillons_biologiques` | Conforme aux conventions de nommage en développement (ex : Python, Java) |
| **Singulier** | Utiliser le singulier pour les noms de classes et d'objets : `PrescriptionMedicale`, `EchantillonBiologique` | Conforme aux conventions de nommage en développement (ex : Java, C#) |
| **CamelCase** | Utiliser pour les noms de classes et méthodes : `PrescriptionMedicale`, `calculerDelaiReponse()` | Conforme aux conventions de nommage en développement (ex : Java, C#) |
| **snake_case** | Utiliser pour les noms de variables, champs de base de données et fichiers : `delai_reponse`, `type_tube` | Conforme aux conventions de nommage en développement (ex : Python, SQL) |
| **Préfixes/suffixes** | Éviter les préfixes/suffixes inutiles : `getDelaiReponse()` au lieu de `getDelaiReponseFromSil()` | Réduit la verbosité et améliore la lisibilité |
| **Acronymes** | Expliquer les acronymes à leur première occurrence : `DFG` (Débit de Filtration Glomérulaire) | Améliore la compréhension pour les nouveaux arrivants |
| **Noms explicites** | Privilégier les noms explicites : `rejet_echantillon` au lieu de `statut_1` | Réduit les ambiguïtés et améliore la maintenance |

---

### **3.2. Règles spécifiques par type de document**

#### **3.2.1. User Stories**
- **Format** : *"En tant que [rôle], je souhaite [action] afin de [bénéfice]."*
- **Exemples** :
  ```markdown
  - **En tant que** médecin prescripteur, **je souhaite** saisir une **prescription médicale** avec les **informations cliniques** obligatoires (traitement, heure de la dernière prise, fonction rénale) **afin de** que le **dosage anti-Xa** soit interprété correctement.
  - **En tant que** biologiste, **je souhaite** recevoir une **alerte** si un **échantillon biologique** est **non conforme** (tube inadapté, volume insuffisant) **afin de** **rejeter l’échantillon** et éviter une erreur d’interprétation.
  - **En tant que** technicien de laboratoire, **je souhaite** que le **SIL** **priorise automatiquement** les **demandes urgentes** **afin de** garantir un **délai de réponse** inférieur à 1 heure pour les cas critiques.
  ```
- **Règles** :
  - Utiliser les termes canoniques du glossaire.
  - Éviter les termes techniques non compris par les métiers.
  - Inclure les critères d'acceptation (ex : *"Le délai de réponse doit être inférieur à 30 minutes pour les urgences vitales"*).

---

#### **3.2.2. Documentation technique**
- **Structure** :
  - **Titre** : Utiliser le terme canonique en **gras**.
  - **Description** : Expliquer le concept métier et son alignement avec le code.
  - **Exemple de code** : Fournir un extrait de code illustrant l'implémentation.
- **Exemple** :
  ```markdown
  ## **Délai de réponse**
  **Définition métier** : Temps maximal autorisé entre la réception de la demande de dosage anti-Xa par le laboratoire et la transmission des résultats au prescripteur.

  **Alignement technique** :
  - Champ `delai_reponse` dans la base de données SIL.
  - Méthode `calculerDelaiReponse()` dans le service de priorisation.

  **Exemple de code** :
  ```python
  class PriorisationService:
      def calculer_delai_reponse(self, urgence: str) -> int:
          if urgence == "urgence_vitale":
              return 30  # minutes
          elif urgence == "urgence_standard":
              return 60  # minutes
          else:
              return 120  # minutes
  ```
  ```

- **Règles** :
  - Utiliser les termes canoniques en **gras** pour les titres.
  - Inclure un exemple de code pour illustrer l'implémentation.
  - Expliquer les choix techniques en lien avec le métier.

---

#### **3.2.3. Code (Python/Java/C#)**
- **Noms de classes** : Utiliser `PascalCase` et le terme canonique.
  ```python
  class PrescriptionMedicale:
      pass
  ```
- **Noms de méthodes** : Utiliser `camelCase` et un verbe d'action.
  ```python
  def prioriser_demandes(self, demandes: List[DemandeUrgente]) -> List[DemandeUrgente]:
      pass
  ```
- **Noms de variables** : Utiliser `snake_case` et le terme canonique.
  ```python
  delai_reponse = 30  # minutes
  ```
- **Noms de champs de base de données** : Utiliser `snake_case` et le terme canonique.
  ```sql
  CREATE TABLE echantillon_biologique (
      id SERIAL PRIMARY KEY,
      type_tube VARCHAR(50) NOT NULL,
      volume DECIMAL(5,2) NOT NULL,
      statut VARCHAR(20) NOT NULL
  );
  ```
- **Noms de fichiers** : Utiliser `snake_case` et le terme canonique.
  ```
  priorisation_service.py
  circuit_informatise.py
  ```

- **Règles** :
  - Utiliser les termes canoniques du glossaire.
  - Éviter les abréviations non standardisées.
  - Inclure des commentaires pour expliquer les choix techniques en lien avec le métier.

---

#### **3.2.4. Tests (unitaires/integration)**
- **Noms de tests** : Utiliser le format *"[Méthode]_[Scénario]_[Résultat attendu]"*.
  ```python
  def test_prioriser_demandes_urgence_vitale():
      # Étant donné une demande d'urgence vitale
      demande = DemandeUrgente(niveau_urgence="urgence_vitale")
      service = PriorisationService()

      # Quand on priorise la demande
      result = service.prioriser_demandes([demande])

      # Alors le délai de réponse doit être de 30 minutes
      assert result[0].delai_reponse == 30
  ```
- **Règles** :
  - Utiliser les termes canoniques dans les noms de tests.
  - Inclure des scénarios clairs et des résultats attendus explicites.

---

### **3.3. Exemples de phrases types pour différents contextes**

| **Contexte** | **Exemple de phrase** |
|--------------|-----------------------|
| **User Story** | *"En tant que médecin prescripteur, je souhaite saisir une **prescription médicale** avec les **informations cliniques** obligatoires afin que le **dosage anti-Xa** soit interprété correctement."* |
| **Documentation technique** | *"Le **circuit informatisé** doit assurer la **traçabilité** de chaque **prescription médicale**, depuis la saisie jusqu’à la transmission des résultats."* |
| **Code (Python)** | ```python
class CircuitInformatise:
    def transmettre_resultats(self, prescription: PrescriptionMedicale) -> ResultatDosageAntiXa:
        # Logique de transmission des résultats
        pass
``` |
| **Code (SQL)** | ```sql
INSERT INTO prescription_medicale (patient_id, anticoagulant, dose, heure_derniere_prise, dfg)
VALUES ('PAT123', 'apixaban', 5, '2023-10-01 14:30:00', 30);
``` |
| **Test unitaire** | ```python
def test_rejet_echantillon_non_conforme():
    # Étant donné un échantillon non conforme
    echantillon = EchantillonBiologique(type_tube="EDTA", volume=0.5)

    # Quand le biologiste vérifie la conformité
    est_conforme = service.verifier_conformite(echantillon)

    # Alors l'échantillon doit être rejeté
    assert not est_conforme
    assert service.rejet_echantillon == True
``` |

---

## **4. Recommandations pour la documentation technique**

### **4.1. Structure type d'un document technique**

```markdown
# **Titre du document**
**Domaine** : Circuit des demandes urgentes de dosage anti-Xa

## **1. Contexte métier**
- **Définition** : [Description du concept métier].
- **Acteurs concernés** : [Liste des acteurs utilisant ce concept].
- **Exemple d'usage** : [Exemple concret dans le processus métier].

## **2. Alignement technique**
- **Terme technique** : [Nom du champ/méthode/classe dans le code].
- **Type de données** : [Type de données (ex : VARCHAR, INT, ENUM)].
- **Exemple de code** : [Extrait de code illustrant l'implémentation].
- **Règles métier associées** : [Liste des règles métier liées à ce concept].

## **3. Bonnes pratiques**
- **À faire** :
  - Utiliser le terme canonique dans tous les documents et le code.
  - Inclure des exemples concrets pour illustrer l'usage.
- **À éviter** :
  - Utiliser des traductions techniques non comprises par les métiers.
  - Oublier de documenter les choix techniques en lien avec le métier.

## **4. Liens utiles**
- [Lien vers le glossaire du langage commun]
- [Lien vers les user stories associées]
- [Lien vers les spécifications techniques]
```

---

### **4.2. Exemple de document technique : "Délai de réponse"**

```markdown
# **Délai de réponse**
**Domaine** : Circuit des demandes urgentes de dosage anti-Xa

## **1. Contexte métier**
- **Définition** : Temps maximal autorisé entre la réception de la demande de dosage anti-Xa par le laboratoire et la transmission des résultats au prescripteur.
- **Acteurs concernés** : Médecins prescripteurs, Biologiste, SIL.
- **Exemple d'usage** : *"Pour les urgences vitales, le délai de réponse ne doit pas excéder 30 minutes."*

## **2. Alignement technique**
- **Terme technique** : `delai_reponse` (champ dans la base de données SIL).
- **Type de données** : `INT` (minutes).
- **Exemple de code** :
  ```python
  class PriorisationService:
      def calculer_delai_reponse(self, urgence: str) -> int:
          if urgence == "urgence_vitale":
              return 30
          elif urgence == "urgence_standard":
              return 60
          else:
              return 120
  ```
- **Règles métier associées** :
  - Le délai de réponse doit être inférieur à 30 minutes pour les urgences vitales.
  - Le délai de réponse doit être inférieur à 1 heure pour les urgences standard.

## **3. Bonnes pratiques**
- **À faire** :
  - Utiliser `delai_reponse` dans tous les documents et le code.
  - Inclure le niveau d'urgence dans le calcul du délai.
- **À éviter** :
  - Utiliser des termes comme `temps_de_rendu` ou `delai_analyse` qui excluent le transport.
  - Oublier de documenter les critères de priorisation.

## **4. Liens utiles**
- [Glossaire du langage commun : Délai de réponse](lien_vers_glossaire)
- [User Story : Prioriser les demandes urgentes](lien_vers_user_story)
- [Spécifications techniques : Circuit informatisé](lien_vers_specs)
```

---

### **4.3. Exemple de document technique : "Circuit informatisé"**

```markdown
# **Circuit informatisé**
**Domaine** : Circuit des demandes urgentes de dosage anti-Xa

## **1. Contexte métier**
- **Définition** : Processus numérique sécurisé et tracé, géré par le SIL, pour la gestion des demandes urgentes de dosage anti-Xa, incluant la priorisation et la transmission des résultats.
- **Acteurs concernés** : SIL, Biologiste, Médecins prescripteurs, Personnel infirmier.
- **Exemple d'usage** : *"Le circuit informatisé doit prioriser automatiquement les demandes urgentes et notifier les acteurs concernés en temps réel."*

## **2. Alignement technique**
- **Terme technique** : `CircuitInformatise` (module dans l'architecture du SIL).
- **Composants associés** :
  - `PrescriptionMedicaleService` : Gestion des prescriptions.
  - `PriorisationService` : Priorisation des demandes.
  - `TraçabilitéService` : Enregistrement des étapes.
  - `TransmissionService` : Transmission des résultats.
- **Exemple de code** :
  ```python
  class CircuitInformatise:
      def __init__(self):
          self.prescription_service = PrescriptionMedicaleService()
          self.priorisation_service = PriorisationService()
          self.traçabilité_service = TraçabilitéService()
          self.transmission_service = TransmissionService()

      def traiter_demande(self, prescription: PrescriptionMedicale) -> ResultatDosageAntiXa:
          # 1. Vérifier la conformité de la prescription
          if not self.prescription_service.est_valide(prescription):
              raise InvalidPrescriptionError()

          # 2. Prioriser la demande
          demande_priorisée = self.priorisation_service.prioriser(prescription)

          # 3. Traçabilité
          self.traçabilité_service.enregistrer_etape(demande_priorisée, "priorisation")

          # 4. Transmission des résultats
          return self.transmission_service.transmettre(demande_priorisée)
  ```
- **Règles métier associées** :
  - Le circuit doit assurer la traçabilité de chaque étape.
  - Le circuit doit prioriser automatiquement les demandes urgentes.
  - Le circuit doit transmettre les résultats en temps réel.

## **3. Bonnes pratiques**
- **À faire** :
  - Utiliser `CircuitInformatise` comme nom de module principal.
  - Décomposer le circuit en services spécialisés (ex : `PriorisationService`).
  - Documenter chaque étape du circuit avec des exemples concrets.
- **À éviter** :
  - Utiliser des termes comme `workflow_numerique` ou `systeme_securise` qui sont trop vagues.
  - Oublier de documenter les interactions entre les services.

## **4. Liens utiles**
- [Glossaire du langage commun : Circuit informatisé](lien_vers_glossaire)
- [User Story : Implémenter un circuit informatisé sécurisé](lien_vers_user_story)
- [Architecture technique : Modules du SIL](lien_vers_architecture)
```

---

## **5. Annexe : Checklist pour la cohérence métier ↔ technique**

| **Étape** | **Action** | **Critères de validation** |
|-----------|------------|-----------------------------|
| **1. Rédaction des user stories** | Utiliser les termes canoniques du glossaire | - Tous les termes sont ceux du glossaire <br> - Pas de traduction technique |
| **2. Conception technique** | Aligner les noms de classes/méthodes avec le glossaire | - Noms de classes : `PascalCase` + terme canonique <br> - Noms de méthodes : `camelCase` + verbe d'action <br> - Noms de variables : `snake_case` + terme canonique |
| **3. Implémentation du code** | Respecter les conventions de nommage | - Pas d'abréviations non standardisées <br> - Commentaires expliquant les choix techniques en lien avec le métier |
| **4. Documentation technique** | Structurer les documents selon le modèle proposé | - Titre en **gras** avec le terme canonique <br> - Section "Alignement technique" avec exemples de code <br> - Section "Bonnes pratiques" avec critères clairs |
| **5. Tests unitaires/integration** | Utiliser les termes canoniques dans les noms de tests | - Format : `[Méthode]_[Scénario]_[Résultat attendu]` <br> - Scénarios clairs et résultats attendus explicites |
| **6. Revue de code** | Vérifier la cohérence avec le glossaire | - Tous les termes techniques correspondent au glossaire <br> - Pas de traduction permanente entre vocabulaire métier et technique |
| **7. Formation des équipes** | Sensibiliser les équipes aux conventions de nommage | - Ateliers pour expliquer les termes canoniques <br> - Exemples concrets d'usage dans le code et la documentation |

---
## **6. Synthèse des actions prioritaires**

| **Priorité** | **Action** | **Responsable** | **Échéance** | **Livrable** |
|--------------|------------|-----------------|---------------|---------------|
| **Haute** | Finaliser le glossaire du langage commun | Curateur de langage commun | J+7 | Glossaire validé par les parties prenantes |
| **Haute** | Former les équipes (développeurs, métiers) aux conventions de nommage | Chef de projet | J+14 | Ateliers de formation + supports |
| **Haute** | Mettre à jour les user stories existantes avec les termes canoniques | Product Owner | J+21 | User stories relues et validées |
| **Moyenne** | Rédiger la documentation technique pour les concepts clés (ex : `Circuit informatisé`, `Délai de réponse`) | Architecte technique | J+30 | Documents techniques validés |
| **Moyenne** | Implémenter les conventions de nommage dans le code (refactoring si nécessaire) | Équipe développement | J+45 | Code relu et validé |
| **Basse** | Intégrer les conventions de nommage dans les processus de revue de code | Équipe qualité | J+60 | Processus de revue mis à jour |

---
## **7. Annexe : Sources et références**

| **Source** | **Description** |
|------------|-----------------|
| **Glossaire du langage commun** | Document de référence pour les termes canoniques. |
| **Demande initiale du biologiste** | `data/input/demande_biologiste.md` |
| **Livrables des étapes 1 et 2** | Cartographie des acteurs, règles métier, conflits d'objectifs. |
| **Normes ISO 15189** | Normes pour les laboratoires d'analyses de biologie médicale. |
| **Normes CLSI GP41** | Normes pour la gestion pré-analytique des échantillons biologiques. |
| **RGPD** | Règlement Général sur la Protection des Données. |
| **Code de la santé publique** | Réglementation française pour les prescriptions médicales. |