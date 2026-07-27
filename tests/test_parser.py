import json


def parse_execution_plan(plan: str) -> dict:
    """
    Parse the planner's JSON response.
    """

    if not plan.strip():
        raise ValueError("Planner returned an empty response.")

    # Remove Markdown code fences if present
    plan = plan.strip()

    if plan.startswith("```json"):
        plan = plan.replace("```json", "", 1)

    if plan.endswith("```"):
        plan = plan[:-3]

    plan = plan.strip()

    try:
        return json.loads(plan)

    except json.JSONDecodeError as e:
        raise ValueError(
            f"Invalid JSON received from Planner Agent.\n{e}"
        )