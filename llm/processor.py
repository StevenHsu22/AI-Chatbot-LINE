from langchain.output_parsers import PydanticOutputParser

from api.models import GrammarOutput
from llm.prompts import GRAMMAR_ANALYSIS_PROMPT
from llm.client import LLMClient
from utils.logger import setup_logger

logger = setup_logger()


class GrammarProcessor:

    def __init__(self):
        self.parser = PydanticOutputParser(pydantic_object=GrammarOutput)

        self.llm_client = LLMClient()
        self.model = self.llm_client.get_default_llm()
        self.openai_model = self.llm_client.get_openai_chat_llm()
        # self.ollama_model = self.llm_client.get_ollama_chat_llm()

        self.prompt = GRAMMAR_ANALYSIS_PROMPT.partial(
            format_instructions=self.parser.get_format_instructions()
        )

        self.chain = self.prompt | self.model | self.parser

    def analyze_grammar(self, grammar_text):
        try:
            result = self.chain.invoke({"grammar": grammar_text})
            logger.info(f"Grammar analysis result: {result}")
            return result
        except Exception as e:
            logger.error(f"Grammar analysis error: {e}")
            return None
