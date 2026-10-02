# S5+ — Mise en ligne, tests sur le site public et secours Gemini

> GET 409 · Tutoriel S5+ (modules A, B, D, F) · Équipe MetroCert (I. NKOUNKOU) · 02/10/2026

## Lien public

**https://pixel-perfect-capture-0446.lovable.app** — page de l'agent : [`/verifier-resultat`](https://pixel-perfect-capture-0446.lovable.app/verifier-resultat), carte « Agent IA MetroCert 🔎 ».

- Projet Lovable « Pixel Perfect Pixels », première publication le 02/10/2026 vers 02:15.
- Mise à jour publiée à 03:01 : liste « Dernières décisions » conservée entre deux contrôles.
- Correctif appliqué dans Lovable le 02/10 vers 04:00, **à publier** (Publish → « Publier les modifications ») : liste visible même après une réponse INSUFFISANT, « N° manquant » pour un certificat sans numéro.
- Visibilité : toute personne disposant du lien.

## Tests sur le site public (02/10/2026)

Contrôles espacés d'1 minute (quota Groq gratuit : 8 000 jetons/min, ≈ 5 300 par contrôle).

| Test | Appareil | Entrée | Résultat | Statut |
|---|---|---|---|:-:|
| T3 | PC (~02:20) | « Contrôle le certificat du manomètre. » | `INSUFFISANT : Aucun texte de certificat ou relevé d'étalonnage fourni…`, sans badge ni bouton. Prouve aussi que le secret `DIFY_API_KEY` est présent en production. | ✅ |
| F1 (chemin ⛔) | PC (~02:22 et ~02:25) | « Charger l'exemple » → « Envoyer le tableau à l'agent » → « Contrôler » | VERDICT ⛔ ; Bilan 2 · 11 · 1 · 1 puis 4 · 10 · 2 · 1 (variabilité du modèle, verdict stable) ; badge et compteurs identiques à la ligne Bilan ; « Renvoyer au technicien » présent. | ✅ |
| F1 (chemin ⛔) | **Téléphone Android, Chrome (02:29)** | idem | VERDICT ⛔ ; Bilan 2 · 11 · 1 · 1 ; badge, 4 pastilles, « Renvoyer au technicien » et bloc « Approbation » affichés ; mise en page mobile lisible. | ✅ |
| T7 | PC (03:03) | Exemple du tableau | « Approuver » **désactivé** avec le nom seul ; actif après la case cochée. « Approuvé par Responsable démo le 2 octobre 2026 à 03:03 » ajouté à « Dernières décisions ». | ✅ |
| T8-2 | PC (~03:05) | Entrée de T3 | `INSUFFISANT…` seul, sans badge ni bouton. | ✅ |
| T8 persistance | PC (~03:07) | Nouveau contrôle complet | Nouveau rapport ⛔ et la décision de 03:03 **toujours listée**. | ✅ |
| Rechargement | PC (~03:08) | F5 | Liste vide ; `localStorage` vide ; `sessionStorage` ne contient que la position de défilement du routeur. | ✅ |
| T2 (public) | PC (03:52) | Certificat fictif complet CE-2026-0215, Pt100, étalon ETA-T-02 ([texte](../s6/demo-s6.md#entrée-a--certificat-avec-étalon-échu-t2)) | ⛔ ; Bilan 13 · 0 · 0 · 2 ; 🔎 « ETA-T-02 … statut Échu (échéance 31/08/2026) … [MC-18] » ; prochaine étape « Refaire l'étalonnage avec un étalon valide du registre (ex. ETA-T-05) ». Après approbation : « CE-2026-0215 — Approuvé par… » (pas de doublon « CE-CE- »). | ✅ |

Captures : [T7](captures/T7_F1_verdict_rouge.jpg) · [T8](captures/T8_F1_verdict_vert.jpg) · captures téléphone (02/10, 02:29) à ajouter dans `captures/`.

## Module A — secours Gemini (02/10/2026, 03:48)

- Clé AI Studio créée sur le projet Google Cloud `metrocert`. Une première clé, apparue en clair sur une capture, a été **supprimée et remplacée** (règle §7 du tutoriel).
- Dify → **Intégrations → Fournisseur de Modèle** → carte Gemini (plugin 0.9.10) → autorisation **Gemini_MetroCert**, point vert.
- Workflow **inchangé** : CHERCHEUR et RÉDACTEUR restent sur Groq ; Gemini ne sert qu'en cas de panne.

**Bascule d'urgence (≈ 2 min)** : Studio → MetroCert_ControleCertificat_v1 → nœuds CHERCHEUR puis RÉDACTEUR → Modèle → section Gemini → Flash-Lite le plus récent, température 0,3 → **Publier → Mettre à jour** → rejouer T2, T3 et T5 avant la démo (un autre modèle change le comportement, tutoriel §2.4). Pas de données client réelles avec une clé gratuite.

## Écarts restants (non bloquants)

1. Mobile : les lignes `═══` / `───` du rapport reviennent à la ligne (un caractère isolé). Cosmétique.
2. Variabilité du décompte d'une exécution à l'autre (ex. M15 « personne qui autorise ») : le verdict et l'étalon échu restent stables ; le badge suit toujours la ligne Bilan.

## Check-list de fin de séance (tutoriel S5+ §8)

- [x] Agent Dify sur un modèle avec notre clé, workflow publié (Groq + secours Gemini_MetroCert)
- [x] T1–T6 écrits et réussis après la dernière modification (T2 et T3 rejoués sur le site public)
- [x] 1 fonctionnalité innovante : F1, spec, app, T7–T8 ([module-d-fonctionnalites.md](module-d-fonctionnalites.md))
- [x] Dépôt GitHub à jour, sans aucune clé
- [x] Lien public testé depuis un autre appareil (téléphone Android)
- [x] Journal L4 complété ([../journal-prompts.md](../journal-prompts.md#journal-de-prompts--s5-module-s5))
- [x] Note d'éthique mise à jour ([../s6/note-ethique-s6.md](../s6/note-ethique-s6.md))
- [x] Aucune clé laissée exposée
