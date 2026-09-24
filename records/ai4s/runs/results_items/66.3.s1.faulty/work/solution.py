import numpy as np
import numpy.linalg as la

def generate_monolayer_graphene(s, a, z, n):
    """Generate the geometry of monolayer graphene.
    Args:
        s (float): Horizontal in-plane sliding distance.
        a (float): Lattice constant.
        z (float): z-coordinate
        n (int): supercell size
    Returns:
        atoms (np.array): Array containing the x, y, and z coordinates of the atoms.
    """
    a1 = np.array([a, 0.0])
    a2 = np.array([a / 2.0, a * np.sqrt(3) / 2.0])
    basis_A = np.array([0.0, 0.0])
    basis_B = np.array([a / 2.0, a / (2.0 * np.sqrt(3))])
    atoms_list = []
    for i in range(-n, n + 1):
        for j in range(-n, n + 1):
            lattice_point = i * a1 + j * a2
            pos_A = lattice_point + basis_A
            pos_A[1] += s
            atoms_list.append([pos_A[0], pos_A[1], z])
            pos_B = lattice_point + basis_B
            pos_B[1] += s
            atoms_list.append([pos_B[0], pos_B[1], z])
    atoms = np.array(atoms_list)
    return atoms

def assign_normals(xyzs):
    """Assign normal vectors on the given atoms
    Args:
        xyzs (np.array): Shape (natoms, 3)
    Returns:
        normed_cross_avg (np.array): Shape (natoms, 3)
    """
    natoms = xyzs.shape[0]
    normed_cross_avg = np.zeros((natoms, 3))
    for i in range(natoms):
        vectors_to_others = xyzs - xyzs[i]
        distances = la.norm(vectors_to_others, axis=1)
        nearest_indices = np.argsort(distances)[1:4]
        v1 = vectors_to_others[nearest_indices[0]]
        v2 = vectors_to_others[nearest_indices[1]]
        v3 = vectors_to_others[nearest_indices[2]]
        cross1 = np.cross(v1, v2)
        cross2 = np.cross(v2, v3)
        cross3 = np.cross(v3, v1)
        norm_cross1 = cross1 / la.norm(cross1)
        norm_cross2 = cross2 / la.norm(cross2)
        norm_cross3 = cross3 / la.norm(cross3)
        avg_cross = (norm_cross1 + norm_cross2 + norm_cross3) / 3.0
        avg_norm = la.norm(avg_cross)
        if avg_norm > 1e-10:
            normed_avg = avg_cross / avg_norm
        else:
            normed_avg = avg_cross
        if xyzs[i, 2] > 0 and normed_avg[2] > 0:
            normed_avg = -normed_avg
        elif xyzs[i, 2] < 0 and normed_avg[2] < 0:
            normed_avg = -normed_avg
        normed_cross_avg[i] = normed_avg
    return normed_cross_avg

def potential_repulsive(r_ij, n_i, n_j, z0, C, C0, C2, C4, delta, lamda):
    """Define repulsive potential.
    Args:
        r_ij: (nmask, 3)
        n_i: (nmask, 3)
        n_j: (nmask, 3)
        z0 (float): KC parameter
        C (float): KC parameter
        C0 (float): KC parameter
        C2 (float): KC parameter
        C4 (float): KC parameter
        delta (float): KC parameter
        lamda (float): KC parameter
    Returns:
        pot (nmask): values of repulsive potential for the given atom pairs.
    """
    r_ij_magnitude = la.norm(r_ij, axis=1)
    r_dot_ni = np.sum(r_ij * n_i, axis=1)
    r_dot_nj = np.sum(r_ij * n_j, axis=1)
    rho_ij_sq = r_ij_magnitude ** 2 - r_dot_ni ** 2
    rho_ji_sq = r_ij_magnitude ** 2 - r_dot_nj ** 2
    rho_ij_sq = np.maximum(rho_ij_sq, 0.0)
    rho_ji_sq = np.maximum(rho_ji_sq, 0.0)
    rho_ij = np.sqrt(rho_ij_sq)
    rho_ji = np.sqrt(rho_ji_sq)
    rho_ij_normalized = rho_ij / delta
    rho_ji_normalized = rho_ji / delta
    f_rho_ij = np.exp(-rho_ij_normalized ** 2) * (C0 + C2 * rho_ij_normalized ** 2 + C4 * rho_ij_normalized ** 4)
    f_rho_ji = np.exp(-rho_ji_normalized ** 2) * (C0 + C2 * rho_ji_normalized ** 2 + C4 * rho_ji_normalized ** 4)
    exp_factor = np.exp(-lamda * (r_ij_magnitude - z0))
    pot = exp_factor * (C + f_rho_ij + f_rho_ji)
    return pot
