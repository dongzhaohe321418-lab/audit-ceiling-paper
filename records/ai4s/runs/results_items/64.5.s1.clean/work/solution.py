import numpy as np
import itertools

def wrap(r, L):
    """Apply periodic boundary conditions to a vector of coordinates r for a cubic box of size L.
    Parameters:
    r : The (x, y, z) coordinates of a particle.
    L (float): The length of each side of the cubic box.
    Returns:
    coord: numpy 1d array of floats, the wrapped coordinates such that they lie within the cubic box.
    """
    r = np.asarray(r)
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
    r1 = np.asarray(r1)
    r2 = np.asarray(r2)
    dr = r1 - r2
    dr = dr - L * np.round(dr / L)
    distance = np.linalg.norm(dr)
    return distance

def E_ij(r, sigma, epsilon):
    """Calculate the Lennard-Jones potential energy between two particles.
    Parameters:
    r : float
        The distance between the two particles.
    sigma : float
        The distance at which the potential is zero.
    epsilon : float
        The depth of the potential well.
    Returns:
    float
        The potential energy between the two particles at distance r.
    """
    sigma_over_r = sigma / r
    E_lj = 4 * epsilon * (sigma_over_r ** 12 - sigma_over_r ** 6)
    return E_lj

def E_i(r, positions, L, sigma, epsilon):
    """Calculate the total Lennard-Jones potential energy of a particle with other particles in a periodic system.
    Parameters:
    r : array_like
        The (x, y, z) coordinates of the target particle.
    positions : array_like
        An array of (x, y, z) coordinates for each of the other particles in the system.
    L : float
        The length of the side of the cubic box
    sigma : float
        The distance at which the potential minimum occurs
    epsilon : float
        The depth of the potential well
    Returns:
    float
        The total Lennard-Jones potential energy of the particle due to its interactions with other particles.
    """
    r = np.asarray(r)
    positions = np.asarray(positions)
    E = 0.0
    for position in positions:
        r_ij = dist(r, position, L)
        E += E_ij(r_ij, sigma, epsilon)
    return E

def E_system(positions, L, sigma, epsilon):
    """Calculate the total Lennard-Jones potential energy of a particle with other particles in a periodic system.
    Parameters:
    positions : array_like
        An array of (x, y, z) coordinates for each of the other particles in the system.
    L : float
        The length of the side of the cubic box
    sigma : float
        The distance at which the potential minimum occurs
    epsilon : float
        The depth of the potential well
    Returns:
    float
        The total Lennard-Jones potential
    """
    positions = np.asarray(positions)
    total_E = 0.0
    for i, j in itertools.combinations(range(len(positions)), 2):
        r_ij = dist(positions[i], positions[j], L)
        total_E += E_ij(r_ij, sigma, epsilon)
    return total_E
