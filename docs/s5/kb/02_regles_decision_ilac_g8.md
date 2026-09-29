# MetroCert KB — Règles de décision et déclaration de conformité (ILAC G8:09/2019, ISO/IEC 17025 §7.8.6)

Source : ILAC G8:09/2019 « Guidelines on Decision Rules and Statements of Conformity » et ISO/IEC 17025:2017 §7.1.3 et §7.8.6. Reformulation de travail MetroCert, à vérifier sur les documents officiels. Version de la base : v1, septembre 2026.

Notations : E = erreur de l'instrument (lecture − valeur de référence) ; U = incertitude élargie (k = 2) ; EMT = erreur maximale tolérée (limite de tolérance) ; w = largeur de la zone de garde.

## RD-01 — Acceptation simple (w = 0)
Conforme si |E| ≤ EMT, non conforme sinon. L'incertitude n'intervient pas dans la décision. Le risque de fausse acceptation peut atteindre 50 % quand E est proche de la limite. Acceptable seulement si le client l'a accepté et si U est petite devant l'EMT. Mots-clés : acceptation simple, règle simple, sans zone de garde.

## RD-02 — Zone de garde w = U (règle binaire)
Conforme si |E| + U ≤ EMT, non conforme sinon. Le risque de fausse acceptation est au plus d'environ 2,5 % (hypothèse de loi normale, k = 2). Mots-clés : zone de garde, bande de garde, guard band, w = U, risque 2,5 %.

## RD-03 — Règle non binaire (4 zones)
Avec w = U : conforme si |E| + U ≤ EMT ; conformité conditionnelle (« conforme, non prouvé ») si |E| ≤ EMT < |E| + U ; non-conformité conditionnelle si |E| − U ≤ EMT < |E| ; non conforme si |E| − U > EMT. Mots-clés : non binaire, conditionnel, indéterminé, pass conditionnel.

## RD-04 — Ce que le certificat doit indiquer
La règle appliquée, les résultats auxquels la déclaration s'applique et la spécification utilisée (EMT, classe de précision, tolérance client, référence de la norme produit). La règle doit être convenue avec le client avant l'étalonnage (revue de la demande, §7.1.3). Mots-clés : règle de décision convenue, revue de contrat, spécification.

## RD-05 — Rapport U / EMT
Lorsque U n'est pas petite devant l'EMT (rapport U/EMT supérieur à environ 1/3 à 1/4 selon les pratiques), une zone de garde réduit fortement la zone d'acceptation : signaler au client que la méthode ou l'étalon est peut-être insuffisant pour la déclaration demandée. Mots-clés : TUR, rapport d'incertitude, capabilité.

## Exemple chiffré (manomètre 0–10 bar, classe 1,0, EMT = 0,10 bar, U = 0,012 bar)
- Point 5,00 bar, lecture 5,05 bar : E = 0,05 bar ; |E| + U = 0,062 bar ≤ 0,10 bar : conforme avec RD-01 et RD-02.
- Point 7,50 bar, lecture 7,60 bar : E = 0,10 bar ; conforme avec RD-01 (|E| = EMT) ; non conforme avec RD-02 (|E| + U = 0,112 bar > 0,10 bar) ; conformité conditionnelle avec RD-03.
