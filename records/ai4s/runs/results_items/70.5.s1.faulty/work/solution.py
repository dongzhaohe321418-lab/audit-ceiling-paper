import numpy as np
import cmath 

def pmns_mixing_matrix(s12, s23, s13, dCP):
    """Returns the 3x3 PMNS mixing matrix.
    Computes and returns the 3x3 complex PMNS mixing matrix
    parameterized by three rotation angles: theta_12, theta_23, theta_13,
    and one CP-violation phase, delta_CP.
    Input
    s12 : Sin(theta_12); float
    s23 : Sin(theta_23); float
    s13 : Sin(theta_13); float
    dCP : delta_CP in radians; float
    Output
    pmns: numpy array of floats with shape (3,3) containing the 3x3 PMNS mixing matrix
    """
    c12 = np.sqrt(1.0 - s12 ** 2)
    c23 = np.sqrt(1.0 - s23 ** 2)
    c13 = np.sqrt(1.0 - s13 ** 2)
    exp_i_dCP = cmath.exp(1j * dCP)
    exp_minus_i_dCP = cmath.exp(-1j * dCP)
    pmns = np.zeros((3, 3), dtype=complex)
    pmns[0, 0] = c12 * c13
    pmns[0, 1] = s12 * c13
    pmns[0, 2] = s13 * exp_minus_i_dCP
    pmns[1, 0] = -s12 * c23 - c12 * s23 * s13 * exp_i_dCP
    pmns[1, 1] = c12 * c23 - s12 * s23 * s13 * exp_i_dCP
    pmns[1, 2] = s23 * c13
    pmns[2, 0] = s12 * s23 - c12 * c23 * s13 * exp_i_dCP
    pmns[2, 1] = -c12 * s23 - s12 * c23 * s13 * exp_i_dCP
    pmns[2, 2] = c23 * c13
    return pmns

def hamiltonian_3nu(s12, s23, s13, dCP, D21, D31):
    """Returns the energy-independent three-neutrino Hamiltonian for vacuum oscillations.
    Input
    s12 : Sin(theta_12); float
    s23 : Sin(theta_23); float
    s13 : Sin(theta_13); float
    dCP : delta_CP in radians; float
    D21 : Mass-squared difference Delta m^2_21; float
    D31 : Mass-squared difference Delta m^2_31; float
    Output
    hamiltonian: a list of lists containing the 3x3 Hamiltonian matrix; each inner list contains three complex numbers
    """
    c12 = np.sqrt(1.0 - s12 ** 2)
    c23 = np.sqrt(1.0 - s23 ** 2)
    c13 = np.sqrt(1.0 - s13 ** 2)
    exp_i_dCP = cmath.exp(1j * dCP)
    exp_minus_i_dCP = cmath.exp(-1j * dCP)
    U = np.zeros((3, 3), dtype=complex)
    U[0, 0] = c12 * c13
    U[0, 1] = s12 * c13
    U[0, 2] = s13 * exp_minus_i_dCP
    U[1, 0] = -s12 * c23 - c12 * s23 * s13 * exp_i_dCP
    U[1, 1] = c12 * c23 - s12 * s23 * s13 * exp_i_dCP
    U[1, 2] = s23 * c13
    U[2, 0] = s12 * s23 - c12 * c23 * s13 * exp_i_dCP
    U[2, 1] = -c12 * s23 - s12 * c23 * s13 * exp_i_dCP
    U[2, 2] = c23 * c13
    M_diag = np.zeros((3, 3), dtype=complex)
    M_diag[0, 0] = 0.0
    M_diag[1, 1] = D21
    M_diag[2, 2] = D31
    U_dagger = np.conj(U.T)
    hamiltonian_matrix = 0.5 * U @ M_diag @ U_dagger
    hamiltonian = hamiltonian_matrix.tolist()
    return hamiltonian

def hamiltonian_3nu_su3_coefficients(hamiltonian):
    """Returns the h_k of the SU(3)-expansion of the 3nu Hamiltonian.
    Input
    hamiltonian: a list of lists containing the 3x3 Hamiltonian matrix; each inner list contains three complex numbers
    Output
    hks: a list containing the h_k coefficients of the 3nu Hamiltonian in the expansion using the Gell-Mann matrices (k=1 to k=8); a list of floats (possibly complex)
    """
    H = np.array(hamiltonian, dtype=complex)
    H_11 = H[0, 0]
    H_22 = H[1, 1]
    H_33 = H[2, 2]
    H_12 = H[0, 1]
    H_13 = H[0, 2]
    H_23 = H[1, 2]
    h1 = float(np.real(H_12))
    h2 = float(-np.imag(H_12))
    h3 = float(0.5 * (np.real(H_11) - np.real(H_22)))
    h4 = float(np.real(H_13))
    h5 = float(-np.imag(H_13))
    h6 = float(np.real(H_23))
    h7 = float(-np.imag(H_23))
    h8 = float(np.sqrt(3) / 6.0 * (np.real(H_11) + np.real(H_22) - 2.0 * np.real(H_33)))
    hks = [h1, h2, h3, h4, h5, h6, h7, h8]
    return hks

def tensor_d(i, j, k):
    """Returns the tensor d_ijk of the SU(3) algebra.
    Input
    i: the first index; int
    j: the second index; int
    k: the third index; int
    Output
    result: the value of d_ijk for given indices i, j, and k; float
    """
    lambda_matrices = {1: np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex), 2: np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex), 3: np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex), 4: np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex), 5: np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex), 6: np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex), 7: np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex), 8: 1 / np.sqrt(3) * np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex)}
    lambda_i = lambda_matrices[i]
    lambda_j = lambda_matrices[j]
    lambda_k = lambda_matrices[k]
    anticommutator = lambda_i @ lambda_j + lambda_j @ lambda_i
    product = anticommutator @ lambda_k
    trace = np.trace(product)
    result = 1 / 4 * trace
    result = float(np.real(result))
    return result

def star_product(i, h):
    """Returns the SU(3) star product (h*h)_i = d_ijk*h^j*h^k (summed over
    repeated indices).
    Input
    i: index of the star product; int
    h: a list of eight expansion coefficients; a list of floats (possibly complex)
    Output
    product: the star product (h*h)_i; complex numbers
    """
    product = 0.0
    for j in range(1, 9):
        for k in range(1, 9):
            d_ijk = tensor_d(i, j, k)
            product += d_ijk * h[j - 1] * h[k - 1]
    return product
