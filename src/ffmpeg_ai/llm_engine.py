"""
LLM engine for ffmpeg-ai using Ollama for local inferencing.
"""
import os
import logging
import subprocess
from typing import List, Dict, Any, Optional

import ollama
from langchain_core.prompts import PromptTemplate
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser

# Updated imports to avoid deprecation warnings
try:
    from langchain_ollama import OllamaLLM
except ImportError:
    # Fallback to the old import if the new package isn't installed
    print("Warning: langchain-ollama not installed. Install with: pip install -U langchain-ollama")
    from langchain_community.llms import Ollama as OllamaLLM

from .retriever import retriever
from .cache import cache

# Configure logging
logger = logging.getLogger("ffmpeg-ai.llm_engine")

# Default Ollama model - use base name without tag for more flexible matching
DEFAULT_MODEL = "mistral"

# Prompt templates
FFMPEG_PROMPT_TEMPLATE = """
You are an expert at FFmpeg, the multimedia framework for processing audio and video.
Your task is to help users generate correct FFmpeg commands based on their natural language queries.

Here is some relevant FFmpeg documentation that might help:

{context}

User Query: {query}

{format_instructions}

First, analyze what the user is trying to accomplish with FFmpeg.
Then, provide the most appropriate FFmpeg command to fulfill their request.
Make sure your command is complete, correct, and follows best practices.
"""

CODE_FORMAT_INSTRUCTIONS = """
Please respond with:
1. The FFmpeg command that addresses the user's query.
2. A {language} script that wraps this FFmpeg command for easier use.
{explain_instructions}

Format your response as follows:
COMMAND: <the FFmpeg command>
CODE: <the {language} script>
{explain_format}
"""

COMMAND_FORMAT_INSTRUCTIONS = """
Please respond with the FFmpeg command that addresses the user's query.
{explain_instructions}

Format your response as follows:
COMMAND: <the FFmpeg command>
{explain_format}
"""

EXPLAIN_INSTRUCTIONS = "Also include a detailed explanation of how the command works."
EXPLAIN_FORMAT = "EXPLANATION: <detailed explanation of how the command works>"


class FFmpegLLMEngine:
    """LLM Engine for generating FFmpeg commands."""

    def __init__(self, model_name: str = DEFAULT_MODEL):
        """
        Initialize the FFmpeg LLM Engine.

        Args:
            model_name: The name of the Ollama model to use
        """
        self.model_name = model_name
        self.llm = None

        # Initialize the LLM
        self._initialize()

    def _initialize(self) -> None:
        """Initialize the LLM."""
        try:
            # Check if Ollama is running and the model is available
            if not self._check_ollama():
                return

            logger.info(f"Initializing LLM with model: {self.model_name}")
            self.llm = OllamaLLM(model=self.model_name)
            logger.info("LLM initialized successfully")

        except Exception as e:
            logger.error(f"Failed to initialize LLM: {e}")
            logger.error(f"Exception details: {str(e)}")
            self.llm = None

    def _check_ollama(self) -> bool:
        """
        Check if Ollama is running and the model is available.

        Returns:
            True if Ollama is running and the model is available, False otherwise
        """
        try:
            # Check if Ollama is running
            models_resp = ollama.list()
            logger.debug(f"Raw Ollama response: {models_resp}")

            # Debug the actual structure of the response
            if isinstance(models_resp, dict):
                logger.debug(f"Ollama response keys: {models_resp.keys()}")

            # Extract model information - handle different possible response formats
            available_models = []

            if isinstance(models_resp, dict) and 'models' in models_resp:
                # Process the models list
                for model in models_resp.get('models', []):
                    if isinstance(model, dict) and 'name' in model:
                        model_name = model.get('name', '')
                        if model_name:  # Only add non-empty names
                            available_models.append(model_name)

                            # Also add base name without tag for flexible matching
                            if ':' in model_name:
                                base_name = model_name.split(':')[0]
                                if base_name:
                                    available_models.append(base_name)

            # If we couldn't parse the response correctly, try a different approach
            if not available_models:
                logger.warning("Couldn't parse model list from standard response format")
                # Direct command to list models as a fallback
                try:
                    import subprocess
                    import json
                    result = subprocess.run(['ollama', 'list', '--json'],
                                            capture_output=True, text=True)
                    if result.stdout:
                        models_data = json.loads(result.stdout)
                        if isinstance(models_data, list):
                            for model_info in models_data:
                                if isinstance(model_info, dict) and 'name' in model_info:
                                    model_name = model_info.get('name')
                                    if model_name:
                                        available_models.append(model_name)
                                        # Also add base name
                                        if ':' in model_name:
                                            base_name = model_name.split(':')[0]
                                            if base_name:
                                                available_models.append(base_name)
                except Exception as e:
                    logger.warning(f"Fallback model list attempt failed: {e}")

            # Print found models for debugging
            logger.info(f"Available model names: {available_models}")

            # If still no models found, use a hardcoded approach
            if not available_models and self.model_name == "mistral":
                # We know from your CLI output that mistral:latest exists
                logger.info("No models detected but command line showed mistral:latest exists")
                logger.info("Using mistral:latest directly")
                self.model_name = "mistral:latest"
                return True

            # More flexible model checking - match either exact name or base name
            if available_models and self.model_name not in available_models:
                # Try to find if any model starts with the requested name
                matching_models = [m for m in available_models if m.startswith(self.model_name)]

                if matching_models:
                    # Use the first matching model
                    logger.info(f"Using model {matching_models[0]} instead of exact match for {self.model_name}")
                    self.model_name = matching_models[0]
                else:
                    logger.error(f"Model {self.model_name} not found. Available models: {available_models}")
                    logger.error(f"Please run 'ollama pull {self.model_name}'")
                    return False

            return True

        except Exception as e:
            logger.error(f"Failed to connect to Ollama: {e}")
            logger.error("Please ensure Ollama is installed and running")

            # Try to check if Ollama server is running
            try:
                # Simple check using subprocess to see if Ollama process is running
                if os.name == 'nt':  # Windows
                    process = subprocess.run(['tasklist', '/FI', 'IMAGENAME eq ollama.exe'],
                                             capture_output=True, text=True)
                    if 'ollama.exe' not in process.stdout:
                        logger.error("Ollama process not found. Please start Ollama service.")
                else:  # Unix-like
                    process = subprocess.run(['pgrep', 'ollama'],
                                             capture_output=True, text=True)
                    if not process.stdout.strip():
                        logger.error("Ollama process not found. Please start Ollama service.")
            except Exception:
                # If the subprocess check fails, don't add more errors
                pass

            return False

    def is_ready(self) -> bool:
        """
        Check if the LLM engine is ready to use.

        Returns:
            True if the LLM engine is ready, False otherwise
        """
        if self.llm is None:
            logger.error("LLM not initialized. Please check Ollama setup.")
            return False

        if not retriever.is_ready():
            logger.error("Retriever not ready. Please check documentation database.")
            return False

        return True

    def generate_response(self,
                          query: str,
                          code: bool = False,
                          explain: bool = False,
                          language: str = "bash") -> Optional[Dict[str, str]]:
        """
        Generate a response for a user query.

        Args:
            query: The user query
            code: Whether to generate code
            explain: Whether to include an explanation
            language: The language for the code (python, bash, node)

        Returns:
            A dictionary containing the command, code (optional), and explanation (optional)
        """
        if not self.is_ready():
            logger.error("LLM engine not ready. Please check Ollama and the retriever setup.")
            return None

        # Check cache first
        options = {
            "code": code,
            "explain": explain,
            "language": language
        }
        cached_result = cache.get(query, options)
        if cached_result:
            return cached_result

        try:
            # Retrieve relevant documents
            docs = retriever.retrieve(query, k=5)
            if not docs:
                logger.warning("No relevant documents found")

            # Prepare context from retrieved documents
            context = "\n\n".join([doc.page_content for doc in docs]) if docs else "No specific documentation found."

            # Set format instructions based on options
            if code:
                explain_instructions = EXPLAIN_INSTRUCTIONS if explain else ""
                explain_format = EXPLAIN_FORMAT if explain else ""
                format_instructions = CODE_FORMAT_INSTRUCTIONS.format(
                    language=language,
                    explain_instructions=explain_instructions,
                    explain_format=explain_format
                )
            else:
                explain_instructions = EXPLAIN_INSTRUCTIONS if explain else ""
                explain_format = EXPLAIN_FORMAT if explain else ""
                format_instructions = COMMAND_FORMAT_INSTRUCTIONS.format(
                    explain_instructions=explain_instructions,
                    explain_format=explain_format
                )

            # Create prompt
            prompt = PromptTemplate(
                input_variables=["context", "query", "format_instructions"],
                template=FFMPEG_PROMPT_TEMPLATE
            )

            # Create chain using the new LCEL (LangChain Expression Language) syntax
            # This replaces the deprecated LLMChain
            output_parser = StrOutputParser()
            chain = prompt | self.llm | output_parser

            # Run chain using invoke instead of the deprecated run method
            logger.info(f"Generating response for query: {query}")
            response = chain.invoke({
                "context": context,
                "query": query,
                "format_instructions": format_instructions
            })

            # Parse response
            result = self._parse_response(response, code, explain)

            # Cache result
            cache.put(query, options, result)

            return result

        except Exception as e:
            logger.error(f"Error generating response: {e}")
            return None

    def _parse_response(self,
                        response: str,
                        code: bool,
                        explain: bool) -> Dict[str, str]:
        """
        Parse the LLM response into a structured format.

        Args:
            response: The raw LLM response
            code: Whether code was requested
            explain: Whether an explanation was requested

        Returns:
            A dictionary containing the command, code (optional), and explanation (optional)
        """
        lines = response.strip().split('\n')
        result = {}

        current_section = None
        section_content = []

        for line in lines:
            # Check for section headers
            if line.startswith("COMMAND:"):
                if current_section and section_content:
                    result[current_section.lower()] = '\n'.join(section_content).strip()
                    section_content = []
                current_section = "COMMAND"
                continue
            elif line.startswith("CODE:"):
                if current_section and section_content:
                    result[current_section.lower()] = '\n'.join(section_content).strip()
                    section_content = []
                current_section = "CODE"
                continue
            elif line.startswith("EXPLANATION:"):
                if current_section and section_content:
                    result[current_section.lower()] = '\n'.join(section_content).strip()
                    section_content = []
                current_section = "EXPLANATION"
                continue

            # Add content to current section
            if current_section:
                section_content.append(line)

        # Add the last section
        if current_section and section_content:
            result[current_section.lower()] = '\n'.join(section_content).strip()

        # Ensure the command is present
        if "command" not in result:
            # Try to extract the command from the response
            for line in lines:
                if line.strip().startswith("ffmpeg"):
                    result["command"] = line.strip()
                    break

            # If still not found, use the whole response
            if "command" not in result:
                result["command"] = response.strip()

        return result


# Create a singleton instance
llm_engine = FFmpegLLMEngine()