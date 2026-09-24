import numpy as np
from math import exp
from scipy.integrate import solve_ivp

def GetComp(d):
    """Concentration matrix of complementary 2-mers
    Inputs:
    d: concentration of 2-mers, numpy float array with dimensions [Z, Z]
    Outputs:
    dcomp: concentration of 2-mers, numpy float array with dimensions [Z, Z], where dcomp[i, j]==d[j', i'].
    """
    Z = d.shape[0]
    dcomp = np.zeros((Z, Z))
    comp_idx = np.zeros(Z, dtype=int)
    for i in range(Z):
        if i < Z // 2:
            comp_idx[i] = i + Z // 2
        else:
            comp_idx[i] = i - Z // 2
    for i in range(Z):
        for j in range(Z):
            dcomp[i, j] = d[comp_idx[j], comp_idx[i]]
    return dcomp
