# Concept de l'application MetroCert

> Document de travail pour les séances suivantes (S2 idéation, S3 agents Dify, S4 prototype Bolt.new). Il s'agit d'une première vision, pas d'une solution figée.

## 1. Promesse

Saisir les relevés d'étalonnage une seule fois et obtenir un certificat PDF conforme à l'ISO/IEC 17025:2017, pour tout type d'instrument, aux couleurs de n'importe quelle société.

## 2. Utilisateurs

| Profil | Besoin principal |
|---|---|
| Technicien d'étalonnage | Saisir les relevés rapidement, au labo ou sur site, même hors connexion |
| Responsable technique | Vérifier et approuver, être alerté des incohérences |
| Responsable qualité | Garantir la conformité des certificats et la traçabilité des étalons |
| Administrateur de la société | Paramétrer logo, en-tête, numérotation, modèles, utilisateurs |
| Client final (lecture seule) | Retrouver et vérifier ses certificats (QR code, portail) |

## 3. « Adaptée à toutes les sociétés » : le paramétrage multi-sociétés

Chaque société (laboratoire prestataire ou service métrologie interne) dispose de son propre espace isolé :

- identité : raison sociale, adresse, logo, n° d'accréditation et organisme (ex. SOAC, COFRAC) ou mention « non accrédité » ;
- format de numérotation des certificats (ex. `CE-{AAAA}-{NNNN}`) ;
- règle de décision par défaut (acceptation simple, zone de garde, risque spécifique — ILAC G8) ;
- modèles de certificat par famille d'instruments, modifiables ;
- langue du certificat (français / anglais) ;
- utilisateurs et rôles (technicien, vérificateur, approbateur, admin).

## 4. Familles d'instruments couvertes

Masse et pesage · pression · température et humidité · dimensionnel · électricité (DC/AC) · volume et verrerie · débit · force et couple · temps et fréquence · pH et conductivité.

Chaque famille est décrite par un **modèle de procédure** : grandeurs, points de mesure types, nombre de répétitions, sources d'incertitude, EMT éventuelles (ex. EN 837 pour les manomètres, ISO 8655 pour les pipettes, EURAMET cg-18 pour les balances). Ajouter une nouvelle famille = créer un modèle, sans développement.

## 5. Parcours principal

1. **Réception** : l'instrument du client est enregistré (identification, fabricant, modèle, n° de série, étendue, résolution).
2. **Préparation** : choix de la procédure et des étalons ; blocage si un étalon est hors validité.
3. **Saisie des relevés** : valeurs de référence, lectures, répétitions, conditions ambiantes.
4. **Calcul** : erreurs, corrections, budget d'incertitude selon le GUM (JCGM 100:2008), incertitude élargie avec k = 2 par défaut.
5. **Conformité** (si demandée) : déclaration selon la règle de décision choisie.
6. **Vérification et approbation** : circuit à deux niveaux, commentaires.
7. **Émission** : PDF signé, numéro unique, QR code de vérification, envoi au client.
8. **Suivi** : historique par instrument, date de prochain étalonnage recommandée, alertes d'échéance.

## 6. Contenu minimal du certificat (ISO/IEC 17025:2017 §7.8)

Titre · nom et adresse du laboratoire · identification unique et pagination · nom et adresse du client · méthode utilisée · identification de l'instrument · date(s) d'étalonnage et d'émission · résultats avec unités · incertitude de mesure et facteur d'élargissement · conditions ambiantes · déclaration de traçabilité métrologique · résultats avant/après ajustage le cas échéant · règle de décision si déclaration de conformité · identification des personnes autorisant le certificat.

## 7. Où intervient l'IA (S3 — agents Dify)

- **Agent contrôle qualité** : relit le certificat avant émission et signale les mentions manquantes ou incohérentes.
- **Agent assistant procédure** : aide à créer un nouveau modèle de famille d'instruments à partir d'une norme ou d'une procédure interne.
- **Agent rédaction** : propose les remarques et observations du certificat à partir des résultats.

L'IA ne calcule pas les résultats ni les incertitudes : ces calculs sont déterministes et vérifiables. Elle assiste la rédaction et le contrôle, et la décision finale reste humaine (voir la note d'éthique).

## 8. Périmètre du MVP (démo S6)

- 1 société de démonstration + paramétrage de logo et numérotation.
- 3 familles : balance (masse), manomètre (pression), thermomètre (température).
- Saisie des relevés, calcul d'incertitude simplifié, génération du PDF avec QR code.
- 1 agent Dify de contrôle de complétude.

## 9. Points d'éthique et de risque (Responsable Impact)

- Confidentialité des données des clients : isolation stricte entre sociétés.
- Intégrité : un certificat émis n'est jamais modifié ; une correction donne lieu à un nouveau certificat qui remplace l'ancien, avec traçabilité.
- Responsabilité : l'approbation reste une signature humaine identifiée.
- Accessibilité : fonctionnement hors connexion sur site, interface utilisable sur smartphone.
