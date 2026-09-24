import numpy as np

def cg(A, b, x, tol):
    """Inputs:
    A : Matrix, 2d array size M * M
    b : Vector, 1d array size M
    x : Initial guess vector, 1d array size M
    tol : tolerance, float
    Outputs:
    x : solution vector, 1d array size M
    """
    r = b - A @ x
    p = r.copy()
    rsold = r @ r
    max_iter = len(b)
    for k in range(max_iter):
        if np.sqrt(rsold) < tol:
            break
        Ap = A @ p
        alpha = rsold / (p @ Ap)
        x = x + alpha * p
        r = r - alpha * Ap
        rsnew = r @ r
        beta = rsnew / rsold
        p = r + beta * p
        rsold = rsnew
    return x
