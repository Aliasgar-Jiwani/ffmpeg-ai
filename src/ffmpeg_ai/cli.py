import logging
from rich.logging import RichHandler

# Configure root logger (optional, but ensures no other logs interfere)
logging.basicConfig(
    level=logging.CRITICAL,  # Suppress all logs except CRITICAL
    handlers=[RichHandler(rich_tracebacks=True, show_time=False, show_level=False)]
)
from typing import Optional
import typer
from rich.console import Console
from rich.logging import RichHandler

from .llm_engine import llm_engine
from .utils import print_command, print_code, get_language_file_extension
from .cache import cache

logging.basicConfig(level=logging.CRITICAL)

logger = logging.getLogger("ffmpeg-ai")

# Create Typer app
app = typer.Typer(
    help="AI-powered FFmpeg command generator",
    add_completion=False
)

# Console for pretty printing
console = Console()


@app.callback()
def callback():
    """AI-powered FFmpeg command generator."""
    pass


@app.command()
def query(
        query: str = typer.Argument(..., help="Natural language query about FFmpeg"),
        code: bool = typer.Option(False, "--code", "-c", help="Generate code wrapper"),
        explain: bool = typer.Option(False, "--explain", "-e", help="Include explanation"),
        lang: str = typer.Option("python", "--lang", "-l", help="Language for code (python, bash, node)"),
        clear_cache: bool = typer.Option(False, "--clear-cache", help="Clear the query cache")
):
    """
    Ask a natural language question about FFmpeg.
    """
    # Clear cache if requested
    if clear_cache:
        cache.clear()
        console.print("[bold green]Cache cleared.[/bold green]")
        if not query:
            return

    # Check if LLM engine is ready
    if not llm_engine.is_ready():
        console.print("[bold red]Error:[/bold red] LLM engine not ready. Please run setup first.")
        console.print("Run 'python -m src.setup' to set up the FFmpeg documentation database.")
        return

    # Show processing message
    with console.status("[bold green]Generating FFmpeg command...[/bold green]"):
        # Generate response
        result = llm_engine.generate_response(
            query=query,
            code=code,
            explain=explain,
            language=lang
        )

    # Print result
    if result:
        if code and "code" in result:
            # Print code
            print_code(
                code=result["code"],
                language=lang,
                explain=result.get("explanation") if explain else None
            )

            # Also print the command
            print_command(
                command=result["command"],
                language="bash"
            )
        else:
            # Print command only
            print_command(
                command=result["command"],
                language="bash",
                explain=result.get("explanation") if explain else None
            )
    else:
        console.print("[bold red]Error:[/bold red] Failed to generate response.")


@app.command()
def setup():
    """
    Set up the FFmpeg documentation database.
    """
    console.print("[bold green]Setting up FFmpeg documentation database...[/bold green]")
    console.print("This may take a few minutes.")

    # Import setup module
    from . import setup as setup_module

    # Run setup
    setup_module.setup()

    console.print("[bold green]Setup completed.[/bold green]")
    console.print("You can now use ffmpeg-ai to ask questions about FFmpeg.")


@app.command()
def clear_cache():
    """
    Clear the query cache.
    """
    cache.clear()
    console.print("[bold green]Cache cleared.[/bold green]")


if __name__ == "__main__":
    app()