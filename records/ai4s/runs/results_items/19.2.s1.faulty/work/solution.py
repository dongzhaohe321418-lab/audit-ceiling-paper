import numpy as np
from scipy.linalg import sqrtm

def tensor(*args):
    """Takes the tensor product of an arbitrary number of matrices/vectors.
    Input:
    args: any number of arrays, corresponding to input matrices
    Output:
    M: the tensor product (kronecker product) of input matrices
    """
    if len(args) == 0:
        raise ValueError('At least one matrix/vector must be provided')
    arrays = [np.asarray(arg) for arg in args]
    result = arrays[0]
    for i in range(1, len(arrays)):
        result = np.kron(result, arrays[i])
    return result

def n_tangle(psi):
    """Returns the n_tangle of pure state psi
    Input:
    psi: 1d array of floats, the vector representation of the state
    Output:
    tangle: float, the n-tangle of psi
    """
    psi = np.asarray(psi, dtype=complex)
    dim = len(psi)
    n = int(np.log2(dim))
    sigma_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sigma_y_tensor = sigma_y
    for _ in range(n - 1):
        sigma_y_tensor = np.kron(sigma_y_tensor, sigma_y)
    psi_conj = np.conj(psi)
    applied_state = sigma_y_tensor @ psi_conj
    inner_product = np.dot(psi, applied_state)
    tangle = np.abs(inner_product) ** 2
    return float(tangle)
