import numpy as np
from scipy.spatial.distance import pdist

def U_ij(r, sigma, epsilon):
    """Lennard Jones Potential between pair of atoms with distance r
    Inputs:
    r: distance, float
    sigma: the distance at which Lennard Jones potential reaches zero, float
    epsilon: potential well depth of Lennard Jones potential, float
    Outputs:
    U: Potential Energy, float
    """
    ratio = sigma / r
    U = 4 * epsilon * (ratio ** 12 - ratio ** 6)
    return U

def U_i(r_i, i, positions, sigma, epsilon):
    """Total energy on a single atom
    Inputs:
    r_i: atom position, 1d array of floats with x,y,z coordinate
    i: atom index, int
    positions: all atom positions, 2D array of floats with shape (N,3), where N is the number of atoms, 3 is x,y,z coordinate
    sigma: the distance at which Lennard Jones potential reaches zero, float
    epsilon: potential well depth of Lennard Jones potential, float 
    Outputs:
    U_i: Aggregated energy on particle i, float
    """
    total_energy = 0.0
    N = positions.shape[0]
    for j in range(N):
        if i != j:
            r_ij = np.linalg.norm(positions[i] - positions[j])
            total_energy += U_ij(r_ij, sigma, epsilon)
    return total_energy

def U_system(positions, sigma, epsilon):
    """Total energy of entire system
    Inputs:
    positions: all atom positions, 2D array of floats with shape (N,3), where N is the number of atoms, 3 is for x,y,z coordinate
    sigma: the distance at which Lennard Jones potential reaches zero, float
    epsilon: potential well depth of Lennard Jones potential, float 
    Outputs:
    U: Aggregated energy of entire system, float
    """
    total_energy = 0.0
    N = positions.shape[0]
    for i in range(N):
        for j in range(i + 1, N):
            r_ij = np.linalg.norm(positions[i] - positions[j])
            total_energy += U_ij(r_ij, sigma, epsilon)
    return total_energy
