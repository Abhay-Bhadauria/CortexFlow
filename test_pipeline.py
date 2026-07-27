import time

from agents.planner_agent import PlannerAgent
from agents.research_agent import ResearchAgent
from agents.summary_agent import SummaryAgent

from utils.parser import parse_execution_plan
from utils.token_counter import TokenCounter
from utils.context_optimizer import ContextOptimizer
from utils.logger import AgentLogger


def main():

    planner = PlannerAgent()
    researcher = ResearchAgent()
    summarizer = SummaryAgent()

    counter = TokenCounter()
    logger = AgentLogger()

    query = "Explain Docker and Kubernetes."

    # ======================================================================
    # STEP 1 : PLANNER
    # ======================================================================

    print("=" * 80)
    print("STEP 1 : PLANNING")
    print("=" * 80)

    try:

        start = time.time()

        plan = planner.plan(query)

        planner_time = time.time() - start

    except Exception as e:

        logger.log_error(
            "Planner Agent",
            str(e),
        )

        print(f"\nPlanner Agent Failed\n{e}")

        return

    planner_input_tokens = counter.count_tokens(query)
    planner_output_tokens = counter.count_tokens(plan)

    logger.log_agent(
        "Planner Agent",
        planner_input_tokens,
        planner_output_tokens,
        planner_time,
    )

    print(f"Planner Input Tokens : {planner_input_tokens}")
    print(f"Planner Output Tokens: {planner_output_tokens}\n")

    print("Execution Plan:\n")
    print(plan)

    try:
        execution_plan = parse_execution_plan(plan)

    except Exception as e:

        logger.log_error(
            "Parser",
            str(e),
        )

        print(f"\nParser Failed\n{e}")

        return

    print("\nParsed Execution Plan:\n")
    print(execution_plan)

    # ======================================================================
    # STEP 2 : RESEARCH
    # ======================================================================

    print("\n" + "=" * 80)
    print("STEP 2 : RESEARCH")
    print("=" * 80)

    compressed_plan = ContextOptimizer.compress_execution_plan(
        execution_plan
    )

    try:

        start = time.time()

        research = researcher.research(execution_plan)

        research_time = time.time() - start

    except Exception as e:

        logger.log_error(
            "Research Agent",
            str(e),
        )

        print(f"\nResearch Agent Failed\n{e}")

        return

    research_input_tokens = counter.count_tokens(
        compressed_plan
    )

    research_output_tokens = counter.count_tokens(
        research
    )

    logger.log_agent(
        "Research Agent",
        research_input_tokens,
        research_output_tokens,
        research_time,
    )

    print(f"Research Input Tokens : {research_input_tokens}")
    print(f"Research Output Tokens: {research_output_tokens}\n")

    print(research)

    # ======================================================================
    # STEP 3 : SUMMARY
    # ======================================================================

    print("\n" + "=" * 80)
    print("STEP 3 : SUMMARY")
    print("=" * 80)

    compressed_research = ContextOptimizer.compress_research(
        research
    )

    try:

        start = time.time()

        summary = summarizer.summarize(
            compressed_research
        )

        summary_time = time.time() - start

    except Exception as e:

        logger.log_error(
            "Summary Agent",
            str(e),
        )

        print(f"\nSummary Agent Failed\n{e}")

        return

    summary_input_tokens = counter.count_tokens(
        compressed_research
    )

    summary_output_tokens = counter.count_tokens(
        summary
    )

    logger.log_agent(
        "Summary Agent",
        summary_input_tokens,
        summary_output_tokens,
        summary_time,
    )

    print(f"Summary Input Tokens : {summary_input_tokens}")
    print(f"Summary Output Tokens: {summary_output_tokens}\n")

    print(summary)

    # ======================================================================
    # TOTAL TOKENS
    # ======================================================================

    print("\n" + "=" * 80)
    print("TOTAL TOKEN USAGE")
    print("=" * 80)

    total_input_tokens = (
        planner_input_tokens
        + research_input_tokens
        + summary_input_tokens
    )

    total_output_tokens = (
        planner_output_tokens
        + research_output_tokens
        + summary_output_tokens
    )

    grand_total_tokens = (
        total_input_tokens
        + total_output_tokens
    )

    print(f"Total Input Tokens : {total_input_tokens}")
    print(f"Total Output Tokens: {total_output_tokens}")
    print(f"Grand Total Tokens : {grand_total_tokens}")

    # ======================================================================
    # COST ESTIMATION
    # ======================================================================

    print("\n" + "=" * 80)
    print("COST ESTIMATION")
    print("=" * 80)

    INPUT_COST_PER_MILLION = 0.05
    OUTPUT_COST_PER_MILLION = 0.08

    planner_cost = counter.estimate_cost(
        planner_input_tokens,
        planner_output_tokens,
        INPUT_COST_PER_MILLION,
        OUTPUT_COST_PER_MILLION,
    )

    research_cost = counter.estimate_cost(
        research_input_tokens,
        research_output_tokens,
        INPUT_COST_PER_MILLION,
        OUTPUT_COST_PER_MILLION,
    )

    summary_cost = counter.estimate_cost(
        summary_input_tokens,
        summary_output_tokens,
        INPUT_COST_PER_MILLION,
        OUTPUT_COST_PER_MILLION,
    )

    total_cost = (
        planner_cost
        + research_cost
        + summary_cost
    )

    print(f"Planner Cost  : £{planner_cost:.8f}")
    print(f"Research Cost : £{research_cost:.8f}")
    print(f"Summary Cost  : £{summary_cost:.8f}")

    print("-" * 80)

    print(f"Total Cost    : £{total_cost:.8f}")

    # ======================================================================
    # EXECUTION TIME
    # ======================================================================

    print("\n" + "=" * 80)
    print("EXECUTION TIME")
    print("=" * 80)

    print(f"Planner Agent  : {planner_time:.2f} sec")
    print(f"Research Agent : {research_time:.2f} sec")
    print(f"Summary Agent  : {summary_time:.2f} sec")

    print("-" * 80)

    print(
        f"Total Time     : "
        f"{planner_time + research_time + summary_time:.2f} sec"
    )


if __name__ == "__main__":
    main()