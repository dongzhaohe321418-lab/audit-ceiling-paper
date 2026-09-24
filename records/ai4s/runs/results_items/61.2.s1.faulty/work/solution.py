import numpy as np

def Bmat(pa):
    """Calculate the B matrix.
    Input
    pa = (a,b,c,alpha,beta,gamma)
    a,b,c: the lengths a, b, and c of the three cell edges meeting at a vertex, float in the unit of angstrom
    alpha,beta,gamma: the angles alpha, beta, and gamma between those edges, float in the unit of degree
    Output
    B: a 3*3 matrix, float
    """
    a, b, c, alpha, beta, gamma = pa
    alpha_rad = np.deg2rad(alpha)
    beta_rad = np.deg2rad(beta)
    gamma_rad = np.deg2rad(gamma)
    a_vec = np.array([a, 0, 0])
    b_vec = np.array([b * np.cos(gamma_rad), b * np.sin(gamma_rad), 0])
    c_x = c * np.cos(beta_rad)
    c_y = c * np.sin(beta_rad) * np.cos(alpha_rad)
    c_z = c * np.sqrt(np.sin(beta_rad) ** 2 * np.sin(alpha_rad) ** 2 - (np.sin(beta_rad) * np.cos(alpha_rad) * np.sin(gamma_rad) - np.cos(beta_rad) * np.cos(gamma_rad)) ** 2 / np.sin(gamma_rad) ** 2)
    volume = a * b * c * np.sqrt(1 + 2 * np.cos(alpha_rad) * np.cos(beta_rad) * np.cos(gamma_rad) - np.cos(alpha_rad) ** 2 - np.cos(beta_rad) ** 2 - np.cos(gamma_rad) ** 2)
    c_vec = np.array([c_x, c_y, c_z])
    A_direct = np.column_stack([a_vec, b_vec, c_vec])
    b1 = np.cross(b_vec, c_vec) / np.dot(a_vec, np.cross(b_vec, c_vec))
    b2 = np.cross(c_vec, a_vec) / np.dot(b_vec, np.cross(c_vec, a_vec))
    b3 = np.cross(a_vec, b_vec) / np.dot(c_vec, np.cross(a_vec, b_vec))
    B = np.column_stack([b1, b2, b3])
    return B

def q_cal(p, b_c, det_d, p_s, wl):
    """Calculate the momentum transfer Q at detector pixel (x,y). Here we're employing the convention, k=1/\\lambda,
    k represents the x-ray momentum and \\lambda denotes the wavelength.
    Input
    p: detector pixel (x,y), a tuple of two integer
    b_c: incident beam center at detector pixel (xc,yc), a tuple of float
    det_d: sample distance to the detector, float in the unit of mm
    p_s: detector pixel size, and each pixel is a square, float in the unit of mm
    wl: X-ray wavelength, float in the unit of angstrom
    Output
    Q: a 3x1 matrix, float in the unit of inverse angstrom
    """
    x, y = p
    xc, yc = b_c
    delta_x_det = (x - xc) * p_s
    delta_y_det = (y - yc) * p_s
    x_lab = det_d
    y_lab = -delta_x_det
    z_lab = -delta_y_det
    direction = np.array([x_lab, y_lab, z_lab])
    magnitude = np.linalg.norm(direction)
    unit_direction = direction / magnitude
    k = 1.0 / wl
    k_s = k * unit_direction
    k_i = np.array([k, 0.0, 0.0])
    Q = k_s - k_i
    Q = Q.reshape(3, 1)
    return Q
