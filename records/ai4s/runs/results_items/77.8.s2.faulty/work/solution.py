import math
import numpy as np
import scipy as sp
from scipy.constants import  Avogadro

def wrap(r, L):
    """Apply periodic boundary conditions to a vector of coordinates r for a cubic box of size L.
    Parameters:
    r : The (x, y, z) coordinates of a particle.
    L (float): The length of each side of the cubic box.
    Returns:
    coord: numpy 1d array of floats, the wrapped coordinates such that they lie within the cubic box.
    """
    r = np.array(r)
    coord = r - L * np.floor(r / L)
    return coord

def dist(r1, r2, L):
    """Calculate the minimum image distance between two atoms in a periodic cubic system.
    Parameters:
    r1 : The (x, y, z) coordinates of the first atom.
    r2 : The (x, y, z) coordinates of the second atom.
    L (float): The length of the side of the cubic box.
    Returns:
    float: The minimum image distance between the two atoms.
    """
    r1 = np.array(r1)
    r2 = np.array(r2)
    dr = r1 - r2
    dr = dr - L * np.round(dr / L)
    distance = np.linalg.norm(dr)
    return distance

def dist_v(r1, r2, L):
    """Calculate the minimum image vector between two atoms in a periodic cubic system.
    Parameters:
    r1 : The (x, y, z) coordinates of the first atom.
    r2 : The (x, y, z) coordinates of the second atom.
    L (float): The length of the side of the cubic box.
    Returns:
    numpy 1d array: The minimum image vector from atom 2 to atom 1.
    """
    r1 = np.array(r1)
    r2 = np.array(r2)
    r12 = r1 - r2
    r12 = r12 - L * np.round(r12 / L)
    return r12

def E_ij(r, sigma, epsilon, rc):
    """Calculate the combined truncated and shifted Lennard-Jones potential energy between two particles.
    Parameters:
    r (float): The distance between particles i and j.
    sigma (float): The distance at which the inter-particle potential is zero for the Lennard-Jones potential.
    epsilon (float): The depth of the potential well for the Lennard-Jones potential.
    rc (float): The cutoff distance beyond which the potentials are truncated and shifted to zero.
    Returns:
    float: The combined potential energy between the two particles, considering the specified potentials.
    """
    if r > rc:
        return 0.0
    sigma_over_r_6 = (sigma / r) ** 6
    sigma_over_r_12 = sigma_over_r_6 ** 2
    V_LJ_r = 4.0 * epsilon * (sigma_over_r_12 - sigma_over_r_6)
    sigma_over_rc_6 = (sigma / rc) ** 6
    sigma_over_rc_12 = sigma_over_rc_6 ** 2
    V_LJ_rc = 4.0 * epsilon * (sigma_over_rc_12 - sigma_over_rc_6)
    E = V_LJ_r - V_LJ_rc
    return E

def f_ij(r, sigma, epsilon, rc):
    """Calculate the force vector between two particles, considering the truncated and shifted
    Lennard-Jones potential.
    Parameters:
    r (array_like): The displacement vector from particle j to particle i (x, y, z components).
    sigma (float): The distance at which the inter-particle potential is zero for the Lennard-Jones potential.
    epsilon (float): The depth of the potential well for the Lennard-Jones potential.
    rc (float): The cutoff distance beyond which the potentials are truncated and shifted to zero.
    Returns:
    array_like: The force vector experienced by particle i due to particle j, considering the specified potentials
    """
    r = np.array(r)
    distance = np.linalg.norm(r)
    if distance > rc or distance < 1e-10:
        return np.array([0.0, 0.0, 0.0])
    sigma_over_distance_6 = (sigma / distance) ** 6
    sigma_over_distance_12 = sigma_over_distance_6 ** 2
    force_magnitude = 4.0 * epsilon * (12.0 * sigma_over_distance_12 / distance - 6.0 * sigma_over_distance_6 / distance)
    force_vector = force_magnitude * (r / distance)
    return force_vector

def E_tail(N, L, sigma, epsilon, rc):
    """Calculate the energy tail correction for a system of particles, considering the truncated and shifted
    Lennard-Jones potential.
    Parameters:
    N (int): The total number of particles in the system.
    L (float): Length of cubic box
    sigma (float): The distance at which the inter-particle potential is zero for the Lennard-Jones potential.
    epsilon (float): The depth of the potential well for the Lennard-Jones potential.
    rc (float): The cutoff distance beyond which the potentials are truncated and shifted to zero.
    Returns:
    float: The energy tail correction for the entire system, considering the specified potentials.
    """
    sigma_over_rc = sigma / rc
    sigma_over_rc_3 = sigma_over_rc ** 3
    sigma_over_rc_9 = sigma_over_rc_3 ** 3
    E_tail_LJ = 8.0 / 3.0 * math.pi * N ** 2 * epsilon * sigma ** 3 * (1.0 / 3.0 * sigma_over_rc_9 - sigma_over_rc_3)
    return E_tail_LJ

def P_tail(N, L, sigma, epsilon, rc):
    """ Calculate the pressure tail correction for a system of particles, including
     the truncated and shifted Lennard-Jones contributions.
    Parameters:
     N (int): The total number of particles in the system.
     L (float): Length of cubic box
     sigma (float): The distance at which the inter-particle potential is zero for the Lennard-Jones potential.
     epsilon (float): The depth of the potential well for the Lennard-Jones potential.
     rc (float): The cutoff distance beyond which the potentials are truncated and shifted to zero.
     Returns:
     float
         The pressure tail correction for the entire system (in bar).
    """
    sigma_over_rc = sigma / rc
    sigma_over_rc_3 = sigma_over_rc ** 3
    sigma_over_rc_9 = sigma_over_rc_3 ** 3
    P_tail_reduced = 16.0 / 3.0 * math.pi * N ** 2 * epsilon * sigma ** 3 * (2.0 / 3.0 * sigma_over_rc_9 - sigma_over_rc_3)
    V = L ** 3
    P_tail_bar = P_tail_reduced / V
    return P_tail_bar

def E_pot(xyz, L, sigma, epsilon, rc):
    """Calculate the total potential energy of a system using the truncated and shifted Lennard-Jones potential.
    Parameters:
    xyz : A NumPy array with shape (N, 3) where N is the number of particles. Each row contains the x, y, z coordinates of a particle in the system.
    L (float): Length of cubic box
    sigma (float): The distance at which the inter-particle potential is zero for the Lennard-Jones potential.
    epsilon (float): The depth of the potential well for the Lennard-Jones potential.
    rc (float): The cutoff distance beyond which the potentials are truncated and shifted to zero.
    Returns:
    float
        The total potential energy of the system (in zeptojoules).
    """
    xyz = np.array(xyz)
    N = len(xyz)
    E = 0.0
    for i in range(N):
        for j in range(i + 1, N):
            r_ij = dist(xyz[i], xyz[j], L)
            E += E_ij(r_ij, sigma, epsilon, rc)
    return E
