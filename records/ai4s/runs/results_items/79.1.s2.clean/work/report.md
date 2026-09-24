# Result

`work/run.py` runs `work/solution.py` on the inputs in `work/inputs.py`, evaluating `Verlet(v0, x0, m, dt, omega)`, and writes `work/outputs/run.log`. The step's output has 2 values, which are, in order, 0.44719123 dimensionless, 0.004472136 dimensionless, recorded in `work/results/results.json`.

```crossaudit-numbers
[{"v": "0.44719123", "u": "dimensionless", "src": {"file": "work/results/results.json", "quote": "\"text\": \"0.44719123 dimensionless\""}}, {"v": "0.004472136", "u": "dimensionless", "src": {"file": "work/results/results.json", "quote": "\"text\": \"0.004472136 dimensionless\""}}]
```
