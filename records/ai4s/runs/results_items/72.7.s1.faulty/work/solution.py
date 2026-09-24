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
        lattice (np.array): shape (N, N), a 2D array +1 and -1
    Return:
        float: energy of site (i, j)
    """
    N = lattice.shape[0]
    spin_current = lattice[i, j]
    neighbors = neighbor_list((i, j), N)
    neighbor_sum = sum((lattice[ni, nj] for ni, nj in neighbors))
    energy = -spin_current * neighbor_sum
    return energy

def energy(lattice):
    """calculate the total energy for the site (i, j) of the periodic Ising model with dimension (N, N)
    Args: 
        lattice (np.array): shape (N, N), a 2D array with elements +1 and -1
    Return:
        float: total energy of the system
    """
    N = lattice.shape[0]
    total_energy = 0.0
    for i in range(N):
        for j in range(N):
            spin_current = lattice[i, j]
            j_right = (j + 1) % N
            spin_right = lattice[i, j_right]
            total_energy += -spin_current * spin_right
            i_down = (i + 1) % N
            spin_down = lattice[i_down, j]
            total_energy += -spin_current * spin_down
    return total_energy

def magnetization(spins):
    """total magnetization of the periodic Ising model with dimension (N, N)
    Args: spins (np.array): shape (N, N), a 2D array with elements +1 and -1
    Return:
        float: total magnetization of the system
    """
    mag = np.sum(spins)
    return mag

def get_flip_probability_magnetization(lattice, i, j, beta):
    """Calculate spin flip probability and change in total magnetization.
    Args:
        lattice (np.array): shape (N, N), 2D lattice of 1 and -1
        i (int): site index along x
        j (int): site index along y
        beta (float): inverse temperature
    Return:
        A (float): acceptance ratio
        dM (int): change in magnetization after the spin flip
    """
    N = lattice.shape[0]
    spin_current = lattice[i, j]
    neighbors = [(i, (j - 1) % N), ((i - 1) % N, j), (i, (j + 1) % N), ((i + 1) % N, j)]
    neighbor_sum = sum((lattice[ni, nj] for ni, nj in neighbors))
    energy_before = -spin_current * neighbor_sum
    spin_flipped = -spin_current
    energy_after = -spin_flipped * neighbor_sum
    dE = energy_after - energy_before
    if dE < 0:
        A = 1.0
    else:
        A = np.exp(-beta * dE)
    dM = -2 * spin_current
    return (A, dM)

def flip(spins, beta):
    """Goes through each spin in the 2D lattice and flip it.
    Args:
        spins (np.array): shape (N, N), 2D lattice of 1 and -1        
        beta (float): inverse temperature
    Return:
        lattice (np.array): final spin configurations
    """
    lattice = spins.copy()
    N = lattice.shape[0]
    for i in range(N):
        for j in range(N):
            A, dM = get_flip_probability_magnetization(lattice, i, j, beta)
            random_number = np.random.rand()
            if random_number < A:
                lattice[i, j] = -lattice[i, j]
    return lattice

def run(T, N, nsweeps):
    """Performs Metropolis to flip spins for nsweeps times and collect magnetization^2 / N^4
    Args: 
        T (float): temperature
        N (int): system size along an axis
        nsweeps: number of iterations to go over all spins
    Return:
        mag2: (numpy array) magnetization^2 / N^4 for each sweep
    """
    beta = 1.0 / T
    lattice = np.random.choice([1, -1], size=(N, N))
    mag2 = np.zeros(nsweeps)
    for sweep in range(nsweeps):
        lattice = flip(lattice, beta)
        M = magnetization(lattice)
        mag2[sweep] = M ** 2 / N ** 4
    return mag2
