from utils.token_counter import TokenCounter


def test_token_count():

    counter = TokenCounter()

    tokens = counter.count_tokens("Hello World")

    assert tokens > 0


def test_cost_estimation():

    counter = TokenCounter()

    cost = counter.estimate_cost(
        100,
        50,
        0.05,
        0.08
    )

    assert cost > 0