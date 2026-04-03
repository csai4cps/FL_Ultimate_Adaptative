# FL_Ultimate_Adaptative

Adaptive Federated Learning framework for CPS security research.

## Repository organization

This repository now has **two complementary layers**:

1. **`original_benchmark/`**  
   Contains the exact benchmark notebooks used in the experiments, preserved as close as possible to the original execution flow to avoid divergence from the paper.

2. **`src/` + `scripts/` + `configs/`**  
   Contains the modular framework intended for future refactoring and extension.

## Reproducibility-first guidance

If your immediate goal is to reproduce the paper results, start with:

```bash
cd original_benchmark
bash scripts/run_sybil.sh
```

Available benchmark runners:

- `bash scripts/run_onoff.sh`
- `bash scripts/run_backdoor.sh`
- `bash scripts/run_sybil.sh`
- `bash scripts/run_model_replacement.sh`

## Important note

The `original_benchmark/` directory is intentionally preserved in benchmark-oriented form. The goal is to keep the execution path aligned with the article and reduce the risk of implementation drift.
