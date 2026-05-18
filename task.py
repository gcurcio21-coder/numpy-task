import numpy as np

# Controlla il file readme.md per i dettagli su ciascun sub-task

def prodotto_scalare(v1: list, v2: list) -> float:
    """Sub-task 1: Prodotto Scalare."""
    pass

def operazioni_elemento_per_elemento(v1: list, v2: list) -> tuple:
    """Sub-task 2: Operazioni Elemento per Elemento."""
    pass

def prodotto_matriciale(m1: list, m2: list) -> np.ndarray:
    """Sub-task 3: Prodotto Matriciale."""
    pass

def risolvi_sistema_lineare(A: list, b: list) -> np.ndarray:
    """Sub-task 4: Risolvere un Sistema Lineare."""
    pass

def correlazione_matrici(m1: list, m2: list) -> float:
    """Sub-task 5: Correlazione tra Matrici 2x2."""
    pass

def main():
    print("Sub-task 1:", prodotto_scalare([1, 2, 3], [4, 5, 6]))
    print("Sub-task 2:", operazioni_elemento_per_elemento([1, 2, 3], [4, 5, 6]))
    print("Sub-task 3:", prodotto_matriciale([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
    print("Sub-task 4:", risolvi_sistema_lineare([[2, 1], [1, 3]], [5, 7]))
    print("Sub-task 5:", correlazione_matrici([[1, 2], [3, 4]], [[2, 4], [6, 8]]))

if __name__ == "__main__":
    main()
