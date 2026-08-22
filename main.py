from src.ai.llm import llm

response = llm.invoke(
    "Hello, world?"
)

print(response.content)