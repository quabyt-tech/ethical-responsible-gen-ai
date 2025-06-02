from enum import Enum


class AnthropicModel(Enum):
    HAIKU = "claude-3-5-haiku-20241022"
    SONNET = "claude-3-5-sonnet-20241022"
    OPUS = "claude-3-opus-20240229"

    @property
    def model_id(self) -> str:
        return f"anthropic/{self.value}"


class GeminiModel(Enum):
    PRO_2_5 = "gemini-2.5-pro-preview-03-25"
    FLASH_2_5 = "gemini-2.5-flash-preview-04-17"
    FLASH_2 = "gemini-2.0-flash"

    @property
    def model_id(self) -> str:
        return f"gemini/{self.value}"


class GroqModel(Enum):
    MIXTRAL = "mixtral-8x7b-32768"
    LLAMA_3_1 = "llama-3.1-8b-instant"
    LLAMA_3_3 = "llama-3.3-70b-versatile"

    @property
    def model_id(self) -> str:
        return f"groq/{self.value}"


class OpenAIModel(Enum):
    O_4_mini = "o4-mini"
    GPT_4_O = "gpt-4o"
    GPT_4_O_mini = "gpt-4o-mini"

    @property
    def model_id(self) -> str:
        return f"openai/{self.value}"
