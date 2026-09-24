import numpy as np

def make_IC(n):
    """The function computes the initial condition mentioned above
    Inputs:
    n  : number of grid points, integer
    Outputs:
    v  : cell averaged approximation of initial condition, 1d array size n-1
    """
    x_left = -np.pi / 2
    x_right = np.pi / 2
    x = np.linspace(x_left, x_right, n)
    h = (x_right - x_left) / (n - 1)
    num_cells = n - 1
    v = np.zeros(num_cells)
    gauss_weights = np.array([5.0 / 9.0, 8.0 / 9.0, 5.0 / 9.0])
    gauss_nodes = np.array([-np.sqrt(3.0 / 5.0), 0.0, np.sqrt(3.0 / 5.0)])

    def u0(x):
        if x <= 0:
            return np.sin(x) - 1
        else:
            return np.sin(x) + 1
    for i in range(num_cells):
        x_left_cell = x[i]
        x_right_cell = x[i + 1]
        x_mid = (x_left_cell + x_right_cell) / 2.0
        x_half_width = (x_right_cell - x_left_cell) / 2.0
        integral = 0.0
        for j in range(3):
            x_quad = x_mid + x_half_width * gauss_nodes[j]
            integral += gauss_weights[j] * u0(x_quad)
        integral *= x_half_width
        v[i] = integral / h
    return v

def LaxF(uL, uR):
    """This function computes Lax-Friedrichs numerical flux.
    Inputs: 
    uL : Cell averaged value at cell i, float
    uR : Cell averaged value at cell i+1, float
    Output: flux, float
    """
    f_uL = 0.5 * uL ** 2
    f_uR = 0.5 * uR ** 2
    alpha_LF = 2.0
    flux = 0.5 * (f_uL + f_uR - alpha_LF * (uR - uL))
    return flux
