"""Writes outputs/run.log: the step's output on the benchmark's test inputs."""
import numpy as np

from solution import *  # noqa: F401,F403  the candidate program

exec(open("inputs.py", encoding="utf-8").read())  # the benchmark's input assignments, verbatim

output = neg_rev_coh_info(p, g, N)
with open("outputs/run.log", "w", encoding="utf-8") as log:
    for value in np.ravel(np.asarray(output, dtype=float)):
        log.write(format(float(value), ".8g") + " dimensionless\n")
