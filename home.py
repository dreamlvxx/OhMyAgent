import os

from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_anthropic import ChatAnthropic

@tool
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

api_key = os.environ.get("ANTHROPIC_AUTH_TOKEN")
if not api_key:
    raise ValueError(
        "OPENAI_API_KEY environment variable is not set. "
        "Please set it before running: export ANTHROPIC_AUTH_TOKEN='your-key'"
    )
model = ChatAnthropic(model="ppio/pa/claude-opus-4-6")

agent = create_agent(model = model)

response = agent.invoke(
    {"messages": [{"role": "user", "content": "who are u"}]}
)
# Only print the last AI reply
print(response["messages"][-1].content)