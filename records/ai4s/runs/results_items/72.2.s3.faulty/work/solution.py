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
    i_left = (i - 1) % N
    i_right = (i + 1) % N
    j_above = (j + 1) % N
    j_below = (j - 1) % N
    nn_wrap = [(i_left, j), (i, j_above), (i_right, j), (i, j_below)]
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
    spin_a = lattice[i, j]
    neighbors = [(i - 1) % N, (i + 1) % N]
    neighbor_coords = [((i - 1) % N, j), ((i + 1) % N, j), (i, (j + 1) % N), (i, (j - 1) % N)]
    neighbor_sum = sum((lattice[ni, nj] for ni, nj in neighbor_coords))
    energy = -spin_a * neighbor_sum
    return energy
