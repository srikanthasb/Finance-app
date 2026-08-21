from src.ai.llm import llm

response = llm.invoke(
    "Hello, who are you?"
)

print(response.content)