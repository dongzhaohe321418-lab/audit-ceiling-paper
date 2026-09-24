import numpy as np

def normalize(v):
    """Normalize the input vector.
    Input:
    v (N*1 numpy array): The input vector.
    Output:
    n (N*1 numpy array): The normalized vector.
    """
    l2_norm = np.linalg.norm(v, ord=2)
    n = v / l2_norm
    return n

def inner_product(u, v):
    """Calculates the inner product of two vectors.
    Input:
    u (numpy array): Vector 1.
    v (numpy array): Vector 2.
    Output:
    p (float): Inner product of the vectors.
    """
    p = np.dot(u, v)
    return p
