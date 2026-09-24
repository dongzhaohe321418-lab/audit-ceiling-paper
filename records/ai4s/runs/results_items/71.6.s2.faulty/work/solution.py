import numpy as np 
from scipy.optimize import fminbound
import itertools
from scipy.linalg import logm

def ket(dim, *args):
    """Input:
    dim: int or list, dimension of the ket
    *args: int or list, the indices of the basis vectors to create
    Output:
    out: array of float, the matrix representation of the ket (tensor product of basis vectors)
    """
    if isinstance(dim, int):
        if len(args) == 0:
            raise ValueError('Must provide basis vector index')
        if len(args) == 1 and isinstance(args[0], int):
            j = args[0]
            if j >= dim or j < 0:
                raise ValueError(f'Index {j} out of range for dimension {dim}')
            out = np.zeros(dim)
            out[j] = 1.0
            return out
        elif len(args) == 1 and isinstance(args[0], list):
            indices = args[0]
            out = np.array([1.0])
            for j in indices:
                if j >= dim or j < 0:
                    raise ValueError(f'Index {j} out of range for dimension {dim}')
                basis_vec = np.zeros(dim)
                basis_vec[j] = 1.0
                out = np.kron(out, basis_vec)
            return out
        else:
            raise ValueError('Invalid arguments')
    elif isinstance(dim, list):
        if len(args) == 0:
            raise ValueError('Must provide basis vector indices')
        indices = args[0] if isinstance(args[0], list) else args
        if len(indices) != len(dim):
            raise ValueError('Number of indices must match number of dimensions')
        out = np.array([1.0])
        for d, j in zip(dim, indices):
            if j >= d or j < 0:
                raise ValueError(f'Index {j} out of range for dimension {d}')
            basis_vec = np.zeros(d)
            basis_vec[j] = 1.0
            out = np.kron(out, basis_vec)
        return out
    else:
        raise ValueError('dim must be int or list')

def tensor(*args):
    """Takes the tensor product of an arbitrary number of matrices/vectors.
    Input:
    *args: any number of nd arrays of floats, corresponding to input matrices/vectors
    Output:
    M: the tensor product (kronecker product) of input matrices, 2d array of floats
    """
    if len(args) == 0:
        raise ValueError('Must provide at least one matrix/vector')
    result = np.array(args[0], dtype=float)
    for matrix in args[1:]:
        matrix = np.array(matrix, dtype=float)
        result = np.kron(result, matrix)
    if result.ndim == 1:
        result = result.reshape(-1, 1)
    return result

def apply_channel(K, rho, sys=None, dim=None):
    """Applies the channel with Kraus operators in K to the state rho on
    systems specified by the list sys. The dimensions of the subsystems of
    rho are given by dim.
    Inputs:
    K: list of 2d array of floats, list of Kraus operators
    rho: 2d array of floats, input density matrix
    sys: list of int or None, list of subsystems to apply the channel, None means full system
    dim: list of int or None, list of dimensions of each subsystem, None means full system
    Output:
    matrix: output density matrix of floats
    """
    if sys is None and dim is None:
        output = np.zeros_like(rho, dtype=complex)
        for k in K:
            output += k @ rho @ k.conj().T
        return np.real(output) if np.allclose(output.imag, 0) else output
    if sys is None or dim is None:
        raise ValueError('Both sys and dim must be provided or both must be None')
    if not isinstance(sys, list):
        sys = [sys]
    if not isinstance(dim, list):
        dim = [dim]
    output = np.zeros_like(rho, dtype=complex)
    for k in K:
        full_op = None
        for i, d in enumerate(dim):
            if i in sys:
                if full_op is None:
                    full_op = k
                else:
                    full_op = np.kron(full_op, k)
            else:
                identity = np.eye(d)
                if full_op is None:
                    full_op = identity
                else:
                    full_op = np.kron(full_op, identity)
        output += full_op @ rho @ full_op.conj().T
    return np.real(output) if np.allclose(output.imag, 0) else output

def syspermute(X, perm, dim):
    """Permutes order of subsystems in the multipartite operator X.
    Inputs:
    X: 2d array of floats with equal dimensions, the density matrix of the state
    perm: list of int containing the desired order
    dim: list of int containing the dimensions of all subsystems.
    Output:
    Y: 2d array of floats with equal dimensions, the density matrix of the permuted state
    """
    X = np.asarray(X, dtype=complex)
    dim = np.asarray(dim, dtype=int)
    perm = np.asarray(perm, dtype=int)
    total_dim = int(np.prod(dim))
    perm_indices = np.zeros(total_dim, dtype=int)
    for idx in range(total_dim):
        multi_idx = np.unravel_index(idx, dim)
        permuted_multi_idx = tuple((multi_idx[i] for i in perm))
        permuted_dim = dim[perm]
        new_idx = np.ravel_multi_index(permuted_multi_idx, permuted_dim)
        perm_indices[idx] = new_idx
    Y = np.zeros_like(X, dtype=complex)
    for i in range(total_dim):
        for j in range(total_dim):
            new_i = perm_indices[i]
            new_j = perm_indices[j]
            Y[new_i, new_j] = X[i, j]
    if np.allclose(Y.imag, 0):
        return np.real(Y)
    return Y

def partial_trace(X, sys, dim):
    """Inputs:
    X: 2d array of floats with equal dimensions, the density matrix of the state
    sys: list of int containing systems over which to take the partial trace (i.e., the systems to discard).
    dim: list of int containing dimensions of all subsystems.
    Output:
    2d array of floats with equal dimensions, density matrix after partial trace.
    """
    X = np.asarray(X, dtype=complex)
    dim = np.asarray(dim, dtype=int)
    if isinstance(sys, int):
        sys = [sys]
    sys = sorted(set(sys))
    all_systems = set(range(len(dim)))
    keep_sys = sorted(list(all_systems - set(sys)))
    perm = keep_sys + sys
    X_perm = syspermute(X, perm, dim)
    dim_perm = dim[perm]
    dim_keep = dim_perm[:len(keep_sys)]
    dim_trace = dim_perm[len(keep_sys):]
    total_keep_dim = int(np.prod(dim_keep)) if len(dim_keep) > 0 else 1
    total_trace_dim = int(np.prod(dim_trace)) if len(dim_trace) > 0 else 1
    shape_reshaped = tuple(dim_keep) + tuple(dim_trace) + tuple(dim_keep) + tuple(dim_trace)
    X_reshaped = X_perm.reshape(shape_reshaped)
    n_keep = len(dim_keep)
    n_trace = len(dim_trace)
    axes_perm = list(range(n_keep)) + list(range(n_keep + n_trace, 2 * n_keep + n_trace)) + list(range(n_keep, n_keep + n_trace)) + list(range(2 * n_keep + n_trace, 2 * n_keep + 2 * n_trace))
    X_reordered = np.transpose(X_reshaped, axes_perm)
    X_reordered = X_reordered.reshape(total_keep_dim, total_keep_dim, total_trace_dim, total_trace_dim)
    result = np.zeros((total_keep_dim, total_keep_dim), dtype=complex)
    for i in range(total_trace_dim):
        result += X_reordered[:, :, i, i]
    if np.allclose(result.imag, 0):
        return np.real(result)
    return result

def entropy(rho):
    """Inputs:
    rho: 2d array of floats with equal dimensions, the density matrix of the state
    Output:
    en: quantum (von Neumann) entropy of the state rho, float
    """
    rho = np.asarray(rho, dtype=complex)
    eigenvalues = np.linalg.eigvalsh(rho)
    eigenvalues = np.real(eigenvalues)
    eigenvalues = eigenvalues[eigenvalues > 1e-15]
    en = -np.sum(eigenvalues * np.log2(eigenvalues))
    return en
