#!/usr/bin/env python3
"""
Setup script to initialize the ffmpeg-ai project structure.
"""
import os
import subprocess
import sys


def create_directory_structure():
    """Create the directory structure for the ffmpeg-ai project."""
    directories = [
        "src",
        "data/docs",
        "data/vector_store",
    ]

    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Created directory: {directory}")

    # Create placeholder README files
    with open("data/docs/README.md", "w") as f:
        f.write("# FFmpeg Documentation\n\nThis directory contains FFmpeg documentation and code snippets.\n")

    with open("data/vector_store/README.md", "w") as f:
        f.write("# Vector Store\n\nThis directory contains the ChromaDB vector store.\n")

    # Create __init__.py file for the src directory
    with open("src/__init__.py", "w") as f:
        f.write("# ffmpeg-ai source code\n")


def install_requirements():
    """Install the required packages."""
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
        print("Successfully installed requirements.")
    except subprocess.CalledProcessError:
        print("Failed to install requirements. Please run 'pip install -r requirements.txt' manually.")


def check_ollama():
    """Check if Ollama is installed and provide instructions if not."""
    try:
        result = subprocess.run(["ollama", "version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            print(f"Ollama is installed: {result.stdout.strip()}")
            print("\nNext steps:")
            print("1. Download the required model: ollama pull mistral")
            print("2. Run the setup script: python src/setup.py")
            print("3. Use the tool: python -m src.cli \"How do I extract audio from a video?\"")
        else:
            print_ollama_instructions()
    except FileNotFoundError:
        print_ollama_instructions()


def print_ollama_instructions():
    """Print instructions for installing Ollama."""
    print("\nOllama is not installed or not found in PATH.")
    print("Please install Ollama from: https://ollama.ai/")
    print("\nInstallation instructions:")
    print("- macOS/Linux: curl -fsSL https://ollama.ai/install.sh | sh")
    print("- Windows: Download and install from the Ollama website")
    print("\nAfter installing Ollama:")
    print("1. Pull the required model: ollama pull mistral")
    print("2. Run the setup script: python src/setup.py")
    print("3. Use the tool: python -m src.cli \"How do I extract audio from a video?\"")


def main():
    """Main function to set up the project."""
    print("Setting up ffmpeg-ai project...")
    create_directory_structure()
    install_requirements()
    check_ollama()


if __name__ == "__main__":
    main()