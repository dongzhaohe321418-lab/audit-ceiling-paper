import numpy as np
from scipy.integrate import solve_bvp

def f(z, y, Pssat, Ppsat, N, sigma_ap, sigma_ep, sigma_as, sigma_es, gamma_p, alpha_p, gamma_s, alpha_s):
    """System of differential equations representing the rate equations of the fiber laser.
    Parameters:
    z : float
        Spatial variable along the fiber's length, representing the position.
    y : ndarray
        Array containing the power values of [forward pump, backward pump, forward signal, backward signal].
    Pssat : float
        Saturation power for the signal.
    Ppsat : float
        Saturation power for the pump.
    N : float
        Total ion population in the fiber.
    sigma_ap : float
        Absorption cross-section for the pump.
    sigma_ep : float
        Emission cross-section for the pump.
    sigma_as : float
        Absorption cross-section for the signal.
    sigma_es : float
        Emission cross-section for the signal.
    gamma_p : float
        Gain coefficient for the pump.
    alpha_p : float
        Loss coefficient for the pump.
    gamma_s : float
        Gain coefficient for the signal.
    alpha_s : float
        Loss coefficient for the signal.
    Returns: ndarray
    The rate of change of the power values for the pump and signal along the fiber:
        dydz[0]: Rate of change of forward pump power.
        dydz[1]: Rate of change of backward pump power.
        dydz[2]: Rate of change of forward signal power.
        dydz[3]: Rate of change of backward signal power.
    """
    Pp_plus = y[0]
    Pp_minus = y[1]
    Ps_plus = y[2]
    Ps_minus = y[3]
    Pp_total = Pp_plus + Pp_minus
    Ps_total = Ps_plus + Ps_minus
    numerator = sigma_ap / (sigma_ap + sigma_ep) * (Pp_total / Ppsat) + sigma_as / (sigma_as + sigma_es) * (Ps_total / Pssat)
    denominator = Pp_total / Ppsat + 1.0 + Ps_total / Pssat
    if denominator == 0:
        N2_N_ratio = 0.0
    else:
        N2_N_ratio = numerator / denominator
    N2 = N2_N_ratio * N
    pump_coeff = sigma_ap * N - (sigma_ap + sigma_ep) * N2
    signal_coeff = (sigma_es + sigma_as) * N2 - sigma_as * N
    dPp_plus_dz = -gamma_p * pump_coeff * Pp_plus - alpha_p * Pp_plus
    dPp_minus_dz = gamma_p * pump_coeff * Pp_minus + alpha_p * Pp_minus
    dPs_plus_dz = gamma_s * signal_coeff * Ps_plus - alpha_s * Ps_plus
    dPs_minus_dz = -gamma_s * signal_coeff * Ps_minus + alpha_s * Ps_minus
    dydz = np.array([dPp_plus_dz, dPp_minus_dz, dPs_plus_dz, dPs_minus_dz])
    return dydz

def bc(ya, yb, Ppl, Ppr, R1, R2):
    """Define the boundary conditions for the fiber laser.
    Parameters:
    ya : ndarray
        Array of power values at the start of the fiber. Contains values corresponding to:
        ya[0] - Power of the forward pump at the fiber input.
        ya[1] - Power of the backward pump at the fiber input.
        ya[2] - Power of the forward signal at the fiber input.
        ya[3] - Power of the backward signal at the fiber input.
    yb : ndarray
        Array of power values at the end of the fiber. Contains values corresponding to:
        yb[0] - Power of the forward pump at the fiber output.
        yb[1] - Power of the backward pump at the fiber output.
        yb[2] - Power of the forward signal at the fiber output.
        yb[3] - Power of the backward signal at the fiber output.
    Ppl : float
        Input power for the left pump, affecting the starting boundary of the laser.
    Ppr : float
        Input power for the right pump, affecting the ending boundary of the laser.
    R1 : float
        Reflectivity of the input mirror, modifying the behavior of the light at the fiber's start.
    R2 : float
        Reflectivity of the output mirror, modifying the behavior of the light at the fiber's end.
    Returns:
    ndarray
        An array of four boundary conditions calculated as follows:
        bc[0]: boudary condition for rate of change of forward pump power.
        bc[1]: boudary condition for rate of change of backward pump power.
        bc[2]: boudary condition for rate of change of forward signal power.
        bc[3]: boudary condition for rate of change of backward signal power.
    """
    bc_0 = ya[0] - Ppl
    bc_1 = yb[1] - Ppr
    bc_2 = ya[2] - R1 * ya[3]
    bc_3 = yb[3] - R2 * yb[2]
    return np.array([bc_0, bc_1, bc_2, bc_3])
