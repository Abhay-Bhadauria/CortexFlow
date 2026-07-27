from abc import ABC

from llm.groq_client import GroqClient
from utils.helpers import load_prompt


class BaseAgent(ABC):
    """
    Base class for all AI agents.

    Responsibilities:
    - Load the agent's system prompt
    - Send requests to the LLM
    """

    def __init__(self, prompt_file: str):
        self.llm = GroqClient()
        self.system_prompt = load_prompt(prompt_file)

    def execute(
        self,
        user_prompt: str,
        temperature: float = 0.3,
        max_tokens: int = 1024,
    ):

        if not user_prompt.strip():
            raise ValueError(
                "Input prompt cannot be empty."
            )

        return self.llm.generate(
            system_prompt=self.system_prompt,
            user_prompt=user_prompt,
            temperature=temperature,
            max_tokens=max_tokens,
        )