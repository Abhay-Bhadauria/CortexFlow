import re


class ContextOptimizer:

    @staticmethod
    def compress_execution_plan(plan: dict):

        tasks = plan.get("tasks", [])

        return "\n".join(
            f"{i + 1}. {task}"
            for i, task in enumerate(tasks)
        )

    @staticmethod
    def compress_research(text: str):

        text = re.sub(r"\n{2,}", "\n", text)
        text = re.sub(r"[ \t]+", " ", text)

        return text.strip()