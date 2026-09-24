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
    exp_minus_i_dCP = cmath.exp(-1j * dCP)
    exp_plus_i_dCP = cmath.exp(1j * dCP)
    pmns = np.array([[c12 * c13, s12 * c13, s13 * exp_minus_i_dCP], [-s12 * c23 - c12 * s23 * s13 * exp_plus_i_dCP, c12 * c23 - s12 * s23 * s13 * exp_plus_i_dCP, s23 * c13], [s12 * s23 - c12 * c23 * s13 * exp_plus_i_dCP, -c12 * s23 - s12 * c23 * s13 * exp_plus_i_dCP, c23 * c13]], dtype=complex)
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
    exp_minus_i_dCP = cmath.exp(-1j * dCP)
    exp_plus_i_dCP = cmath.exp(1j * dCP)
    U = np.array([[c12 * c13, s12 * c13, s13 * exp_minus_i_dCP], [-s12 * c23 - c12 * s23 * s13 * exp_plus_i_dCP, c12 * c23 - s12 * s23 * s13 * exp_plus_i_dCP, s23 * c13], [s12 * s23 - c12 * c23 * s13 * exp_plus_i_dCP, -c12 * s23 - s12 * c23 * s13 * exp_plus_i_dCP, c23 * c13]], dtype=complex)
    mass_diag = np.array([[0, 0, 0], [0, D21, 0], [0, 0, D31]], dtype=complex)
    U_dagger = np.conj(U).T
    H = 0.5 * U @ mass_diag @ U_dagger
    hamiltonian = [[H[i, j] for j in range(3)] for i in range(3)]
    return hamiltonian

def hamiltonian_3nu_su3_coefficients(hamiltonian):
    """Returns the h_k of the SU(3)-expansion of the 3nu Hamiltonian.
    Input
    hamiltonian: a list of lists containing the 3x3 Hamiltonian matrix; each inner list contains three complex numbers
    Output
    hks: a list containing the h_k coefficients of the 3nu Hamiltonian in the expansion using the Gell-Mann matrices (k=1 to k=8); a list of floats (possibly complex)
    """
    H11 = hamiltonian[0][0]
    H22 = hamiltonian[1][1]
    H33 = hamiltonian[2][2]
    H12 = hamiltonian[0][1]
    H13 = hamiltonian[0][2]
    H23 = hamiltonian[1][2]
    h1 = H12.real
    h2 = -H12.imag
    h3 = 0.5 * (H11 - H22).real
    h4 = H13.real
    h5 = -H13.imag
    h6 = H23.real
    h7 = -H23.imag
    h8 = np.sqrt(3) / 6 * (H11 + H22 - 2 * H33).real
    hks = [h1, h2, h3, h4, h5, h6, h7, h8]
    return hks
