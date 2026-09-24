import numpy as np

def Verlet(v0, x0, m, dt, omega):
    """Calculate the position and velocity of the harmonic oscillator using the velocity-Verlet algorithm
    Inputs:
    v0 : float
        The initial velocity of the harmonic oscillator.
    x0 : float
        The initial position of the harmonic oscillator.
    m : float
        The mass of the oscillator.
    dt : float
        The integration time step.
    omega: float
        The angular frequency of the oscillator.
    Output:
    [vt, xt] : list
        The updated velocity and position of the harmonic oscillator.
    """
    F_t = -m * omega ** 2 * x0
    v_half = v0 + F_t / m * (dt / 2)
    x_new = x0 + v_half * dt
    F_new = -m * omega ** 2 * x_new
    v_new = v_half + F_new / m * (dt / 2)
    return [v_new, x_new]
