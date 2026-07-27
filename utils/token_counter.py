import tiktoken


class TokenCounter:
    """
    Utility class for counting tokens in prompts and responses.
    """

    def __init__(self, model: str = "cl100k_base"):
        """
        Initialize the tokenizer.

        cl100k_base is compatible with most modern LLMs and is
        sufficient for estimating token usage even when using Groq.
        """
        self.encoding = tiktoken.get_encoding(model)

    def count_tokens(self, text: str) -> int:
        """
        Count the number of tokens in the given text.
        """
        return len(self.encoding.encode(text))

    def estimate_cost(
        self,
        input_tokens: int,
        output_tokens: int,
        input_cost_per_million: float,
        output_cost_per_million: float,
    ) -> float:
        """
        Estimate the API cost based on token pricing.
        """

        input_cost = (input_tokens / 1_000_000) * input_cost_per_million
        output_cost = (output_tokens / 1_000_000) * output_cost_per_million

        return input_cost + output_cost