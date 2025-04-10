# Functions for building dynamic prompts based on input
def format_prompt(agent_level: str, query: str) -> str:
    """
    Standardizes prompt input for embedding, logging, or traceability.
    """
    return f"[Agent Level {agent_level}] Query: {query.strip()}"
