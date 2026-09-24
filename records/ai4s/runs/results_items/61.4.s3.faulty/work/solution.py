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
    alpha_rad = np.radians(alpha)
    beta_rad = np.radians(beta)
    gamma_rad = np.radians(gamma)
    a_vec = np.array([a, 0, 0])
    b_vec = np.array([b * np.cos(gamma_rad), b * np.sin(gamma_rad), 0])
    cos_A = (np.cos(alpha_rad) - np.cos(beta_rad) * np.cos(gamma_rad)) / (np.sin(beta_rad) * np.sin(gamma_rad))
    sin_A = np.sqrt(1 - cos_A ** 2)
    c_vec = np.array([c * np.cos(beta_rad), c * np.sin(beta_rad) * cos_A, c * np.sin(beta_rad) * sin_A])
    volume = np.dot(a_vec, np.cross(b_vec, c_vec))
    b1 = np.cross(b_vec, c_vec) / volume
    b2 = np.cross(c_vec, a_vec) / volume
    b3 = np.cross(a_vec, b_vec) / volume
    B_raw = np.column_stack([b1, b2, b3])
    x_star = b1 / np.linalg.norm(b1)
    z_star_direction = np.cross(b1, b2)
    z_star = z_star_direction / np.linalg.norm(z_star_direction)
    y_star = np.cross(z_star, x_star)
    y_star = y_star / np.linalg.norm(y_star)
    R = np.column_stack([x_star, y_star, z_star])
    B = R.T @ B_raw
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
    x_pix, y_pix = p
    xc, yc = b_c
    k = 1.0 / wl
    x_det = (x_pix - xc) * p_s
    y_det = (y_pix - yc) * p_s
    k_s_cart = np.array([det_d, -x_det, -y_det])
    k_s_magnitude = np.linalg.norm(k_s_cart)
    k_s_unit = k_s_cart / k_s_magnitude
    k_s = k * k_s_unit
    k_i = np.array([k, 0.0, 0.0])
    Q = k_s - k_i
    Q = Q.reshape(3, 1)
    return Q

def u_triple(pa, H1, H2, p1, p2, b_c, det_d, p_s, wl, z1, z2, z_s):
    """Calculate two orthogonal unit-vector triple t_i_c and t_i_g. Frame z starts from 0
    Input
    pa = (a,b,c,alpha,beta,gamma)
    a,b,c: the lengths a, b, and c of the three cell edges meeting at a vertex, float in the unit of angstrom
    alpha,beta,gamma: the angles alpha, beta, and gamma between those edges, float in the unit of degree
    H1 = (h1,k1,l1),primary reflection, h1,k1,l1 is integer
    H2 = (h2,k2,l2),secondary reflection, h2,k2,l2 is integer
    p1: detector pixel (x1,y1), a tuple of two integer
    p2: detector pixel (x2,y2), a tuple of two integer
    b_c: incident beam center at detector pixel (xc,yc), a tuple of float
    det_d: sample distance to the detector, float in the unit of mm
    p_s: detector pixel size, and each pixel is a square, float in the unit of mm
    wl: X-ray wavelength, float in the unit of angstrom
    z1,z2: frame number, integer
    z_s: step size in the φ rotation, float in the unit of degree
    Output
    t_c_t_g: tuple (t_c,t_g), t_c = (t1c,t2c,t3c) and t_g = (t1g,t2g,t3g).
    Each element inside t_c and t_g is a 3x1 matrix, float
    """
    a, b, c, alpha, beta, gamma = pa
    alpha_rad = np.radians(alpha)
    beta_rad = np.radians(beta)
    gamma_rad = np.radians(gamma)
    a_vec = np.array([a, 0, 0])
    b_vec = np.array([b * np.cos(gamma_rad), b * np.sin(gamma_rad), 0])
    cos_A = (np.cos(alpha_rad) - np.cos(beta_rad) * np.cos(gamma_rad)) / (np.sin(beta_rad) * np.sin(gamma_rad))
    sin_A = np.sqrt(1 - cos_A ** 2)
    c_vec = np.array([c * np.cos(beta_rad), c * np.sin(beta_rad) * cos_A, c * np.sin(beta_rad) * sin_A])
    volume = np.dot(a_vec, np.cross(b_vec, c_vec))
    b1 = np.cross(b_vec, c_vec) / volume
    b2 = np.cross(c_vec, a_vec) / volume
    b3 = np.cross(a_vec, b_vec) / volume
    B_raw = np.column_stack([b1, b2, b3])
    x_star = b1 / np.linalg.norm(b1)
    z_star_direction = np.cross(b1, b2)
    z_star = z_star_direction / np.linalg.norm(z_star_direction)
    y_star = np.cross(z_star, x_star)
    y_star = y_star / np.linalg.norm(y_star)
    R = np.column_stack([x_star, y_star, z_star])
    B = R.T @ B_raw
    h1, k1, l1 = H1
    h2, k2, l2 = H2
    hkl1 = np.array([[h1], [k1], [l1]], dtype=float)
    hkl2 = np.array([[h2], [k2], [l2]], dtype=float)
    q1 = B @ hkl1
    q2 = B @ hkl2
    Q1 = q_cal(p1, b_c, det_d, p_s, wl)
    Q2 = q_cal(p2, b_c, det_d, p_s, wl)
    theta1 = -z1 * z_s
    theta2 = -z2 * z_s
    theta1_rad = np.radians(theta1)
    theta2_rad = np.radians(theta2)
    R_y_1 = np.array([[np.cos(theta1_rad), 0, -np.sin(theta1_rad)], [0, 1, 0], [np.sin(theta1_rad), 0, np.cos(theta1_rad)]])
    R_y_2 = np.array([[np.cos(theta2_rad), 0, -np.sin(theta2_rad)], [0, 1, 0], [np.sin(theta2_rad), 0, np.cos(theta2_rad)]])
    Q1_rotated = R_y_1 @ Q1
    Q2_rotated = R_y_2 @ Q2
    t1c = q1 / np.linalg.norm(q1)
    cross_q = np.cross(q1.flatten(), q2.flatten())
    t3c = cross_q.reshape(3, 1) / np.linalg.norm(cross_q)
    t2c = np.cross(t3c.flatten(), t1c.flatten()).reshape(3, 1)
    t2c = t2c / np.linalg.norm(t2c)
    t1g = Q1_rotated / np.linalg.norm(Q1_rotated)
    cross_Q = np.cross(Q1_rotated.flatten(), Q2_rotated.flatten())
    t3g = cross_Q.reshape(3, 1) / np.linalg.norm(cross_Q)
    t2g = np.cross(t3g.flatten(), t1g.flatten()).reshape(3, 1)
    t2g = t2g / np.linalg.norm(t2g)
    t_c = (t1c, t2c, t3c)
    t_g = (t1g, t2g, t3g)
    return (t_c, t_g)

def Umat(t_c, t_g):
    """Write down the orientation matrix which transforms from bases t_c to t_g
    Input
    t_c, tuple with three elements, each element is a 3x1 matrix, float
    t_g, tuple with three elements, each element is a 3x1 matrix, float
    Output
    U: 3x3 orthogonal matrix, float
    """
    T_c = np.column_stack([t_c[0], t_c[1], t_c[2]])
    T_g = np.column_stack([t_g[0], t_g[1], t_g[2]])
    U = T_g @ T_c.T
    return U
