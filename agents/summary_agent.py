from agents.base_agent import BaseAgent


class SummaryAgent(BaseAgent):
    """
    Converts detailed research into a clean, structured final response.
    """

    def __init__(self):
        super().__init__("summary_prompt.txt")

    def summarize(self, research: str) -> str:
        """
        Generate the final summarized response.
        """

        return self.execute(research)