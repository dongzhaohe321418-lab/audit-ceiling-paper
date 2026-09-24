import os
import math
import time
import numpy as np
import scipy as sp
from mpl_toolkits.mplot3d import Axes3D
import pickle
from scipy.constants import  Avogadro

def dist(r1, r2, L):
    """Calculate the minimum image distance between two atoms in a periodic cubic system.
    Parameters:
    r1 : The (x, y, z) coordinates of the first atom.
    r2 : The (x, y, z) coordinates of the second atom.
    L (float): The length of the side of the cubic box.
    Returns:
    float: The minimum image distance between the two atoms.
    """
    r1 = np.array(r1)
    r2 = np.array(r2)
    delta = np.abs(r1 - r2)
    delta = np.minimum(delta, L - delta)
    distance = np.linalg.norm(delta)
    return distance

def E_ij(r, sigma, epsilon, rc):
    """Calculate the combined truncated and shifted Lennard-Jones potential energy and,
    if specified, the truncated and shifted Yukawa potential energy between two particles.
    Parameters:
    r (float): The distance between particles i and j.
    sigma (float): The distance at which the inter-particle potential is zero for the Lennard-Jones potential.
    epsilon (float): The depth of the potential well for the Lennard-Jones potential.
    rc (float): The cutoff distance beyond which the potentials are truncated and shifted to zero.
    Returns:
    float: The combined potential energy between the two particles, considering the specified potentials.
    """
    if r > rc:
        return 0.0
    sigma_over_r_6 = (sigma / r) ** 6
    sigma_over_r_12 = sigma_over_r_6 ** 2
    V_LJ_r = 4 * epsilon * (sigma_over_r_12 - sigma_over_r_6)
    sigma_over_rc_6 = (sigma / rc) ** 6
    sigma_over_rc_12 = sigma_over_rc_6 ** 2
    V_LJ_rc = 4 * epsilon * (sigma_over_rc_12 - sigma_over_rc_6)
    E = V_LJ_r - V_LJ_rc
    return E
