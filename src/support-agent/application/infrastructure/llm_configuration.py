from attr import dataclass

@dataclass
class LlmConfiguration:
    openai_key = "klucz-do-api-nie-wrzucam"
    model = "gpt-4o-mini"
    temperature = 0.2