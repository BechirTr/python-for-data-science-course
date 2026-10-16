"""Comparer les mêmes sommes en séquentiel et dans deux processus."""
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import get_context
from time import perf_counter
from ch06_travailleurs import somme_carres


def comparer(tailles):
    debut = perf_counter()
    reference = [somme_carres(n) for n in tailles]
    duree_seq = perf_counter() - debut

    debut = perf_counter()
    with ProcessPoolExecutor(
            max_workers=2, mp_context=get_context("spawn")) as pool:
        lots = list(pool.map(somme_carres, tailles))
    duree_processus = perf_counter() - debut

    assert lots == reference
    print("Tailles :", tailles)
    print("Resultats :", lots)
    print("Resultats identiques :", lots == reference)
    print("Secondes, sequentiel :", round(duree_seq, 4))
    print("Secondes, processus :", round(duree_processus, 4))
    print("Les temps incluent le demarrage et les echanges du pool.")


if __name__ == "__main__":
    comparer([4, 5])
    comparer([3_000_000, 4_000_000])
    print("Un gain de temps n'est pas garanti.")
