import numpy as np

def second_diff(target, u, dx):
    """Inputs:
    target : Target cell index, int
    u      : Approximated solution value, array of floats with minimum length of 5
    dx     : Spatial interval, float
    Outputs:
    deriv  : Second order derivative of the given target cell, float
    """
    n = len(u)
    if target == 0:
        u_left = u[0]
    else:
        u_left = u[target - 1]
    if target == n - 1:
        u_right = u[n - 1]
    else:
        u_right = u[target + 1]
    u_center = u[target]
    deriv = (u_right - 2 * u_center + u_left) / dx ** 2
    return deriv
