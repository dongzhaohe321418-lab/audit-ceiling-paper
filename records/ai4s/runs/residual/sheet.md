# Rating sheet

## S001

### Problem
Write a script for indexing Bragg peaks collected from x-ray diffraction (XRD). We're focusing on a one-circle diffractometer with a fixed area detector perpendicular to the x-ray beam. To orient the crystal, we'll need to determine the indices of two Bragg reflections and then find the rotation matrix that maps these two scattering vectors from lab space to reciprocal space.

### Step
Write down the orientation matrix $\mathbf{U}$ as the unitary transformation from the bases {$\mathbf{\hat{t}}_i^c$} to {$\mathbf{\hat{t}}_i^g$}

### Background
Background
To orient the crystal, we determine the directions of the reciprocal lattice primitive vectors in the lab coordinate system. We define the Cartesian coordinate system in reciprocal space to be the same as the lab coordinate system.  Our goal is to rotate the reciprocal lattice so that it aligns with our observed diffraction pattern. The rotation matrix used for this purpose is the orientation matrix $\mathbf{U}$, given by:
$$\mathbf{T}_g = \mathbf{U}\mathbf{T}_c$$
where $\mathbf{T}_c$ represents the matrix with columns {$\mathbf{\hat{t}}_i^c$} and similarly for $\mathbf{T}_g$.

### Function header
```python
def Umat(t_c, t_g):
    '''Write down the orientation matrix which transforms from bases t_c to t_g
    Input
    t_c, tuple with three elements, each element is a 3x1 matrix, float
    t_g, tuple with three elements, each element is a 3x1 matrix, float
    Output
    U: 3x3 orthogonal matrix, float
    '''
    return U
```

### Candidate
```python
def Umat(t_c, t_g):
    """Write down the orientation matrix which transforms from bases t_c to t_g
    Input
    t_c, tuple with three elements, each element is a 3x1 matrix, float
    t_g, tuple with three elements, each element is a 3x1 matrix, float
    Output
    U: 3x3 orthogonal matrix, float
    """
    T_c = np.hstack([t_c[0], t_c[1], t_c[2]])
    T_g = np.hstack([t_g[0], t_g[1], t_g[2]])
    U = T_g @ T_c.T
    return U
```

### Tests
Test 1 inputs:
```python
a,b,c,alpha,beta,gamma = (5.39097,5.39097,5.39097,90,90,90)
pa = (a,b,c,alpha,beta,gamma)
H1 = (1,1,1)
H2 = (2,2,0)
p1 = (1689,2527)
p2 = (2190,2334)
b_c = (1699.85, 3037.62)
det_d = 219.741
p_s = 0.1
wl = 0.710511
z1 = 132-1
z2 = 225-1
z_s = 0.05
t_c,t_g = u_triple(pa,H1,H2,p1,p2,b_c,det_d,p_s,wl,z1,z2,z_s)
```
Test 1 check: `assert np.allclose(Umat(t_c,t_g), target)`
Test 1 expected value (`target`): array of shape (3, 3): [-0.7239298299324541, 0.6889781485539036, 0.03513847107093829, -0.3652234930059384, -0.4259669506714146, 0.8277463120378359, 0.5852669489134931, 0.5863968517573502, 0.5600011881760243]

Test 2 inputs:
```python
a,b,c,alpha,beta,gamma = (5.39097,5.39097,5.39097,90,90,90)
pa = (a,b,c,alpha,beta,gamma)
H1 = (1,1,3)
H2 = (2,2,0)
p1 = (1166,2154)
p2 = (2190,2334)
b_c = (1699.85, 3037.62)
det_d = 219.741
p_s = 0.1
wl = 0.710511
z1 = 329-1
z2 = 225-1
z_s = 0.05
t_c,t_g = u_triple(pa,H1,H2,p1,p2,b_c,det_d,p_s,wl,z1,z2,z_s)
```
Test 2 check: `assert np.allclose(Umat(t_c,t_g), target)`
Test 2 expected value (`target`): array of shape (3, 3): [-0.7239191400866434, 0.6886369406035594, 0.04147580803775469, -0.36496579530990453, -0.4332961906030542, 0.8240475589810886, 0.5854408995535106, 0.5814065490214672, 0.5650003344113388]

Test 3 inputs:
```python
a,b,c,alpha,beta,gamma = (5.39097,5.39097,5.39097,90,90,90)
pa = (a,b,c,alpha,beta,gamma)
H1 = (1,1,1)
H2 = (3,1,5)
p1 = (1689,2527)
p2 = (632,1060)
b_c = (1699.85, 3037.62)
det_d = 219.741
p_s = 0.1
wl = 0.710511
z1 = 132-1
z2 = 232-1
z_s = 0.05
t_c,t_g = u_triple(pa,H1,H2,p1,p2,b_c,det_d,p_s,wl,z1,z2,z_s)
```
Test 3 check: `assert np.allclose(Umat(t_c,t_g), target)`
Test 3 expected value (`target`): array of shape (3, 3): [-0.7246025766852356, 0.6881946932057537, 0.03659467317186983, -0.3639307126624786, -0.4271958243001678, 0.8276824053231291, 0.5852397305738033, 0.5864228780870839, 0.5600023801859806]


## S002

### Problem
Calculate the coherent information of a generalized amplitude damping channel (GADC)

### Step
Consider sending one qubit of the state $\sqrt{1-p}|00\rangle + \sqrt{p}|11\rangle$ through a GADC with damping parameters $\gamma$ and thermal parameter $N$. Calculate the negative of reverse coherent information of the output state.

Background
The reverse coherent information of a bipartite state $\rho$ is given by
$$
I_R(A\rangle B) = S(A)_\rho - S(AB)_\rho
$$
where $S(X)_\rho$ is the von Neuman entropy of $\rho$ on system $X$.

### Background


### Function header
```python
def neg_rev_coh_info(p, g, N):
    '''Calculates the negative of coherent information of the output state
    Inputs:
    p: float, parameter for the input state
    g: float, damping parameter
    N: float, thermal parameter
    Outputs:
    neg_I_c: float, negative of coherent information of the output state
    '''
    return neg_I_R
```

### Candidate
```python
def neg_rev_coh_info(p, g, N):
    """Calculates the negative of coherent information of the output state
    Inputs:
    p: float, parameter for the input state
    g: float, damping parameter
    N: float, thermal parameter
    Outputs:
    neg_I_R: float, negative of reverse coherent information of the output state
    """
    psi = np.sqrt(1 - p) * ket([0, 0], [2, 2]) + np.sqrt(p) * ket([1, 1], [2, 2])
    rho_initial = np.outer(psi, psi.conj())
    K = generalized_amplitude_damping_channel(g, N)
    rho_output = apply_channel(K, rho_initial, sys=[1], dim=[2, 2])
    rho_A = partial_trace(rho_output, sys=[1], dim=[2, 2])
    S_A = entropy(rho_A)
    S_AB = entropy(rho_output)
    I_R = S_A - S_AB
    neg_I_R = -I_R
    return neg_I_R
```

### Tests
Test 1 inputs:
```python
p = 0.477991
g = 0.2
N = 0.4
```
Test 1 check: `assert np.allclose(neg_rev_coh_info(p,g,N), target)`
Test 1 expected value (`target`): np.float64(-0.4088186219043247)

Test 2 inputs:
```python
p = 0.407786
g = 0.2
N = 0.1
```
Test 2 check: `assert np.allclose(neg_rev_coh_info(p,g,N), target)`
Test 2 expected value (`target`): np.float64(-0.4945582030078741)

Test 3 inputs:
```python
p = 0.399685
g = 0.4
N = 0.2
```
Test 3 check: `assert np.allclose(neg_rev_coh_info(p,g,N), target)`
Test 3 expected value (`target`): np.float64(-0.08913394183531942)


## S003

### Problem
Calculate the coherent information of a generalized amplitude damping channel (GADC)

### Step
Calculate the von Neumann entropy of a state

### Background


### Function header
```python
def entropy(rho):
    '''Inputs:
    rho: 2d array of floats with equal dimensions, the density matrix of the state
    Output:
    en: quantum (von Neumann) entropy of the state rho, float
    '''
    return en 
```

### Candidate
```python
def entropy(rho):
    """Inputs:
    rho: 2d array of floats with equal dimensions, the density matrix of the state
    Output:
    en: quantum (von Neumann) entropy of the state rho, float
    """
    eigenvalues = np.linalg.eigvalsh(rho)
    eigenvalues = np.maximum(eigenvalues, 0)
    eigenvalues = eigenvalues[eigenvalues > 1e-15]
    en = -np.sum(eigenvalues * np.log(eigenvalues))
    return en
```

### Tests
Test 1 inputs:
```python
rho = np.eye(4)/4
```
Test 1 check: `assert np.allclose(entropy(rho), target)`
Test 1 expected value (`target`): np.float64(2.0)

Test 2 inputs:
```python
rho = np.ones((3,3))/3
```
Test 2 check: `assert np.allclose(entropy(rho), target)`
Test 2 expected value (`target`): np.float64(-9.39671774452376e-15)

Test 3 inputs:
```python
rho = np.diag([0.8,0.2])
```
Test 3 check: `assert np.allclose(entropy(rho), target)`
Test 3 expected value (`target`): np.float64(0.7219280948873623)


## S004

### Problem
Write a script for indexing Bragg peaks collected from x-ray diffraction (XRD). We're focusing on a one-circle diffractometer with a fixed area detector perpendicular to the x-ray beam. To orient the crystal, we'll need to determine the indices of two Bragg reflections and then find the rotation matrix that maps these two scattering vectors from lab space to reciprocal space.

### Step
Write down the orientation matrix $\mathbf{U}$ as the unitary transformation from the bases {$\mathbf{\hat{t}}_i^c$} to {$\mathbf{\hat{t}}_i^g$}

### Background
Background
To orient the crystal, we determine the directions of the reciprocal lattice primitive vectors in the lab coordinate system. We define the Cartesian coordinate system in reciprocal space to be the same as the lab coordinate system.  Our goal is to rotate the reciprocal lattice so that it aligns with our observed diffraction pattern. The rotation matrix used for this purpose is the orientation matrix $\mathbf{U}$, given by:
$$\mathbf{T}_g = \mathbf{U}\mathbf{T}_c$$
where $\mathbf{T}_c$ represents the matrix with columns {$\mathbf{\hat{t}}_i^c$} and similarly for $\mathbf{T}_g$.

### Function header
```python
def Umat(t_c, t_g):
    '''Write down the orientation matrix which transforms from bases t_c to t_g
    Input
    t_c, tuple with three elements, each element is a 3x1 matrix, float
    t_g, tuple with three elements, each element is a 3x1 matrix, float
    Output
    U: 3x3 orthogonal matrix, float
    '''
    return U
```

### Candidate
```python
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
```

### Tests
Test 1 inputs:
```python
a,b,c,alpha,beta,gamma = (5.39097,5.39097,5.39097,90,90,90)
pa = (a,b,c,alpha,beta,gamma)
H1 = (1,1,1)
H2 = (2,2,0)
p1 = (1689,2527)
p2 = (2190,2334)
b_c = (1699.85, 3037.62)
det_d = 219.741
p_s = 0.1
wl = 0.710511
z1 = 132-1
z2 = 225-1
z_s = 0.05
t_c,t_g = u_triple(pa,H1,H2,p1,p2,b_c,det_d,p_s,wl,z1,z2,z_s)
```
Test 1 check: `assert np.allclose(Umat(t_c,t_g), target)`
Test 1 expected value (`target`): array of shape (3, 3): [-0.7239298299324541, 0.6889781485539036, 0.03513847107093829, -0.3652234930059384, -0.4259669506714146, 0.8277463120378359, 0.5852669489134931, 0.5863968517573502, 0.5600011881760243]

Test 2 inputs:
```python
a,b,c,alpha,beta,gamma = (5.39097,5.39097,5.39097,90,90,90)
pa = (a,b,c,alpha,beta,gamma)
H1 = (1,1,3)
H2 = (2,2,0)
p1 = (1166,2154)
p2 = (2190,2334)
b_c = (1699.85, 3037.62)
det_d = 219.741
p_s = 0.1
wl = 0.710511
z1 = 329-1
z2 = 225-1
z_s = 0.05
t_c,t_g = u_triple(pa,H1,H2,p1,p2,b_c,det_d,p_s,wl,z1,z2,z_s)
```
Test 2 check: `assert np.allclose(Umat(t_c,t_g), target)`
Test 2 expected value (`target`): array of shape (3, 3): [-0.7239191400866434, 0.6886369406035594, 0.04147580803775469, -0.36496579530990453, -0.4332961906030542, 0.8240475589810886, 0.5854408995535106, 0.5814065490214672, 0.5650003344113388]

Test 3 inputs:
```python
a,b,c,alpha,beta,gamma = (5.39097,5.39097,5.39097,90,90,90)
pa = (a,b,c,alpha,beta,gamma)
H1 = (1,1,1)
H2 = (3,1,5)
p1 = (1689,2527)
p2 = (632,1060)
b_c = (1699.85, 3037.62)
det_d = 219.741
p_s = 0.1
wl = 0.710511
z1 = 132-1
z2 = 232-1
z_s = 0.05
t_c,t_g = u_triple(pa,H1,H2,p1,p2,b_c,det_d,p_s,wl,z1,z2,z_s)
```
Test 3 check: `assert np.allclose(Umat(t_c,t_g), target)`
Test 3 expected value (`target`): array of shape (3, 3): [-0.7246025766852356, 0.6881946932057537, 0.03659467317186983, -0.3639307126624786, -0.4271958243001678, 0.8276824053231291, 0.5852397305738033, 0.5864228780870839, 0.5600023801859806]


## S005

### Problem
Calculate the coherent information of a generalized amplitude damping channel (GADC)

### Step
Write a function that returns the tensor product of an arbitrary number of matrices/vectors.

### Background


### Function header
```python
def tensor():
    '''Takes the tensor product of an arbitrary number of matrices/vectors.
    Input:
    args: any number of nd arrays of floats, corresponding to input matrices
    Output:
    M: the tensor product (kronecker product) of input matrices, 2d array of floats
    '''
    return M
```

### Candidate
```python
def tensor(*args):
    """Takes the tensor product of an arbitrary number of matrices/vectors.
    Input:
    args: any number of nd arrays of floats, corresponding to input matrices
    Output:
    M: the tensor product (kronecker product) of input matrices, 2d array of floats
    """
    if len(args) == 0:
        raise ValueError('At least one matrix/vector must be provided')
    M = np.array(args[0], dtype=float)
    for matrix in args[1:]:
        M = np.kron(M, np.array(matrix, dtype=float))
    if M.ndim == 1:
        M = M.reshape(-1, 1)
    return M
```

### Tests
Test 1 inputs:
```python

```
Test 1 check: `assert np.allclose(tensor([0,1],[0,1]), target)`
Test 1 expected value (`target`): array of shape (4,): [0, 0, 0, 1]

Test 2 inputs:
```python

```
Test 2 check: `assert np.allclose(tensor(np.eye(3),np.ones((3,3))), target)`
Test 2 expected value (`target`): array of shape (9, 9): [1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, ... (81 elements)]

Test 3 inputs:
```python

```
Test 3 check: `assert np.allclose(tensor([[1/2,1/2],[0,1]],[[1,2],[3,4]]), target)`
Test 3 expected value (`target`): array of shape (4, 4): [0.5, 1.0, 0.5, 1.0, 1.5, 2.0, 1.5, 2.0, 0.0, 0.0, 1.0, 2.0, 0.0, 0.0, 3.0, 4.0]


## S006

### Problem
Calculate the coherent information of a generalized amplitude damping channel (GADC)

### Step
Calculate the von Neumann entropy of a state

### Background


### Function header
```python
def entropy(rho):
    '''Inputs:
    rho: 2d array of floats with equal dimensions, the density matrix of the state
    Output:
    en: quantum (von Neumann) entropy of the state rho, float
    '''
    return en 
```

### Candidate
```python
def entropy(rho):
    """Inputs:
    rho: 2d array of floats with equal dimensions, the density matrix of the state
    Output:
    en: quantum (von Neumann) entropy of the state rho, float
    """
    eigenvalues = np.linalg.eigvalsh(rho)
    eigenvalues = np.maximum(eigenvalues, 0)
    en = 0.0
    for lam in eigenvalues:
        if lam > 1e-15:
            en -= lam * np.log(lam)
    return en
```

### Tests
Test 1 inputs:
```python
rho = np.eye(4)/4
```
Test 1 check: `assert np.allclose(entropy(rho), target)`
Test 1 expected value (`target`): np.float64(2.0)

Test 2 inputs:
```python
rho = np.ones((3,3))/3
```
Test 2 check: `assert np.allclose(entropy(rho), target)`
Test 2 expected value (`target`): np.float64(-9.39671774452376e-15)

Test 3 inputs:
```python
rho = np.diag([0.8,0.2])
```
Test 3 check: `assert np.allclose(entropy(rho), target)`
Test 3 expected value (`target`): np.float64(0.7219280948873623)


## S007

### Problem
Calculate the coherent information of a generalized amplitude damping channel (GADC)

### Step
Consider sending one qubit of the state $\sqrt{1-p}|00\rangle + \sqrt{p}|11\rangle$ through a GADC with damping parameters $\gamma$ and thermal parameter $N$. Calculate the negative of reverse coherent information of the output state.

Background
The reverse coherent information of a bipartite state $\rho$ is given by
$$
I_R(A\rangle B) = S(A)_\rho - S(AB)_\rho
$$
where $S(X)_\rho$ is the von Neuman entropy of $\rho$ on system $X$.

### Background


### Function header
```python
def neg_rev_coh_info(p, g, N):
    '''Calculates the negative of coherent information of the output state
    Inputs:
    p: float, parameter for the input state
    g: float, damping parameter
    N: float, thermal parameter
    Outputs:
    neg_I_c: float, negative of coherent information of the output state
    '''
    return neg_I_R
```

### Candidate
```python
def neg_rev_coh_info(p, g, N):
    """Calculates the negative of reverse coherent information of the output state
    Inputs:
    p: float, parameter for the input state
    g: float, damping parameter
    N: float, thermal parameter
    Outputs:
    neg_I_R: float, negative of reverse coherent information of the output state
    """
    ket00 = ket(2, [0, 0])
    ket11 = ket(2, [1, 1])
    psi_init = np.sqrt(1 - p) * ket00 + np.sqrt(p) * ket11
    rho_init = np.outer(psi_init, psi_init.conj())
    K = generalized_amplitude_damping_channel(g, N)
    dim = [2, 2]
    rho_out = apply_channel(K, rho_init, sys=[0], dim=dim)
    rho_A = partial_trace(rho_out, [1], dim)
    S_A = entropy(rho_A)
    S_AB = entropy(rho_out)
    I_R = S_A - S_AB
    neg_I_R = -I_R
    return neg_I_R
```

### Tests
Test 1 inputs:
```python
p = 0.477991
g = 0.2
N = 0.4
```
Test 1 check: `assert np.allclose(neg_rev_coh_info(p,g,N), target)`
Test 1 expected value (`target`): np.float64(-0.4088186219043247)

Test 2 inputs:
```python
p = 0.407786
g = 0.2
N = 0.1
```
Test 2 check: `assert np.allclose(neg_rev_coh_info(p,g,N), target)`
Test 2 expected value (`target`): np.float64(-0.4945582030078741)

Test 3 inputs:
```python
p = 0.399685
g = 0.4
N = 0.2
```
Test 3 check: `assert np.allclose(neg_rev_coh_info(p,g,N), target)`
Test 3 expected value (`target`): np.float64(-0.08913394183531942)

