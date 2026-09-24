import numpy as np
import itertools
import scipy.linalg

def ket(j, dim):
    """Input:
    j: int or list, the index/indices of the basis vector(s)
    dim: int or list, dimension(s) of the ket
    Output:
    out: numpy array of float, the matrix representation of the ket
    """
    if isinstance(j, int):
        if isinstance(dim, int):
            out = np.zeros(dim)
            out[j] = 1.0
            return out
        else:
            j = [j]
    if isinstance(dim, int):
        dims = [dim] * len(j)
    else:
        dims = dim
    result = None
    for idx, dim_i in zip(j, dims):
        basis_vec = np.zeros(dim_i)
        basis_vec[idx] = 1.0
        if result is None:
            result = basis_vec
        else:
            result = np.kron(result, basis_vec)
    return result

def multi_rail_encoding_state(rails):
    """Returns the density matrix of the multi-rail encoding state
    Input:
    rails: int, number of rails
    Output:
    state: 2**(2*rails) x 2**(2*rails) dimensional array of numpy.float64 type
    """
    m = rails
    total_dim = 2 ** (2 * rails)
    state_vector = np.zeros(total_dim, dtype=np.float64)
    for k in range(m):
        ket_A = ket(k, 2 ** rails)
        ket_B = ket(k, 2 ** rails)
        combined_state = np.kron(ket_A, ket_B)
        state_vector += combined_state
    state_vector = state_vector / np.sqrt(m)
    density_matrix = np.outer(state_vector, state_vector.conj())
    return density_matrix

def tensor(*args):
    """Takes the tensor product of an arbitrary number of matrices/vectors.
    Input:
    args: any number of nd arrays of floats, corresponding to input matrices
    Output:
    M: the tensor product (kronecker product) of input matrices, 2d array of floats
    """
    if len(args) == 0:
        return np.array([[1.0]])
    result = args[0]
    for matrix in args[1:]:
        result = np.kron(result, matrix)
    return result
