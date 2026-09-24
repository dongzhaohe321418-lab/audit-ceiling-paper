import numpy as np
from scipy import integrate, optimize

def f_x(x, En):
    """Return the value of f(x) with energy En
    Input
    x: coordinate x; a float or a 1D array of float
    En: energy; a float
    Output
    f_x: the value of f(x); a float or a 1D array of float
    """
    return x ** 2 - En

def Numerov(f_in, u_b, up_b, step):
    """Given precomputed function f(x), solve the differential equation u''(x) = f(x)*u(x)
    using the Numerov method.
    Inputs:
    - f_in: input function f(x); a 1D array of float representing the function values at discretized points
    - u_b: the value of u at boundary; a float
    - up_b: the derivative of u at boundary; a float
    - step: step size; a float.
    Output:
    - u: u(x); a 1D array of float representing the solution.
    """
    n = len(f_in)
    u = np.zeros(n)
    u[0] = u_b
    u[1] = u_b + step * up_b + step ** 2 / 2 * f_in[0] * u_b
    h2 = step ** 2
    for i in range(1, n - 1):
        numerator = 2 * u[i] * (1 - h2 * f_in[i] / 12) - u[i - 1] * (1 - h2 * f_in[i - 1] / 12) + h2 * f_in[i] * u[i]
        denominator = 1 - h2 * f_in[i + 1] / 12
        u[i + 1] = numerator / denominator
    return u

def Solve_Schrod(x, En, u_b, up_b, step):
    """Input
    x: coordinate x; a float or a 1D array of float
    En: energy; a float
    u_b: value of u(x) at one boundary for the Numerov function; a float
    up_b: value of the derivative of u(x) at one boundary for the Numerov function; a float
    step: the step size for the Numerov method; a float
    Output
    u_norm: normalized u(x); a float or a 1D array of float
    """
    x = np.atleast_1d(x)
    f_in = x ** 2 - En
    u = Numerov(f_in, u_b, up_b, step)
    u_squared = u ** 2
    norm_integral = integrate.simpson(u_squared, x=x)
    u_norm = u / np.sqrt(norm_integral)
    return u_norm

def count_sign_changes(solv_schrod):
    """Input
    solv_schrod: a 1D array
    Output
    sign_changes: number of times of sign change occurrence; an int
    """
    solv_schrod = np.atleast_1d(solv_schrod)
    consecutive_products = solv_schrod[:-1] * solv_schrod[1:]
    sign_changes = np.sum(consecutive_products < 0)
    return int(sign_changes)
