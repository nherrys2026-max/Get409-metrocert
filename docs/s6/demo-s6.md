# Démo S6 — évaluation intermédiaire (10 min)

> GET 409 · Équipe MetroCert (I. NKOUNKOU) · préparé le 02/10/2026
> Grille : C1 MVP fonctionnel /4 · C2 architecture agentique /2 · C3 clarté /2.
> Lien : **https://pixel-perfect-capture-0446.lovable.app/verifier-resultat**

## Avant de passer (J-0, 15 min avant)

- [ ] Ouvrir le lien public et la page « Vérifier un résultat » ; ouvrir Dify (workflow MetroCert_ControleCertificat_v1) dans un 2ᵉ onglet ; ouvrir [architecture-v2-1.png](../s5/architecture-v2-1.png) dans un 3ᵉ.
- [ ] Faire **un** contrôle de chauffe (entrée B) ≥ 1 min avant de passer, pour vérifier que Groq répond.
- [ ] Si Groq ne répond pas : bascule Gemini ([s5plus-mise-en-ligne.md](../s5/s5plus-mise-en-ligne.md#module-a--secours-gemini-02102026-0348)) ou plan B ci-dessous.
- [ ] Entrées A et B copiées dans le presse-papiers ou un bloc-notes.
- [ ] Laisser **1 minute** entre deux contrôles (quota Groq gratuit).

## Déroulé

| Temps | Partie | À l'écran | Ce que je dis | Critère |
|---|---|---|---|---|
| 0:00–1:00 | Problème et valeur | Page d'accueil MetroCert | « Au Sénégal, les laboratoires d'étalonnage rédigent leurs certificats à la main, avec un modèle par instrument et par client. Résultat : 2 à 5 jours de délai et des écarts en audit. MetroCert relit le certificat avant signature, pour livrer dans la journée et passer l'audit sans écart lié aux certificats. » | C3 |
| 1:00–3:30 | Fonctionnalité 1 : calcul de conformité ILAC G8 | « Vérifier un résultat » → **Charger l'exemple** → basculer entre « Acceptation simple » et « Zone de garde w = U » | « Le calcul E = lecture − référence et le verdict par point sont faits dans l'application, sans IA, donc vérifiables. À 10 bar, E = 0,10 bar = EMT : conforme en acceptation simple, non conforme avec la zone de garde. » | C1 |
| 3:30–7:00 | Fonctionnalité 2 : agent RAG + circuit de validation (F1) | Coller l'**entrée A** → **Contrôler avec l'agent MetroCert** (≈ 20 s) → montrer 🔎 ETA-T-02 échu [MC-18] → badge rouge et compteurs → **Renvoyer au technicien** (e-mail prérempli, sans destinataire) → **Approuver** grisé, puis nom + case | « L'agent a trouvé dans le registre que l'étalon ETA-T-02 est échu depuis le 31/08/2026 : la traçabilité est rompue, il propose ETA-T-05. Il n'approuve jamais : l'approbation reste un acte humain, nominatif et confirmé. » | C1, C2 |
| 7:00–8:00 | Garde-fou « demander plutôt qu'inventer » | Coller l'**entrée B** (après 1 min) | « Sans certificat, l'agent répond INSUFFISANT au lieu d'inventer. » | C2 |
| 8:00–9:30 | Architecture | [architecture-v2-1.png](../s5/architecture-v2-1.png), puis l'onglet Dify | « Lovable appelle une fonction serveur qui garde la clé Dify. Le workflow fait deux recherches : la base fixe des règles, renvoyée en entier, et la base des instruments. CHERCHEUR, puis nœuds Code qui recalculent le bilan, puis RÉDACTEUR. » | C2 |
| 9:30–10:00 | Éthique et suite | [note-ethique-s6.md](note-ethique-s6.md) | « Données fictives seulement, rien n'est stocké, secours Gemini prêt. Prochaine étape : alerte d'échéance des étalons à 30 jours, puis un pilote contrôlé. » | C3 |

## Entrées à coller

### Entrée A — certificat avec étalon échu (T2)

```text
CERTIFICAT D'ÉTALONNAGE N° CE-2026-0215 — page 1/1
Laboratoire : MetroCert, Zone industrielle de Mbao, Dakar — laboratoire non accrédité
Lieu de l'étalonnage : laboratoire MetroCert
Client : Agro Démo SARL, Rufisque (client fictif)
Instrument : thermomètre à sonde Pt100, fabricant Démo, modèle T-100, n° de série DEMO-0215, résolution 0,01 °C
Méthode : procédure interne PE-T-01 (comparaison en bain thermostaté)
Date d'étalonnage : 25/09/2026 — date d'émission : 26/09/2026
Conditions ambiantes : 22,5 °C ± 1 °C ; 48 %HR
Étalon utilisé : ETA-T-02 (certificat 2025-T-091)
Résultats :
Référence 0,00 °C — lecture 0,05 °C — E = 0,05 °C — U = 0,06 °C (k = 2)
Référence 50,00 °C — lecture 50,08 °C — E = 0,08 °C — U = 0,06 °C (k = 2)
Référence 100,00 °C — lecture 100,12 °C — E = 0,12 °C — U = 0,07 °C (k = 2)
Approuvé par : Responsable technique (démo), signature
```

### Entrée B — entrée incomplète (T3)

```text
Contrôle le certificat du manomètre.
```

## Questions probables du jury

| Question | Réponse courte |
|---|---|
| Que se passe-t-il si l'agent se trompe ? | Il ne signe rien : il liste des points à vérifier, chacun avec sa référence. Le verdict de conformité des mesures est calculé sans IA, et la signature reste celle du responsable technique. |
| Pourquoi deux recherches RAG ? | Avec une seule, les 22 exigences et le registre complet ne remontaient pas : l'étalon échu passait inaperçu. La base fixe est renvoyée en entier à chaque contrôle. |
| Les compteurs changent d'un essai à l'autre ? | Oui, le modèle varie sur certaines mentions (ex. M15). Le verdict et l'étalon échu restent stables, et le bilan est recalculé par un nœud Code. |
| Où sont les données ? | Prototype : données fictives uniquement, rien n'est stocké. En usage réel : anonymisation et offre sans réutilisation des données (note d'éthique). |
| Et si Groq tombe ? | Clé Gemini déjà configurée dans Dify, bascule en 2 minutes ; sinon plan B ci-dessous. |

## Plan B

Si l'agent ne répond pas pendant la démo (quota, réseau) : dire « l'API est indisponible, voici la sortie enregistrée sur le site public le 02/10/2026 » et montrer les réponses ci-dessous ou les captures du dossier [`../s5/captures/`](../s5/captures/). La partie 1 (calcul ILAC G8) fonctionne sans API.

### Réponse enregistrée à l'entrée A (site public, 02/10/2026, 03:52)

```text
RAPPORT DE CONTRÔLE — METROCERT
Complétude ISO/IEC 17025:2017 §7.8
═══════════════════════════════
CERTIFICAT : CE-2026-0215
INSTRUMENT : thermomètre à sonde Pt100, n° de série DEMO-0215
LABORATOIRE : MetroCert
CLIENT : Agro Démo SARL
───────────────────────────────
VERDICT : ⛔ À CORRIGER AVANT APPROBATION
Bilan : 13 présentes · 0 manquantes · 0 à vérifier · 2 non applicables
───────────────────────────────
❌ MENTIONS MANQUANTES
Aucune
───────────────────────────────
⚠️ POINTS À VÉRIFIER
Aucune
───────────────────────────────
🔎 INCOHÉRENCES
1. L'étalon cité (ETA-T-02) apparaît dans le registre des étalons avec le statut Échu (échéance 31/08/2026) → utilisation non conforme à la traçabilité métrologique [MC-18].
───────────────────────────────
✅ MENTIONS PRÉSENTES
M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12, M15
───────────────────────────────
PROCHAINE ÉTAPE
Refaire l'étalonnage avec un étalon valide du registre (ex. ETA-T-05 pour la température) : un étalon échu rompt la traçabilité (MC-18).
───────────────────────────────
Contrôle automatique d'aide à la relecture. Il ne remplace ni la vérification ni la signature du responsable technique.
```

### Réponse enregistrée à l'entrée B (site public, 02/10/2026, 02:20)

```text
INSUFFISANT : Aucun texte de certificat ou relevé d'étalonnage fourni pour effectuer le contrôle.
```

### Réponse enregistrée à « Envoyer le tableau à l'agent » (exemple du manomètre, 02/10/2026, 02:22)

Verdict ⛔ ; Bilan 2 présentes · 11 manquantes · 1 à vérifier · 1 non applicable : le tableau seul ne contient ni numéro de certificat, ni laboratoire, ni client, ni étalon ; M10 « U indiqué sans unité » à vérifier. Prochaine étape : compléter M1 à M8, M11, M12, M15 et préciser l'unité et le facteur k de U.
