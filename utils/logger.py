import logging
import os


class AgentLogger:

    def __init__(self):

        os.makedirs("logs", exist_ok=True)

        logging.basicConfig(
            filename="logs/agent.log",
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        self.logger = logging.getLogger(__name__)

    def log_agent(
        self,
        agent_name,
        input_tokens,
        output_tokens,
        execution_time,
        status="SUCCESS",
    ):

        self.logger.info(
            f"{agent_name} | "
            f"Input Tokens={input_tokens} | "
            f"Output Tokens={output_tokens} | "
            f"Execution Time={execution_time:.2f}s | "
            f"Status={status}"
        )

    def log_error(
        self,
        agent_name,
        error,
    ):

        self.logger.exception(
            f"{agent_name} | ERROR | {error}"
        )