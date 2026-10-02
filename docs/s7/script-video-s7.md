# S7 — Script de la vidéo teaser MetroCert (60–75 s)

> GET 409 · Séance 7 · Template « Mon script vidéo teaser » · Équipe MetroCert (I. NKOUNKOU) · Groupe : _à compléter_
> Livrable : MP4 · 16:9 · 1080p · **60 à 90 s** · sous-titres obligatoires. Workflow : script → prompts Kling AI → clips → montage CapCut → export.

## Étape 1 — Script en 4 actes

Rythme de la voix off : environ 2,3 mots par seconde, soit 30 à 35 mots par acte de 15 s.

| Acte | Temps | Visuel | Voix off (texte exact) | Ton |
|---|---|---|---|---|
| **1. Le problème** | 0–15 s | Bureau de laboratoire le soir, une responsable technique relit seule une pile de certificats papier, lampe de bureau, horloge qui tourne. | « Un certificat d'étalonnage, c'est jusqu'à vingt-deux mentions obligatoires selon l'ISO/IEC 17025. À Dakar, beaucoup sont encore relus à la main, le soir. Une mention oubliée, un étalon échu… et c'est l'écart d'audit. » | Urgence |
| **2. La solution** | 15–30 s | Captures du MVP : page « Vérifier un résultat », clic sur « Charger l'exemple », pastilles Conforme / Non conforme, bascule acceptation simple ↔ zone de garde. | « MetroCert transforme les relevés en verdict de conformité selon la règle de décision ILAC G8, en un clic, sans ressaisie. Le calcul est fait par l'application : il est vérifiable. » | Clarté |
| **3. L'agent IA** | 30–45 s | Capture : certificat collé, clic « Contrôler avec l'agent MetroCert », rapport qui apparaît, zoom sur « ETA-T-02 … Échu [MC-18] », badge rouge « À corriger avant approbation ». | « Notre agent IA relit le certificat en vingt secondes. Il compare chaque mention aux exigences et au registre des étalons, et repère ici un étalon échu. Il ne signe jamais : l'approbation reste humaine. » | Précision |
| **4. Impact + appel à l'action** | 45–60 s | Schéma d'architecture V2.1, puis écran final : logo MetroCert, URL, QR code vers le site. | « Objectif : livrer le client dans la journée et passer l'audit sans écart lié aux certificats. MetroCert, la relecture de vos certificats, en un clic. Essayez-le : pixel-perfect-capture-0446 point lovable point app. » | Conviction |

Durée cible : 60 s. Marge possible jusqu'à 75 s en allongeant la démo de l'acte 3 ; ne jamais dépasser 90 s.

Les chiffres cités viennent du projet : 22 exigences MC-01 à MC-22 (base `MetroCert_Regles_v1`, ISO/IEC 17025 §7.8), 20 s de réponse de l'agent mesurée sur le site public, ETA-T-02 échu au 31/08/2026 dans le registre fictif. Aucune statistique externe n'est citée : en ajouter une seulement avec sa source affichée à l'écran.

## Étape 2 — Prompts Kling AI (en anglais, 5 s, 16:9)

Formule : lieu + lumière · sujet + action · style · 5 s · 16:9. Générer 2 variantes par acte.

| Acte | Prompt A | Prompt B |
|---|---|---|
| 1 | `Small calibration laboratory office in Dakar at night, warm desk lamp light, a West African woman quality manager in a lab coat reviewing a stack of paper calibration certificates, pressure gauges and thermometers on the shelf behind her, wall clock showing 9 pm, cinematic, shallow depth of field, 5 seconds, 16:9` | `Close-up of hands flipping through paper calibration certificates with stamps and signatures, a red pen circling a missing field, dim office light, cinematic realistic style, slow push-in, 5 seconds, 16:9` |
| 2 | `Bright modern calibration laboratory, technician placing a pressure gauge on a test bench, laptop screen showing a clean web app with green and red status badges, soft daylight, realistic documentary style, 5 seconds, 16:9` | `Over-the-shoulder shot of a laptop in a lab, a web table of measurement results turning green check by check, blue and white interface, soft focus background with instruments, modern tech style, 5 seconds, 16:9` |
| 3 | `Abstract visualization of an AI reading a document: lines of text scanned by a soft blue light, one line highlighted in red with a warning icon, dark navy background with subtle glow, futuristic but clean tech style, 5 seconds, 16:9` | `Quality manager in a lab coat looking at a laptop, red warning badge on screen, she nods and types her name to approve, warm office light, realistic cinematic style, 5 seconds, 16:9` |
| 4 | `Calibration laboratory team in Dakar handing a sealed certificate to a smiling industrial client at the door, golden hour light, documentary style, 5 seconds, 16:9` | `Clean end card animation: navy blue background, a ruler icon and the word MetroCert appearing, subtle light sweep, minimal corporate motion design, 5 seconds, 16:9` |

Précautions : les clips Kling sont des illustrations, à mêler aux **vraies captures du MVP** (actes 2 et 3), qui montrent le produit réel. Ne pas faire générer de faux écrans de l'application.

**Plan B si Kling est lent** : captures d'écran du site public (dossier `docs/s5/captures/` et captures plein écran à faire en 1920 × 1080), images libres Pexels ou Unsplash pour l'acte 1, écran final fait dans Canva ou CapCut.

## Étape 3–4 — Montage CapCut

1. Importer dans l'ordre : acte 1 (Kling) → acte 2 (captures MVP) → acte 3 (capture du rapport + clip Kling) → acte 4 (schéma, puis écran final).
2. Voix off : enregistrer le texte ci-dessus (téléphone ou micro CapCut), caler chaque phrase sur son acte.
3. Sous-titres automatiques, puis **corriger à la main** : MetroCert · ISO/IEC 17025 · ILAC G8 · ETA-T-02 · MC-18 · Dakar · lovable.app.
4. Musique libre de droits de la bibliothèque CapCut, volume 20 à 30 % sous la voix.
5. Écran final : URL lisible au moins 3 s et QR code vers https://pixel-perfect-capture-0446.lovable.app.

## Étape 5 — Export et dépôt

- [ ] MP4, 1080p, 16:9 paysage
- [ ] Durée entre 60 et 90 s (cible 60–75 s)
- [ ] Sous-titres présents et vérifiés
- [ ] Voix off audible et synchronisée
- [ ] Aucune donnée réelle de client ni clé API visible à l'écran
- [ ] Upload Google Drive, lien « toute personne disposant du lien », dépôt e-Academy (livrable L2)
