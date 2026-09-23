# HMW définitif — MetroCert

> GET 409 · Séance 2 · Décision d'équipe — ce HMW guide le projet jusqu'à la soutenance.

## HMW S1 (validé en séance 1)

> « Comment pourrions-nous permettre aux techniciens et responsables de laboratoires d'étalonnage de générer, pour n'importe quel instrument et n'importe quelle société cliente, un certificat d'étalonnage conforme à l'ISO/IEC 17025 en quelques minutes, afin de supprimer les erreurs de recopie et de livrer leurs clients plus rapidement ? »

## HMW définitif S2

> **« Comment pourrions-nous permettre aux responsables techniques de laboratoires d'étalonnage au Sénégal, comme Mame Diarra, qui jonglent avec un modèle de certificat différent par famille d'instruments et par client, de passer des relevés de mesure à un certificat conforme à l'ISO/IEC 17025 sans aucune ressaisie, afin de livrer leurs clients dans la journée et de passer leurs audits d'accréditation sans écart lié aux certificats ? »**

**Lecture en 4 blocs** (pour le pitch oral) :

| Qui | Dans quelle situation | Quoi | Pour quel résultat |
|---|---|---|---|
| Les responsables techniques de labos d'étalonnage au Sénégal, comme Mame Diarra | Un modèle de certificat différent par famille d'instruments et par client | Passer des relevés à un certificat conforme ISO/IEC 17025 **sans aucune ressaisie** | Livrer **dans la journée** (au lieu de 2 à 5 jours) et **zéro écart d'audit** lié aux certificats |

---

## Ce qui change par rapport à S1

| Critère | HMW S1 | HMW définitif S2 | Pourquoi |
|---|---|---|---|
| **Utilisateur** | « les techniciens **et** responsables de laboratoires » | « les **responsables techniques** de laboratoires d'étalonnage **au Sénégal, comme Mame Diarra** » | Un seul utilisateur principal, celui qui porte la frustration et signe les certificats. Le technicien reste un utilisateur secondaire. Le contexte géographique est nommé. |
| **Périmètre** | « **n'importe quel** instrument et **n'importe quelle** société » | « qui jonglent avec **un modèle différent par famille d'instruments et par client** » | « N'importe quel… » rendait le HMW trop large (critère « sauver le monde »). On nomme la **cause observée** du problème. |
| **Solution implicite** | « **générer** un certificat » (suggère déjà un générateur) | « **passer des relevés de mesure à un certificat** […] **sans aucune ressaisie** » | On décrit le besoin (supprimer la ressaisie), pas l'outil. Un générateur n'est qu'une des réponses possibles. |
| **Mesure du succès** | « en quelques minutes », « plus rapidement » (vague) | « **dans la journée** » | Ancré sur le délai réel observé (2 à 5 jours) : un objectif crédible et mesurable. |
| **Bénéfice** | Supprimer les erreurs de recopie + livrer plus vite | + « **passer leurs audits d'accréditation sans écart lié aux certificats** » | Le HMW 2 de la S1 (conformité des mentions) est intégré : c'est la peur n° 1 du persona (« toute la série est remise en question »). |

## Test des critères de validation (slide 8 — S2)

| Critère | Résultat | Justification |
|---|:-:|---|
| Désigne un utilisateur réel au Sénégal | ✅ OUI | Responsables techniques de labos d'étalonnage (Dakar, zone de Mbao) |
| Décrit une vraie frustration | ✅ OUI | Ressaisie carnet → Excel → Word, 2 à 5 jours de délai, peur de l'écart d'audit. *À confirmer par 2 entretiens.* |
| Assez large pour plusieurs solutions | ✅ OUI | 3 pistes ci-dessous |
| Assez précis (pas « sauver le monde ») | ✅ OUI | 1 profil, 1 cause (multiplicité des modèles), 2 résultats mesurables |
| Contient déjà une solution | ✅ NON | Ni application, ni générateur, ni IA dans l'énoncé |
| Formulable par n'importe quelle équipe | ✅ NON | Vocabulaire et contraintes propres à la métrologie (ISO/IEC 17025, relevés, audit d'accréditation) |

## Actionnable : au moins 3 solutions possibles

1. **Application web/mobile de saisie unique** qui calcule l'incertitude et produit le PDF (piste retenue — voir [`vpc.md`](vpc.md)).
2. **Classeur Excel maître verrouillé** par famille, avec publipostage vers un modèle unique habillé par client.
3. **Service de rédaction mutualisé** : les relevés sont envoyés à une cellule qui émet les certificats pour plusieurs labos.

## Ce que ce HMW guide en S3

La priorité du MVP : **une saisie unique des relevés pour 3 familles (balance, manomètre, thermomètre), qui produit un PDF contenant toutes les mentions §7.8**. L'agent Dify de contrôle de complétude vérifie les mentions avant l'approbation humaine. Le succès se mesure au délai saisie → PDF et au nombre de mentions manquantes détectées.

---

## Pitch HMW — 2 minutes

| Temps | Bloc | Texte |
|---|---|---|
| 20 s | Secteur & persona | « Nous travaillons sur la métrologie industrielle au Sénégal. Mame Diarra, 38 ans, dirige techniquement un laboratoire d'étalonnage privé à Mbao : 4 techniciens, environ 150 certificats par mois pour l'agroalimentaire, le pétrole, les mines ou la pharmacie. » |
| 30 s | Problème | « Chaque relevé est recopié trois fois : du carnet à Excel, puis d'Excel à Word, dans un modèle différent pour chaque instrument et chaque client. Résultat : 2 à 5 jours de délai, des erreurs, et une peur permanente de l'audit. Comme elle dit : "Mesurer, on sait faire. Ce qui nous tue, c'est la paperasse autour de la mesure." » |
| 30 s | HMW | « Comment pourrions-nous permettre aux responsables techniques de laboratoires d'étalonnage au Sénégal, comme Mame Diarra, qui jonglent avec un modèle de certificat différent par famille d'instruments et par client, de passer des relevés de mesure à un certificat conforme à l'ISO/IEC 17025 sans aucune ressaisie, afin de livrer leurs clients dans la journée et de passer leurs audits sans écart lié aux certificats ? » |
| 40 s | Solution V0 | « MetroCert : les relevés sont saisis une seule fois, même hors connexion sur site. Le calcul d'incertitude est automatique et vérifiable. Le PDF sort aux couleurs de chaque client, avec toutes les mentions exigées et un QR code. Un agent IA vérifie les mentions avant la signature humaine, et un étalon expiré bloque la saisie. Démo S6 : balance, manomètre et thermomètre. » |
