import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
    )

response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt="Tell me about capital of France"
)

print("\n" + response.choices[0].text.strip())