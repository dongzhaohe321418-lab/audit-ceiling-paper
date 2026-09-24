import numpy as np
import itertools

def ground_state_wavelength(L, mr):
    """Given the width of a infinite square well, provide the corresponding wavelength of the ground state eigen-state energy.
    Input:
    L (float): Width of the infinite square well (nm).
    mr (float): relative effective electron mass.
    Output:
    lmbd (float): Wavelength of the ground state energy (nm).
    """
    h = 6.626e-34
    c = 300000000.0
    m0 = 9.109e-31
    L_m = L * 1e-09
    E_ground = h ** 2 / (8 * mr * m0 * L_m ** 2)
    lmbd_m = h * c / E_ground
    lmbd = lmbd_m * 1000000000.0
    return lmbd
