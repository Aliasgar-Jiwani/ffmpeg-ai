#!/bin/bash
set -e

echo "Installing FFmpeg AI Assistant..."

# Check if Python 3.8+ is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is required but not found. Please install Python 3.8 or higher."
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)

if [ "$PYTHON_MAJOR" -lt 3 ] || ([ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 8 ]); then
    echo "Python 3.8 or higher is required. Found: Python $PYTHON_VERSION"
    exit 1
fi

# Check if Ollama is installed
if ! command -v ollama &> /dev/null; then
    echo "Ollama is required but not found."
    echo "Would you like to install Ollama? (y/n)"
    read -r INSTALL_OLLAMA

    if [[ "$INSTALL_OLLAMA" =~ ^[Yy]$ ]]; then
        echo "Installing Ollama..."
        # Check OS and install accordingly
        if [[ "$OSTYPE" == "darwin"* ]]; then
            # macOS
            curl -fsSL https://ollama.com/install.sh | sh
        elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
            # Linux
            curl -fsSL https://ollama.com/install.sh | sh
        else
            echo "Please install Ollama manually from https://ollama.com/download"
            echo "After installing Ollama, run this script again."
            exit 1
        fi
    else
        echo "Please install Ollama manually from https://ollama.com/download"
        echo "After installing Ollama, run this script again."
        exit 1
    fi
fi

# Create a virtual environment
echo "Creating virtual environment..."
python3 -m venv .venv
source .venv/bin/activate

# Install the package
echo "Installing FFmpeg AI Assistant..."
pip install -e .

# Pull Ollama model
echo "Downloading Mistral model for Ollama..."
ollama pull mistral

# Generate example documentation
echo "Generating example documentation..."
python -c "from ffmpeg_ai.data_loader import FFmpegDocLoader; FFmpegDocLoader().create_example_docs()"

echo "Installation complete!"
echo "You can now use FFmpeg AI Assistant by running the 'ffmpeg-ai' command."
echo "Example: ffmpeg-ai \"convert .mov to .mp4 using H.264 codec\""

# Create an activation script for future use
cat > activate-ffmpeg-ai.sh << 'EOF'
#!/bin/bash
source .venv/bin/activate
echo "FFmpeg AI Assistant environment activated. You can now use the 'ffmpeg-ai' command."
EOF

chmod +x activate-ffmpeg-ai.sh

echo "To activate the environment in future sessions, run: source ./activate-ffmpeg-ai.sh"