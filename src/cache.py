"""
Cache layer for ffmpeg-ai to store previous query → response mappings.
"""
import os
import json
import hashlib
from typing import Dict, Any, Optional, Tuple
from pathlib import Path
import logging

from .utils import PROJECT_ROOT

logger = logging.getLogger("ffmpeg-ai.cache")

# Cache directory
CACHE_DIR = PROJECT_ROOT / "data" / "cache"
CACHE_FILE = CACHE_DIR / "query_cache.json"

# Ensure cache directory exists
CACHE_DIR.mkdir(parents=True, exist_ok=True)


class QueryCache:
    """Cache for storing query results to avoid repeated LLM calls."""

    def __init__(self, max_size: int = 1000):
        """
        Initialize the query cache.

        Args:
            max_size: Maximum number of entries in the cache
        """
        self.max_size = max_size
        self.cache: Dict[str, Dict[str, Any]] = {}
        self._load_cache()

    def _compute_key(self, query: str, options: Dict[str, Any]) -> str:
        """
        Compute a cache key for a query and its options.

        Args:
            query: The user query
            options: Query options (explain, language, etc.)

        Returns:
            A unique hash for the query and options
        """
        # Create a string representation of the query and options
        options_str = json.dumps(options, sort_keys=True)
        key_str = f"{query.lower().strip()}|{options_str}"

        # Create a hash of the string
        return hashlib.md5(key_str.encode('utf-8')).hexdigest()

    def get(self, query: str, options: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Get a cached result for a query if it exists.

        Args:
            query: The user query
            options: Query options (explain, language, etc.)

        Returns:
            The cached result or None if not found
        """
        key = self._compute_key(query, options)
        if key in self.cache:
            logger.info(f"Cache hit for query: {query}")
            return self.cache[key]

        logger.info(f"Cache miss for query: {query}")
        return None

    def put(self, query: str, options: Dict[str, Any], result: Dict[str, Any]) -> None:
        """
        Store a result in the cache.

        Args:
            query: The user query
            options: Query options (explain, language, etc.)
            result: The result to cache
        """
        key = self._compute_key(query, options)

        # If cache is full, remove the first entry (oldest)
        if len(self.cache) >= self.max_size:
            # Get the first key
            first_key = next(iter(self.cache))
            del self.cache[first_key]

        self.cache[key] = result
        logger.info(f"Cached result for query: {query}")

        # Save the cache to disk
        self._save_cache()

    def _load_cache(self) -> None:
        """Load the cache from disk if it exists."""
        if CACHE_FILE.exists():
            try:
                with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                    self.cache = json.load(f)
                logger.info(f"Loaded {len(self.cache)} entries from cache")
            except (json.JSONDecodeError, IOError) as e:
                logger.error(f"Failed to load cache: {e}")
                self.cache = {}
        else:
            logger.info("No cache file found, starting with empty cache")
            self.cache = {}

    def _save_cache(self) -> None:
        """Save the cache to disk."""
        try:
            with open(CACHE_FILE, 'w', encoding='utf-8') as f:
                json.dump(self.cache, f, indent=2)
            logger.info(f"Saved {len(self.cache)} entries to cache")
        except IOError as e:
            logger.error(f"Failed to save cache: {e}")

    def clear(self) -> None:
        """Clear the cache."""
        self.cache = {}
        self._save_cache()
        logger.info("Cache cleared")


# Singleton instance
cache = QueryCache()