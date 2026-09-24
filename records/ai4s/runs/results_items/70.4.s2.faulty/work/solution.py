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
    c12 = np.sqrt(1 - s12 ** 2)
    c23 = np.sqrt(1 - s23 ** 2)
    c13 = np.sqrt(1 - s13 ** 2)
    exp_neg_i_dCP = cmath.exp(-1j * dCP)
    exp_pos_i_dCP = cmath.exp(1j * dCP)
    pmns = np.array([[c12 * c13, s12 * c13, s13 * exp_neg_i_dCP], [-s12 * c23 - c12 * s23 * s13 * exp_pos_i_dCP, c12 * c23 - s12 * s23 * s13 * exp_pos_i_dCP, s23 * c13], [s12 * s23 - c12 * c23 * s13 * exp_pos_i_dCP, -c12 * s23 - s12 * c23 * s13 * exp_pos_i_dCP, c23 * c13]], dtype=complex)
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
    c12 = np.sqrt(1 - s12 ** 2)
    c23 = np.sqrt(1 - s23 ** 2)
    c13 = np.sqrt(1 - s13 ** 2)
    exp_neg_i_dCP = cmath.exp(-1j * dCP)
    exp_pos_i_dCP = cmath.exp(1j * dCP)
    U = np.array([[c12 * c13, s12 * c13, s13 * exp_neg_i_dCP], [-s12 * c23 - c12 * s23 * s13 * exp_pos_i_dCP, c12 * c23 - s12 * s23 * s13 * exp_pos_i_dCP, s23 * c13], [s12 * s23 - c12 * c23 * s13 * exp_pos_i_dCP, -c12 * s23 - s12 * c23 * s13 * exp_pos_i_dCP, c23 * c13]], dtype=complex)
    mass_matrix = np.diag([0.0, D21, D31])
    U_dagger = np.conj(U.T)
    hamiltonian = 0.5 * U @ mass_matrix @ U_dagger
    hamiltonian_list = hamiltonian.tolist()
    return hamiltonian_list

def hamiltonian_3nu_su3_coefficients(hamiltonian):
    """Returns the h_k of the SU(3)-expansion of the 3nu Hamiltonian.
    Input
    hamiltonian: a list of lists containing the 3x3 Hamiltonian matrix; each inner list contains three complex numbers
    Output
    hks: a list containing the h_k coefficients of the 3nu Hamiltonian in the expansion using the Gell-Mann matrices (k=1 to k=8); a list of floats
    """
    H = np.array(hamiltonian, dtype=complex)
    h1 = np.real(H[0, 1])
    h2 = -np.imag(H[0, 1])
    h3 = 0.5 * (np.real(H[0, 0]) - np.real(H[1, 1]))
    h4 = np.real(H[0, 2])
    h5 = -np.imag(H[0, 2])
    h6 = np.real(H[1, 2])
    h7 = -np.imag(H[1, 2])
    h8 = np.sqrt(3) / 6.0 * (np.real(H[0, 0]) + np.real(H[1, 1]) - 2.0 * np.real(H[2, 2]))
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
    gell_mann = {}
    gell_mann[1] = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex)
    gell_mann[2] = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex)
    gell_mann[3] = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex)
    gell_mann[4] = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex)
    gell_mann[5] = np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex)
    gell_mann[6] = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
    gell_mann[7] = np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex)
    gell_mann[8] = np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex) / np.sqrt(3)
    lambda_i = gell_mann[i]
    lambda_j = gell_mann[j]
    lambda_k = gell_mann[k]
    anticommutator = lambda_i @ lambda_j + lambda_j @ lambda_i
    product = anticommutator @ lambda_k
    trace = np.trace(product)
    result = np.real(0.25 * trace)
    return result
