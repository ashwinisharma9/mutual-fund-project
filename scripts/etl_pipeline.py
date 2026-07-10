from pathlib import Path
import subprocess
import sys

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

print("=" * 50)
print("Starting ETL Pipeline")
print("=" * 50)

# List of scripts to run
scripts = [
    "live_nav_fetch.py",
    "compute_metrics.py"
]

for script in scripts:
    script_path = BASE_DIR / "scripts" / script

    print(f"\nRunning {script}...")

    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=BASE_DIR
    )

    if result.returncode != 0:
        print(f"\nError while running {script}")
        sys.exit(1)

print("\nETL Pipeline Completed Successfully!")