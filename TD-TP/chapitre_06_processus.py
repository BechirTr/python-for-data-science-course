"""Comparer les mêmes quatre lots en séquentiel et avec deux processus."""
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import get_context
from time import perf_counter
import numpy as np
from ch06_travailleurs import simuler_lot

if __name__ == "__main__":
    graines = np.random.SeedSequence(2026).spawn(4)
    debut = perf_counter()
    reference = [simuler_lot(graine) for graine in graines]
    duree_seq = perf_counter() - debut

    debut = perf_counter()
    with ProcessPoolExecutor(
            max_workers=2, mp_context=get_context("spawn")) as pool:
        lots = list(pool.map(simuler_lot, graines))
    duree_processus = perf_counter() - debut

    assert lots == reference
    pertes = sum(lot[0] for lot in lots)
    total = sum(lot[1] for lot in lots)
    print("Lots identiques :", lots == reference)
    print("Pertes / jours :", pertes, total)
    print("Frequence :", pertes / total)
    print("Secondes, sequentiel :", round(duree_seq, 4))
    print("Secondes, processus :", round(duree_processus, 4))
    print("Les temps incluent le demarrage et les echanges du pool.")
