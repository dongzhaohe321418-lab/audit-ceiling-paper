import numpy as np
import itertools
import scipy.linalg

def ket(dim, *args):
    """Input:
    dim: int or list, dimension of the ket
    args: int or list, the i-th basis vector
    Output:
    out: dim dimensional array of float, the matrix representation of the ket
    """
    if isinstance(dim, int):
        if len(args) == 1:
            j = args[0]
        else:
            j = args
        if isinstance(j, (list, tuple)):
            result = None
            for idx in j:
                basis_vec = np.zeros(dim, dtype=float)
                basis_vec[idx] = 1.0
                if result is None:
                    result = basis_vec
                else:
                    result = np.kron(result, basis_vec)
            return result
        else:
            out = np.zeros(dim, dtype=float)
            out[j] = 1.0
            return out
    elif isinstance(dim, (list, tuple)):
        if len(args) == 1:
            indices = args[0]
        else:
            indices = args
        if not isinstance(indices, (list, tuple)):
            indices = [indices]
        result = None
        for d, j in zip(dim, indices):
            basis_vec = np.zeros(d, dtype=float)
            basis_vec[j] = 1.0
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
    total_dim = 2 ** (2 * rails)
    state = np.zeros((total_dim, total_dim), dtype=np.float64)
    for k in range(rails):
        idx_first = 2 ** k
        idx_second = 2 ** k
        full_index = idx_first * 2 ** rails + idx_second
        ket_vector = ket([2] * (2 * rails), [k, k])
        state += 1.0 / rails * np.outer(ket_vector, ket_vector)
    return state

def tensor(*args):
    """Takes the tensor product of an arbitrary number of matrices/vectors.
    Input:
    args: any number of nd arrays of floats, corresponding to input matrices
    Output:
    M: the tensor product (kronecker product) of input matrices, 2d array of floats
    """
    if len(args) == 0:
        raise ValueError('At least one matrix/vector must be provided')
    result = np.asarray(args[0], dtype=float)
    if result.ndim == 1:
        result = result.reshape(-1, 1)
    for matrix in args[1:]:
        matrix = np.asarray(matrix, dtype=float)
        if matrix.ndim == 1:
            matrix = matrix.reshape(-1, 1)
        result = np.kron(result, matrix)
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
        result = np.zeros_like(rho, dtype=float)
        for Ki in K:
            result += Ki @ rho @ Ki.conj().T
        return result
    if sys is None or dim is None:
        raise ValueError('Both sys and dim must be provided together or both None')
    if not isinstance(sys, list):
        sys = [sys]
    result = np.zeros_like(rho, dtype=float)
    n_subsystems = len(dim)
    for Ki in K:
        ops = []
        for subsys_idx in range(n_subsystems):
            if subsys_idx in sys:
                sys_position = sys.index(subsys_idx)
                ops.append(Ki)
            else:
                ops.append(np.eye(dim[subsys_idx], dtype=float))
        Ki_full = tensor(*ops)
        result += Ki_full @ rho @ Ki_full.conj().T
    return result

def generalized_amplitude_damping_channel(gamma, N):
    """Generates the generalized amplitude damping channel.
    Inputs:
    gamma: float, damping parameter
    N: float, thermal parameter
    Output:
    kraus: list of Kraus operators as 2x2 arrays of floats, [A1, A2, A3, A4]
    """
    ket_0 = np.array([[1.0], [0.0]])
    ket_1 = np.array([[0.0], [1.0]])
    P_0 = ket_0 @ ket_0.conj().T
    P_1 = ket_1 @ ket_1.conj().T
    P_01 = ket_0 @ ket_1.conj().T
    P_10 = ket_1 @ ket_0.conj().T
    K_1 = np.sqrt(1 - N) * (P_0 + np.sqrt(1 - gamma) * P_1)
    K_2 = np.sqrt(gamma * (1 - N)) * P_01
    K_3 = np.sqrt(N) * (np.sqrt(1 - gamma) * P_0 + P_1)
    K_4 = np.sqrt(gamma * N) * P_10
    kraus = [K_1, K_2, K_3, K_4]
    return kraus

def output_state(rails, gamma_1, N_1, gamma_2, N_2):
    """Inputs:
    rails: int, number of rails
    gamma_1: float, damping parameter of the first channel
    N_1: float, thermal parameter of the first channel
    gamma_2: float, damping parameter of the second channel
    N_2: float, thermal parameter of the second channel
    Output
    state: 2**(2*rails) x 2**(2*rails) dimensional array of floats, the output state
    """
    rho = multi_rail_encoding_state(rails)
    K_1 = generalized_amplitude_damping_channel(gamma_1, N_1)
    K_2 = generalized_amplitude_damping_channel(gamma_2, N_2)
    dim = [2] * (2 * rails)
    sys_1 = list(range(rails))
    rho = apply_channel(K_1, rho, sys=sys_1, dim=dim)
    sys_2 = list(range(rails, 2 * rails))
    state = apply_channel(K_2, rho, sys=sys_2, dim=dim)
    return state

def measurement(rails):
    """Returns the measurement projector
    Input:
    rails: int, number of rails
    Output:
    global_proj: ( 2**(2*rails), 2**(2*rails) ) dimensional array of floats
    """
    total_dim = 2 ** (2 * rails)
    receiver_dim = 2 ** rails
    receiver_proj = np.zeros((receiver_dim, receiver_dim), dtype=float)
    for k in range(rails):
        state_idx = 2 ** k
        basis_vec = np.zeros(receiver_dim, dtype=float)
        basis_vec[state_idx] = 1.0
        receiver_proj += np.outer(basis_vec, basis_vec)
    global_proj = np.kron(receiver_proj, receiver_proj)
    return global_proj

def syspermute(X, perm, dim):
    """Permutes order of subsystems in the multipartite operator X.
    Inputs:
    X: 2d array of floats with equal dimensions, the density matrix of the state
    perm: list of int containing the desired order
    dim: list of int containing the dimensions of all subsystems.
    Output:
    Y: 2d array of floats with equal dimensions, the density matrix of the permuted state
    """
    total_dim = np.prod(dim)
    total_dim = int(total_dim)
    Y = np.zeros_like(X, dtype=float)
    ranges = [range(d) for d in dim]
    for row_indices in itertools.product(*ranges):
        for col_indices in itertools.product(*ranges):
            row_idx_original = 0
            col_idx_original = 0
            multiplier = 1
            for i in range(len(dim) - 1, -1, -1):
                row_idx_original += row_indices[i] * multiplier
                col_idx_original += col_indices[i] * multiplier
                multiplier *= dim[i]
            row_indices_permuted = tuple((row_indices[perm[i]] for i in range(len(perm))))
            col_indices_permuted = tuple((col_indices[perm[i]] for i in range(len(perm))))
            permuted_dims = [dim[perm[i]] for i in range(len(perm))]
            row_idx_permuted = 0
            col_idx_permuted = 0
            multiplier = 1
            for i in range(len(permuted_dims) - 1, -1, -1):
                row_idx_permuted += row_indices_permuted[i] * multiplier
                col_idx_permuted += col_indices_permuted[i] * multiplier
                multiplier *= permuted_dims[i]
            Y[row_idx_permuted, col_idx_permuted] = X[row_idx_original, col_idx_original]
    return Y

def partial_trace(X, sys, dim):
    """Inputs:
    X: 2d array of floats with equal dimensions, the density matrix of the state
    sys: list of int containing systems over which to take the partial trace (i.e., the systems to discard).
    dim: list of int containing dimensions of all subsystems.
    Output:
    2d array of floats with equal dimensions, density matrix after partial trace.
    """
    if not isinstance(sys, list):
        sys = [sys]
    n_subsystems = len(dim)
    keep_sys = [i for i in range(n_subsystems) if i not in sys]
    if len(keep_sys) == n_subsystems:
        return X.copy()
    if len(keep_sys) == 0:
        return np.array([[np.trace(X)]], dtype=float)
    perm = keep_sys + sys
    X_perm = syspermute(X, perm, dim)
    dim_perm = [dim[perm[i]] for i in range(len(perm))]
    kept_dim = [dim[i] for i in keep_sys]
    traced_dim = [dim[i] for i in sys]
    kept_total_dim = int(np.prod(kept_dim))
    traced_total_dim = int(np.prod(traced_dim))
    X_reshaped = X_perm.reshape((kept_total_dim, traced_total_dim, kept_total_dim, traced_total_dim))
    result = np.zeros((kept_total_dim, kept_total_dim), dtype=float)
    for i in range(traced_total_dim):
        result += X_reshaped[:, i, :, i]
    return result

def entropy(rho):
    """Inputs:
    rho: 2d array of floats with equal dimensions, the density matrix of the state
    Output:
    en: quantum (von Neumann) entropy of the state rho, float
    """
    eigenvalues = np.linalg.eigvalsh(rho)
    eigenvalues = np.real(eigenvalues)
    eigenvalues = eigenvalues[eigenvalues > 1e-15]
    en = -np.sum(eigenvalues * np.log2(eigenvalues))
    return float(en)
