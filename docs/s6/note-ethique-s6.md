# Note d'éthique IA — S6

> GET 409 · Équipe MetroCert (I. NKOUNKOU) · Swiss UMEF — Campus de Dakar · 02/10/2026
> Axes demandés en S6 : biais du RAG, confidentialité des données, impact socio-économique ; une ligne par fonctionnalité (tutoriel S5+ §7).

## Contexte

MetroCert aide Mame Diarra, responsable technique d'un laboratoire d'étalonnage à Dakar, à relire ses certificats avant signature. L'agent Dify compare le certificat aux exigences ISO/IEC 17025 §7.8 (MC-01 à MC-22), aux règles de décision ILAC G8 (RD-01 à RD-05) et au registre des étalons. Un certificat engage le laboratoire devant son client et devant l'auditeur d'accréditation : une erreur de l'agent peut laisser sortir un résultat non traçable.

## Risques et garde-fous

| Axe | Risque propre à MetroCert | Garde-fou technique | Garde-fou organisationnel | Preuve |
|---|---|---|---|---|
| **Biais du RAG** | La base ne couvre que 3 familles (pression, masse, température) et une lecture de l'ISO/IEC 17025 §7.8 faite par l'équipe. Pour un pied à coulisse ou un pH-mètre, l'agent peut déclarer « présentes » des mentions sans connaître les exigences de la norme produit. | L'agent cite l'exigence (MC-xx, RD-xx, ETA-xx) pour chaque point ; « Information non disponible » si la base ne répond pas ; badge calculé sur la ligne Bilan, pas par l'IA. | Domaine d'emploi affiché : 3 familles seulement pendant le pilote ; relecture de la base par un métrologue avant chaque nouvelle famille. | T1, T4, test hors base « HICEB2026 » |
| **Référentiel périmé** | Registre des étalons figé au 29/09/2026 : un étalon qui expire après cette date sera vu comme valide. | L'étalon échu est signalé [MC-18] et bloque le verdict ✅ ; fonctionnalité F3 prévue : date du registre affichée et alerte à 30 jours. | Mise à jour mensuelle du registre par le responsable des étalons. | T2 (ETA-T-02 échu, rejoué sur le site public) |
| **Confidentialité** | Un vrai certificat contient le nom du client, les numéros de série et les résultats. Il part vers Dify Cloud puis vers Groq (et Gemini en secours), hors du Sénégal, sur des offres gratuites qui peuvent réutiliser les requêtes (loi 2008-12 sur les données personnelles). | Clé Dify en secret serveur, jamais dans le code ni sur GitHub ; aucune décision stockée (ni navigateur, ni serveur) ; e-mail au technicien sans destinataire imposé. | Prototype : certificats **fictifs uniquement**. Avant usage réel : anonymiser le client avant envoi, offre payante sans réutilisation des données ou Dify auto-hébergé, accord de sous-traitance. | Rechargement : liste vide, `localStorage` vide |
| **Fiabilité et responsabilité (F1)** | Un verdict ✅ erroné, ou l'approbation d'un certificat ⛔ en un clic, ferait signer un certificat non conforme. | Ligne finale fixe « ne remplace ni la vérification ni la signature » ; bilan recalculé par un nœud Code ; « Approuver » exige un nom et, si ⛔, la case « J'ai relu les points signalés et j'assume l'approbation ». | La signature reste celle de la personne autorisée (§7.8.2.1) ; toute approbation d'un ⛔ est justifiée dans le dossier qualité. | T6, T7, T8 |
| **Impact socio-économique** | Gain : relecture plus rapide, livraison dans la journée, accès plus facile à l'accréditation pour les petits laboratoires. Risques : dépendance à des API étrangères gratuites (quota, coupure de compte), déqualification si les techniciens ne relisent plus, exclusion des laboratoires mal connectés. | Secours Gemini prêt (bascule en 2 min) ; l'agent liste les points à corriger au lieu de corriger lui-même ; interface utilisable sur téléphone. | L'outil est présenté comme aide à la relecture, pas comme remplaçant du technicien ; formation courte à la lecture du rapport ; plan B hors ligne pour la démo. | Lien public testé sur Android ; plan B ([demo-s6.md](demo-s6.md#plan-b)) |

## Recommandation

**Pilote contrôlé.** L'agent détecte de façon stable les étalons échus et les mentions manquantes, mais le décompte varie d'un essai à l'autre et le quota gratuit ne tient pas une charge réelle. Pilote proposé : 4 semaines, 3 familles d'instruments, certificats anonymisés, relecture en double. Indicateurs : taux de mentions manquées par l'agent (cible < 5 %), délai d'émission, nombre d'approbations de certificats ⛔.
