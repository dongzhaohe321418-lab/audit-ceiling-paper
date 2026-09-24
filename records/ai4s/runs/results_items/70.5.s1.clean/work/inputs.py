s12 = 1/cmath.sqrt(2)
s13 = 0
s23 = 1/cmath.sqrt(3)
dCP = 1
D21 = 5e-4
D31 = 5e-3
hamiltonian = hamiltonian_3nu(s12, s13, s23, dCP, D21, D31)
h_coefficient = hamiltonian_3nu_su3_coefficients(hamiltonian)
