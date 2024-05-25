import os
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),  
    api_version="2024-02-01",
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    )

response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt="Tell me about capital of France"
)

print("\n" + response.choices[0].text.strip())