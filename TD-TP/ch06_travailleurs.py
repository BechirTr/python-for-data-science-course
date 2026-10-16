"""Fonction importable par les processus du chapitre 6."""

def somme_carres(n):
    total = 0
    for i in range(n):
        total += i * i
    return total

