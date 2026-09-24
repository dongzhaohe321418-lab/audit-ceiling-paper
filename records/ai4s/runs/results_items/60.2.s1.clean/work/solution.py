import numpy as np

def wrap(r, L):
    """Apply periodic boundary conditions to a vector of coordinates r for a cubic box of size L.
    Parameters:
    r : The (x, y, z) coordinates of a particle.
    L (float): The length of each side of the cubic box.
    Returns:
    coord: numpy 1d array of floats, the wrapped coordinates such that they lie within the cubic box.
    """
    r = np.asarray(r)
    coord = r % L
    return coord

def E_i(r, pos, sigma, epsilon, L, r_c):
    """Calculate the total Lennard-Jones potential energy of a particle with other particles in a periodic system.
    Parameters:
    r : array, the (x, y, z) coordinates of the target particle.
    pos : An array of (x, y, z) coordinates for each of the other particles in the system.
    sigma : float, the distance at which the potential minimum occurs
    epsilon : float, the depth of the potential well
    L : float, the length of the side of the cubic box
    r_c : float, cut-off distance
    Returns:
    float, the total Lennard-Jones potential energy of the particle due to its interactions with other particles.
    """

    def E_ij(r_ij, sigma, epsilon, r_c):
        """Calculate the Lennard-Jones potential between a pair of atoms.
        Parameters:
        r_ij : float, the distance between two particles
        sigma : float, the distance at which the potential is zero
        epsilon : float, the depth of the potential well
        r_c : float, cut-off distance
        Returns:
        float, the Lennard-Jones potential energy for this pair
        """
        if r_ij < r_c:
            return 4 * epsilon * ((sigma / r_ij) ** 12 - (sigma / r_ij) ** 6)
        else:
            return 0.0
    r = np.asarray(r)
    pos = np.asarray(pos)
    E = 0.0
    for particle_pos in pos:
        dr = r - particle_pos
        dr = dr - L * np.round(dr / L)
        r_ij = np.linalg.norm(dr)
        E += E_ij(r_ij, sigma, epsilon, r_c)
    return E
