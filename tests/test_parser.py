import pytest
from utils.parser import parse_execution_plan


def test_parse_valid_json():
    """Test parsing of valid JSON."""
    plan = """
    {
        "tasks": [
            {
                "title": "Task 1",
                "description": "Research AI agents"
            }
        ]
    }
    """

    result = parse_execution_plan(plan)

    assert isinstance(result, dict)
    assert "tasks" in result
    assert result["tasks"][0]["title"] == "Task 1"


def test_parse_invalid_json():
    """Test that invalid JSON raises ValueError."""
    invalid_plan = "{ invalid json }"

    with pytest.raises(ValueError, match="Invalid JSON"):
        parse_execution_plan(invalid_plan)


def test_parse_empty_response():
    """Test that an empty response raises ValueError."""
    with pytest.raises(ValueError, match="empty response"):
        parse_execution_plan("")
