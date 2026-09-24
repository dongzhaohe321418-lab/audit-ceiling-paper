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
    N, R = pref.shape
    all_orders = list(itertools.permutations(range(1, R + 1)))
    allowed_orders_list = []
    for order in all_orders:
        depletion_rank = {resource: rank for rank, resource in enumerate(order)}
        is_allowed = True
        for species_idx in range(N):
            preference = pref[species_idx]
            for i in range(len(preference) - 1):
                preferred_resource = preference[i]
                less_preferred_resource = preference[i + 1]
                if depletion_rank[preferred_resource] > depletion_rank[less_preferred_resource]:
                    is_allowed = False
                    break
            if not is_allowed:
                break
        if is_allowed:
            allowed_orders_list.append(order)
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
    N, R = g.shape
    G = np.zeros((N, R))
    for j in range(R):
        depleted_resources = set(dep_order[:j])
        available_resources = set(range(1, R + 1)) - depleted_resources
        for i in range(N):
            for preferred_resource in pref[i]:
                if preferred_resource in available_resources:
                    resource_idx = preferred_resource - 1
                    G[i, j] = g[i, resource_idx]
                    break
    return G
