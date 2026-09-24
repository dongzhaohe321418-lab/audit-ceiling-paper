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
    atoms = []
    sqrt3 = np.sqrt(3)
    a1_x = 3 * a / 2
    a1_y = sqrt3 * a / 2
    a2_x = 3 * a / 2
    a2_y = -sqrt3 * a / 2
    basis_A = np.array([0, 0])
    basis_B = np.array([a / 2, sqrt3 * a / 2 + s])
    for i in range(-n, n + 1):
        for j in range(-n, n + 1):
            lattice_pos = i * np.array([a1_x, a1_y]) + j * np.array([a2_x, a2_y])
            pos_A = lattice_pos + basis_A
            atoms.append([pos_A[0], pos_A[1], z])
            pos_B = lattice_pos + basis_B
            atoms.append([pos_B[0], pos_B[1], z])
    atoms = np.array(atoms)
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
        atom_pos = xyzs[i]
        distances = la.norm(xyzs - atom_pos, axis=1)
        distances[i] = np.inf
        nearest_indices = np.argsort(distances)[:3]
        neighbor_positions = xyzs[nearest_indices]
        vectors = neighbor_positions - atom_pos
        cross_products = []
        for k in range(3):
            v1 = vectors[k]
            v2 = vectors[(k + 1) % 3]
            cross = np.cross(v1, v2)
            cross_products.append(cross)
        cross_products = np.array(cross_products)
        cross_norms = la.norm(cross_products, axis=1, keepdims=True)
        cross_norms = np.where(cross_norms == 0, 1, cross_norms)
        normalized_crosses = cross_products / cross_norms
        avg_normal = np.mean(normalized_crosses, axis=0)
        avg_norm = la.norm(avg_normal)
        if avg_norm > 0:
            avg_normal = avg_normal / avg_norm
        if atom_pos[2] > 0 and avg_normal[2] > 0:
            avg_normal = -avg_normal
        elif atom_pos[2] < 0 and avg_normal[2] < 0:
            avg_normal = -avg_normal
        normed_cross_avg[i] = avg_normal
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
    r_ij_dist = la.norm(r_ij, axis=1)
    r_dot_ni = np.sum(r_ij * n_i, axis=1)
    r_dot_nj = np.sum(r_ij * n_j, axis=1)
    rho_ij_sq = r_ij_dist ** 2 - r_dot_ni ** 2
    rho_ji_sq = r_ij_dist ** 2 - r_dot_nj ** 2
    rho_ij_sq = np.maximum(rho_ij_sq, 0)
    rho_ji_sq = np.maximum(rho_ji_sq, 0)
    rho_ij = np.sqrt(rho_ij_sq)
    rho_ji = np.sqrt(rho_ji_sq)

    def f_rho(rho):
        rho_norm = rho / delta
        rho_norm_sq = rho_norm ** 2
        rho_norm_4th = rho_norm_sq ** 2
        gaussian_envelope = np.exp(-rho_norm_sq)
        polynomial = C0 + C2 * rho_norm_sq + C4 * rho_norm_4th
        return gaussian_envelope * polynomial
    f_rho_ij = f_rho(rho_ij)
    f_rho_ji = f_rho(rho_ji)
    exponential_term = np.exp(-lamda * (r_ij_dist - z0))
    bracket_term = C + f_rho_ij + f_rho_ji
    pot = exponential_term * bracket_term
    return pot
