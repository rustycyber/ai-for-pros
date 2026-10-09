"""Pytest configuration for share tests."""
import sys
from pathlib import Path

# Setup paths - share uses solution tools
_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(_root / "share"))
sys.path.insert(0, str(_root / "solution"))
