# Original Experimental Benchmark

This directory preserves the benchmark in a format that stays as close as possible to the execution logic used in the article.

## Objective

Avoid divergence between the repository implementation and the results reported in the paper.

## Included notebooks

The following notebooks were preserved with their original names:

- `AUTOMATED BENCHMARK ON-OFF ATTACK.ipynb`
- `Automated Benchmark_ Cumulative Backdoor_asr_fixed.ipynb`
- `AUTOMATED BENCHMARK PIPELINE_ SYBIL ATTACK - IDENTITY FLOOD - ASR Fixed.ipynb`
- `AUTOMATED BENCHMARK PIPELINE MODEL REPLACEMENT - SCALING ATTACK ASR FIXED.ipynb`

## Execution strategy

To preserve fidelity with the article, this benchmark is executed by running the notebooks directly through scripted wrappers instead of rewriting the experimental logic first.

Each script:

1. calls the original notebook;
2. executes it end-to-end with Jupyter;
3. stores the executed copy in `original_benchmark/results/`.

## How to run

From the repository root:

```bash
cd original_benchmark
bash scripts/run_onoff.sh
bash scripts/run_backdoor.sh
bash scripts/run_sybil.sh
bash scripts/run_model_replacement.sh
```

Or run all benchmarks:

```bash
cd original_benchmark
bash scripts/run_all.sh
```

## Notes for scientific reproducibility

- notebook logic was preserved;
- filenames remain traceable to the original experiment package;
- the wrappers reduce manual execution variability;
- this directory should be treated as the paper-faithful benchmark layer.
