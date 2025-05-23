import os
import sys
import logging
from typing import List, Dict, Any, Optional
from pathlib import Path

import chromadb
from chromadb.config import Settings

# Updated import to avoid deprecation warnings
try:
    from langchain_chroma import Chroma
except ImportError:
    # Fallback to the old import if the new package isn't installed
    print("Warning: langchain-chroma not installed. Install with: pip install -U langchain-chroma")
    from langchain_community.vectorstores import Chroma

from langchain_huggingface import HuggingFaceEmbeddings
from langchain.schema import Document

from .utils import VECTOR_STORE_DIR, ensure_directories

# Configure logging
logger = logging.getLogger("ffmpeg-ai.retriever")


class FFmpegRetriever:
    """Retriever for FFmpeg documentation and code snippets."""

    def __init__(self,
                 embedding_model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
                 collection_name: str = "ffmpeg_docs"):
        """
        Initialize the FFmpeg retriever.

        Args:
            embedding_model_name: The name of the embedding model to use
            collection_name: The name of the ChromaDB collection
        """
        self.embedding_model_name = embedding_model_name
        self.collection_name = collection_name
        self.embeddings = None
        self.vectorstore = None

        # Ensure the vector store directory exists
        ensure_directories()

        # Initialize the embedding model and vector store
        self._initialize()

    def _initialize(self) -> None:
        """Initialize the embedding model and vector store."""
        try:
            logger.info(f"Initializing embedding model: {self.embedding_model_name}")
            self.embeddings = HuggingFaceEmbeddings(model_name=self.embedding_model_name)

            # Correct check: only check if VECTOR_STORE_DIR exists
            if VECTOR_STORE_DIR.exists() and any(VECTOR_STORE_DIR.iterdir()):
                logger.info(f"Loading existing vector store from {VECTOR_STORE_DIR}")
                self.vectorstore = Chroma(
                    collection_name=self.collection_name,
                    embedding_function=self.embeddings,
                    persist_directory=str(VECTOR_STORE_DIR)
                )
            else:
                logger.warning("Vector store not found. Please run setup.py first to create it.")
                self.vectorstore = None

        except Exception as e:
            logger.error(f"Failed to initialize retriever: {e}")
            self.embeddings = None
            self.vectorstore = None

    def is_ready(self) -> bool:
        """
        Check if the retriever is ready to use.

        Returns:
            True if the retriever is ready, False otherwise
        """
        return self.embeddings is not None and self.vectorstore is not None

    def retrieve(self, query: str, k: int = 5) -> List[Document]:
        """
        Retrieve relevant documents for a query.

        Args:
            query: The query to search for
            k: The number of documents to retrieve

        Returns:
            A list of retrieved documents
        """
        if not self.is_ready():
            logger.error("Retriever not initialized. Please run setup.py first.")
            return []

        try:
            logger.info(f"Retrieving documents for query: {query}")
            docs = self.vectorstore.similarity_search(query, k=k)
            logger.info(f"Retrieved {len(docs)} documents")
            return docs

        except Exception as e:
            logger.error(f"Error retrieving documents: {e}")
            return []

    def add_documents(self, docs: List[Document]) -> None:
        """
        Add documents to the vector store.

        Args:
            docs: The documents to add
        """
        if self.embeddings is None:
            logger.error("Embedding model not initialized")
            return

        try:
            logger.info(f"Adding {len(docs)} documents to vector store")

            # Create a new vector store if it doesn't exist
            if self.vectorstore is None:
                self.vectorstore = Chroma.from_documents(
                    documents=docs,
                    embedding=self.embeddings,
                    collection_name=self.collection_name,
                    persist_directory=str(VECTOR_STORE_DIR)
                )
            else:
                # Add documents to existing vector store
                self.vectorstore.add_documents(docs)

            # Persist the vector store
            self.vectorstore.persist()
            logger.info("Documents added and vector store persisted")

        except Exception as e:
            logger.error(f"Error adding documents: {e}")


# Create a singleton instance
retriever = FFmpegRetriever()