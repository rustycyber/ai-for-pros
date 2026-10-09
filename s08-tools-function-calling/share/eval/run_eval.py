"""Run the 20-input eval against the OpenRouter agent.

Usage:
    python share/eval/run_eval.py
    python share/eval/run_eval.py --tool flight_status --n 5
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from agents import run_openrouter as run
from eval.dataset import DATASET
from eval.scorer import score_run


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tool", default=None,
                        help="Filter dataset to one tool name")
    parser.add_argument("--n", type=int, default=None,
                        help="Run only the first N rows")
    args = parser.parse_args()

    rows = DATASET
    if args.tool:
        rows = [r for r in rows if r[1] == args.tool]
    if args.n:
        rows = rows[: args.n]

    print(f"Running {len(rows)} eval rows against OpenRouter ({run.__module__}) ...\n")
    passes = 0
    for i, (prompt, expected_tool, expected_partial) in enumerate(rows, 1):
        result = run(prompt)
        ok, reason = score_run(result["tool_calls"], expected_tool, expected_partial)
        passes += int(ok)
        marker = "PASS" if ok else "FAIL"
        print(f"[{i:02d}/{len(rows):02d}] {marker}  {prompt[:60]:<60}  {reason}")

    print(f"\n=== {passes}/{len(rows)} passed ({100*passes/len(rows):.0f}%) ===")
    sys.exit(0 if passes == len(rows) else 1)


if __name__ == "__main__":
    main()
