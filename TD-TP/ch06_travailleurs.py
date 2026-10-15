"""Fonction importable par les processus du chapitre 6."""
import numpy as np

def simuler_lot(graine, n_jours=25_000):
    rng_local = np.random.default_rng(graine)
    k = rng_local.binomial(10, 0.2, size=n_jours)
    pertes = int(np.count_nonzero(15 * k - 20 < 0))
    return pertes, n_jours

