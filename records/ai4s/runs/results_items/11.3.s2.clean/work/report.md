# Result

`work/run.py` runs `work/solution.py` on the inputs in `work/inputs.py`, evaluating `tensor([0, 1], [0, 1])`, and writes `work/outputs/run.log`. The step's output has 4 values, which are, in order, 0 dimensionless, 0 dimensionless, 0 dimensionless, 1 dimensionless, recorded in `work/results/results.json`.

```crossaudit-numbers
[{"v": "0", "u": "dimensionless", "src": {"file": "work/results/results.json", "quote": "\"text\": \"0 dimensionless\""}}, {"v": "0", "u": "dimensionless", "src": {"file": "work/results/results.json", "quote": "\"text\": \"0 dimensionless\""}}, {"v": "0", "u": "dimensionless", "src": {"file": "work/results/results.json", "quote": "\"text\": \"0 dimensionless\""}}, {"v": "1", "u": "dimensionless", "src": {"file": "work/results/results.json", "quote": "\"text\": \"1 dimensionless\""}}]
```
