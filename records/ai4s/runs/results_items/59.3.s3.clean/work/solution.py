import numpy as np
from cmath import exp
from scipy.linalg import block_diag
from scipy.optimize import minimize
from scipy.linalg import expm

def rotation_matrices(axis, theta):
    """Create rotation matrices Rx, Ry, and Rz with the given angle theta.
    Inputs:
    axis : int
        The rotation axis. 1 = x, 2 = y, 3 = z.
    theta : float
        The rotation angle.
    Output:
    R : matrix of shape(2, 2)
        The rotation matrix.
    """
    if axis == 1:
        cos_half = np.cos(theta / 2)
        sin_half = np.sin(theta / 2)
        R = np.array([[cos_half, -1j * sin_half], [-1j * sin_half, cos_half]], dtype=complex)
        return R
    elif axis == 2:
        cos_half = np.cos(theta / 2)
        sin_half = np.sin(theta / 2)
        R = np.array([[cos_half, -sin_half], [sin_half, cos_half]], dtype=complex)
        return R
    elif axis == 3:
        exp_neg = exp(-1j * theta / 2)
        exp_pos = exp(1j * theta / 2)
        R = np.array([[exp_neg, 0], [0, exp_pos]], dtype=complex)
        return R
    else:
        raise ValueError('axis must be 1 (x), 2 (y), or 3 (z)')

def create_ansatz(theta):
    """Create the ansatz wavefunction with a given theta.
    Input:
    theta : float
        The only variational parameter.
    Output:
    ansatz : array of shape (4, 1)
        The ansatz wavefunction.
    """
    psi = np.array([[1], [0], [0], [0]], dtype=complex)
    cos_half = np.cos(np.pi / 2)
    sin_half = np.sin(np.pi / 2)
    Rx_pi = np.array([[cos_half, -1j * sin_half], [-1j * sin_half, cos_half]], dtype=complex)
    I = np.eye(2, dtype=complex)
    gate_hf = np.kron(I, Rx_pi)
    psi = gate_hf @ psi
    cos_half = np.cos(np.pi / 4)
    sin_half = np.sin(np.pi / 4)
    Ry_pi2 = np.array([[cos_half, -sin_half], [sin_half, cos_half]], dtype=complex)
    gate = np.kron(Ry_pi2, I)
    psi = gate @ psi
    cos_half = np.cos(-np.pi / 4)
    sin_half = np.sin(-np.pi / 4)
    Rx_neg_pi2 = np.array([[cos_half, -1j * sin_half], [-1j * sin_half, cos_half]], dtype=complex)
    gate = np.kron(I, Rx_neg_pi2)
    psi = gate @ psi
    CNOT = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], dtype=complex)
    psi = CNOT @ psi
    exp_neg = exp(-1j * (-2 * theta) / 2)
    exp_pos = exp(1j * (-2 * theta) / 2)
    Rz = np.array([[exp_neg, 0], [0, exp_pos]], dtype=complex)
    gate = np.kron(I, Rz)
    psi = gate @ psi
    psi = CNOT @ psi
    cos_half = np.cos(-np.pi / 4)
    sin_half = np.sin(-np.pi / 4)
    Ry_neg_pi2 = np.array([[cos_half, -sin_half], [sin_half, cos_half]], dtype=complex)
    gate = np.kron(Ry_neg_pi2, I)
    psi = gate @ psi
    cos_half = np.cos(np.pi / 4)
    sin_half = np.sin(np.pi / 4)
    Rx_pi2 = np.array([[cos_half, -1j * sin_half], [-1j * sin_half, cos_half]], dtype=complex)
    gate = np.kron(I, Rx_pi2)
    psi = gate @ psi
    ansatz = psi
    return ansatz

def measureZ(U, psi):
    """Perform a measurement in the Z-basis for a 2-qubit system where only Pauli Sz measurements are possible.
    The measurement is applied to the first qubit.
    Inputs:
    U : matrix of shape(4, 4)
        The unitary transformation to be applied before measurement.
    psi : array of shape (4, 1)
        The two-qubit state before the unitary transformation.
    Output:
    measured_result: float
        The result of the Sz measurement after applying U.
    """
    Z1_I = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]], dtype=complex)
    psi_prime = U @ psi
    U_dagger = np.conj(U.T)
    Z1_I_rotated = U_dagger @ Z1_I @ U
    measured_result = np.real(np.conj(psi_prime.T) @ Z1_I @ psi_prime)[0, 0]
    return measured_result
