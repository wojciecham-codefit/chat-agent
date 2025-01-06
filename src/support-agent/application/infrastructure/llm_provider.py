from langchain_core.language_models import BaseChatModel
from langchain_openai import ChatOpenAI

from application.infrastructure.llm_configuration import LlmConfiguration


class LlmProvider:
    def __init__(self):
        self._configuration = LlmConfiguration()

    def get_llm(self) -> BaseChatModel:
        return ChatOpenAI(
            model_name=self._configuration.model,
            temperature=self._configuration.temperature,
            api_key=self._configuration.openai_key
        )

