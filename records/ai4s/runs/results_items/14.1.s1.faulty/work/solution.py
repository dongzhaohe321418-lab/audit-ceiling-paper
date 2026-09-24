import numpy as np

def harmonic_mannella_leapfrog(x0, v0, t0, steps, taup, omega0, vrms):
    """Function to employ Mannella's leapfrog method to solve the Langevin equation of a microsphere optically trapped in the gas.
    Input
    x0 : float
        Initial position of the microsphere.
    v0 : float
        Initial velocity of the microsphere.
    t0 : float
        Total simulation time.
    steps : int
        Number of integration steps.
    taup : float
        Momentum relaxation time of the trapped microsphere in the gas (often referred to as the particle relaxation time).
    omega0 : float
        Resonant frequency of the harmonic potential (optical trap).
    vrms : float
        Root mean square velocity of the trapped microsphere in the gas.
    Output
    x : float
        Final position of the microsphere after the simulation time.
    """
    dt = t0 / steps
    x = x0
    v = v0
    half_dt = dt / 2.0
    damping_coeff = 1.0 / (2.0 * taup)
    noise_coeff = np.sqrt(2.0 / taup) * vrms
    velocity_denominator = 1.0 + dt * damping_coeff
    sqrt_dt = np.sqrt(dt)
    for _ in range(steps):
        x_half = x + v * half_dt
        dW = np.random.normal(0.0, sqrt_dt)
        v_numerator = v - v * dt * damping_coeff - omega0 ** 2 * x_half * dt + noise_coeff * dW
        v = v_numerator / velocity_denominator
        x = x_half + v * half_dt
    return x
