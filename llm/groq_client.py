import os

from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()


class GroqClient:
    """
    A reusable client for interacting with the Groq API.

    Responsibilities:
    - Load API key
    - Create Groq client
    - Send prompts to the LLM
    - Return generated responses
    """

    DEFAULT_MODEL = "llama-3.3-70b-versatile"

    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError(
                "GROQ_API_KEY not found. Please add it to your .env file."
            )

        self.client = Groq(api_key=api_key)

    def generate(
        self,
        user_prompt: str,
        system_prompt: str = "You are a helpful assistant.",
        model: str | None = None,
        temperature: float = 0.3,
        max_tokens: int = 1024,
    ):

        model = model or self.DEFAULT_MODEL

        try:

            response = self.client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt,
                    },
                    {
                        "role": "user",
                        "content": user_prompt,
                    },
                ],
                temperature=temperature,
                max_tokens=max_tokens,
            )

            content = response.choices[0].message.content

            if content is None or not content.strip():
                raise RuntimeError(
                    "LLM returned an empty response."
                )

            return content.strip()

        except Exception as e:
            raise RuntimeError(
                f"Groq API Error: {str(e)}"
            )