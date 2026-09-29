# S4 — MVP V1 MetroCert avec Lovable.dev

> Séance 4 / 8 · Outil : lovable.dev · Livrables L1 (MVP en ligne, 35 pts), L2 (projet Lovable public + README, 25 pts), L3 (journal de prompts, 25 pts), L4 (captures + note d'itération, 15 pts).
> Dépôt au plus tard 48 h après la séance sur e-Academy.

## 0. Ce que le MVP V1 doit démontrer

Un seul parcours, celui du persona Mame Diarra : **relevés saisis une fois → erreurs calculées → déclaration de conformité selon une règle de décision → aperçu d'un certificat qui contient les mentions ISO/IEC 17025 §7.8**.

| Règle des 3 C | Ce que ça veut dire pour MetroCert V1 |
|---|---|
| Correct | Erreur = lecture − valeur de référence ; incertitude élargie U (k = 2) **saisie** par le technicien depuis son budget (l'app ne l'invente pas) ; règle de décision affichée |
| Complet | 4 pages navigables, 2 fonctionnalités testables (saisie + calcul/conformité ; liste filtrable des certificats) |
| Convaincant | Données réalistes d'un labo de Dakar (manomètre, balance, thermomètre), écriture SI (virgule décimale, espace avant l'unité) |

Hors périmètre V1 : génération PDF réelle, QR code, authentification, calcul automatique du budget d'incertitude (V2/V3). L'agent Dify arrive en S5.

---

## 1. Prompt d'initialisation (E1 / S1 personnalisé) — à coller dans Lovable

```text
Crée une application web complète appelée MetroCert.

CONTEXTE :
MetroCert est une plateforme pour les laboratoires d'étalonnage au Sénégal (zone UEMOA).
Aujourd'hui, les techniciens recopient leurs relevés de mesure du carnet vers Excel puis vers
un modèle Word différent pour chaque type d'instrument et chaque client. MetroCert permet de
saisir les relevés une seule fois et d'obtenir l'aperçu d'un certificat d'étalonnage conforme
à la norme ISO/IEC 17025:2017, pour livrer le client dans la journée.

PAGES À CRÉER (4 pages, navigation fixe en haut) :

1. ACCUEIL
   - Header : logo (emoji 📏) + nom "MetroCert" + sous-titre "Certificats d'étalonnage ISO/IEC 17025"
   - Hero : titre "Des relevés au certificat, sans ressaisie", sous-titre sur la livraison
     dans la journée, 2 boutons : "Nouveau certificat" et "Voir les certificats"
   - 3 chiffres clés : "150 certificats / mois", "3 familles d'instruments", "0 ressaisie"
   - Footer : "Prototype pédagogique GET 409 — données fictives", contact

2. NOUVEAU CERTIFICAT (formulaire en 4 blocs)
   - Bloc Client : société, adresse
   - Bloc Instrument : famille (liste : Pression — manomètre / Masse — balance /
     Température — thermomètre), fabricant, modèle, n° de série, étendue, résolution, unité
   - Bloc Conditions : température ambiante (°C), humidité relative (%), étalon utilisé
     (identifiant + n° de certificat d'étalonnage de l'étalon), date d'étalonnage
   - Bloc Relevés : tableau de 5 lignes éditables avec colonnes
     "Valeur de référence", "Lecture instrument", "Erreur" (calculée = lecture − référence),
     "U (k = 2)" (saisie manuelle), "EMT" (saisie manuelle, facultative)
   - Choix de la règle de décision (boutons radio) :
     "Aucune déclaration de conformité" / "Acceptation simple : |E| ≤ EMT" /
     "Zone de garde w = U : |E| + U ≤ EMT"
   - Pour chaque ligne, badge "Conforme" (vert) ou "Non conforme" (rouge) selon la règle
     choisie ; pas de badge si "Aucune déclaration"
   - Bouton "Aperçu du certificat" qui affiche en dessous un aperçu structuré avec :
     titre "Certificat d'étalonnage", n° unique au format CE-2026-0001, laboratoire
     (Laboratoire de démonstration, Dakar), client, identification de l'instrument,
     date d'étalonnage et date d'émission, lieu de réalisation, conditions ambiantes,
     tableau des résultats avec unités et U (k = 2, niveau de confiance d'environ 95 %),
     déclaration de traçabilité métrologique (étalon + n° de certificat),
     règle de décision appliquée, mention "Les résultats ne se rapportent qu'à
     l'instrument étalonné", zone "Approuvé par" (nom + fonction)

3. CERTIFICATS
   - Liste des 5 certificats d'exemple sous forme de cartes : n°, client, instrument,
     famille, date, statut (Émis / À approuver / Brouillon)
   - Filtres : par famille (Toutes / Pression / Masse / Température) et par statut
   - Barre de recherche par client ou n° de série

4. CONTACT
   - Formulaire : nom, e-mail, laboratoire, message ; bouton "Envoyer"
   - Adresse : Zone industrielle de Mbao, Dakar, Sénégal (fictive)

DESIGN :
- Couleur principale : #1E3A8A (bleu métrologie) ; accent : #0EA5E9 ; succès #16A34A ;
  erreur #DC2626 ; fond blanc et gris très clair #F8FAFC
- Police : Inter ; style sobre, professionnel, type application de laboratoire
- Nombres au format français : virgule décimale et espace avant l'unité (ex. 2,02 bar)
- Responsive mobile first (breakpoint 768 px) : les tableaux défilent horizontalement sur mobile

DONNÉES D'EXEMPLE (page Certificats) :
1. CE-2026-0141 │ SAR – raffinerie │ Manomètre 0–10 bar classe 1,0 │ Pression │ 22/09/2026 │ Émis
2. CE-2026-0142 │ Laiterie du Cap-Vert │ Balance 220 g, résolution 0,1 mg │ Masse │ 23/09/2026 │ Émis
3. CE-2026-0143 │ Pharmacie Nationale d'Approvisionnement │ Thermomètre −20 à 150 °C │ Température │ 24/09/2026 │ À approuver
4. CE-2026-0144 │ Cimenterie de Rufisque │ Manomètre 0–25 bar classe 1,6 │ Pression │ 25/09/2026 │ Brouillon
5. CE-2026-0145 │ Industries Chimiques du Sénégal │ Balance 30 kg, résolution 1 g │ Masse │ 26/09/2026 │ À approuver

PRÉ-REMPLISSAGE du formulaire "Nouveau certificat" (bouton "Charger un exemple") :
Manomètre 0–10 bar classe 1,0, résolution 0,05 bar, étalon "Manomètre numérique ETA-P-03,
certificat n° 2026-P-117". Conditions 22,5 °C / 48 %.
Relevés (référence → lecture, U = 0,012 bar, EMT = 0,10 bar) :
0,00 → 0,00 ; 2,50 → 2,55 ; 5,00 → 5,05 ; 7,50 → 7,60 ; 10,00 → 10,10

Stack : React + Tailwind CSS + Vite. Pas de base de données pour l'instant : données en mémoire.
```

**Contrôle métrologique du jeu d'exemple** (pour vérifier ce que Lovable calcule) — manomètre classe 1,0 sur 0–10 bar : EMT = 1,0 % de l'étendue = 0,10 bar (classe de précision EN 837-1 exprimée en % de l'étendue de mesure).

| Réf. (bar) | Lecture (bar) | E (bar) | U (bar) | Accept. simple \|E\| ≤ 0,10 | Zone de garde \|E\| + U ≤ 0,10 |
|---:|---:|---:|---:|:-:|:-:|
| 0,00 | 0,00 | 0,00 | 0,012 | Conforme | Conforme |
| 2,50 | 2,55 | 0,05 | 0,012 | Conforme | Conforme |
| 5,00 | 5,05 | 0,05 | 0,012 | Conforme | Conforme |
| 7,50 | 7,60 | 0,10 | 0,012 | Conforme | **Non conforme** (0,112 > 0,10) |
| 10,00 | 10,10 | 0,10 | 0,012 | Conforme | **Non conforme** |

Le point 7,50 bar est choisi exprès : il montre au jury que la règle de décision change la déclaration (ILAC G8:09/2019, ISO/IEC 17025 §7.8.6). C'est la meilleure démo de 30 secondes du MVP.

---

## 2. Prompts d'itération (1 prompt = 1 modification)

### I1 — Correction visuelle (format des nombres)

```text
Dans la page Nouveau certificat et dans l'aperçu du certificat, tous les nombres doivent
être affichés au format français : virgule décimale, et une espace insécable entre la valeur
et l'unité (ex. "2,55 bar", "22,5 °C"). Affiche l'erreur avec le même nombre de décimales
que la lecture. Ne modifie rien d'autre.
```

### I2 — Ajout de fonctionnalité (Few-Shot, sur le modèle du filtre existant)

```text
Sur la page Certificats, j'ai déjà un filtre par famille qui fonctionne
(Toutes / Pression / Masse / Température). Ajoute de la même façon, sur la page
Nouveau certificat, un contrôle de complétude avant l'aperçu :
quand on clique "Aperçu du certificat", si l'un de ces champs est vide — client, n° de série,
étalon, n° de certificat de l'étalon, température ambiante, date d'étalonnage, au moins une
ligne de relevés, U d'au moins une ligne — affiche un encadré orange "Mentions manquantes"
qui liste les champs vides, et n'affiche pas l'aperçu. Même style que les badges existants.
```

### I3 — Responsive mobile

```text
Sur mobile (écran < 768 px) : 1) le menu devient un menu hamburger ☰ en overlay ;
2) le tableau des relevés défile horizontalement au lieu de déborder ;
3) les boutons "Aperçu du certificat" et "Charger un exemple" prennent toute la largeur.
Ne modifie pas l'affichage desktop.
```

### Débogage (E3) — si besoin

```text
Le build a échoué avec cette erreur : [COLLER L'ERREUR DE LA CONSOLE]
Identifie la cause, corrige uniquement le fichier concerné et explique en 2 phrases ce qui
était incorrect. Ne modifie aucun autre fichier.
```

---

## 3. Publication (L1 + L2)

1. Tester la preview : 4 pages, bouton « Charger un exemple », changer la règle de décision et vérifier le point 7,50 bar, filtre de la page Certificats.
2. **Publish** (haut droite) → URL `https://metrocert-[xxx].lovable.app` → la tester sur 2 navigateurs + un vrai smartphone.
3. Projet Lovable en **Public** ; connecter GitHub depuis Lovable → dépôt `GET409-MetroCert-MVP` **public** (le dépôt actuel `Get409-metrocert` reste celui de la documentation).
4. Reporter les deux URL dans le README du dépôt et dans le formulaire e-Academy.
5. Captures : desktop (F12 → Ctrl+Shift+P → « Capture full size screenshot ») et mobile (DevTools → icône smartphone), de préférence sur l'aperçu montrant le point 7,50 bar « Non conforme ».

---

## 4. Journal de prompts S4 (L3 — min. 4 prompts)

> À compléter après exécution : la colonne « Résultat observé » et la note doivent décrire ce que Lovable a réellement produit.

| # | Technique | Prompt | Résultat attendu | Résultat observé | Note /5 |
|---|---|---|---|---|:-:|
| P1 | Prompt structuré (6 sections) | Initialisation §1 | 4 pages, formulaire en 4 blocs, calcul de E, badges selon la règle | _à compléter_ | |
| P2 | Correctif ciblé | I1 format des nombres | Virgule décimale et espace avant l'unité partout | _à compléter_ | |
| P3 | Few-Shot | I2 contrôle de complétude | Encadré « Mentions manquantes » bloquant l'aperçu | _à compléter_ | |
| P4 | Correctif ciblé | I3 responsive | Hamburger, tableau défilant, boutons pleine largeur | _à compléter_ | |

Grille d'analyse de chaque prompt : ce qui a marché · ce qui a été mal interprété · ce qu'on a changé dans le prompt suivant.

---

## 5. Note d'itération (L4 — ½ page, brouillon à ajuster)

> **Ce que nous avons changé et pourquoi.** La génération initiale a produit les quatre pages, mais [décrire l'écart constaté, ex. nombres au format anglais]. Or un certificat d'étalonnage doit exprimer les résultats avec leurs unités de façon non ambiguë (ISO/IEC 17025 §7.8.2.1 m) : nous avons donc imposé la virgule décimale et l'écriture SI (I1). Nous avons ensuite ajouté un contrôle de complétude (I2), parce que la peur n° 1 de notre persona est l'écart d'audit dû à une mention manquante : l'aperçu est bloqué tant que l'étalon, son certificat ou les conditions ambiantes ne sont pas renseignés. Enfin, 70 % des utilisateurs au Sénégal sont sur smartphone et les techniciens saisissent parfois sur site : nous avons rendu le tableau des relevés utilisable sur mobile (I3).
>
> **Choix de conception assumé.** Le MVP ne calcule pas l'incertitude : U est saisie depuis le budget validé du laboratoire. Un calcul d'incertitude généré par une IA ne serait ni vérifiable ni défendable en audit ; la V2 intégrera des budgets déterministes par famille.
>
> **Ce qui reste difficile.** [ex. Lovable réécrit parfois le formulaire entier quand on demande un petit changement → un prompt = une modification.]

---

## 6. Points d'éthique à reprendre dans la note (S4 · S5 prompt)

| Axe | Risque concret MetroCert | Garde-fou V1 |
|---|---|---|
| Accessibilité | Saisie sur site en 3G instable | Pages légères, pas d'images lourdes ; hors ligne prévu en V2 |
| Biais / représentation | Seulement 3 familles → les labos BTP (force) ou pharma (volume) exclus | Afficher clairement le périmètre ; familles ajoutables par modèle |
| Données | Formulaire Contact + noms de clients industriels | Données fictives dans le prototype ; mention de consentement sur le formulaire |
| Responsabilité | Un certificat « généré » perçu comme validé | Zone « Approuvé par » obligatoire : la décision reste humaine |
