# FFmpeg AI Assistant

A command-line utility that acts as an intelligent FFmpeg assistant for developers. This tool runs entirely offline and uses a local LLM via Ollama to provide context-aware FFmpeg commands, code snippets, and explanations.

---

## Features

- Generate FFmpeg commands from natural language queries
- Get Python, Bash, or Node.js code wrappers for FFmpeg commands
- Detailed explanations of command parameters
- 100% offline operation with local LLM and vector database
- Smart caching for repeated queries
- Easy customization and model switching

---

## Installation

### Recommended: PyPI Installation

Install the tool from PyPI using:

```bash
pip install ffmpeg-ai
```

---

## Documentation Setup After Installation

After installing, you must initialize the documentation database:

```bash
ffmpeg-ai setup
```

### Command-Line Interface

Once installed, you can interact with the tool via the command line. Use the following command to get help:

```bash
ffmpeg-ai --help
```

This will display the available options and commands:

```
Usage: ffmpeg-ai --help

AI-powered FFmpeg command generator

Options:
  --help  Show this message and exit.

Commands:
  query        Ask a natural language question about FFmpeg.
  setup        Set up the FFmpeg documentation database.
  clear-cache  Clear the query cache.
```

---

## Documentation Setup

Running `ffmpeg-ai setup` will:

- Download and parse FFmpeg's official documentation
- Create vector embeddings for faster and more accurate querying
- Store the embeddings locally for offline use

---

## Real Usage Example

Here's an example of using the tool in your project:

```bash
# In your project directory, run:
ffmpeg-ai query "convert .mov to .mp4 using H.264 codec" --code
```

**Result:**

**FFmpeg Command:**

```bash
ffmpeg -i input.mov -vcodec libx264 output.mp4
```

**Generated Python Script:**

```python
import os
import subprocess

def convert_mov_to_mp4(input_file, output_file):
    command = f'ffmpeg -i {input_file} -vcodec libx264 {output_file}'
    subprocess.run(command, shell=True, check=True)

# Usage example:
input_file = 'input.mov'
output_file = 'output.mp4'
convert_mov_to_mp4(input_file, output_file)
```

---

## How It Works

1. **Document Retrieval**: Fetches the most relevant chunks from embedded FFmpeg documentation using sentence-transformers and ChromaDB.
2. **Query Augmentation**: Combines your query with retrieved context before sending it to the local LLM.
3. **LLM Generation**: The local model (e.g., Mistral) generates the command, code, and explanations.
4. **Result Formatting**: Outputs are formatted cleanly and cached for faster future retrieval.

---

## Requirements

- Python 3.10+
- FFmpeg installed system-wide
- Ollama installed and running
- Local machine with ~8GB RAM or more recommended

---

## Limitations

- Responses depend on the quality of the local LLM model.
- Currently limited to embedded and user-added FFmpeg documentation.
- Hardware-intensive for optimal performance.

---

## License

MIT License
