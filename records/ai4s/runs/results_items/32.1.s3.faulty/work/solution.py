import numpy as np
import scipy
from scipy.constants import epsilon_0, c

def binding_force(P, phi, R, l, w, a, n):
    """Function to calculate the optical binding force between two trapped nanospheres.
    Input
    P : list of length 2
        Power of the two optical traps.
    phi : float
        Polarization direction of the optical traps.
    R : float
        Distance between the trapped nanospheres.
    l : float
        Wavelength of the optical traps.
    w : float
        Beam waist of the optical traps.
    a : float
        Radius of the trapped microspheres.
    n : float
        Refractive index of the trapped microspheres.
    Output
    F : float
        The optical binding force between two trapped nanospheres.
    """
    P1, P2 = (P[0], P[1])
    alpha = 4 * np.pi * epsilon_0 * a ** 3 * (n ** 2 - 1) / (n ** 2 + 2)
    E1 = np.sqrt(4 * P1 / (np.pi * w ** 2 * epsilon_0 * c))
    E2 = np.sqrt(4 * P2 / (np.pi * w ** 2 * epsilon_0 * c))
    k = 2 * np.pi / l
    kR = k * R
    F_xx_factor = 2 * alpha ** 2 * E1 * E2 * np.cos(phi) ** 2 / (8 * np.pi * epsilon_0 * R ** 4)
    F_xx_term = -3 * np.cos(kR) - 3 * kR * np.sin(kR) + kR ** 2 * np.cos(kR)
    F_xx = F_xx_factor * F_xx_term
    F_xy_factor = alpha ** 2 * E1 * E2 * np.sin(phi) ** 2 / (8 * np.pi * epsilon_0 * R ** 4)
    F_xy_term = 3 * np.cos(kR) + 3 * kR * np.sin(kR) - 2 * kR ** 2 * np.cos(kR) - kR ** 3 * np.sin(kR)
    F_xy = F_xy_factor * F_xy_term
    F = F_xx + F_xy
    return F
