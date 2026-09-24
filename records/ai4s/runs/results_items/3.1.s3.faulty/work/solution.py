import numpy as np

def GS(A, b, eps, x_true, x0):
    """Solve a given linear system Ax=b using Gauss-Seidel iteration
    Input
    A:      N by N matrix, 2D array
    b:      N by 1 right hand side vector, 1D array
    eps:    Float number indicating error tolerance
    x_true: N by 1 true solution vector, 1D array
    x0:     N by 1 zero vector, 1D array
    Output
    residual: Float number shows L2 norm of residual (||Ax - b||_2)
    error:    Float number shows L2 norm of error vector (||x-x_true||_2) 
    """
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    x_true = np.array(x_true, dtype=float)
    x = np.array(x0, dtype=float)
    n = len(b)
    while True:
        x_old = x.copy()
        for i in range(n):
            sum_lower = np.dot(A[i, :i], x[:i])
            sum_upper = np.dot(A[i, i + 1:], x_old[i + 1:])
            x[i] = (b[i] - sum_lower - sum_upper) / A[i, i]
        increment_norm = np.linalg.norm(x - x_old)
        if increment_norm < eps:
            break
    residual = np.linalg.norm(np.dot(A, x) - b)
    error = np.linalg.norm(x - x_true)
    return (residual, error)
