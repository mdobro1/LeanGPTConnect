import os
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),  
    api_version="2024-02-01",
    azure_endpoint = os.getenv("OPENAI_ENDPOINT")
    )

# you could also use custom name you chose 
# for your deployment when you deployed a model. 
my_openai_model = "gpt-35-turbo-instruct"

response = client.completions.create(
  model=my_openai_model,
  prompt="Tell me about capital of France"
)

print("\n" + response.choices[0].text.strip())