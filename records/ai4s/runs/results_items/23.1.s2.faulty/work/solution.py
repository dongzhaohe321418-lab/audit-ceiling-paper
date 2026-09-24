import numpy as np

def KL_divergence(p, q):
    """Input
    p: probability distributions, 1-dimensional numpy array (or list) of floats
    q: probability distributions, 1-dimensional numpy array (or list) of floats
    Output
    divergence: KL-divergence of two probability distributions, a single scalar value (float)
    """
    p = np.asarray(p, dtype=float)
    q = np.asarray(q, dtype=float)
    divergence = 0.0
    for i in range(len(p)):
        if p[i] > 0:
            divergence += p[i] * np.log2(p[i] / q[i])
    return float(divergence)
