from strands import Agent
from strands.models.ollama import OllamaModel
from strands_tools import calculator

from app.core.config import settings

def create_agent():
    model = OllamaModel(
        host=settings.llm_endpoint,
        model_id=settings.llm_model,
    )

    agent = Agent(
        model=model,
        tools=[calculator],
    )

    return agent

agent_instance = create_agent()
