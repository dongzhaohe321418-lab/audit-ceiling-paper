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
    return divergence

def mutual_info(channel, prior):
    """Input
    channel: a classical channel, 2d array of floats; channel[i][j] means probability of i given j
    prior:   input random variable, 1d array of floats.
    Output
    mutual: mutual information between the input random variable and the random variable associated with the output of the channel, a single scalar value (float)
    """
    channel = np.asarray(channel, dtype=float)
    prior = np.asarray(prior, dtype=float)

    def entropy(p):
        """Compute Shannon entropy: H(p) = -sum(p(x) * log2(p(x)))"""
        h = 0.0
        for prob in p:
            if prob > 0:
                h -= prob * np.log2(prob)
        return h
    h_x = entropy(prior)
    num_outputs = channel.shape[0]
    num_inputs = channel.shape[1]
    p_y = np.zeros(num_outputs)
    for y in range(num_outputs):
        for x in range(num_inputs):
            p_y[y] += prior[x] * channel[y, x]
    h_y = entropy(p_y)
    h_xy = 0.0
    for x in range(num_inputs):
        for y in range(num_outputs):
            p_xy = prior[x] * channel[y, x]
            if p_xy > 0:
                h_xy -= p_xy * np.log2(p_xy)
    mutual = h_x + h_y - h_xy
    return mutual
