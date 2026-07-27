from utils.context_optimizer import ContextOptimizer


def test_compress_execution_plan():

    plan = {
        "goal": "Test",
        "tasks": [
            "Task 1",
            "Task 2",
            "Task 3"
        ]
    }

    compressed = ContextOptimizer.compress_execution_plan(plan)

    assert "1. Task 1" in compressed
    assert "2. Task 2" in compressed
    assert "3. Task 3" in compressed


def test_compress_research():

    text = "Hello\n\n\nWorld      Test"

    compressed = ContextOptimizer.compress_research(text)

    assert "\n\n" not in compressed
    assert "      " not in compressed