# Données fictives du chapitre 7

- commandes_ch07.csv : 26 lignes d’export. Une commande concerne un seul produit. id identifie la commande, date est une date civile, client et produit sont des références, quantite compte les articles, remise_pct est un pourcentage. Une remise vide signifie zéro dans ce fichier. L’export complet couvre le 1 au 12 septembre 2026. Le 6 septembre est un jour sans commande.
- produits_ch07.csv : une ligne par code produit. prix et cout sont des euros par article. Trois produits : cahier, gourde et lampe.
- clients_ch07.csv : une ligne par client et sa ville. Les villes ne définissent aucune population réelle.
- livraisons_ch07.csv : 40 clients distincts, une livraison par client, deux méthodes fictivement affectées au hasard. delai est en minutes. Les observations sont supposées indépendantes pour l’exercice.
- energie_ch07.csv : 40 journées fictives. temperature_prevue est en degrés Celsius, heures_prevues en heures et conso_kwh en kWh. Les deux premières variables sont supposées disponibles avant la journée. La cible ne l’est qu’après. Les 30 premières journées servent à apprendre, les dix suivantes à évaluer.

Les erreurs intentionnelles du fichier de commandes permettent d’étudier les contrôles. Le notebook conserve les rejets et la référence produit inconnue. Aucun montant réel n’est extrapolé à partir de ces données.
