"""Pytest configuration for share tests."""
import os
import sys
from pathlib import Path

# Setup paths - respect PYTHONPATH if set, otherwise default to solution
_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(_root / "share"))
if "PYTHONPATH" not in os.environ:
    sys.path.insert(0, str(_root / "solution"))
