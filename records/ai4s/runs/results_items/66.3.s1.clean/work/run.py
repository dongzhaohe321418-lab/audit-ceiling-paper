"""Writes outputs/run.log: the step's output on the benchmark's test inputs."""
import numpy as np

from solution import *  # noqa: F401,F403  the candidate program

exec(open("inputs.py", encoding="utf-8").read())  # the benchmark's input assignments, verbatim

output = potential_repulsive(np.array([[-2.46, -4.26084499, 3.2]]), n_i, n_j, z0, C, C0, C2, C4, delta, lamda)
with open("outputs/run.log", "w", encoding="utf-8") as log:
    for value in np.ravel(np.asarray(output, dtype=float)):
        log.write(format(float(value), ".8g") + " dimensionless\n")
