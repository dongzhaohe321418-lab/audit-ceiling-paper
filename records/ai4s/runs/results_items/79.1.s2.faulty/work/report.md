# Result

`work/run.py` runs `work/solution.py` on the inputs in `work/inputs.py`, evaluating `Verlet(v0, x0, m, dt, omega)`, and writes `work/outputs/run.log`. The step's output has 2 values, which are, in order, 0.4695508 dimensionless, 0.0046957428 dimensionless, recorded in `work/results/results.json`.

```crossaudit-numbers
[{"v": "0.4695508", "u": "dimensionless", "src": {"file": "work/results/results.json", "quote": "\"text\": \"0.4695508 dimensionless\""}}, {"v": "0.0046957428", "u": "dimensionless", "src": {"file": "work/results/results.json", "quote": "\"text\": \"0.0046957428 dimensionless\""}}]
```
