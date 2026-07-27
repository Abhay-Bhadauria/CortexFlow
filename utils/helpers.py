from pathlib import Path


def load_prompt(filename: str) -> str:
    """
    Loads a prompt template from the prompts folder.
    """

    prompt_path = Path("prompts") / filename

    with open(prompt_path, "r", encoding="utf-8") as file:
        return file.read()