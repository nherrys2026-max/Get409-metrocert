# Module D (S5+) : fonctionnalité IA innovante MetroCert

> GET 409 · Tutoriel S5+ §5 · Équipe MetroCert (I. NKOUNKOU, M. S. COULIBALY) · 01/10/2026
> Point de départ : agent **v2.3** publié, T1–T6 réussis ([`s5bis-rag-deux-recherches.md`](s5bis-rag-deux-recherches.md)).

## 1. Point de départ : HMW et douleurs ciblées

HMW définitif ([`hmw-definitif.md`](../hmw-definitif.md)) : passer des relevés à un certificat conforme **sans ressaisie**, **livrer dans la journée** et passer l'audit **sans écart lié aux certificats**.

Douleurs du VPC ([`vpc.md`](../vpc.md)) visées par le module D :

| Douleur | Intensité | Ce que l'agent v2.3 fait déjà | Ce qui manque |
|---|:-:|---|---|
| P5 Mentions oubliées | ★★★★☆ | les détecte (❌ / ⚠️ / 🔎) | le rapport reste du texte : rien ne part vers le technicien |
| P7 Relecture solitaire le soir | ★★★★☆ | signale les anomalies | aucune étape d'approbation tracée ; la correction se fait par recopie à la main |
| P2 Délais de 2 à 5 jours | ★★★★★ | – | la boucle « défaut → correction → approbation » reste manuelle |
| P4 Étalons échus | ★★★★★ | ETA-T-02 détecté (T2) | pas d'alerte avant l'échéance |

## 2. Trois propositions (catalogue §5.2 adapté à la métrologie)

### F1. Circuit de validation : verdict lisible, renvoi au technicien et approbation tracée
*Patterns 6 (validation humaine), 5 (sortie actionnable) et 7 (sortie structurée, lue par l'app)*

> **Pour** Mame Diarra, responsable technique, **quand** l'agent rend son rapport sur un certificat, **l'application** affiche le verdict en badge avec les compteurs du bilan, prépare en 1 clic le message de correction au technicien (❌ + ⚠️ + 🔎 + prochaine étape) et n'autorise l'approbation qu'avec un nom et une confirmation explicite, **afin de** boucler correction et approbation dans la journée sans rien recopier.

- **Côté Dify** : aucune modification. Le rapport v2.3 a des rubriques fixes, garanties par le test T6 et par le nœud *Nettoyage RÉDACTEUR*.
- **Côté application** : dans la carte « Agent IA MetroCert » (page `/verifier-resultat`), l'app lit les lignes `VERDICT :` et `Bilan :` et découpe les rubriques. Elle affiche un badge vert ou rouge et 4 compteurs, un bouton **« Renvoyer au technicien »** (lien `mailto:` prérempli, sans destinataire imposé) et un bloc **« Approuver »** (nom de l'approbateur et case à cocher). Elle garde aussi l'historique des 3 dernières décisions, en mémoire de session uniquement.
- **Risque éthique** : approuver un certificat ⛔ par réflexe.
- **Garde-fous** :
  - le bouton « Approuver » est désactivé tant que le verdict est ⛔ et que la case « J'ai relu les points signalés et j'assume l'approbation » n'est pas cochée ;
  - le nom de l'approbateur est obligatoire ;
  - aucun envoi automatique : l'humain relit le message dans sa messagerie.

### F2. Photo d'un certificat papier vers contrôle
*Pattern 3 (photo vers extraction, multimodal)*

> **Pour** le technicien, **quand** il doit contrôler un ancien certificat imprimé ou scanné, **l'agent** extrait le texte de la photo puis lance le contrôle §7.8, **afin de** supprimer la ressaisie.

- **Côté Dify** :
  - variable *fichier* dans DÉBUT ;
  - nœud LLM **vision** placé avant CHERCHEUR, ce qui exige Gemini (gpt-oss sur Groq n'accepte pas les images), donc une nouvelle clé et un deuxième quota.
- **Côté application** : champ « Prendre une photo » et téléversement vers Dify.
- **Risque éthique** : chiffre mal lu (0,06 → 0,08) présenté comme conforme ; données réelles d'un client envoyées à un modèle gratuit.
- **Garde-fous** : texte extrait affiché pour relecture avant le contrôle ; documents fictifs seulement.

### F3. Fraîcheur du référentiel et alerte d'échéance des étalons
*Patterns 13 (fraîcheur et traçabilité de la donnée RAG) et 4 (garde-fou métier par RAG)*

> **Pour** Mame Diarra, **quand** un certificat cite un étalon qui expire dans moins de 30 jours, ou quand le registre a plus de 30 jours, **l'agent** ajoute un point ⚠️ et la ligne « Registre des étalons au JJ/MM/AAAA », **afin de** ne jamais émettre de lot avec un étalon qui devient échu.

- **Côté Dify** :
  - date du registre en variable d'environnement ;
  - calcul des écarts de dates dans un nœud **Code** (le LLM n'est pas fiable sur l'arithmétique de dates) ;
  - règle ajoutée au prompt du RÉDACTEUR, puis publication.
- **Côté application** : bandeau « Données du … ».
- **Risque éthique** : registre non mis à jour, donc fausse assurance.
- **Garde-fou** : date affichée à chaque contrôle et ⚠️ automatique au-delà de 30 jours.

## 3. Notation (grille §5.3, chaque critère /5)

| Critère | F1 Validation et renvoi | F2 Photo | F3 Fraîcheur et échéance |
|---|:-:|:-:|:-:|
| Alignement HMW | 5 (P5, P7, P2 ; « dans la journée », « sans écart d'audit ») | 4 (sans ressaisie) | 4 (P4) |
| Valeur démontrable en soutenance (< 2 min) | 5 (T2 → badge rouge → mail prêt en 30 s) | 5 | 3 (il faut simuler une date) |
| Faisabilité (1 séance, Dify gratuit et stack) | 5 (app seule, 1 prompt Lovable) | 2 (nouveau modèle, nouvelle clé, image dans le workflow) | 3 (nœud Code et prompt à republier, T1–T6 à rejouer) |
| Risque maîtrisé | 4 (approbation forcée possible mais nominative et confirmée) | 2 (erreur de lecture d'un chiffre) | 4 |
| Dépendance (sans service payant ni nouvelle clé) | 5 | 2 (Gemini) | 5 |
| **Total /25** | **24** | **15** | **19** |

**Recommandation [Analyse] : F1.** C'est la seule qui ferme la boucle du HMW. Aujourd'hui l'agent *trouve* le défaut ; avec F1, le défaut *repart* vers le technicien et l'approbation devient un acte humain nominatif. Elle ne touche ni Dify ni le quota Groq, donc ne fait courir aucun risque de régression sur T1–T6. F3 est la suivante (post-S6), et F2 reste en idée tant qu'il n'y a pas de clé vision.

## 4. Spécification de F1 (P-Spec)

**User story.** En tant que responsable technique, je veux, depuis le rapport de l'agent, renvoyer en un clic les corrections au technicien et approuver le certificat sous mon nom, afin de livrer le client dans la journée sans rien recopier et en gardant la décision humaine.

**Critères d'acceptation (vérifiables)**

| # | Critère |
|---|---|
| CA1 | Pour tout rapport contenant `VERDICT :`, la carte affiche un badge **vert « Prêt pour approbation »** si la ligne contient `✅`, sinon **rouge « À corriger avant approbation »**, ainsi que les 4 compteurs lus dans la ligne `Bilan :` (présentes, manquantes, à vérifier, non applicables). |
| CA2 | Le bouton « Renvoyer au technicien » ouvre un `mailto:` **sans destinataire**. L'objet est `MetroCert – corrections certificat <n° lu après CERTIFICAT :>`. Le corps contient les rubriques ❌, ⚠️, 🔎 et PROCHAINE ÉTAPE recopiées telles quelles, puis la dernière ligne de signature humaine. Le bouton n'apparaît que si le verdict est ⛔. |
| CA3 | « Approuver » exige un nom (≥ 3 caractères). Si le verdict est ⛔, il exige en plus la case « J'ai relu les points signalés et j'assume l'approbation ». Après le clic, la carte affiche « Approuvé par <nom> le <date heure> ». Les 3 dernières décisions sont gardées en mémoire de session, et rien n'est enregistré dans le navigateur ni sur un serveur. Si la réponse est un `message_erreur` (`INSUFFISANT`) ou si `VERDICT :` est absent, la carte affiche le texte seul : ni badge, ni bouton. |

**Modifications Dify** : aucune. Les sorties `rapport_controle` et `message_erreur` restent inchangées. Aucune republication, donc T1–T6 restent valides côté agent.

**Modifications de l'application** [Hypothèse : stack Lovable récente TanStack Start, à confirmer dans la vue Code] :
- composant qui affiche la réponse de l'agent sur `/verifier-resultat` (carte « Agent IA MetroCert ») ;
- nouveau composant `RapportControleActions` (badge, compteurs, renvoi, approbation) ;
- **aucune** modification de la fonction serveur `controle-certificat` : la clé `DIFY_API_KEY` reste côté serveur.

**Prompt Lovable (1 prompt = 1 modification)**, à coller dans le chat Lovable du projet :

```text
Dans la carte « Agent IA MetroCert » de la page /verifier-resultat, ajoute un composant RapportControleActions qui s'affiche sous le texte du rapport renvoyé par l'agent (data.outputs.rapport_controle). Ne modifie PAS la fonction serveur controle-certificat ni l'appel à Dify.

1. Analyse du texte (côté navigateur, sans IA) :
   - verdict = la ligne qui commence par « VERDICT : ». Si elle contient « ✅ » → vert « Prêt pour approbation », sinon rouge « À corriger avant approbation ».
   - compteurs = les nombres de la ligne « Bilan : » (présentes · manquantes · à vérifier · non applicable).
   - numéro = le texte après « CERTIFICAT : ».
   - rubriques = les blocs qui commencent par « ❌ MENTIONS MANQUANTES », « ⚠️ POINTS À VÉRIFIER », « 🔎 INCOHÉRENCES », « PROCHAINE ÉTAPE » (jusqu'à la ligne de séparation ───).
   - Si la ligne VERDICT est absente (ex. réponse « INSUFFISANT : … » ou message_erreur), n'affiche rien de plus que le texte actuel.

2. Affichage : un badge (vert #15803D / rouge #B91C1C) avec le verdict et 4 petites pastilles de compteurs.

3. Si le verdict est rouge : bouton secondaire « Renvoyer au technicien » qui ouvre un lien mailto: SANS destinataire, objet « MetroCert – corrections certificat <numéro> », corps = les rubriques ❌, ⚠️, 🔎 et PROCHAINE ÉTAPE recopiées telles quelles, puis la ligne « Contrôle automatique d'aide à la relecture. Il ne remplace ni la vérification ni la signature du responsable technique. » (encodeURIComponent).

4. Bloc « Approbation » : champ « Nom de l'approbateur » (obligatoire, 3 caractères min.) ; si le verdict est rouge, case à cocher obligatoire « J'ai relu les points signalés et j'assume l'approbation » ; bouton « Approuver » désactivé tant que ces conditions ne sont pas remplies. Au clic : afficher « Approuvé par <nom> le <date heure locale> » et l'ajouter à une liste « Dernières décisions » (3 maximum).

5. Stockage : uniquement l'état React en mémoire (pas de localStorage, pas de base de données, pas d'appel serveur).

Garde le style existant de la carte et reste responsive (boutons empilés sous 480 px).
```

## 5. Tests T7–T8 (à ajouter à T1–T6)

| # | Type | Entrée | Critère de réussite |
|---|---|---|---|
| T7 | F1, chemin ⛔ | Entrée de **T2** (CE-2026-0215, ETA-T-02) | Badge **rouge**, compteurs = ligne Bilan. « Renvoyer au technicien » ouvre un mail : objet `MetroCert – corrections certificat CE-2026-0215`, corps avec « ETA-T-02 » et « Refaire l'étalonnage avec un étalon valide », champ À vide. « Approuver » reste grisé tant que le nom et la case ne sont pas remplis, puis affiche « Approuvé par … le … ». |
| T8 | F1, chemin ✅ et robustesse | 1) Entrée de **T1** (CE-2026-0230). 2) Une minute plus tard, entrée de **T3** (`Contrôle le certificat du manomètre.`) | 1) Badge **vert**, pas de bouton « Renvoyer », « Approuver » actif avec le seul nom (pas de case). 2) Texte `INSUFFISANT : …` seul : ni badge ni bouton. |

Puis **rejouer T1–T6** dans le MVP (1 contrôle par minute, quota Groq) et recharger la page : l'historique « Dernières décisions » doit être vide, ce qui montre qu'aucune décision n'est persistée.

## 6. Ligne à ajouter à la note d'éthique S6

| Fonctionnalité | Risque | Garde-fou | Test qui le prouve |
|---|---|---|---|
| F1 Validation et renvoi au technicien | Approbation réflexe d'un certificat ⛔ ; message envoyé au mauvais destinataire | Approbation nominative + case de confirmation obligatoire si ⛔ ; `mailto:` sans destinataire, relu et envoyé par l'humain ; aucune décision persistée (loi 2008-12) | T7 (bouton grisé, mail sans destinataire), T8 (✅ sans case, INSUFFISANT sans bouton), rechargement (historique vide) |

## 7. Ligne pour le Journal L4

| Séance | Prompt | Outil | Résultat | Note /5 |
|---|---|---|---|:-:|
| S5+ module D | P-Idées puis P-Spec (§5.4) adaptés à MetroCert, puis le prompt Lovable du §4 | Claude, Lovable | 3 fonctionnalités notées (F1 24/25, F3 19/25, F2 15/25) ; F1 retenue et spécifiée ; T7–T8 écrits | à compléter après T7–T8 |

## 8. Reste à faire (équipe)

1. Dans Lovable : envoyer d'abord le brouillon en cours (correctif du menu mobile), **puis** coller le prompt du §4 seul.
2. Lancer T7, puis T8, puis rejouer T1–T6, à 1 minute d'intervalle. Faire des captures sans aucune clé visible.
3. **Publish → Update** dans Lovable, puis tester le lien public depuis un téléphone.
4. Compléter la note du Journal L4 et la note d'éthique (§6).
