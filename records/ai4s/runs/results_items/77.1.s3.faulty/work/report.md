# Result

`work/run.py` runs `work/solution.py` on the inputs in `work/inputs.py`, evaluating `wrap(particle_position2, box_length2)`, and writes `work/outputs/run.log`. The step's output has 3 values, which are, in order, 3700 dimensionless, 7900 dimensionless, 4300 dimensionless, recorded in `work/results/results.json`.

```crossaudit-numbers
[{"v": "3700", "u": "dimensionless", "src": {"file": "work/results/results.json", "quote": "\"text\": \"3700 dimensionless\""}}, {"v": "7900", "u": "dimensionless", "src": {"file": "work/results/results.json", "quote": "\"text\": \"7900 dimensionless\""}}, {"v": "4300", "u": "dimensionless", "src": {"file": "work/results/results.json", "quote": "\"text\": \"4300 dimensionless\""}}]
```
