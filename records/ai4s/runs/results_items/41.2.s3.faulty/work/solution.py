import numpy as np
from math import exp

def Conversion(g, pref, t, dep_order):
    """This function calculates the biomass conversion matrix M
    Inputs:
    g: growth rates based on resources, 2d numpy array with dimensions [N, R] and float elements
    pref: species' preference order, 2d numpy array with dimensions [N, R] and int elements between 1 and R
    t: temporal niches, 1d numpy array with length R and float elements
    dep_order: resource depletion order, a tuple of length R with int elements between 1 and R
    Outputs:
    M: conversion matrix of biomass from resource to species. 2d float numpy array with dimensions [R, N].
    """
    N, R = g.shape
    M = np.zeros((R, N))
    abundance = np.ones(N)
    resource_preference_idx = np.zeros(N, dtype=int)
    for niche_idx in range(R):
        current_resource = dep_order[niche_idx] - 1
        niche_duration = t[niche_idx]
        for species_idx in range(N):
            current_pref_resource = pref[species_idx, resource_preference_idx[species_idx]] - 1
            if current_pref_resource == current_resource:
                growth_rate = g[species_idx, current_resource]
                biomass_conversion = abundance[species_idx] * (exp(growth_rate * niche_duration) - 1)
                M[current_resource, species_idx] += biomass_conversion
                abundance[species_idx] *= exp(growth_rate * niche_duration)
                resource_preference_idx[species_idx] += 1
    return M

def GetResPts(M):
    """This function finds the endpoints of the feasibility convex hull
    Inputs:
    M: conversion matrix of biomass, 2d float numpy array of size [R, N]
    Outputs:
    res_pts: a set of points in the resource supply space that marks the region of feasibility. 2d float numpy array of size [R, N].
    """
    R, N = M.shape
    res_pts = np.zeros((R, N))
    for species_idx in range(N):
        resource_supply = M[:, species_idx]
        total_supply = np.sum(resource_supply)
        if total_supply > 0:
            normalized_supply = resource_supply / total_supply
        else:
            normalized_supply = np.ones(R) / R
        res_pts[:, species_idx] = normalized_supply
    return res_pts
