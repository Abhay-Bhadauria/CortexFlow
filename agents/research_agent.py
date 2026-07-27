from agents.base_agent import BaseAgent
from utils.context_optimizer import ContextOptimizer


class ResearchAgent(BaseAgent):
    """
    Performs detailed research based on the execution plan.
    """

    def __init__(self):
        super().__init__("research_prompt.txt")

    def research(self, execution_plan: dict) -> str:
        """
        Generate detailed research from a parsed execution plan.
        """

        compressed_plan = ContextOptimizer.compress_execution_plan(
            execution_plan
        )

        return self.execute(compressed_plan)