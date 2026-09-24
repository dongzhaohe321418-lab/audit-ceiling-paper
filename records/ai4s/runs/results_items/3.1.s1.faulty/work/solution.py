import numpy as np

def GS(A, b, eps, x_true, x0):
    """Solve a given linear system Ax=b using Gauss-Seidel iteration
    Input
    A:      N by N matrix, 2D array
    b:      N by 1 right hand side vector, 1D array
    eps:    Float number indicating error tolerance
    x_true: N by 1 true solution vector, 1D array
    x0:     N by 1 initial guess vector, 1D array
    Output
    residual: Float number shows L2 norm of residual (||Ax - b||_2)
    error:    Float number shows L2 norm of error vector (||x-x_true||_2) 
    """
    n = len(b)
    x = x0.copy()
    while True:
        x_prev = x.copy()
        for i in range(n):
            sum_lower = np.dot(A[i, :i], x[:i])
            sum_upper = np.dot(A[i, i + 1:], x_prev[i + 1:])
            x[i] = (b[i] - sum_lower - sum_upper) / A[i, i]
        increment_norm = np.linalg.norm(x - x_prev)
        if increment_norm < eps:
            break
    residual = np.linalg.norm(np.dot(A, x) - b)
    error = np.linalg.norm(x - x_true)
    return (residual, error)
