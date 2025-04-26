from setuptools import setup, find_packages
import os

# Read requirements from requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

# Ensure data directory exists
os.makedirs('ffmpeg_ai/data/ffmpeg_docs', exist_ok=True)

setup(
    name="ffmpeg-ai",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'ffmpeg-ai=ffmpeg_ai.cli:app',
        ],
    },
    python_requires='>=3.8',
    description="An intelligent FFmpeg assistant CLI tool using local LLM",
    author="Aliasgar Jiwani",
    author_email="aliasgarjiwani@gmail.com",
    url="https://github.com/Aliasgar-Jiwani/ffmpeg-ai",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={
        'ffmpeg_ai': ['data/ffmpeg_docs/*.md'],
    },
)