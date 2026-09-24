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
    k = 2 * np.pi / l
    E1 = np.sqrt(4 * P1 / (np.pi * w ** 2 * epsilon_0 * c))
    E2 = np.sqrt(4 * P2 / (np.pi * w ** 2 * epsilon_0 * c))
    alpha = 4 * np.pi * epsilon_0 * a ** 3 * (n ** 2 - 1) / (n ** 2 + 2)
    kR = k * R
    cos_phi = np.cos(phi)
    cos_kR = np.cos(kR)
    sin_kR = np.sin(kR)
    F_xx_coefficient = 2 * alpha ** 2 * E1 * E2 * cos_phi ** 2 / (8 * np.pi * epsilon_0 * R ** 4)
    F_xx_term = -3 * cos_kR - 3 * kR * sin_kR + kR ** 2 * cos_kR
    F_xx = F_xx_coefficient * F_xx_term
    sin_phi = np.sin(phi)
    F_xy_coefficient = alpha ** 2 * E1 * E2 * sin_phi ** 2 / (8 * np.pi * epsilon_0 * R ** 4)
    F_xy_term = 3 * cos_kR + 3 * kR * sin_kR - 2 * kR ** 2 * cos_kR - kR ** 3 * sin_kR
    F_xy = F_xy_coefficient * F_xy_term
    F = F_xx + F_xy
    return F
