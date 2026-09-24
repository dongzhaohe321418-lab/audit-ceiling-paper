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
    if sys is None or dim is None:
        matrix = np.zeros_like(rho, dtype=np.float64)
        for K_i in K:
            matrix += K_i @ rho @ K_i.conj().T
        return matrix
    matrix = np.zeros_like(rho, dtype=np.float64)
    for K_i in K:
        ops_per_subsystem = []
        for subsys_idx in range(len(dim)):
            if subsys_idx in sys:
                ops_per_subsystem.append(K_i)
            else:
                ops_per_subsystem.append(np.eye(dim[subsys_idx], dtype=np.float64))
        full_K = tensor(*ops_per_subsystem)
        matrix += full_K @ rho @ full_K.conj().T
    return matrix

def generalized_amplitude_damping_channel(gamma, N):
    """Generates the generalized amplitude damping channel.
    Inputs:
    gamma: float, damping parameter (0 <= gamma <= 1)
    N: float, thermal parameter (0 <= N <= 1)
    Output:
    kraus: list of Kraus operators as 2x2 arrays of floats, [K1, K2, K3, K4]
    """
    proj_0 = np.array([[1.0, 0.0], [0.0, 0.0]], dtype=np.float64)
    proj_1 = np.array([[0.0, 0.0], [0.0, 1.0]], dtype=np.float64)
    off_diag_01 = np.array([[0.0, 1.0], [0.0, 0.0]], dtype=np.float64)
    off_diag_10 = np.array([[0.0, 0.0], [1.0, 0.0]], dtype=np.float64)
    K1 = np.sqrt(1.0 - N) * (proj_0 + np.sqrt(1.0 - gamma) * proj_1)
    K2 = np.sqrt(gamma * (1.0 - N)) * off_diag_01
    K3 = np.sqrt(N) * (np.sqrt(1.0 - gamma) * proj_0 + proj_1)
    K4 = np.sqrt(gamma * N) * off_diag_10
    kraus = [K1, K2, K3, K4]
    return kraus

def output_state(rails, gamma_1, N_1, gamma_2, N_2):
    """Inputs:
    rails: int, number of rails
    gamma_1: float, damping parameter of the first channel
    N_1: float, thermal parameter of the first channel
    gamma_2: float, damping parameter of the second channel
    N_2: float, thermal parameter of the second channel
    Output:
    state: 2**(2*rails) x 2**(2*rails) dimensional array of floats, the output state
    """
    m = rails
    rho = multi_rail_encoding_state(m)
    K_channel_1 = generalized_amplitude_damping_channel(gamma_1, N_1)
    K_channel_2 = generalized_amplitude_damping_channel(gamma_2, N_2)
    dims = [2] * (2 * m)
    sys_A = list(range(m))
    rho = apply_channel(K_channel_1, rho, sys=sys_A, dim=dims)
    sys_B = list(range(m, 2 * m))
    rho = apply_channel(K_channel_2, rho, sys=sys_B, dim=dims)
    state = rho
    return state

def measurement(rails):
    """Returns the measurement projector
    Input:
    rails: int, number of rails
    Output:
    global_proj: ( 2**(2*rails), 2**(2*rails) ) dimensional array of floats
    """
    m = rails
    dim_subsystem = 2 ** m
    total_dim = 2 ** (2 * m)
    local_proj = np.zeros((dim_subsystem, dim_subsystem), dtype=np.float64)
    for k in range(m):
        idx = 2 ** k
        basis_vec = np.zeros(dim_subsystem, dtype=np.float64)
        basis_vec[idx] = 1.0
        local_proj += np.outer(basis_vec, basis_vec)
    global_proj = np.kron(local_proj, local_proj)
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
    n = len(dim)
    D = int(np.prod(dim))
    tensor_shape = tuple(dim) + tuple(dim)
    X_reshaped = np.reshape(X, tensor_shape)
    perm_axes = list(perm) + [n + p for p in perm]
    X_permuted = np.transpose(X_reshaped, perm_axes)
    new_dim = [dim[p] for p in perm]
    Y = np.reshape(X_permuted, (D, D))
    return Y

def partial_trace(X, sys, dim):
    """Inputs:
    X: 2d array of floats with equal dimensions, the density matrix of the state
    sys: list of int containing systems over which to take the partial trace (i.e., the systems to discard).
    dim: list of int containing dimensions of all subsystems.
    Output:
    2d array of floats with equal dimensions, density matrix after partial trace.
    """
    n = len(dim)
    keep_sys = [i for i in range(n) if i not in sys]
    if len(keep_sys) == n:
        return X
    perm = keep_sys + sys
    X_perm = syspermute(X, perm, dim)
    dim_keep = [dim[i] for i in keep_sys]
    dim_trace = [dim[i] for i in sys]
    D_keep = int(np.prod(dim_keep)) if dim_keep else 1
    D_trace = int(np.prod(dim_trace))
    tensor_shape = tuple(dim_keep) + tuple(dim_trace) + tuple(dim_keep) + tuple(dim_trace)
    X_tensor = np.reshape(X_perm, tensor_shape)
    num_keep = len(dim_keep)
    num_trace = len(dim_trace)
    result_shape = tuple(dim_keep) + tuple(dim_keep)
    result = np.zeros(result_shape, dtype=np.float64)
    trace_indices = list(itertools.product(*[range(d) for d in dim_trace]))
    for trace_idx in trace_indices:
        idx_bra = tuple([slice(None)] * num_keep) + trace_idx
        idx_ket = tuple([slice(None)] * num_keep) + trace_idx
        result += X_tensor[idx_bra + idx_ket]
    result_matrix = np.reshape(result, (D_keep, D_keep))
    return result_matrix

def entropy(rho):
    """Inputs:
    rho: 2d array of floats with equal dimensions, the density matrix of the state
    Output:
    en: quantum (von Neumann) entropy of the state rho, float
    """
    eigenvalues = np.linalg.eigvalsh(rho)
    eigenvalues = eigenvalues[eigenvalues > 1e-15]
    en = -np.sum(eigenvalues * np.log2(eigenvalues))
    return en

def coherent_inf_state(rho_AB, dimA, dimB):
    """Inputs:
    rho_AB: 2d array of floats with equal dimensions, the state we evaluate coherent information
    dimA: int, dimension of system A
    dimB: int, dimension of system B
    Output:
    co_inf: float, the coherent information of the state rho_AB
    """
    rho_B = partial_trace(rho_AB, sys=[0], dim=[dimA, dimB])
    S_AB = entropy(rho_AB)
    S_B = entropy(rho_B)
    co_inf = S_B - S_AB
    return co_inf
