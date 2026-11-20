# SMS Spam Collection

**Attribution :** Almeida, T. et Hidalgo, J. (2011). *SMS Spam Collection*. UCI Machine Learning Repository. [DOI 10.24432/C5CC84](https://doi.org/10.24432/C5CC84).

- Page du jeu de données : https://archive.ics.uci.edu/dataset/228/sms+spam+collection
- Archive originale : https://archive.ics.uci.edu/static/public/228/sms+spam+collection.zip
- Licence indiquée par UCI : **Creative Commons Attribution 4.0 International (CC BY 4.0)**.
- Licence : https://creativecommons.org/licenses/by/4.0/
- Récupération : 19 novembre 2026.

## Fichiers conservés

**SMSSpamCollection** est le fichier original, sans modification. Chaque ligne contient une étiquette ham ou spam, une tabulation, puis le texte du SMS.

SHA-256 :

    7d039a24a6083ed9ef0f806ebad56bbb976e3aeb8de05669173bfdc4996c239d

**UCI_Readme.txt** est la notice extraite de l’archive originale, renommée sans changer son contenu. Elle est encodée en Latin-1. Le fichier des SMS est lu en UTF-8.

## Audit reproductible et transformations

Le fichier fourni contient **5 574 messages**, soit 4 827 ham et 747 spam. Les comptes annoncés sur certaines descriptions peuvent différer légèrement ; le notebook compte les lignes du fichier réellement utilisé.

Le notebook construit une clé de contrôle en passant le texte en minuscules, en ramenant les suites d’espaces à un espace et en retirant les espaces de début et de fin. Il vérifie les étiquettes contradictoires, n’en trouve aucune, puis conserve la première occurrence de chaque clé.

- Répétitions selon cette règle : **415**.
- Textes conservés : **5 159**.
- Ham conservés : **4 517**.
- Spam conservés : **642**.

Cette clé sert à dédupliquer et à vérifier les séparations. **Le texte original est l’entrée du modèle.** Le fichier source livré n’est pas réécrit.

## Population et limites

Le corpus rassemble des SMS en anglais provenant de plusieurs sources, notamment de contributions d’étudiants. Il est ancien, contient des étiquettes de corpus et ne fournit pas de dates ni d’identifiants de conversation ou d’expéditeur.

Le partage stratifié évalue une généralisation à des textes réservés de ce corpus, après la déduplication décrite. Il ne suffit pas à évaluer une généralisation à des campagnes nouvelles ou à des SMS français récents. Les textes proches qui ne deviennent pas identiques avec cette normalisation peuvent subsister.

Le notebook affiche quelques extraits tronqués du corpus pour analyser des erreurs, en masquant les suites d’au moins cinq chiffres. Les quatre SMS utilisés pour la démonstration finale ont été rédigés pour le cours ; ils n’ont pas servi à l’entraînement ni à l’évaluation chiffrée.
