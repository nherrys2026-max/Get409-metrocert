# Journal de prompts — S1

Traçabilité de l'usage de l'IA, conformément au Code de déontologie IA du cours GET 409.

| # | Date | Outil | Objectif | Contribution humaine |
|---|---|---|---|---|
| 1 | 23/09/2026 | Claude | Structurer le dépôt, rédiger la carte d'empathie, les énoncés HMW et le concept de l'application à partir des supports de la S1 | Choix du secteur et du problème (métrologie), expertise terrain fournie par l'équipe ; relecture et validation à faire par l'équipe ; entretiens réels à conduire |

## Prompt de départ

> Inspecte les supports de la S1. Aide-moi à concevoir une application qui génère les certificats d'étalonnage de tous les instruments de mesure en métrologie, adaptée à toutes les sociétés. Crée le dépôt GitHub, la carte d'empathie et l'énoncé HMW.

## À compléter

- Résultats des entretiens de validation (guide : [guide-entretien.md](guide-entretien.md)).
- Modifications apportées à la carte d'empathie après entretiens.

---

# Journal de prompts — S2 (Idéation, VPC & Prompt Engineering)

> Format demandé par le cours : n° · technique · prompt exact · résumé de la réponse · note /5 · itération.
> Prompts exécutés avec Claude le 23/09/2026. Les notes et itérations reflètent la relecture de l'équipe ; à revoir après les entretiens de validation.

| # | Technique | Objet | Note |
|---|---|---|:-:|
| P1 | Zero-Shot | 3 principaux problèmes du persona | 4/5 |
| P2 | Zero-Shot (format imposé) | 5 fonctionnalités MVP | 2/5 → 4/5 |
| P3 | Few-Shot | Compléter un 3ᵉ défi du secteur | 4/5 |
| P4 | Chain-of-Thought | Cause → obstacle → solution | 5/5 |
| P5 | Libre (critique de HMW) | Tester le HMW définitif | 4/5 |

## P1 — Zero-Shot · Problèmes du persona

**Prompt envoyé**

```text
ROLE : Tu es consultant en métrologie et en accréditation ISO/IEC 17025 en Afrique de l'Ouest.
CONTEXTE : Mame Diarra Sow, 38 ans, est responsable technique d'un laboratoire d'étalonnage
privé à Dakar (Mbao) : 4 techniciens, ~150 certificats/mois (balances, manomètres,
thermomètres, dimensionnel, électricité, verrerie). Certificats rédigés dans un modèle Word
+ un classeur Excel d'incertitude par famille d'instruments, envoyés par e-mail ou WhatsApp.
TACHE : Identifie ses 3 principaux problèmes dans la production des certificats et propose
une piste de solution numérique pour chacun.
FORMAT : Tableau | Problème | Conséquence | Piste numérique |, en français.
```

**Réponse IA (résumé)** — 1) Ressaisie multiple des relevés → erreurs et écarts d'audit → saisie unique alimentant calcul et certificat ; 2) Multiplicité des modèles Word/Excel → incohérences, maintenance lourde → modèle unique paramétrable par client ; 3) Suivi manuel des étalons → risque de certificat invalide → registre avec alertes et blocage.

**Note : 4/5** — Fidèle à la carte d'empathie. −1 : n'a pas relevé le délai de 2 à 5 jours, pourtant la frustration principale côté client.

**Itération** — Aucune (note ≥ 3).

## P2 — Zero-Shot · Fonctionnalités MVP (format imposé)

**Version 1 (non structurée)**

```text
Quelles fonctionnalités pour une application de certificats d'étalonnage ?
```

**Réponse IA (résumé)** — Liste générique : gestion de parc, ERP qualité, planning, facturation, signature électronique, tableau de bord, application mobile. Aucune priorité, aucune référence à l'ISO/IEC 17025 §7.8, ni au contexte sénégalais.

**Note : 2/5** — Inutilisable pour un MVP : trop large, confond gestion de parc et production de certificats.

**Version 2 (itération)**

```text
ROLE : Tu es Product Manager spécialisé en logiciels qualité pour laboratoires accrédités.
CONTEXTE : Notre équipe MetroCert s'adresse aux responsables techniques de laboratoires
d'étalonnage au Sénégal, comme Mame Diarra, qui gèrent un modèle de certificat différent
par famille d'instruments et par client, et veulent passer des relevés à un certificat
conforme ISO/IEC 17025 sans ressaisie. Connexion 4G instable sur site. Démo en 6 semaines
avec des outils no-code (Bolt.new + Dify).
TACHE : Propose les 5 fonctionnalités prioritaires du MVP, classées par impact.
FORMAT : Pour chaque fonctionnalité : Nom court | Problème résolu pour Mame Diarra |
Effort (faible/moyen/élevé) | Réalisable en no-code (oui/non).
```

**Réponse IA (résumé)** — Saisie unique hors connexion (moyen, oui) ; calcul d'incertitude GUM par famille (élevé, partiellement) ; PDF conforme §7.8 (moyen, oui) ; paramétrage multi-sociétés (moyen, oui) ; registre des étalons avec blocage (faible, oui).

**Note : 4/5** — Directement repris dans les Produits & Services du [`vpc.md`](vpc.md). −1 : n'a pas proposé de contrôle de complétude, alors que c'est la peur n° 1 du persona (ajouté par l'équipe : agent Dify S6).

## P3 — Few-Shot · Défis du secteur

**Prompt envoyé**

```text
Tu es un expert des laboratoires d'étalonnage accrédités ISO/IEC 17025 au Sénégal.
Voici des problèmes observés et des solutions adaptées :

PROBLÈME : Les techniciens recopient les relevés du carnet vers Excel puis vers Word.
SOLUTION : Formulaire de saisie unique par famille d'instruments, qui alimente directement
le calcul et le certificat.

PROBLÈME : Un étalon de référence peut être utilisé après sa date d'échéance sans que
personne ne s'en aperçoive.
SOLUTION : Registre des étalons qui bloque la sélection d'un étalon hors validité.

En suivant exactement ce format et ces contraintes, propose une solution pour :
PROBLÈME : Chaque client impose son propre modèle de certificat avec son logo et ses champs.
SOLUTION :

Contraintes : pas de nouveau fichier Word par client, contenu ISO/IEC 17025 §7.8 inchangé,
configurable par un non-développeur.
```

**Réponse IA (résumé)** — « Fiche de paramétrage par société cliente (logo, en-tête, champs additionnels, numérotation, langue) appliquée à un modèle unique par famille ; les mentions §7.8 sont verrouillées et ne peuvent pas être retirées par le paramétrage. »

**Note : 4/5** — Le format et les contraintes sont respectés. L'idée des mentions verrouillées est reprise dans le VPC (S3/S4). −1 : ne dit pas comment traiter un client qui exige un champ contraire à la norme.

**Itération** — Aucune.

## P4 — Chain-of-Thought · Cause → obstacle → solution

**Prompt envoyé**

```text
Tu es un expert en métrologie et en transformation numérique des laboratoires en Afrique de l'Ouest.
Analyse le problème suivant : les laboratoires d'étalonnage au Sénégal mettent 2 à 5 jours
à livrer leurs certificats et subissent des écarts d'audit liés au contenu des certificats.
Réfléchis étape par étape :
Étape 1 : Identifie la cause principale du problème dans le contexte de ces laboratoires.
Étape 2 : Décris l'obstacle principal qui empêche une solution classique (logiciel LIMS
du commerce) de fonctionner.
Étape 3 : Propose une solution technologique accessible à une responsable technique qui
gère 4 techniciens et ~150 certificats/mois.
Développe chaque étape avant de conclure.
```

**Réponse IA (résumé)** — Étape 1 : la chaîne documentaire (ressaisie, modèles multiples, relecture manuelle), pas la mesure elle-même. Étape 2 : les LIMS du commerce sont coûteux, en anglais, pensés pour de gros labos, peu adaptés aux formats imposés par les clients locaux et à la connexion instable sur site. Étape 3 : un outil léger, centré sur le certificat : saisie unique hors connexion, calcul déterministe, modèle unique habillé par client, contrôle automatique des mentions ; démarrer par 3 familles d'instruments.

**Note : 5/5** — Raisonnement vérifiable à chaque étape et cohérent avec le HMW définitif. L'étape 2 justifie le positionnement face aux LIMS (question jury probable).

**Itération** — Aucune.

## P5 — Libre · Critique du HMW définitif

**Prompt envoyé**

```text
Tu es membre d'un jury de Master en innovation. Voici notre HMW S1 et notre HMW S2.
S1 : « Comment pourrions-nous permettre aux techniciens et responsables de laboratoires
d'étalonnage de générer, pour n'importe quel instrument et n'importe quelle société cliente,
un certificat d'étalonnage conforme à l'ISO/IEC 17025 en quelques minutes, afin de supprimer
les erreurs de recopie et de livrer leurs clients plus rapidement ? »
S2 : « Comment pourrions-nous permettre aux responsables techniques de laboratoires
d'étalonnage au Sénégal, comme Mame Diarra, qui jonglent avec un modèle de certificat
différent par famille d'instruments et par client, de passer des relevés de mesure à un
certificat conforme à l'ISO/IEC 17025 sans aucune ressaisie, afin de livrer leurs clients
dans la journée et de passer leurs audits d'accréditation sans écart lié aux certificats ? »
Évalue chacun sur 6 critères (utilisateur réel, vraie frustration, assez large, assez précis,
sans solution imposée, contextualisé). Donne une note /6 et la faiblesse principale restante du S2.
```

**Réponse IA (résumé)** — S1 : 4/6 (deux utilisateurs mélangés, « n'importe quel instrument / société » trop large, « générer » oriente déjà vers un générateur). S2 : 6/6. Faiblesse restante : la phrase est longue pour un pitch oral ; conseille de la découper en 4 blocs (qui / situation / quoi / résultat).

**Note : 4/5** — Critique utile ; le découpage en 4 blocs est repris dans [`hmw-definitif.md`](hmw-definitif.md). −1 : n'a pas signalé que la frustration reste à confirmer par des entretiens réels.

**Itération** — Aucune.

## Ce que nous retenons (S2)

- Le **format imposé** (P2 v2) fait passer la réponse de 2/5 à 4/5 : le contexte (persona, contrainte hors connexion, no-code) élimine les fonctionnalités hors sujet.
- Le **Few-Shot** (P3) fait respecter nos contraintes (mentions §7.8 verrouillées) sans les répéter.
- Le **Chain-of-Thought** (P4) est le plus utile pour l'analyse stratégique : il prépare la réponse au jury « pourquoi pas un LIMS ? ».
- Règle de l'équipe : l'IA ne produit jamais un résultat de mesure ni une incertitude ; elle aide à structurer, rédiger et contrôler.
