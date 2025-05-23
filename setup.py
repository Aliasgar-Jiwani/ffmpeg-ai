from setuptools import setup, find_packages

# Read the contents of README.md
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="ffmpeg-ai",
    version="0.1.8",
    description="AI-powered FFmpeg command generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Aliasgar Jiwani",
    author_email="aliasgarjiwani@gmail.com",
    url="https://github.com/Aliasgar-Jiwani/ffmpeg-ai",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "typer",
        "rich",
        "langchain",
        "ollama",
        "chromadb",
        "requests",
        "beautifulsoup4",
        "html2text",
        "langchain-huggingface",
    ],
    entry_points={
        "console_scripts": [
            "ffmpeg-ai=ffmpeg_ai.cli:app",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
