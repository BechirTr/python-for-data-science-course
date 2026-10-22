"""Corrections des exercices et problèmes Python des chapitres 1 à 4."""


# Exercice 1 : Comprendre un filtrage de caractères
texte = "banane"
resultat = ""
trace_1 = []
for lettre in texte:
    if lettre != "a":
        resultat = resultat + lettre
    trace_1.append((lettre, lettre != "a", resultat))
print(resultat)
print(trace_1)

assert resultat == "bnne" and len(trace_1) == 6


# Exercice 2 : Comprendre une copie superficielle
a = [[1], [2]]
b = a.copy()
b[0].append(3)
b.append([4])
print(a)
print(b)

assert a == [[1,3],[2]] and b == [[1,3],[2],[4]]
assert a is not b and a[0] is b[0]


# Exercice 3 : Suivre une fonction et sa variable locale
def total_pairs(valeurs):
    total = 0
    for valeur in valeurs:
        if valeur % 2 == 0:
            total += valeur
    return total

total = 100
r = total_pairs([2, 3, 4])
print(r, total)

assert r == 6 and total == 100
assert total_pairs([]) == 0


# Exercice 4 : Tracer une recherche dichotomique
def chercher(valeurs, cible):
    gauche, droite = 0, len(valeurs) - 1
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        if valeurs[milieu] == cible:
            return milieu
        if valeurs[milieu] < cible:
            gauche = milieu + 1
        else:
            droite = milieu - 1
    return -1
print(chercher([1,4,7,10,13,16,19],13))

assert chercher([],3) == -1
assert chercher([1,4,7,10,13,16,19],13) == 4
assert chercher([1,4,7],6) == -1


# Exercice 5 : Comprendre l’héritage et le polymorphisme
class Tarif:
    def __init__(self, prix):
        self.prix = prix
    def montant(self):
        return self.prix

class Reduit(Tarif):
    def montant(self):
        return self.prix / 2

resultats = [t.montant() for t in [Tarif(12), Reduit(12)]]
print(*resultats, sep="\n")

assert resultats == [12, 6.0]
assert Reduit(8).prix == 8


# Exercice 6 : Corriger une recherche du dernier indice
def dernier_indice(valeurs, cible):
    indice = -1
    for i in range(len(valeurs)):
        if valeurs[i] == cible:
            indice = i
    return indice
print(dernier_indice([4,2,4],4))

assert dernier_indice([],4) == -1
assert dernier_indice([1,2],4) == -1
assert dernier_indice([4,2,4],4) == 2


# Exercice 7 : Corriger un dictionnaire de fréquences
def frequences(texte):
    compte = {}
    for lettre in texte:
        if lettre in compte:
            compte[lettre] += 1
        else:
            compte[lettre] = 1
    return compte
print(frequences("aba"))

assert frequences("") == {}
assert frequences("aba") == {"a":2,"b":1}
assert frequences("aaaa") == {"a":4}


# Exercice 8 : Corriger une propriété et sa validation
class Batterie:
    def __init__(self, capacite):
        self.capacite = capacite
    @property
    def capacite(self):
        return self._capacite
    @capacite.setter
    def capacite(self, valeur):
        if valeur < 0:
            raise ValueError("capacite negative")
        self._capacite = valeur

batterie = Batterie(10)
batterie.capacite = 5
print(batterie.capacite)

assert Batterie(0).capacite == 0
try:
    Batterie(-1)
    raise AssertionError("validation absente")
except ValueError:
    pass
try:
    batterie.capacite = -2
    raise AssertionError("validation absente")
except ValueError:
    pass
assert batterie.capacite == 5


# Problème 1 : Regrouper les répétitions consécutives
def compresser(texte):
    if texte == "":
        return []
    sortie = []
    caractere, nombre = texte[0], 1
    for i in range(1, len(texte)):
        if texte[i] == caractere:
            nombre += 1
        else:
            sortie.append((caractere, nombre))
            caractere, nombre = texte[i], 1
    sortie.append((caractere, nombre))
    return sortie

assert compresser("") == []
assert compresser("aaabbca") == [("a",3),("b",2),("c",1),("a",1)]
assert compresser("aabb") == [("a",2),("b",2)]
assert compresser("abc") == [("a",1),("b",1),("c",1)]
assert compresser("Aaa") == [("A",1),("a",2)]


# Problème 2 : La plus longue série de jours positifs
def plus_longue_serie(bilans):
    courante = 0
    meilleure = 0
    for valeur in bilans:
        if valeur > 0:
            courante += 1
            if courante > meilleure:
                meilleure = courante
        else:
            courante = 0
    return meilleure

assert plus_longue_serie([]) == 0
assert plus_longue_serie([-1,0]) == 0
assert plus_longue_serie([1,2,3]) == 3
assert plus_longue_serie([2,1,0,3,4,5,-1,2]) == 3


# Problème 3 : Fusionner deux relevés déjà triés
def fusionner(gauche, droite):
    i, j = 0, 0
    sortie = []
    while i < len(gauche) and j < len(droite):
        if gauche[i] <= droite[j]:
            sortie.append(gauche[i])
            i += 1
        else:
            sortie.append(droite[j])
            j += 1
    while i < len(gauche):
        sortie.append(gauche[i])
        i += 1
    while j < len(droite):
        sortie.append(droite[j])
        j += 1
    return sortie

assert fusionner([],[]) == []
assert fusionner([],[2]) == [2]
assert fusionner([1,4,4],[2,4,6]) == [1,2,4,4,4,6]
assert fusionner([-2,3],[-1,3]) == [-2,-1,3,3]


# Problème 4 : Quels postes reçoivent le message ?
def accessibles(graphe, depart):
    if depart not in graphe:
        return []
    a_traiter = [depart]
    vus = {depart}
    i = 0
    while i < len(a_traiter):
        sommet = a_traiter[i]
        for voisin in graphe[sommet]:
            if voisin not in vus:
                vus.add(voisin)
                a_traiter.append(voisin)
        i += 1
    return a_traiter

graphe = {"A":["B","C"],"B":["D"],"C":["D"],
          "D":["B"],"E":["F"],"F":[]}
assert accessibles(graphe,"A") == ["A","B","C","D"]
assert accessibles(graphe,"E") == ["E","F"]
assert accessibles(graphe,"absent") == []
assert accessibles({"A":["A"]},"A") == ["A"]


# Problème 5 : Concevoir un petit stock de matériel
class Stock:
    def __init__(self):
        self._quantites = {}
    def disponible(self, article):
        return self._quantites.get(article, 0)
    def ajouter(self, article, quantite):
        if quantite <= 0:
            raise ValueError("quantite non positive")
        self._quantites[article] = self.disponible(article) + quantite
    def retirer(self, article, quantite):
        if quantite <= 0:
            raise ValueError("quantite non positive")
        if self.disponible(article) < quantite:
            return False
        self._quantites[article] = self.disponible(article) - quantite
        return True

s1, s2 = Stock(), Stock()
assert s1.disponible("cable") == 0
s1.ajouter("cable",3)
assert s1.retirer("cable",2) is True
assert s1.disponible("cable") == 1
assert s1.retirer("cable",2) is False
assert s1.disponible("cable") == 1 and s2.disponible("cable") == 0
assert s1.retirer("inconnu",1) is False
for q in [0,-1]:
    try:
        s1.ajouter("cable",q)
        raise AssertionError("validation absente")
    except ValueError:
        pass
    try:
        s1.retirer("cable",q)
        raise AssertionError("validation absente")
    except ValueError:
        pass
assert s1.disponible("cable") == 1


print("Tous les cas de vérification ont réussi.")
