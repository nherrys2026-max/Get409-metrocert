# Value Proposition Canvas — MetroCert

> GET 409 · Séance 2 · Swiss UMEF University — Campus de Dakar · 2025-2026
> Visuel du canvas ci-dessous ([`vpc-metrocert.svg`](vpc-metrocert.svg)) · version PDF déposée sur e-Academy (`GET409-MetroCert_VPC.pdf`)
> Sources : [`carte-empathie.md`](../carte-empathie.md) (S1) · [`hmw.md`](../hmw.md) (S1) · [`concept-application.md`](concept-application.md)

![Value Proposition Canvas — MetroCert](vpc-metrocert.svg)

## HMW définitif (S2)

> **Comment pourrions-nous permettre aux responsables techniques de laboratoires d'étalonnage au Sénégal, comme Mame Diarra, qui jonglent avec un modèle de certificat différent par famille d'instruments et par client, de passer des relevés de mesure à un certificat conforme à l'ISO/IEC 17025 sans aucune ressaisie, afin de livrer leurs clients dans la journée et de passer leurs audits d'accréditation sans écart lié aux certificats ?**

Justification et comparaison avec le HMW S1 : [`hmw-definitif.md`](hmw-definitif.md)

---

## 👤 Persona

| Champ | Détail |
|---|---|
| Identité | Mame Diarra Sow, 38 ans |
| Poste | Responsable technique d'un laboratoire d'étalonnage privé, zone industrielle de Dakar (Mbao) |
| Équipe | 4 techniciens, 1 responsable qualité à temps partiel |
| Volume | ≈ 150 certificats/mois — balances, manomètres, thermomètres et sondes, dimensionnel, multimètres, verrerie, pipettes |
| Clients | Agroalimentaire, pharmaceutique, pétrole et gaz, mines, BTP — chacun avec ses exigences de présentation |
| Outils actuels | 1 modèle Word + 1 classeur Excel d'incertitude par famille ; PDF signés envoyés par e-mail ou WhatsApp |
| Équipement | PC portable au labo, smartphone Android sur site, 4G parfois instable chez les clients |
| Enjeu | Obtenir / maintenir l'accréditation ISO/IEC 17025 |
| Verbatim | « Mesurer, on sait faire. Ce qui nous tue, c'est la paperasse autour de la mesure. » |

Légende des sources : **[CE]** carte d'empathie S1 · **[HMW2]** / **[HMW3]** énoncés alternatifs S1 · **[À valider]** hypothèse de l'équipe, à confirmer en entretien.

---

## 👤 PROFIL CLIENT

### 🔧 Jobs To Be Done

| # | Type | Job | Source |
|---|---|---|---|
| J1 | Fonctionnel | **Émettre des certificats d'étalonnage conformes** à l'ISO/IEC 17025 §7.8 pour ≈ 150 instruments/mois, toutes familles confondues | [CE] |
| J2 | Fonctionnel | **Tenir les délais clients**, notamment avant leurs audits ISO 9001 (« il nous faut les certificats pour vendredi ») | [CE] |
| J3 | Fonctionnel | **Garantir la traçabilité métrologique** : étalons de référence en cours de validité, conditions ambiantes enregistrées | [CE] |
| J4 | Fonctionnel | **Respecter le format imposé par chaque client** (logo, champs obligatoires, numérotation) | [CE] |
| J5 | Fonctionnel | **Augmenter le nombre de certificats sans embaucher** (demande de la direction) | [CE] |
| J6 | Social | **Être reconnue comme un labo « au niveau des labos européens »** par les clients et l'auditeur | [CE] |
| J7 | Émotionnel | **Aborder un audit sereinement** et ne plus relire chaque certificat seule le soir | [CE] |

### 😣 Pains

| # | Pain | Type | Intensité | Source |
|---|---|---|:-:|---|
| P1 | **Erreurs de recopie** carnet → Excel → Word (relevés, incertitude, k) : écart d'audit, voire rappel de toute une série | Risque | ★★★★★ | [CE] |
| P2 | **Délais de 2 à 5 jours** entre l'intervention et l'envoi du certificat | Fonctionnel | ★★★★★ | [CE] |
| P3 | **Un modèle par instrument et par client** : impossible à maintenir, aucune cohérence, refait à chaque nouveau client | Fonctionnel | ★★★★☆ | [CE] |
| P4 | **Suivi manuel des échéances des étalons** dans un fichier séparé : un oubli invalide un lot de certificats | Risque | ★★★★★ | [CE] |
| P5 | **Mentions obligatoires oubliées** (traçabilité, règle de décision, conditions ambiantes) relevées par l'auditeur | Risque | ★★★★☆ | [CE] [HMW2] |
| P6 | **Classeurs Excel fragiles** et versionnés à la main (`certif_manometre_v3_FINAL2.xlsx`) qui cassent dès qu'on ajoute une colonne | Fonctionnel | ★★★☆☆ | [CE] |
| P7 | **Relecture solitaire le soir** de chaque certificat : charge mentale et goulot d'étranglement | Émotionnel | ★★★★☆ | [CE] |
| P8 | **Aucun historique exploitable** pour justifier les intervalles d'étalonnage ou suivre la dérive | Fonctionnel | ★★☆☆☆ | [CE] |
| P9 | **Certificats perdus par le client** (PDF par e-mail / WhatsApp), impossibles à authentifier | Fonctionnel | ★★☆☆☆ | [CE] [HMW3] |

### 🌟 Gains

| # | Gain | Priorité | Indicateur mesurable | Source |
|---|---|:-:|---|---|
| G1 | **Saisir les relevés une seule fois** (labo ou site, même hors connexion) et obtenir le PDF automatiquement | ★★★★★ | 0 ressaisie ; temps saisie → PDF | [CE] |
| G2 | **Certificats conformes par construction** (§7.8 : incertitude avec k, traçabilité, règle de décision…) | ★★★★★ | 0 écart d'audit lié au contenu des certificats | [CE] |
| G3 | **Livraison dans la journée** | ★★★★★ | Délai intervention → envoi < 24 h | [CE] |
| G4 | **Un seul outil pour tous les clients** : logo, en-tête, numérotation, règle de décision paramétrés par société | ★★★★☆ | Nouveau client configuré en < 30 min, sans modifier de modèle Word | [CE] |
| G5 | **Blocage automatique** si un étalon utilisé est hors validité | ★★★★☆ | 0 certificat émis avec un étalon échu | [CE] |
| G6 | **Plus de certificats par technicien** | ★★★★☆ | Certificats/mois à effectif constant | [CE] |
| G7 | **Image de labo moderne** : QR code de vérification comme les concurrents étrangers | ★★★☆☆ | Certificat vérifiable en ligne | [CE] |
| G8 | **Historique par instrument** pour conseiller les intervalles (ILAC G24 / OIML D10) | ★★☆☆☆ | Historique disponible par n° de série | [CE] |

---

## 💡 PROPOSITION DE VALEUR — MetroCert

### 📦 Produits & services

| # | Élément | Description (sans jargon) | Priorité |
|---|---|---|:-:|
| S1 | **Saisie unique des relevés** | Formulaire par famille d'instruments (valeurs de référence, lectures, répétitions, conditions ambiantes), utilisable sur PC ou smartphone, **hors connexion** puis synchronisé | MUST |
| S2 | **Calcul automatique et vérifiable** | Erreurs, corrections et budget d'incertitude selon le GUM, incertitude élargie avec k = 2 par défaut. Calcul **déterministe** (pas d'IA), formules visibles | MUST |
| S3 | **Certificat PDF généré** | Contenu minimal ISO/IEC 17025 §7.8 garanti par le modèle, numéro unique, circuit vérification → approbation, signature humaine identifiée | MUST |
| S4 | **Paramétrage multi-sociétés** | Logo, en-tête, format de numérotation, n° d'accréditation, règle de décision par défaut (ILAC G8), langue — par société cliente | MUST |
| S5 | **Registre des étalons** | Dates d'échéance des étalons de référence ; **blocage** de la saisie si un étalon sélectionné est hors validité | MUST |
| S6 | **Agent Dify « contrôle de complétude »** | Relit le certificat avant approbation et signale les mentions manquantes ou incohérentes | MUST (démo S6) |
| S7 | **QR code de vérification** | Chaque PDF porte un QR code qui renvoie vers la page d'authenticité du certificat | SHOULD |
| S8 | **Historique par instrument + alertes d'échéance** | Suivi de dérive, date de prochain étalonnage recommandée | COULD |
| S9 | **Agent Dify « rédaction des remarques »** | Propose les observations du certificat | COULD — voir FIT |

**Périmètre démo S6** : 1 société de démonstration, 3 familles (balance, manomètre, thermomètre), S1 à S6 + S7.

### 💊 Pain Relievers

| Pain | Pain Reliever | Service |
|---|---|---|
| **P1** Erreurs de recopie | Les relevés sont saisis **une seule fois** ; le calcul et le PDF sont alimentés directement : plus de copier-coller entre carnet, Excel et Word | S1, S2, S3 |
| **P2** Délais 2–5 jours | Le PDF est prêt dès la fin de la saisie ; il ne reste que la vérification et l'approbation | S1, S3 |
| **P3** Un modèle par client | **Un seul modèle par famille**, habillé automatiquement aux couleurs de chaque société | S4 |
| **P4** Suivi manuel des étalons | Registre central + **blocage** à la sélection d'un étalon échu | S5 |
| **P5** Mentions oubliées | Champs §7.8 **obligatoires dans le modèle** + contrôle de complétude par l'agent avant approbation | S3, S6 |
| **P6** Excel fragiles | Calcul centralisé et versionné, identique pour tous les techniciens | S2 |
| **P7** Relecture solitaire le soir | L'agent signale d'abord les anomalies ; la relecture humaine se concentre sur la mesure, pas sur la mise en forme | S6, S3 |
| **P8** Pas d'historique | *Post-MVP* : historique par instrument | S8 |
| **P9** Certificats perdus / non authentifiables | *Partiel* : QR code de vérification ; portail client reporté | S7 |

### 🎁 Gain Creators

| Gain | Gain Creator | Service |
|---|---|---|
| **G1** Saisie unique, même hors connexion | Formulaire hors connexion synchronisé au retour du réseau | S1 |
| **G2** Conforme par construction | Contenu §7.8 intégré au modèle, incertitude toujours affichée avec k, règle de décision tirée du paramétrage | S2, S3, S4, S6 |
| **G3** Livraison dans la journée | Saisie → PDF immédiat ; circuit d'approbation en ligne | S1, S3 |
| **G4** Un seul outil pour tous | Ajout d'un client = une fiche de paramétrage, pas un nouveau fichier Word | S4 |
| **G5** Blocage étalon échu | Contrôle automatique à la préparation de l'étalonnage | S5 |
| **G6** Plus de certificats par technicien | Suppression des tâches de ressaisie et de mise en page | S1, S2, S3 |
| **G7** Image de labo moderne | QR code de vérification sur chaque certificat | S7 |
| **G8** Historique / intervalles | *Post-MVP* | S8 |

---

## ✅ FIT CHECK

### Matrice Pains × Services

| | S1 Saisie | S2 Calcul | S3 PDF | S4 Multi-sociétés | S5 Étalons | S6 Agent contrôle | S7 QR | S8 Historique |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **P1** Recopie | ● | ● | ● | | | ◐ | | |
| **P2** Délais | ● | ◐ | ● | | | | | |
| **P3** Modèle par client | | | ◐ | ● | | | | |
| **P4** Étalons échus | | | | | ● | | | |
| **P5** Mentions oubliées | | | ● | ◐ | | ● | | |
| **P6** Excel fragiles | | ● | | | | | | |
| **P7** Relecture le soir | | | ◐ | | | ● | | |
| **P8** Pas d'historique | | | | | | | | ● |
| **P9** Certificats perdus | | | | | | | ● | ◐ |

● répond directement · ◐ répond partiellement

### Verdict

- **FIT fort sur le cœur du problème** : les 5 pains les plus intenses (P1, P2, P4, P5, P7) ont chacun au moins un Pain Reliever direct dans le MVP.
- **Services sans Pain correspondant** : **S9 (agent de rédaction des remarques)** ne soulage aucun pain exprimé par Mame Diarra → **retiré du MVP** (reste en idée COULD).
- **Pains couverts après le MVP** : P8 (historique) et P9 (certificats perdus, sauf le QR code) → roadmap post-S6.
- **Garde-fou éthique** : l'IA ne calcule ni résultat ni incertitude ; elle contrôle et signale. L'approbation reste une signature humaine identifiée.

### Hypothèses à valider en S3 (entretiens avec ≥ 2 responsables de labo)

| # | Nous croyons que… | Nous le saurons si… | Lien |
|---|---|---|---|
| H1 | La ressaisie et la mise en forme représentent la part principale du délai de 2 à 5 jours | ≥ 2 responsables sur 3 citent la rédaction du certificat comme 1ʳᵉ cause de délai | P1, P2 |
| H2 | Un modèle unique par famille, habillé par société, est accepté par les clients qui imposent leur format | ≥ 2 clients acceptent le certificat MetroCert sans exiger leur propre modèle Word | P3, G4 |
| H3 | Les écarts d'audit liés aux certificats portent surtout sur des mentions manquantes | Revue de 2 rapports d'audit ou témoignages confirmant ce type d'écart | P5, S6 |
| H4 | La saisie hors connexion sur smartphone est indispensable sur site | ≥ 1 intervention sur 2 se fait sur site avec réseau instable | G1 |

---

*Construit à partir de la carte d'empathie S1 (persona composite, à valider par entretiens) et des prompts VPC documentés dans [`journal-prompts.md`](journal-prompts.md).*
