"""Corrigés de l'atelier sur les chapitres 1 à 4.

Les exemples suivent les diapositives : lecture, recherche, club, zéros,
doublons, anagrammes, salles et parking.
Les distances et les tickets correspondent aux compléments au choix.
Aucun module externe n'est nécessaire.
"""

# compter_e
def compter_e(texte):
    total = 0
    for lettre in texte:
        if lettre == 'e':
            total = total + 1
    return total


# contient
def contient(valeurs, cible):
    for valeur in valeurs:
        if valeur == cible:
            return True
    return False


# resume_lettres
def resume_lettres(texte):
    ordre, comptes = ([], {})
    for lettre in texte:
        if lettre != ' ':
            if lettre not in comptes:
                ordre.append(lettre)
            comptes[lettre] = comptes.get(lettre, 0) + 1
    return (ordre, comptes)


# chercher
def chercher(valeurs, cible):
    for i in range(len(valeurs)):
        if valeurs[i] == cible:
            return i
    return None


# club
class Club:

    def __init__(self, limite):
        self.membres = []
        self.limite = limite

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, valeur):
        if valeur < 1:
            raise ValueError('limite invalide')
        self._limite = valeur


# zeros_a_la_fin
def zeros_a_la_fin(valeurs):
    resultat = []
    nb_zeros = 0
    for nombre in valeurs:
        if nombre == 0:
            nb_zeros = nb_zeros + 1
        else:
            resultat.append(nombre)
    for i in range(nb_zeros):
        resultat.append(0)
    return resultat


# doublon_liste
def a_un_doublon_liste(valeurs):
    vus = []
    for nombre in valeurs:
        if nombre in vus:
            return True
        vus.append(nombre)
    return False


# a_un_doublon
def a_un_doublon(valeurs):
    vus = set()
    for nombre in valeurs:
        if nombre in vus:
            return True
        vus.add(nombre)
    return False


# anagrammes
def anagrammes(s, t):
    if len(s) != len(t):
        return False
    reserve = {}
    for lettre in s:
        reserve[lettre] = reserve.get(lettre, 0) + 1
    for lettre in t:
        if reserve.get(lettre, 0) == 0:
            return False
        reserve[lettre] -= 1
    return True


# plan
plan = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D'], 'D': ['B', 'C', 'E'], 'E': ['D'], 'F': []}


# parcourir
def parcourir(plan, depart):
    a_visiter = [depart]
    position = 0
    vus = {depart}
    while position < len(a_visiter):
        salle = a_visiter[position]
        position = position + 1
        for voisine in plan[salle]:
            if voisine not in vus:
                vus.add(voisine)
                a_visiter.append(voisine)
    return a_visiter


# distances_depuis
def distances_depuis(plan, depart):
    a_visiter = [depart]
    position = 0
    distances = {depart: 0}
    while position < len(a_visiter):
        salle = a_visiter[position]
        position = position + 1
        for voisine in plan[salle]:
            if voisine not in distances:
                distances[voisine] = distances[salle] + 1
                a_visiter.append(voisine)
    return distances


# parking
class Parking:

    def __init__(self, capacite):
        self.capacite = capacite
        self.occupes = 0

    @property
    def places_libres(self):
        return self.capacite - self.occupes

    def entrer(self):
        if self.occupes == self.capacite:
            return False
        self.occupes = self.occupes + 1
        return True

    def sortir(self):
        if self.occupes == 0:
            return False
        self.occupes = self.occupes - 1
        return True


# ticket
class Ticket:

    def prix(self, heures):
        return 2 * heures


# ticket_gratuit
class TicketGratuit(Ticket):

    def prix(self, heures):
        return 0

# Variante de l'exercice de lecture : compter une lettre choisie.
def compter(texte, cible):
    total = 0
    for lettre in texte:
        if lettre == cible:
            total = total + 1
    return total


if __name__ == "__main__":
    print("Zéros :", zeros_a_la_fin([0, 3, 0, 1, 2]))
    print("Doublon :", a_un_doublon([4, 2, 4]))
    print("Anagrammes :", anagrammes("gare", "rage"))
    print("Parcours :", parcourir(plan, "A"))
    print("Distances :", distances_depuis(plan, "A"))
    parking = Parking(2)
    print("Entrée :", parking.entrer())
    print("Places libres :", parking.places_libres)
