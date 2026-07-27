from agents.base_agent import BaseAgent


class PlannerAgent(BaseAgent):
    """
    Breaks a user query into logical execution steps.
    """

    def __init__(self):
        super().__init__("planner_prompt.txt")

    def plan(self, query: str) -> str:
        """
        Generate an execution plan.
        """

        return self.execute(query)