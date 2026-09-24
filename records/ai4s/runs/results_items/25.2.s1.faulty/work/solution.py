import numpy as np
from scipy.integrate import solve_ivp
from functools import partial

def SpeciesGrowth(spc, res, b, c, w, m):
    """This function calcuates the species growth rate
    Inputs:
    spc: species abundance, 1D array of length N
    res: resource level, 1D array of length R
    b: inverse timescale of species dynamics, 1D array of length N
    c: consumer-resource conversion matrix, 2D array of shape [N, R]
    w: value/efficiency of resoruce, 1D array of length R
    m: species maintainance cost, 1D array of length N
    Outputs: 
    g_spc: growth rate of species, 1D array of length N
    """
    weighted_resources = c @ (w * res)
    g_spc = b * (weighted_resources - m)
    return g_spc

def ResourcesUpdate(spc, res, c, r, K):
    """This function calculates the changing rates of resources
    Inputs:
    spc: species population, 1D array of length N
    res: resource abundance, 1D array of length R
    c: consumer-resource conversion matrix, 2D array of shape [N, R]
    r: inverse timescale of resource growth, 1D array of length R
    K: resource carrying capacity, 1D array of length R
    Outputs: 
    f_res: growth rate of resources, 1D array of length R
    """
    logistic_growth = r * (1 - res / K)
    consumption = c.T @ spc
    f_res = res * (logistic_growth - consumption)
    return f_res
