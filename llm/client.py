from langchain.chat_models import ChatOpenAI, ChatVertexAI, ChatGoogleGenerativeAI
from langchain.llms import AzureOpenAI, VertexAI
from langchain.embeddings import VertexAIEmbeddings
from config.settings import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_ENDPOINT,
    GOOGLE_API_KEY,
    GCP_PROJECT_ID,
)
from utils.logger import setup_logger

logger = setup_logger()


class LLMClient:
    """class for accessing various LLM models"""

    def __init__(self):
        """Initialize AI models"""
        try:
            # Initialize Azure OpenAI
            self._init_azure_models()

            # Initialize Google Vertex AI models
            self._init_vertex_models()

            # Initialize Google Generative AI models (Gemini)
            self._init_gemini_models()

            logger.info("LLMClient initialized successfully")
        except Exception as e:
            logger.error(f"Error initializing LLMClient: {e}")
            raise

    def _init_azure_models(self):
        """Initialize Azure OpenAI models"""
        try:
            self.azure_openai_llm = AzureOpenAI(
                deployment_name="gpt-35-turbo-instruct-model",
                openai_api_version="2023-07-01-preview",
                model_name="gpt-35-turbo-instruct",
                azure_endpoint=AZURE_OPENAI_ENDPOINT,
                api_key=AZURE_OPENAI_API_KEY,
                max_tokens=800,
            )

            # Add Azure OpenAI chat model if needed
            self.azure_openai_chat = ChatOpenAI(
                deployment_name="gpt-4-model",
                openai_api_version="2023-07-01-preview",
                model_name="gpt-4",
                azure_endpoint=AZURE_OPENAI_ENDPOINT,
                api_key=AZURE_OPENAI_API_KEY,
                max_tokens=1000,
            )
        except Exception as e:
            logger.error(f"Failed to initialize Azure models: {e}")
            # Consider whether to raise or continue with partial initialization

    def _init_vertex_models(self):
        """Initialize Google Vertex AI models"""
        try:
            # Text models
            self.palm_llm = VertexAI(
                project=GCP_PROJECT_ID,
                model_name="text-bison",
                max_tokens=2048,
            )

            # Chat models
            self.palm_chat_model = ChatVertexAI(
                project=GCP_PROJECT_ID,
                model_name="chat-bison",
                max_tokens=2048,
            )

            # Embedding models
            self.palm_embeddings = VertexAIEmbeddings(
                project=GCP_PROJECT_ID,
                model_name="textembedding-gecko-multilingual@latest",
            )
        except Exception as e:
            logger.error(f"Failed to initialize Vertex AI models: {e}")

    def _init_gemini_models(self):
        """Initialize Google Generative AI (Gemini) models"""
        try:
            # Vertex AI Gemini
            self.gemini_llm = VertexAI(
                project=GCP_PROJECT_ID,
                model_name="gemini-pro",
                max_tokens=2048,
            )

            self.gemini_chat_model = ChatVertexAI(
                project=GCP_PROJECT_ID,
                model_name="gemini-pro",
                convert_system_message_to_human=True,
            )

            # Direct Gemini API models
            self.gemini_gen_chat_model = ChatGoogleGenerativeAI(
                google_api_key=GOOGLE_API_KEY,
                model="gemini-pro",
                max_tokens=2048,
            )

            self.gemini_vision_model = ChatGoogleGenerativeAI(
                google_api_key=GOOGLE_API_KEY,
                model="gemini-pro-vision",
            )
        except Exception as e:
            logger.error(f"Failed to initialize Gemini models: {e}")

    def get_default_llm(self):
        """Get the default LLM for general text generation"""
        return self.gemini_chat_model  # You can change the default as needed

    def get_vision_model(self):
        """Get the model for vision tasks"""
        return self.gemini_vision_model

    def get_embedding_model(self):
        """Get the model for embeddings"""
        return self.palm_embeddings
