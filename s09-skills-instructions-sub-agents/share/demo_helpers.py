"""
Shared utilities for demo scripts - Interactive execution helpers and cross-platform support
"""
import sys
import os
from pathlib import Path
from typing import Optional


def pause(message: str = "Press [Enter] to continue...", clear_screen: bool = False) -> None:
    """
    Interactive pause between demo steps.
    
    Args:
        message: Custom message to display
        clear_screen: Whether to clear screen before pause (default: False)
    """
    if clear_screen:
        # Cross-platform clear screen
        os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"\n{'─' * 70}")
    try:
        input(f"⏸️  {message}")
    except (EOFError, KeyboardInterrupt):
        print("\n[Skipped - non-interactive mode]")
    print(f"{'─' * 70}\n")


def section_header(title: str, char: str = "=", width: int = 70) -> None:
    """
    Print a formatted section header.
    
    Args:
        title: Section title
        char: Character for border (default: "=")
        width: Width of header (default: 70)
    """
    print(f"\n{char * width}")
    print(f" {title.upper()}")
    print(f"{char * width}\n")


def subsection_header(title: str, char: str = "-", width: int = 70) -> None:
    """
    Print a formatted subsection header.
    
    Args:
        title: Subsection title
        char: Character for border (default: "-")
        width: Width of header (default: 70)
    """
    print(f"\n{char * width}")
    print(f" {title}")
    print(f"{char * width}")


def python_cmd() -> str:
    """
    Get the correct Python command for the current platform.
    
    Returns:
        'python' on Windows, 'python3' on Unix-like systems
    """
    return "python" if os.name == 'nt' else "python3"


def get_project_root() -> Path:
    """
    Get the project root directory.
    
    Returns:
        Path object for project root
    """
    return Path(__file__).parent.parent.parent


def ensure_path(path_str: str) -> Path:
    """
    Resolve a path string to absolute Path, handling relative paths correctly.
    
    Args:
        path_str: Path string (can be relative or absolute)
    
    Returns:
        Resolved absolute Path object
    """
    path = Path(path_str)
    if not path.is_absolute():
        # Resolve relative to current working directory
        path = Path.cwd() / path
    return path.resolve()


def step_marker(step_num: int, total_steps: int, description: str) -> None:
    """
    Print a formatted step marker.
    
    Args:
        step_num: Current step number
        total_steps: Total number of steps
        description: Step description
    """
    print(f"\n📍 Step {step_num}/{total_steps}: {description}")
    print(f"{'─' * 70}")


def demo_title(module_name: str, demo_num: str = "") -> None:
    """
    Print formatted demo title.
    
    Args:
        module_name: Name of the module/demo
        demo_num: Optional demo number (e.g., "03")
    """
    prefix = f"{demo_num} - " if demo_num else ""
    section_header(f"{prefix}{module_name}")


def show_result(data: dict, title: str = "Result", truncate: int = 500) -> None:
    """
    Display a formatted result.
    
    Args:
        data: Dictionary to display
        title: Title for the result section
        truncate: Maximum characters before truncation (default: 500)
    """
    import json
    
    print(f"\n📊 {title}:")
    print("-" * 70)
    output = json.dumps(data, indent=2)
    if len(output) > truncate:
        print(output[:truncate] + "\n... (truncated)")
    else:
        print(output)


def show_key_takeaways(takeaways: list) -> None:
    """
    Display formatted key takeaways.
    
    Args:
        takeaways: List of takeaway strings
    """
    section_header("KEY TAKEAWAYS")
    for takeaway in takeaways:
        print(f"✅ {takeaway}")
    print()


def next_step(next_demo: str) -> None:
    """
    Show next demo command.
    
    Args:
        next_demo: Path to next demo script
    """
    print(f"\n{'=' * 70}")
    print(f" NEXT: {python_cmd()} {next_demo}")
    print(f"{'=' * 70}\n")


# Platform detection utility
def is_windows() -> bool:
    """Check if running on Windows."""
    return os.name == 'nt'


def is_macos() -> bool:
    """Check if running on macOS."""
    return sys.platform == 'darwin'


def is_linux() -> bool:
    """Check if running on Linux."""
    return sys.platform.startswith('linux')


if __name__ == "__main__":
    # Test the helpers
    print(f"Platform: {sys.platform}")
    print(f"OS Name: {os.name}")
    print(f"Python command: {python_cmd()}")
    print(f"Project root: {get_project_root()}")
    
    section_header("Test Demo")
    print("This is a test demo.")
    
    pause("Test pause - press Enter to continue")
    
    subsection_header("Test Subsection")
    print("Subsection content here.")
