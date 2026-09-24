import itertools
import numpy as np
from math import *

def allowed_orders(pref):
    """Check allowed depletion orders for a set of species with given preference orders
    Input:
    pref: species' preference order, 2d numpy array with dimensions [N, R] and int elements between 1 and R
    Output:
    allowed_orders_list: n_allowed by R, list of tuples with int elements betweem 1 and R. 
    """
    pref = np.asarray(pref)
    N, R = pref.shape
    allowed_orders_list = []
    for depletion_order in itertools.permutations(range(1, R + 1)):
        is_allowed = True
        for species_idx in range(N):
            species_pref = pref[species_idx]
            pref_position = {resource: pos for pos, resource in enumerate(species_pref)}
            for i, resource_being_depleted in enumerate(depletion_order):
                for preferred_resource in species_pref:
                    pref_pos_preferred = pref_position[preferred_resource]
                    pref_pos_current = pref_position[resource_being_depleted]
                    if pref_pos_preferred < pref_pos_current:
                        if preferred_resource not in depletion_order[:i + 1]:
                            is_allowed = False
                            break
                if not is_allowed:
                    break
            if not is_allowed:
                break
        if is_allowed:
            allowed_orders_list.append(depletion_order)
    return allowed_orders_list

def G_mat(g, pref, dep_order):
    """Convert to growth rates based on temporal niches
    Input
    g: growth rates based on resources, 2d numpy array with dimensions [N, R] and float elements
    pref: species' preference order, 2d numpy array with dimensions [N, R] and int elements between 1 and R
    dep_order: resource depletion order, a tuple of length R with int elements between 1 and R
    Output
    G: "converted" growth rates based on temporal niches, 2d numpy array with dimensions [N, R]
    """
    g = np.asarray(g)
    pref = np.asarray(pref)
    N, R = g.shape
    G = np.zeros((N, R))
    for niche_idx in range(R):
        available_resources = set(dep_order[niche_idx:])
        for species_idx in range(N):
            species_pref = pref[species_idx]
            best_available_resource = None
            for preferred_resource in species_pref:
                if preferred_resource in available_resources:
                    best_available_resource = preferred_resource
                    break
            if best_available_resource is not None:
                resource_idx = best_available_resource - 1
                G[species_idx, niche_idx] = g[species_idx, resource_idx]
            else:
                G[species_idx, niche_idx] = 0.0
    return G
