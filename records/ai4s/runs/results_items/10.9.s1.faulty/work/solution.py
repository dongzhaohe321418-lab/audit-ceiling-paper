import numpy as np
from scipy.special import erfc

def get_alpha(recvec, alpha_scaling=5):
    """Calculate the alpha value for the Ewald summation, scaled by a specified factor.
    Parameters:
        recvec (np.ndarray): A 3x3 array representing the reciprocal lattice vectors.
        alpha_scaling (float): A scaling factor applied to the alpha value. Default is 5.
    Returns:
        float: The calculated alpha value.
    """
    recvec_magnitudes = np.linalg.norm(recvec, axis=1)
    nonzero_magnitudes = recvec_magnitudes[recvec_magnitudes > 1e-10]
    if len(nonzero_magnitudes) == 0:
        min_magnitude = 1.0
    else:
        min_magnitude = np.min(nonzero_magnitudes)
    alpha = alpha_scaling * min_magnitude
    return alpha

def get_lattice_coords(latvec, nlatvec=1):
    """Generate lattice coordinates based on the provided lattice vectors.
    Parameters:
        latvec (np.ndarray): A 3x3 array representing the lattice vectors.
        nlatvec (int): The number of lattice coordinates to generate in each direction.
    Returns:
        np.ndarray: An array of shape ((2 * nlatvec + 1)^3, 3) containing the lattice coordinates.
    """
    indices = np.arange(-nlatvec, nlatvec + 1)
    n1, n2, n3 = np.meshgrid(indices, indices, indices, indexing='ij')
    n1_flat = n1.flatten()
    n2_flat = n2.flatten()
    n3_flat = n3.flatten()
    lattice_coords = n1_flat[:, np.newaxis] * latvec[0] + n2_flat[:, np.newaxis] * latvec[1] + n3_flat[:, np.newaxis] * latvec[2]
    return lattice_coords

def distance_matrix(configs):
    """Args:
        configs (np.array): (nparticles, 3)
    Returns:
        distances (np.array): distance vector for each particle pair. Shape (npairs, 3), where npairs = (nparticles choose 2)
        pair_idxs (list of tuples): list of pair indices
    """
    nparticles = configs.shape[0]
    pair_idxs = []
    distances_list = []
    for i in range(nparticles):
        for j in range(i + 1, nparticles):
            pair_idxs.append((i, j))
            distance_vector = configs[j] - configs[i]
            distances_list.append(distance_vector)
    distances = np.array(distances_list) if distances_list else np.empty((0, 3))
    return (distances, pair_idxs)

def real_cij(distances, lattice_coords, alpha):
    """Calculate the real-space terms for the Ewald summation over particle pairs.
    Parameters:
        distances (np.ndarray): An array of shape (natoms, npairs, 1, 3) representing the distance vectors between pairs of particles where npairs = (nparticles choose 2).
        lattice_coords (np.ndarray): An array of shape (natoms, 1, ncells, 3) representing the lattice coordinates.
        alpha (float): The alpha value used for the Ewald summation.
    Returns:
        np.ndarray: An array of shape (npairs,) representing the real-space sum for each particle pair.
    """
    r_plus_n = distances + lattice_coords
    magnitudes = np.linalg.norm(r_plus_n, axis=3)
    magnitudes_safe = np.where(magnitudes < 1e-10, 10000000000.0, magnitudes)
    erfc_term = erfc(alpha * magnitudes_safe) / magnitudes_safe
    erfc_term = np.where(magnitudes < 1e-10, 0, erfc_term)
    cij = np.sum(np.sum(erfc_term, axis=2), axis=0)
    return cij

def sum_real_cross(atom_charges, atom_coords, configs, lattice_coords, alpha):
    """Calculate the sum of real-space cross terms for the Ewald summation.
    Parameters:
        atom_charges (np.ndarray): An array of shape (natoms,) representing the charges of the atoms.
        atom_coords (np.ndarray): An array of shape (natoms, 3) representing the coordinates of the atoms.
        configs (np.ndarray): An array of shape (nelectrons, 3) representing the configurations of the electrons.
        lattice_coords (np.ndarray): An array of shape (ncells, 3) representing the lattice coordinates.
        alpha (float): The alpha value used for the Ewald summation.
    Returns:
        float: The sum of ion-ion, electron-ion, and electron-electron cross terms.
    """
    natoms = atom_coords.shape[0]
    nelectrons = configs.shape[0]
    ntotal = natoms + nelectrons
    all_coords = np.vstack([atom_coords, configs])
    all_charges = np.hstack([atom_charges, -np.ones(nelectrons)])
    distances_list = []
    pair_idxs = []
    for i in range(ntotal):
        for j in range(i + 1, ntotal):
            pair_idxs.append((i, j))
            distance_vector = all_coords[j] - all_coords[i]
            distances_list.append(distance_vector)
    distances = np.array(distances_list) if distances_list else np.empty((0, 3))
    if len(distances) == 0:
        return 0.0
    npairs = distances.shape[0]
    distances_reshaped = distances[np.newaxis, :, np.newaxis, :]
    lattice_coords_reshaped = lattice_coords[np.newaxis, np.newaxis, :, :]
    cij = real_cij(distances_reshaped, lattice_coords_reshaped, alpha)
    energy_sum = 0.0
    for idx, (i, j) in enumerate(pair_idxs):
        energy_sum += all_charges[i] * all_charges[j] * cij[idx]
    return energy_sum

def generate_gpoints(recvec, gmax):
    """Generate a grid of g-points for reciprocal space based on the provided lattice vectors.
    Parameters:
        recvec (np.ndarray): A 3x3 array representing the reciprocal lattice vectors.
        gmax (int): The maximum integer number of lattice points to include in one positive direction.
    Returns:
        np.ndarray: An array of shape (nk, 3) representing the grid of g-points.
    """
    gpoints_list = []
    for n1 in range(0, gmax + 1):
        for n2 in range(-gmax, gmax + 1):
            for n3 in range(-gmax, gmax + 1):
                if n1 == 0 and n2 == 0 and (n3 == 0):
                    continue
                if n1 == 0 and n2 == 0 and (n3 < 0):
                    continue
                if n1 == 0 and n2 < 0:
                    continue
                gpoint = n1 * recvec[0] + n2 * recvec[1] + n3 * recvec[2]
                gpoints_list.append(gpoint)
    gpoints_all = np.array(gpoints_list) if gpoints_list else np.empty((0, 3))
    return gpoints_all

def select_big_weights(gpoints_all, cell_volume, alpha, tol=1e-10):
    """Filter g-points based on weight in reciprocal space.
    Parameters:
        gpoints_all (np.ndarray): An array of shape (nk, 3) representing all g-points.
        cell_volume (float): The volume of the unit cell.
        alpha (float): The alpha value used for the Ewald summation.
        tol (float, optional): The tolerance for filtering weights. Default is 1e-10.
    Returns:
        tuple: 
            gpoints (np.array): An array of shape (nk, 3) containing g-points with significant weights.
            gweights (np.array): An array of shape (nk,) containing the weights of the selected g-points.       
    """
    k_magnitudes = np.linalg.norm(gpoints_all, axis=1)
    weights = np.zeros_like(k_magnitudes)
    nonzero_mask = k_magnitudes > 1e-10
    k_safe = k_magnitudes[nonzero_mask]
    weights[nonzero_mask] = 4 * np.pi / cell_volume * np.exp(-k_safe ** 2 / (4 * alpha ** 2)) / k_safe ** 2
    significant_mask = weights > tol
    gpoints = gpoints_all[significant_mask]
    gweights = weights[significant_mask]
    return (gpoints, gweights)

def sum_recip(atom_charges, atom_coords, configs, gweights, gpoints):
    """Calculate the reciprocal lattice sum for the Ewald summation.
    Parameters:
        atom_charges (np.ndarray): An array of shape (natoms,) representing the charges of the atoms.
        atom_coords (np.ndarray): An array of shape (natoms, 3) representing the coordinates of the atoms.
        configs (np.ndarray): An array of shape (nelectrons, 3) representing the configurations of the electrons.
        gweights (np.ndarray): An array of shape (nk,) representing the weights of the g-points.
        gpoints (np.ndarray): An array of shape (nk, 3) representing the g-points.
    Returns:
        float: The reciprocal lattice sum.
    """
    natoms = atom_coords.shape[0]
    nelectrons = configs.shape[0]
    all_coords = np.vstack([atom_coords, configs])
    all_charges = np.hstack([atom_charges, -np.ones(nelectrons)])
    energy_sum = 0.0
    for k_idx, gpoint in enumerate(gpoints):
        k_dot_r = np.dot(all_coords, gpoint)
        exp_phase = np.exp(1j * k_dot_r)
        structure_factor = np.sum(all_charges * exp_phase)
        magnitude_squared = np.abs(structure_factor) ** 2
        energy_sum += gweights[k_idx] * magnitude_squared
    return energy_sum

def sum_real_self(atom_charges, nelec, alpha):
    """Calculate the real-space summation of the self terms for the Ewald summation.
    Parameters:
        atom_charges (np.ndarray): An array of shape (natoms,) representing the charges of the atoms.
        nelec (int): The number of electrons.
        alpha (float): The alpha value used for the Ewald summation.
    Returns:
        float: The real-space sum of the self terms.
    """
    atom_charge_squared_sum = np.sum(atom_charges ** 2)
    electron_charge_squared_sum = nelec
    total_charge_squared_sum = atom_charge_squared_sum + electron_charge_squared_sum
    val = -alpha / np.sqrt(np.pi) * total_charge_squared_sum
    return val
