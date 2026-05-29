import numpy as np

# Controlla il file readme.md per i dettagli su ciascun sub-task

def prodotto_scalare(v1: list, v2: list) -> float:
    """Sub-task 1: Prodotto Scalare."""
    try:
        a = np.asarray(v1, dtype=float)
        b = np.asarray(v2, dtype=float)

    except Exception as e:
        raise TypeError("I vettori devono contenere valori numerici.") from e

        # Controllo dimensioni
    if a.shape != b.shape:
        raise ValueError("I vettori devono avere la stessa dimensione.")

        # Prodotto scalare
    return float(np.dot(a, b))


def rango_matrice(m: list) -> int:
    """Sub-task 2: Calcola il rango di una matrice."""

    if not m or not isinstance(m, list):
        raise ValueError("La matrice non può essere vuota.")

    try:
        matrice = np.asarray(m, dtype=float)
    except Exception as e:
        raise TypeError(
            "La matrice deve contenere solo valori numerici."
        ) from e

    if matrice.ndim != 2:
        raise ValueError(
            "L'input deve essere una matrice (lista di liste)."
        )

    rango = np.linalg.matrix_rank(matrice)

    return int(rango)



def risolvi_sistema_lineare(A: list, b: list) -> np.ndarray:
    """Sub-task 3: Risolvere un Sistema Lineare."""

    if not A or not b:
        raise ValueError("La matrice A e il vettore b non possono essere vuoti.")

    try:
        matrice = np.asarray(A, dtype=float)
        vettore = np.asarray(b, dtype=float)
    except (TypeError, ValueError) as e:
        raise TypeError(
            "A e b devono contenere solo valori numerici."
        ) from e

    if matrice.ndim != 2:
        raise ValueError("A deve essere una matrice bidimensionale.")

    if vettore.ndim != 1:
        raise ValueError("b deve essere un vettore monodimensionale.")

    righe, colonne = matrice.shape

    if righe != colonne:
        raise ValueError("La matrice A deve essere quadrata.")

    if righe != vettore.shape[0]:
        raise ValueError(
            "Le dimensioni di A e b non sono compatibili."
        )

    try:
        soluzione = np.linalg.solve(matrice, vettore)
    except np.linalg.LinAlgError as e:
        raise ValueError(
            "Il sistema non ha una soluzione unica."
        ) from e

    return soluzione


def correlazione_matrici(m1: list, m2: list) -> np.ndarray:
    """Sub-task 4: Correlazione tra Matrici 2x2."""

    if not m1 or not m2:
        raise ValueError("Le matrici non possono essere vuote.")

    try:
        A = np.asarray(m1, dtype=float)
        B = np.asarray(m2, dtype=float)
    except (TypeError, ValueError) as e:
        raise TypeError(
            "Le matrici devono contenere solo valori numerici."
        ) from e

    if A.shape != (2, 2) or B.shape != (2, 2):
        raise ValueError(
            "Entrambe le matrici devono avere dimensione 2x2."
        )

    v1 = A.ravel()
    v2 = B.ravel()

    return np.corrcoef(v1, v2)


def operazioni_elemento_per_elemento(v1: list) -> tuple:
    """Sub-task 5: Restituisce (seno, coseno, arcoseno, arcocoseno) elemento per elemento calcolati sul primo array."""



def main():
    print("Sub-task 1:", prodotto_scalare([1, 2, 3], [4, 5, 6]))
    print("Sub-task 1:", rango_matrice([[1, 2], [3, 4]]))
    print("Sub-task 3:", risolvi_sistema_lineare([[2, 1], [1, 3]], [5, 7]))
    print("Sub-task 4:", correlazione_matrici([[1, 2], [3, 4]], [[2, 4], [6, 8]]))
    print("Sub-task 5:", operazioni_elemento_per_elemento([0, 0.5, 1, -0.5]))

if __name__ == "__main__":
    main()
