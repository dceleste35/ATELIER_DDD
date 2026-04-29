# Synthèse étape 2 — Structuration du domaine

## Synthèse des acteurs et de leurs interactions clés

### Acteurs et leurs Rôles
1. **Biologiste**
   - Responsable de l'analyse et interprétation des résultats des dosages anti-Xa.
   - Interagit principalement avec les médecins prescripteurs et techniciens de laboratoire.

2. **Médecins prescripteurs (Urgences, Réanimation, Bloc opératoire)**
   - Évaluent et prescrivent les dosages, transmettent des informations cliniques.
   - Ont un rôle central dans la communication avec le biologiste et le personnel infirmier.

3. **Personnel infirmier**
   - Effectue les prélèvements, garantit la conformité des échantillons.
   - Sert d'interface entre les médecins prescripteurs et le laboratoire.

4. **Techniciens de laboratoire**
   - Réalisent les analyses, assurent la qualité et la traçabilité des échantillons.
   - Travaillent en collaboration avec le biologiste et le personnel infirmier.

5. **Services cliniques (Urgences, Réanimation, Bloc opératoire)**
   - Origine des prescriptions, garantissent la prise en charge rapide des patients.

6. **Système d'Information de Laboratoire (SIL)**
   - Centralise les données, assure la gestion des demandes et le suivi des analyses.

### Interactions Clés
- Les médecins prescripteurs soumettent des demandes au personnel infirmier, qui effectue les prélèvements et les envoie au laboratoire.
- Les techniciens de laboratoire manipulent les échantillons et communiquent les résultats aux biologistes, qui informent les médecins prescripteurs.
- Le SIL standardise et facilite les échanges de données entre les acteurs.

## Tableau de bord des règles métier majeures

| Catégorie                        | Règle                                                         | Acteurs concernés                                     |
|----------------------------------|--------------------------------------------------------------|------------------------------------------------------|
| Validation                       | Les échantillons doivent respecter des normes de conformité  | Biologiste, Personnel infirmier                       |
| Priorité                        | Les demandes urgentes doivent être traitées en priorité     | Techniciens de laboratoire, SIL                       |
| Sécurité patient                | Les données patients doivent être protégées et traçables    | SIL, Personnel infirmier, Biologiste                  |
| Documentation                    | Chaque étape doit être correctement documentée               | SIL, Techniciens de laboratoire                       |
| Communication                    | Les médecins doivent fournir des informations cliniques complètes | Médecins prescripteurs                               |
| Enchaînement                    | Prescription médicale requise pour prélèvement               | Médecins prescripteurs, Personnel infirmier           |

## Synthèse des conflits d'objectifs et arbitrages proposés

| Conflit                                      | Acteurs impliqués                        | Objectifs opposés                                                  | Consequences                                    | Pistes d'arbitrage métier                                             |
|----------------------------------------------|-----------------------------------------|--------------------------------------------------------------------|------------------------------------------------|---------------------------------------------------------------------|
| Rapidité clinique vs. Qualité pré-analytique | Médecins prescripteurs, Personnel infirmier, Biologiste, Techniciens de laboratoire | Rapidité des résultats vs. conformité des échantillons            | Risque d’analyses imprécises, erreurs de traitement | Formation sur conformité, procédures d'escalade pour demandes urgentes |
| Charge IDE vs. Traçabilité                   | Personnel infirmier, Techniciens de laboratoire | Charge de travail vs. traçabilité complète                       | Documentation incomplète, interprétation erronée | Simplification administrative, ajustement des affectations         |
| Productivité du laboratoire vs. Sécurité patient | Techniciens de laboratoire, Biologiste  | Productivité vs. garantie de sécurité                              | Erreurs d’analyse conduisant à des risques       | Système de priorisation pour urgences, audits réguliers            |
| Communication des informations vs. Délai de réponse | Médecins prescripteurs, Personnel infirmier, SIL | Réponses rapides vs. communication précise                        | Retards dans le processus d'analyse                | Protocoles standardisés pour communication, outils de communication instantanée |

## Liste des points à clarifier auprès du métier
1. Critères précis de conformité des tubes de prélèvement pour assurer leur acceptabilité.
2. Mécanismes de priorisation des demandes urgentes entre différents services.
3. Protocole standardisé pour la transmission d'informations cliniques essentielles.
4. Évaluation des systèmes capables d'intégration avec le SIL existant.
5. Attentes spécifiques des parties prenantes sur la sécurité et la traçabilité du circuit proposé.

## Éléments prêts à être utilisés en étape 3 (modélisation DDD)
- **Contextes bornés** : Identification des contextes correspondants aux acteurs majeurs (Biologiste, SIL, Personnel infirmier).
- **Agrégats** : Proposition d'entités regroupant les demandes, les résultats, les échantillons et la traçabilité.
- **Événements** : Définition des événements clés tels que la création de demandes, l'analyse des résultats, les ajustements thérapeutiques, et les alertes sur les non-conformités.

---

Cette synthèse fournit une vue d'ensemble structurée du domaine lié aux demandes urgentes de dosage anti-Xa et constitue une base solide pour la phase suivante de modélisation DDD. Elle souligne également les nécessités d'éclaircissement sur certains aspects avant de poursuivre vers des solutions adaptées.