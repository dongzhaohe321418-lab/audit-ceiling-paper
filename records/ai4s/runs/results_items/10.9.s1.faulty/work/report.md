# Result

`work/run.py` runs `work/solution.py` on the inputs in `work/inputs.py`, evaluating `sum_real_self(EX['atom_charges'], EX['configs'].shape[0], get_alpha(np.linalg.inv(EX['latvec']).T))`, and writes `work/outputs/run.log`. The step's output is -4886.0251 dimensionless, recorded in `work/results/results.json`.

```crossaudit-numbers
[{"v": "-4886.0251", "u": "dimensionless", "src": {"file": "work/results/results.json", "quote": "\"text\": \"-4886.0251 dimensionless\""}}]
```
