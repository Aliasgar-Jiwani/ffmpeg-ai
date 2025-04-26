# FFmpeg AI Assistant

A command-line utility that acts as an intelligent FFmpeg assistant for developers. This tool runs entirely offline and uses a local LLM via Ollama to provide context-aware FFmpeg commands and code.

## Features

- Generate FFmpeg commands based on natural language queries
- Get Python or Bash code wrappers for FFmpeg commands
- Detailed explanations of how commands work
- 100% offline operation - no external API calls
- Caching of previous queries for faster reuse

## Installation

### One-Line Installation

For Linux and macOS users:

```bash
curl -fsSL https://raw.githubusercontent.com/Aliasgar-Jiwani/ffmpeg-ai/main/install.sh | bash

```

Or download the repository and run the installation script:

```bash
git clone https://github.com/yourusername/ffmpeg-ai.git
cd ffmpeg-ai
bash install.sh
```

### Manual Installation

1. **Install Ollama**

   Follow the instructions at [ollama.com/download](https://ollama.com/download) to install Ollama on your system.

2. **Install FFmpeg AI Assistant**

   ```bash
   # Clone this repository
   git clone https://github.com/Aliasgar-Jiwani/ffmpeg-ai.git
   cd ffmpeg-ai

   # Install the package
   pip install -e .

   # Pull the Mistral model
   ollama pull mistral

   # Generate example documentation
   python -c "from ffmpeg_ai.data_loader import FFmpegDocLoader; FFmpegDocLoader().create_example_docs()"
   ```

## Usage

After installation, you can use the `ffmpeg-ai` command directly:

```bash
# Basic usage
ffmpeg-ai "convert .mov to .mp4 using H.264 codec"

# Get Python code
ffmpeg-ai "extract audio from video" --code python

# Get detailed explanation
ffmpeg-ai "scale video to 720p" --explain

# Force bypass cache
ffmpeg-ai "convert video to HLS" --force
```

## Examples

1. **Convert MOV to MP4**

   ```bash
   ffmpeg-ai "convert .mov to .mp4 using H.264 codec"
   ```

2. **Extract keyframes with Python code**

   ```bash
   ffmpeg-ai "extract keyframes" --code python
   ```

3. **Scale video to 720p with explanation**

   ```bash
   ffmpeg-ai "scale video to 720p" --explain
   ```

## How It Works

1. When you make a query, the system searches through embedded FFmpeg documentation chunks using sentence transformers and ChromaDB.
2. The most relevant documentation chunks are retrieved and sent to the local LLM along with your query.
3. The LLM generates a response, which is parsed into command, code, and explanation components.
4. The results are displayed in a formatted way and cached for future use.

## Customization

### Adding More Documentation

You can add more FFmpeg documentation to improve the assistant's knowledge:

1. Create markdown files in the `~/.ffmpeg_ai/docs` directory
2. Follow the format of the existing documentation files
3. Use the `--force` flag to refresh the document embeddings

### Changing the LLM Model

You can switch to a different Ollama model:

```bash
# Pull a different model
ollama pull llama2

# Use it with the --model flag
ffmpeg-ai "convert video to gif" --model llama2
```

## Limitations

- The quality of responses depends on the LLM model you're using
- Limited to the FFmpeg documentation included in the data directory
- Performance depends on your local hardware capabilities

## License

MIT