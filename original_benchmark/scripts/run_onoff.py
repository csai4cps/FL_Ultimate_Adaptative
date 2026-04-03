from pathlib import Path
import subprocess
import sys

NOTEBOOK = Path(__file__).resolve().parent.parent / "notebooks" / 'AUTOMATED BENCHMARK ON-OFF ATTACK.ipynb'
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "results"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT = OUTPUT_DIR / NOTEBOOK.name

cmd = [
    sys.executable,
    "-m",
    "jupyter",
    "nbconvert",
    "--to",
    "notebook",
    "--execute",
    str(NOTEBOOK),
    "--output",
    str(OUTPUT.name),
    "--output-dir",
    str(OUTPUT_DIR),
]

print("Executing:", NOTEBOOK.name)
subprocess.run(cmd, check=True)
print("Saved executed notebook to:", OUTPUT)
