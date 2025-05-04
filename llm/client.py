from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI

from config.settings import (
    OPENAI_MODEL,
    OLLAMA_MODEL,
    GEMINI_API_KEY,
    GEMINI_MODEL,
)
from utils.logger import setup_logger

logger = setup_logger()


class LLMClient:
    """class for accessing various LLM models"""

    def __init__(self, temperature=0.5):
        self.temperature = temperature

        try:
            self._init_openai_models()
            self._init_ollama_models()
            self._init_gemini_models()

            logger.info("LLMClient initialized successfully")
        except Exception as e:
            logger.error(f"Error initializing LLMClient: {e}")
            raise

    def _init_openai_models(self):
        try:
            self.openai_chat_model = ChatOpenAI(
                model=OPENAI_MODEL,
                temperature=self.temperature,
                max_tokens=800,
            )
            logger.info("OpenAI models initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize OpenAI models: {e}")

    def _init_ollama_models(self):
        try:
            self.ollama_chat_model = ChatOllama(
                model=OLLAMA_MODEL,
                temperature=self.temperature,
            )
            logger.info("Ollama models initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize Ollama models: {e}")

    def _init_gemini_models(self):
        try:
            self.gemini_chat_model = ChatGoogleGenerativeAI(
                model=GEMINI_MODEL,
                temperature=self.temperature,
                google_api_key=GEMINI_API_KEY,
            )
            logger.info("Gemini model initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize Gemini model: {e}")

    def get_default_llm(self):
        return self.gemini_chat_model

    def get_openai_chat_llm(self):
        return self.openai_chat_model

    def get_ollama_chat_llm(self):
        return self.ollama_chat_model

    def get_gemini_chat_llm(self):
        return self.gemini_chat_model
