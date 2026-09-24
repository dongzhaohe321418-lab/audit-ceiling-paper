import numpy as np

def neighbor_list(site, N):
    """Return all nearest neighbors of site (i, j).
    Args:
        site (Tuple[int, int]): site indices
        N (int): number of sites along each dimension
    Return:
        list: a list of 2-tuples, [(i_left, j_left), (i_above, j_above), (i_right, j_right), (i_below, j_below)]
    """
    i, j = site
    i_left = i
    j_left = (j - 1) % N
    i_above = (i - 1) % N
    j_above = j
    i_right = i
    j_right = (j + 1) % N
    i_below = (i + 1) % N
    j_below = j
    nn_wrap = [(i_left, j_left), (i_above, j_above), (i_right, j_right), (i_below, j_below)]
    return nn_wrap

def energy_site(i, j, lattice):
    """Calculate the energy of site (i, j)
    Args:
        i (int): site index along x
        j (int): site index along y
        lattice (np.array): shape (N, N), a 2D array of +1 and -1
    Return:
        float: energy of site (i, j)
    """
    N = lattice.shape[0]
    s_a = lattice[i, j]
    neighbors = neighbor_list((i, j), N)
    neighbor_sum = 0
    for neighbor_i, neighbor_j in neighbors:
        neighbor_sum += lattice[neighbor_i, neighbor_j]
    energy = -s_a * neighbor_sum
    return energy
