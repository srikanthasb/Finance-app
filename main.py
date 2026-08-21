from src.ai.llm import llm

response = llm.invoke(
    "Hello, whats'up?"
)

print(response.content)