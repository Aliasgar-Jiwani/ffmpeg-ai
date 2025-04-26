"""
Utility functions for the ffmpeg-ai project.
"""
import os
import json
import logging
from pathlib import Path
from typing import Dict, Any, List, Optional
from rich.console import Console
from rich.syntax import Syntax

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("ffmpeg-ai")

# Rich console for pretty printing
console = Console()

# Project paths
PROJECT_ROOT = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = PROJECT_ROOT / "data"
DOCS_DIR = DATA_DIR / "docs"
VECTOR_STORE_DIR = DATA_DIR / "vector_store"


def ensure_directories():
    """Ensure all required directories exist."""
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    VECTOR_STORE_DIR.mkdir(parents=True, exist_ok=True)
    logger.info(f"Directories ensured: {DOCS_DIR}, {VECTOR_STORE_DIR}")


def print_command(command: str, language: str = "bash", explain: Optional[str] = None):
    """
    Print a command with syntax highlighting.

    Args:
        command: The command to print
        language: The language for syntax highlighting
        explain: Optional explanation text
    """
    console.print("\n[bold green]FFmpeg Command:[/bold green]")
    syntax = Syntax(command, language, theme="monokai", line_numbers=False, word_wrap=True)
    console.print(syntax)

    if explain:
        console.print("\n[bold blue]Explanation:[/bold blue]")
        console.print(explain)

    console.print()  # Add a new line for better spacing


def print_code(code: str, language: str = "python", explain: Optional[str] = None):
    """
    Print code with syntax highlighting.

    Args:
        code: The code to print
        language: The language for syntax highlighting
        explain: Optional explanation text
    """
    console.print(f"\n[bold green]{language.capitalize()} Code:[/bold green]")
    syntax = Syntax(code, language, theme="monokai", line_numbers=True, word_wrap=True)
    console.print(syntax)

    if explain:
        console.print("\n[bold blue]Explanation:[/bold blue]")
        console.print(explain)

    console.print()  # Add a new line for better spacing


def save_json(data: Dict[str, Any], file_path: str):
    """
    Save data as JSON to the specified file path.

    Args:
        data: The data to save
        file_path: The file path to save to
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    logger.info(f"Saved data to {file_path}")


def load_json(file_path: str) -> Dict[str, Any]:
    """
    Load JSON data from the specified file path.

    Args:
        file_path: The file path to load from

    Returns:
        The loaded data
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        return {}
    except json.JSONDecodeError:
        logger.error(f"Failed to decode JSON from {file_path}")
        return {}


def get_language_file_extension(language: str) -> str:
    """
    Get the file extension for a given language.

    Args:
        language: The language name

    Returns:
        The file extension
    """
    extensions = {
        "python": "py",
        "bash": "sh",
        "node": "js",
        "javascript": "js",
    }
    return extensions.get(language.lower(), "txt")