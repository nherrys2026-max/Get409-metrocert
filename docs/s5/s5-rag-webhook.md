# S5 — MVP V2 MetroCert : RAG + webhook Lovable ↔ Dify

> Séance 5 / 8 · Livrables : L1 MVP V2 en ligne avec webhook (30 pts) · L2 pipeline RAG, capture Dify (30 pts) · L3 schéma d'architecture V2 (20 pts) · L4 journal de prompts S5, min. 3 prompts (20 pts). Dépôt 48 h après la séance ; S6 = évaluation intermédiaire.

## 0. Point de départ : l'application L1 (S3)

| Élément | État constaté le 29/09/2026 |
|---|---|
| Application | `GreenSprint_FicheMarche_v1_[HERRYSTEAM]` — type Workflow — https://udify.app/workflow/QXaHDWAvm4XwbX8c |
| Web app | Activée, mais **« App unavailable »** : `/api/parameters` renvoie `app_unavailable` (400) |
| Cause probable | Workflow non publié après une modification, ou fournisseur de modèle (clé Groq / modèle) retiré ou invalide |
| À faire avant tout | Studio → ouvrir le workflow → vérifier le modèle de chaque nœud LLM (Paramètres → Fournisseurs de modèles) → **Publier une mise à jour** → rouvrir l'URL L1 et vérifier que le formulaire s'affiche |

**Principe retenu** : on garde l'architecture de L1 (Début `query` → CHERCHEUR → RÉDACTEUR → Fin), on la **duplique** en `MetroCert_ControleCertificat_v2` (L1 reste intacte pour l'évaluation S3) et on remplace le métier « fiche marché » par le métier MetroCert : **l'agent de contrôle de complétude du certificat**, défini dans `docs/concept-application.md` §7-8.

```
Début (query) → Récupération de connaissances (MetroCert_KB_v1) → CHERCHEUR → RÉDACTEUR → Fin (rapport)
```

L'agent **ne calcule ni les erreurs ni les incertitudes** (calcul déterministe dans le MVP) : il relit, il cite l'exigence manquante, il ne décide pas à la place du signataire.

---

## Étape A — Base de connaissances `MetroCert_KB_v1` (20 min)

Fichiers prêts dans `docs/s5/kb/` :

| Fichier | Contenu | Longueur de morceau |
|---|---|---:|
| `01_exigences_certificat_17025_7-8.md` | 22 exigences MC-01 à MC-22 (§7.8.2, §7.8.4, §7.8.6, §7.8.8) + distinctions VIM | 500 |
| `02_regles_decision_ilac_g8.md` | Règles RD-01 à RD-05 + exemple chiffré | 500 |
| `03_familles_instruments.csv` | Manomètres, balance, thermomètre : référentiels, points, sources d'incertitude, spécification | 300 |
| `04_registre_etalons_demo.csv` | 5 étalons fictifs, dont **ETA-T-02 échu** (utile pour la démo) | 300 |

1. Dify → **Connaissance** → **+ Créer des connaissances** → Importer à partir d'un fichier → sélectionner les 4 fichiers.
2. Segmentation personnalisée : délimiteur `\n\n`, longueur 500 (Markdown) — si Dify impose un réglage unique, prendre **300** ; chevauchement 50.
3. Mode d'index : **Économique** (index inversé, plan gratuit) ; Top K = 3.
4. Enregistrer & Traiter → attendre 🟢 Disponible → renommer la base `MetroCert_KB_v1`.
5. **Test de récupération** (capture pour L2) :

| # | Requête (mots proches du texte : mode Économique = mots-clés) | Morceau attendu |
|---|---|---|
| 1 | `incertitude élargie k = 2 certificat` | MC-16 |
| 2 | `zone de garde conforme EMT` | RD-02 |
| 3 | `ETA-T-02 échéance` | ligne ETA-T-02 « Échu » |
| 4 | `météo Dakar` | aucun morceau ou score faible (hors base, comportement attendu) |

> Les identifiants MC-xx et les « Mots-clés » ajoutés à chaque exigence servent justement l'index inversé : un certificat qui contient « conditions ambiantes » ou « traçabilité » remonte la bonne exigence.

---

## Étape B — Adapter le workflow L1 et le connecter à la base (15 min)

1. Studio → `GreenSprint_FicheMarche_v1_[HERRYSTEAM]` → **⋯ → Dupliquer** → renommer `MetroCert_ControleCertificat_v2`.
2. Nœud **Début** : variable `query`, type **Paragraphe**, longueur max **4000**, libellé « Certificat à contrôler ou question ».
3. **+** entre Début et CHERCHEUR → **Récupération de connaissances** : texte de la requête = `Début · query` ; connaissances = `MetroCert_KB_v1` ; Top K = **5** (un certificat touche plusieurs exigences).
4. Nœud **CHERCHEUR** → Contexte = `Récupération de connaissances · result` → remplacer le prompt SYSTEM par :

```text
Tu es l'agent CHERCHEUR de MetroCert, assistant de contrôle qualité d'un laboratoire
d'étalonnage (ISO/IEC 17025:2017). Tu ne calcules rien et tu n'inventes aucune exigence.

L'entrée est soit un projet de certificat d'étalonnage, soit une question.

SI C'EST UN CERTIFICAT :
- Pour chaque exigence MC-01 à MC-22 présente dans les DONNÉES DE LA BASE, indique :
  PRÉSENTE (cite l'extrait du certificat), ABSENTE, ou NON APPLICABLE (explique pourquoi,
  ex. MC-19 si aucun ajustage, MC-21 si aucune déclaration de conformité).
- Relève les incohérences observables : conformité déclarée sans règle de décision,
  incertitude sans k, étalon dont le statut est « Échu » dans le registre, recommandation
  de périodicité non convenue, unités manquantes.
- Ne recalcule ni erreurs ni incertitudes ; tu peux seulement signaler qu'une valeur
  manque ou qu'une déclaration contredit la règle annoncée.

SI C'EST UNE QUESTION :
- Réponds uniquement à partir des DONNÉES DE LA BASE, en citant les identifiants
  (MC-xx, RD-xx, nom de l'étalon ou de la famille).

Si les DONNÉES DE LA BASE ne contiennent pas l'information, écris exactement :
« HORS BASE ».

DONNÉES DE LA BASE DE CONNAISSANCES :
{{#context#}}
```

   USER : `{{#start.query#}}` (sélectionner la variable via `{x}`). Température du modèle : **0,1 à 0,2**.

5. Nœud **RÉDACTEUR** → prompt SYSTEM :

```text
Tu es l'agent RÉDACTEUR de MetroCert. À partir de l'analyse du CHERCHEUR, rédige en
français, avec la terminologie du VIM, une réponse courte et structurée.

SI L'ANALYSE PORTE SUR UN CERTIFICAT, utilise exactement ce format :
📋 CONTRÔLE DE COMPLÉTUDE — MetroCert
Verdict : ✅ Prêt pour approbation  |  ⚠️ À corriger avant approbation
Mentions manquantes : liste « MC-xx — libellé » (ou « aucune »)
Incohérences : liste courte (ou « aucune »)
Actions pour le technicien : 1 à 3 actions concrètes
Rappel : ce contrôle est une aide ; l'approbation reste celle du signataire autorisé.

SI C'EST UNE QUESTION : 3 à 6 phrases, avec les identifiants MC-xx / RD-xx cités.

SI L'ANALYSE CONTIENT « HORS BASE » : réponds uniquement
« Information non disponible dans la base MetroCert (exigences ISO/IEC 17025 §7.8,
règles ILAC G8, familles d'instruments, registre des étalons). »

N'ajoute aucune exigence qui ne figure pas dans l'analyse.
```

   USER : `{{#[CHERCHEUR].text#}}` (sortie du nœud CHERCHEUR).

6. Nœud **Fin** : une seule variable de sortie nommée **`rapport`** = `RÉDACTEUR · text`.
7. **Exécuter** (test) avec le certificat incomplet de l'étape D → vérifier le format → **Publier**.
8. Publier → Accéder à la référence API → **Clé API** → + Créer une nouvelle clé secrète → la copier (affichée une seule fois).
9. Capture L2 : base 🟢 + canvas du workflow montrant le nœud Récupération relié au CHERCHEUR.

---

## Étape C — Webhook dans le MVP Lovable (20 min)

Prompt à coller dans Lovable (remplacer uniquement la clé) :

```text
Dans mon MVP MetroCert, ajoute l'agent de contrôle IA à deux endroits.

1. PAGE "NOUVEAU CERTIFICAT" : sous l'aperçu du certificat, ajoute un bouton bleu
   "Contrôler avec l'agent MetroCert 🔎". Au clic, construis un texte à partir de toutes
   les informations de l'aperçu (titre, n°, laboratoire, client, instrument, dates, lieu,
   conditions ambiantes, étalon et n° de certificat, tableau des résultats avec unités,
   U et k, règle de décision, déclaration de conformité, approuvé par) et envoie-le à l'agent.

2. NOUVELLE SECTION "Demander à l'agent" en haut de la page Certificats : un champ texte
   (placeholder "Ex. : quelles mentions pour l'incertitude ? l'étalon ETA-T-02 est-il valide ?")
   et un bouton "Demander à l'agent".

CONNEXION WEBHOOK DIFY (même appel pour les deux) :
URL : https://api.dify.ai/v1/workflows/run
Méthode : POST
Headers :
  Authorization: Bearer [COLLER_LA_CLÉ_API_ICI]
  Content-Type: application/json
Body JSON :
  { "inputs": { "query": texteAEnvoyer },
    "response_mode": "blocking",
    "user": "metrocert-" + Date.now() }

TRAITEMENT DE LA RÉPONSE :
- Succès : afficher response.data.outputs.rapport dans une zone à fond gris clair,
  en conservant les retours à la ligne (white-space: pre-wrap)
- Si response.data.status vaut "failed" : afficher response.data.error en rouge
- Erreur réseau : "Service temporairement indisponible"
- Timeout > 30 s : "La réponse prend trop de temps — réessayez"
- Spinner pendant la requête ; bouton désactivé pendant le chargement

STYLE : cohérent avec le MVP (bleu #1E3A8A). Responsive mobile. Ne modifie rien d'autre.
```

> Timeout porté à 30 s : deux nœuds LLM en série + récupération dépassent souvent 10 s.
> **Sécurité** : la clé sera visible dans le code du navigateur (acceptable pour le prototype, à écrire dans la note d'éthique). Ne jamais la committer dans le dépôt public. Version propre si le temps le permet : « Déplace l'appel Dify dans une fonction serveur Lovable Cloud et stocke la clé en secret `DIFY_API_KEY` ».

Dépannage : 401 → clé mal copiée ou régénérée ; `rapport` undefined → ouvrir F12 → Réseau → réponse, vérifier le nom de la variable de sortie du nœud Fin ; 400 `app_unavailable` → workflow non publié.

---

## Étape D — Tests bout en bout et peer review (20 min)

### Certificat de test incomplet (à coller dans « Demander à l'agent » ou via le formulaire)

```text
CERTIFICAT D'ÉTALONNAGE N° CE-2026-0144
Laboratoire de démonstration MetroCert, Zone industrielle de Mbao, Dakar.
Client : Cimenterie de Rufisque.
Instrument : manomètre à tube de Bourdon, fabricant X, n° de série 18-5521, étendue 0 à 25 bar, classe 1,6.
Date d'étalonnage : 25/09/2026. Date d'émission : 26/09/2026.
Résultats : 0 bar → 0,0 ; 10 bar → 10,2 ; 20 bar → 20,3 ; 25 bar → 25,4.
Incertitude : 0,05.
Instrument déclaré conforme à la classe 1,6.
Prochain étalonnage recommandé : septembre 2027.
Étalon utilisé : ETA-T-02.
```

Anomalies volontaires (ce que l'agent doit trouver) : pas d'unités dans les lectures (MC-12) ; U sans unité ni k (MC-16) ; pas de conditions ambiantes (MC-17) ; étalon sans n° de certificat, **échu** et de la mauvaise famille (température pour un manomètre) (MC-18) ; conformité sans règle de décision (MC-21) ; périodicité recommandée sans accord client (MC-20) ; pas de méthode (MC-06), de lieu (MC-03), de pagination (MC-04), de mention « les résultats ne se rapportent qu'à… » (MC-11) ni de signataire (MC-14).

### Les 3 tests obligatoires (+1)

| # | Entrée dans le MVP | Résultat attendu | Capture |
|---|---|---|:-:|
| T1 | Certificat incomplet ci-dessus | Verdict ⚠️, au moins MC-12, MC-16, MC-17, MC-18, MC-20, MC-21 cités | 📸 |
| T2 | `L'étalon ETA-T-02 peut-il être utilisé aujourd'hui ?` | Non : échu le 31/08/2026 (registre) | 📸 |
| T3 | `Météo demain à Dakar ?` | « Information non disponible dans la base MetroCert… » | 📸 |
| T4 | Aperçu généré avec « Charger un exemple » (manomètre 0–10 bar) | Verdict ✅ ou mentions mineures seulement ; pas de recalcul de U | 📸 |

Grille peer review (5 min/équipe) : réponse pertinente et sourcée (/3) · affichage dans le MVP (/3) · base structurée (/2) · webhook sans erreur console (/2). Noter les 2 feedbacks reçus dans le journal.

### Plan B S6 (obligatoire)

Prompt Lovable à garder prêt :

```text
Ajoute un interrupteur discret "Mode démo" dans le pied de page. Quand il est activé,
le bouton "Contrôler avec l'agent MetroCert" n'appelle pas l'API : il affiche après
1,5 s de spinner le texte enregistré ci-dessous. Ne modifie rien d'autre.
[COLLER ICI LA RÉPONSE RÉELLE OBTENUE AU TEST T1]
```

---

## Journal de prompts S5 (L4 — min. 3 prompts)

| # | Technique | Objet | Résultat observé | Note /5 | Itération |
|---|---|---|---|:-:|---|
| P1 | Prompt système + RAG (`{{#context#}}`) | CHERCHEUR : contrôle MC-01…MC-22 | _à compléter après T1_ | | ex. Top K 3 → 5 si des exigences manquent |
| P2 | Structure imposée (format de sortie) | RÉDACTEUR : rapport de contrôle | _à compléter_ | | |
| P3 | Prompt structuré Lovable | Webhook `workflows/run` + `outputs.rapport` | _à compléter_ | | ex. timeout 10 s → 30 s |
| P4 | Test de cohérence (hors base) | T3 météo | _à compléter_ | | |

Pour chaque prompt : texte exact (copier depuis ce document), résumé de la réponse, note, ce qui a été modifié.

## Note d'éthique RAG (à reprendre en S6)

- **Sources** : la base reformule la norme ; elle ne remplace pas l'exemplaire officiel. Chaque réponse cite l'identifiant MC/RD pour être vérifiable.
- **Données périmées** : le registre des étalons est daté (statut au 29/09/2026). Un registre non mis à jour ferait valider un étalon échu → à terme, le registre doit venir de l'application, pas d'un CSV importé à la main.
- **Confidentialité** : aucun certificat réel de client n'est envoyé à Dify (cloud hors Sénégal) pendant le prototype ; données fictives uniquement.
- **Transparence des limites** : réponse « hors base » imposée ; l'agent n'approuve jamais, il signale.
- **Clé API côté client** : risque d'usage abusif du quota ; fonction serveur prévue en V3.
