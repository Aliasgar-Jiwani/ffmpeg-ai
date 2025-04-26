#!/usr/bin/env python3
"""
Setup script to scrape FFmpeg documentation, chunk it, and create a vector database.
"""
import os
import logging
import requests
import html2text
from typing import List, Dict, Any
from bs4 import BeautifulSoup
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from urllib.parse import urljoin, urlparse

from .utils import DOCS_DIR, ensure_directories
from .retriever import retriever


logger = logging.getLogger("ffmpeg-ai.setup")

# FFmpeg documentation URLs
FFMPEG_DOCS = [
    "https://ffmpeg.org/ffmpeg.html",
    "https://ffmpeg.org/ffmpeg-all.html",
    "https://ffmpeg.org/ffmpeg-filters.html",
    "https://ffmpeg.org/ffmpeg-formats.html",
    "https://ffmpeg.org/ffmpeg-codecs.html",
    "https://ffmpeg.org/ffmpeg-utils.html",
]

# StackOverflow FFmpeg tag URL
STACKOVERFLOW_FFMPEG = "https://stackoverflow.com/questions/tagged/ffmpeg?tab=votes&pagesize=50"

# Common FFmpeg usage examples
COMMON_USAGE = [
    {
        "title": "Extract audio from video",
        "content": "To extract audio from a video file:\n\nffmpeg -i input.mp4 -q:a 0 -map a output.mp3",
        "metadata": {"type": "usage", "topic": "audio extraction"}
    },
    {
        "title": "Convert video format",
        "content": "To convert a video from one format to another:\n\nffmpeg -i input.mov -c:v libx264 -c:a aac -strict experimental output.mp4",
        "metadata": {"type": "usage", "topic": "format conversion"}
    },
    {
        "title": "Trim video",
        "content": "To trim a video to a specific duration:\n\nffmpeg -i input.mp4 -ss 00:01:00 -to 00:02:00 -c copy output.mp4",
        "metadata": {"type": "usage", "topic": "trim"}
    },
    {
        "title": "Scale video resolution",
        "content": "To scale a video to a specific resolution:\n\nffmpeg -i input.mp4 -vf scale=1280:720 -c:a copy output.mp4",
        "metadata": {"type": "usage", "topic": "scaling"}
    },
    {
        "title": "Extract frames",
        "content": "To extract frames from a video:\n\nffmpeg -i input.mp4 -vf fps=1 frames/frame_%04d.png",
        "metadata": {"type": "usage", "topic": "frame extraction"}
    },
    {
        "title": "Convert video to GIF",
        "content": "To convert a video to GIF:\n\nffmpeg -i input.mp4 -vf \"fps=10,scale=320:-1:flags=lanczos\" -c:v gif output.gif",
        "metadata": {"type": "usage", "topic": "gif conversion"}
    },
    {
        "title": "Add subtitles to video",
        "content": "To add subtitles to a video:\n\nffmpeg -i input.mp4 -vf subtitles=subtitles.srt output.mp4",
        "metadata": {"type": "usage", "topic": "subtitles"}
    },
    {
        "title": "Convert video to HLS",
        "content": "To convert a video to HLS format for streaming:\n\nffmpeg -i input.mp4 -profile:v baseline -level 3.0 -start_number 0 -hls_time 10 -hls_list_size 0 -f hls output.m3u8",
        "metadata": {"type": "usage", "topic": "streaming"}
    },
    {
        "title": "Concatenate videos",
        "content": "To concatenate multiple videos:\n\n1. Create a text file (inputs.txt):\nfile 'input1.mp4'\nfile 'input2.mp4'\n\n2. Run the command:\nffmpeg -f concat -safe 0 -i inputs.txt -c copy output.mp4",
        "metadata": {"type": "usage", "topic": "concatenation"}
    },
    {
        "title": "Extract audio from video (Python)",
        "content": "Python script:\n\n```python\nimport subprocess\n\ndef extract_audio(input_file, output_file):\n    cmd = ['ffmpeg', '-i', input_file, '-q:a', '0', '-map', 'a', output_file]\n    subprocess.run(cmd)\n\nextract_audio('input.mp4', 'output.mp3')\n```",
        "metadata": {"type": "code", "language": "python", "topic": "audio extraction"}
    },
    {
        "title": "Convert video format (Bash)",
        "content": "Bash script:\n\n```bash\n#!/bin/bash\ninput_file=$1\noutput_file=$2\nffmpeg -i \"$input_file\" -c:v libx264 -c:a aac -strict experimental \"$output_file\"\n```",
        "metadata": {"type": "code", "language": "bash", "topic": "format conversion"}
    },
    {
        "title": "Trim video (Node.js)",
        "content": "Node.js script:\n\n```javascript\nconst { spawn } = require('child_process');\n\nfunction trimVideo(inputFile, outputFile, startTime, endTime) {\n  const cmd = 'ffmpeg';\n  const args = [\n    '-i', inputFile,\n    '-ss', startTime,\n    '-to', endTime,\n    '-c', 'copy',\n    outputFile\n  ];\n  const ffmpeg = spawn(cmd, args);\n  ffmpeg.on('close', (code) => {\n    console.log(`Process exited with code ${code}`);\n  });\n}\n\ntrimVideo('input.mp4', 'output.mp4', '00:01:00', '00:02:00');\n```",
        "metadata": {"type": "code", "language": "javascript", "topic": "trim"}
    }
]


def scrape_ffmpeg_docs() -> List[Dict[str, Any]]:
    docs = []
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = True

    for url in FFMPEG_DOCS:
        try:
            logger.info(f"Scraping {url}")
            response = requests.get(url)
            response.raise_for_status()
            markdown = h.handle(response.text)
            page_name = url.split('/')[-1].replace('.html', '')
            with open(DOCS_DIR / f"{page_name}.md", "w", encoding="utf-8") as f:
                f.write(markdown)
            docs.append({
                "title": f"FFmpeg {page_name} Documentation",
                "content": markdown,
                "metadata": {"type": "documentation", "source": url}
            })
            logger.info(f"Successfully scraped {url}")
        except Exception as e:
            logger.error(f"Failed to scrape {url}: {e}")
    return docs


def scrape_stackoverflow() -> List[Dict[str, Any]]:
    docs = []
    h = html2text.HTML2Text()
    h.ignore_links = True
    h.ignore_images = True

    try:
        logger.info(f"Scraping {STACKOVERFLOW_FFMPEG}")
        response = requests.get(STACKOVERFLOW_FFMPEG)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        questions = soup.select('.question-hyperlink')

        for i, question in enumerate(questions[:30]):
            try:
                href = question['href']
                parsed_href = urlparse(href)

                # Skip external StackExchange sites
                if parsed_href.netloc and parsed_href.netloc != 'stackoverflow.com':
                    logger.debug(f"Skipping external question: {href}")
                    continue

                base_url = "https://stackoverflow.com"
                question_url = urljoin(base_url, href)
                logger.info(f"Scraping question: {question_url}")

                q_response = requests.get(question_url)
                q_response.raise_for_status()
                q_soup = BeautifulSoup(q_response.text, 'html.parser')

                q_title = q_soup.select_one('.question-hyperlink').text
                q_body = q_soup.select_one('.js-post-body')
                q_text = h.handle(str(q_body)) if q_body else ""

                answer = (q_soup.select_one('.js-accepted-answer .js-post-body') or
                          q_soup.select_one('.answercell .js-post-body'))
                a_text = h.handle(str(answer)) if answer else ""

                content = f"Question: {q_title}\n\n{q_text}\n\nAnswer:\n{a_text}"
                docs.append({
                    "title": q_title,
                    "content": content,
                    "metadata": {"type": "stackoverflow", "source": question_url}
                })

                if i > 0 and i % 5 == 0:
                    import time
                    time.sleep(2)
            except Exception as e:
                logger.error(f"Failed to scrape question {question.text}: {e}")
    except Exception as e:
        logger.error(f"Failed to scrape StackOverflow: {e}")
    return docs


def chunk_documents(documents: List[Dict[str, Any]]) -> List[Document]:
    logger.info(f"Chunking {len(documents)} documents")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    chunks = []
    for doc in documents:
        doc_chunks = text_splitter.split_text(doc["content"])
        for i, chunk in enumerate(doc_chunks):
            chunks.append(
                Document(
                    page_content=chunk,
                    metadata={
                        "title": doc["title"],
                        "chunk": i,
                        **doc["metadata"]
                    }
                )
            )
    logger.info(f"Created {len(chunks)} chunks")
    return chunks


def create_vector_store(chunks: List[Document]) -> None:
    logger.info("Creating vector store")
    retriever.add_documents(chunks)
    logger.info("Vector store created successfully")


def setup():
    logger.info("Starting FFmpeg documentation setup")
    ensure_directories()
    documents = []
    documents.extend(COMMON_USAGE)
    logger.info(f"Added {len(COMMON_USAGE)} common usage examples")
    ffmpeg_docs = scrape_ffmpeg_docs()
    documents.extend(ffmpeg_docs)
    logger.info(f"Added {len(ffmpeg_docs)} FFmpeg documentation pages")
    stackoverflow_docs = scrape_stackoverflow()
    documents.extend(stackoverflow_docs)
    logger.info(f"Added {len(stackoverflow_docs)} StackOverflow Q&A")
    chunks = chunk_documents(documents)
    create_vector_store(chunks)
    logger.info("Setup completed successfully")


if __name__ == "__main__":
    setup()